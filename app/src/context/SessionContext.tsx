import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react';
import type { ReactNode } from 'react';
import { api, ApiError } from '../lib/api';
import type { AppState, ProfileInput } from '../lib/types';

const TOKEN_KEY = 'vf_access_token';

type SessionContextValue = {
  token: string | null;
  state: AppState | null;
  loading: boolean;
  error: string | null;
  login: (email: string, idCompra: number) => Promise<void>;
  logout: () => void;
  refresh: () => Promise<void>;
  saveProfiles: (profiles: ProfileInput[]) => Promise<void>;
  toggleCheck: (runId: string, checkDate: string, itemKey: string, done: boolean) => Promise<void>;
  completeRun: (runId: string, transformacao: string, relato?: string) => ReturnType<typeof api.completeRun>;
};

const SessionContext = createContext<SessionContextValue | null>(null);

export function SessionProvider({ children }: { children: ReactNode }) {
  const [token, setToken] = useState<string | null>(() => localStorage.getItem(TOKEN_KEY));
  const [state, setState] = useState<AppState | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const refresh = useCallback(async () => {
    const currentToken = localStorage.getItem(TOKEN_KEY);
    if (!currentToken) {
      setState(null);
      setLoading(false);
      return;
    }
    setLoading(true);
    setError(null);
    try {
      const newState = await api.getState(currentToken);
      setState(newState);
    } catch (err) {
      if (err instanceof ApiError && err.status === 401) {
        localStorage.removeItem(TOKEN_KEY);
        setToken(null);
        setState(null);
      } else {
        setError('Não consegui carregar seus dados agora. Tenta de novo em instantes.');
      }
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    refresh();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const login = useCallback(
    async (email: string, idCompra: number) => {
      setError(null);
      const result = await api.verifyPurchase(email, idCompra);
      localStorage.setItem(TOKEN_KEY, result.access_token);
      setToken(result.access_token);
      await refresh();
    },
    [refresh],
  );

  const logout = useCallback(() => {
    localStorage.removeItem(TOKEN_KEY);
    setToken(null);
    setState(null);
  }, []);

  const saveProfiles = useCallback(
    async (profiles: ProfileInput[]) => {
      if (!token) return;
      await api.saveProfiles(token, profiles);
      await refresh();
    },
    [token, refresh],
  );

  const toggleCheck = useCallback(
    async (runId: string, checkDate: string, itemKey: string, done: boolean) => {
      if (!token) return;
      await api.toggleCheck(token, runId, checkDate, itemKey, done);
      await refresh();
    },
    [token, refresh],
  );

  const completeRun = useCallback(
    async (runId: string, transformacao: string, relato?: string) => {
      if (!token) throw new Error('sem sessão');
      const result = await api.completeRun(token, runId, transformacao, relato);
      await refresh();
      return result;
    },
    [token, refresh],
  );

  const value = useMemo(
    () => ({ token, state, loading, error, login, logout, refresh, saveProfiles, toggleCheck, completeRun }),
    [token, state, loading, error, login, logout, refresh, saveProfiles, toggleCheck, completeRun],
  );

  return <SessionContext.Provider value={value}>{children}</SessionContext.Provider>;
}

export function useSession() {
  const ctx = useContext(SessionContext);
  if (!ctx) throw new Error('useSession precisa estar dentro de SessionProvider');
  return ctx;
}
