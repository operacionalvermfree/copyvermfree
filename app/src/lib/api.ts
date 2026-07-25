import type { AppState, CompleteRunResult, ProfileInput, ProdutosComprados, QuizCheckout } from './types';

const SUPABASE_URL = import.meta.env.VITE_SUPABASE_URL as string;
const SUPABASE_ANON_KEY = import.meta.env.VITE_SUPABASE_ANON_KEY as string;

export class ApiError extends Error {
  status: number;
  constructor(message: string, status: number) {
    super(message);
    this.status = status;
  }
}

async function callApi<T>(action: string, payload: Record<string, unknown> = {}): Promise<T> {
  const res = await fetch(`${SUPABASE_URL}/functions/v1/protocol-api`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${SUPABASE_ANON_KEY}`,
      apikey: SUPABASE_ANON_KEY,
    },
    body: JSON.stringify({ action, ...payload }),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw new ApiError((data && data.error) || 'unknown_error', res.status);
  }
  return data as T;
}

export type VerifyPurchaseResult = {
  access_token: string;
  customer: { id: string; nome: string | null; email: string };
  produtos: ProdutosComprados;
  quiz_checkout: QuizCheckout | null;
};

export const api = {
  verifyPurchase: (email: string, id_compra: number) =>
    callApi<VerifyPurchaseResult>('verify-purchase', { email, id_compra }),
  getState: (access_token: string) => callApi<AppState>('get-state', { access_token }),
  saveProfiles: (access_token: string, profiles: ProfileInput[]) =>
    callApi<{ created: unknown[] }>('save-profiles', { access_token, profiles }),
  toggleCheck: (access_token: string, run_id: string, check_date: string, item_key: string, done: boolean) =>
    callApi<{ ok: true }>('toggle-check', { access_token, run_id, check_date, item_key, done }),
  completeRun: (access_token: string, run_id: string, transformacao: string, relato?: string) =>
    callApi<CompleteRunResult>('complete-run', { access_token, run_id, transformacao, relato }),
};
