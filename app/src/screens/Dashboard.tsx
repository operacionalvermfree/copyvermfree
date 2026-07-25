import { useSession } from '../context/SessionContext';
import { faseAtual, formatDatePt } from '../lib/dates';
import MoonCountdown from '../components/MoonCountdown';
import type { Profile, ProtocolRun } from '../lib/types';

function runFor(profileId: string, runs: ProtocolRun[]): ProtocolRun | undefined {
  return runs.find((r) => r.profile_id === profileId);
}

export default function Dashboard({ onOpenProfile }: { onOpenProfile: (profileId: string) => void }) {
  const { state, logout } = useSession();
  if (!state) return null;

  return (
    <div className="mx-auto min-h-svh max-w-lg bg-[var(--vf-cream)] px-5 py-8">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-xl font-semibold text-[var(--vf-green-dark)]">
            Oi{state.customer.nome ? `, ${state.customer.nome.split(' ')[0]}` : ''} 🌿
          </h1>
          <p className="text-sm text-neutral-600">Seu protocolo VermeFree</p>
        </div>
        <button onClick={logout} className="text-xs text-neutral-400 hover:text-neutral-600">
          sair
        </button>
      </div>

      <div className="mt-6 space-y-4">
        {state.profiles.map((profile) => (
          <ProfileCard
            key={profile.id}
            profile={profile}
            run={runFor(profile.id, state.runs)}
            items={profile.tipo === 'kids' ? state.items_kids : state.items_adulto}
            onOpen={() => onOpenProfile(profile.id)}
          />
        ))}
      </div>
    </div>
  );
}

function ProfileCard({
  profile,
  run,
  items,
  onOpen,
}: {
  profile: Profile;
  run: ProtocolRun | undefined;
  items: import('../lib/types').ChecklistItem[];
  onOpen: () => void;
}) {
  const isKids = profile.tipo === 'kids';
  const accent = isKids ? 'var(--vf-kids)' : 'var(--vf-green)';
  const accentDark = isKids ? 'var(--vf-kids-dark)' : 'var(--vf-green-dark)';

  if (!run) return null;
  const fase = faseAtual(run, items);

  return (
    <button
      onClick={onOpen}
      className="w-full rounded-2xl bg-white p-5 text-left shadow-sm ring-1 ring-black/5 transition hover:shadow-md"
      style={{ borderLeft: `4px solid ${accent}` }}
    >
      <div className="flex items-center justify-between">
        <span className="text-base font-semibold" style={{ color: accentDark as string }}>
          {isKids ? '🧒' : '🌿'} {profile.nome}
        </span>
        {isKids && profile.faixa_etaria && (
          <span className="rounded-full bg-[var(--vf-kids)]/15 px-2 py-0.5 text-xs text-[var(--vf-kids-dark)]">
            {profile.faixa_etaria} anos
          </span>
        )}
      </div>

      {fase.tipo === 'agendado' && (
        <div className="mt-2">
          <MoonCountdown moonDate={run.moon_date} />
          <p className="mt-1 text-xs text-neutral-500">
            Preparo começa em {formatDatePt(run.silimarina_start_date || run.start_date)}
          </p>
        </div>
      )}

      {fase.tipo === 'em_andamento' && (
        <div className="mt-2">
          <p className="text-sm text-neutral-700">
            Dia <span className="font-semibold">{fase.diaAtual}</span> de {fase.totalDias}
          </p>
          <div className="mt-2 h-1.5 w-full overflow-hidden rounded-full bg-neutral-100">
            <div
              className="h-full rounded-full"
              style={{ width: `${Math.min(100, (fase.diaAtual / fase.totalDias) * 100)}%`, background: accent as string }}
            />
          </div>
          <p className="mt-2 text-sm font-medium" style={{ color: accentDark as string }}>
            Ver o que fazer hoje →
          </p>
        </div>
      )}

      {fase.tipo === 'pronto_para_concluir' && (
        <p className="mt-2 text-sm font-medium text-[var(--vf-green-dark)]">
          Protocolo completo! Conta pra gente como foi →
        </p>
      )}

      {fase.tipo === 'concluido' && (
        <p className="mt-2 text-sm text-neutral-500">
          Protocolo concluído em {run.completed_at ? formatDatePt(run.completed_at.slice(0, 10)) : ''} ✅
        </p>
      )}
    </button>
  );
}
