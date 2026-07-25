import { useState } from 'react';
import { useSession } from './context/SessionContext';
import Login from './screens/Login';
import Onboarding from './screens/Onboarding';
import Dashboard from './screens/Dashboard';
import ProfileDetail from './screens/ProfileDetail';

export default function App() {
  const { token, state, loading, error } = useSession();
  const [openProfileId, setOpenProfileId] = useState<string | null>(null);

  if (!token) return <Login />;

  if (loading) {
    return (
      <div className="flex min-h-svh items-center justify-center bg-[var(--vf-cream)]">
        <p className="text-sm text-neutral-500">Carregando seu protocolo…</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex min-h-svh items-center justify-center bg-[var(--vf-cream)] px-6 text-center">
        <p className="text-sm text-neutral-600">{error}</p>
      </div>
    );
  }

  if (!state) return <Login />;

  if (state.profiles.length === 0) return <Onboarding />;

  if (openProfileId) {
    return <ProfileDetail profileId={openProfileId} onBack={() => setOpenProfileId(null)} />;
  }

  return <Dashboard onOpenProfile={setOpenProfileId} />;
}
