import { useState } from 'react';
import { useSession } from '../context/SessionContext';
import { faseAtual, formatDatePt, itemsDoDia, todayStr } from '../lib/dates';
import type { ChecklistItem, Transformacao } from '../lib/types';

const TRANSFORMACAO_OPCOES: { valor: Transformacao; label: string }[] = [
  { valor: 'bastante', label: 'Senti bastante diferença' },
  { valor: 'leve', label: 'Senti uma leve diferença' },
  { valor: 'nenhuma', label: 'Ainda não senti diferença' },
];

export default function ProfileDetail({ profileId, onBack }: { profileId: string; onBack: () => void }) {
  const { state, toggleCheck, completeRun } = useSession();
  const [savingKey, setSavingKey] = useState<string | null>(null);
  const [quizResult, setQuizResult] = useState<{ recomendacao: string; cupom_oferecido: string | null } | null>(null);

  if (!state) return null;
  const profile = state.profiles.find((p) => p.id === profileId);
  const run = state.runs.find((r) => r.profile_id === profileId);
  if (!profile || !run) return null;

  const items = profile.tipo === 'kids' ? state.items_kids : state.items_adulto;
  const fase = faseAtual(run, items);
  const isKids = profile.tipo === 'kids';
  const accentDark = isKids ? 'var(--vf-kids-dark)' : 'var(--vf-green-dark)';

  const hoje = todayStr();
  const itensHoje = itemsDoDia(run, items, hoje);
  const checksHoje = new Map(
    state.checks.filter((c) => c.run_id === run.id && c.check_date === hoje).map((c) => [c.item_key, c.done]),
  );

  const runId = run.id;

  async function handleToggle(item: ChecklistItem) {
    setSavingKey(item.key);
    const doneAgora = !(checksHoje.get(item.key) || false);
    try {
      await toggleCheck(runId, hoje, item.key, doneAgora);
    } finally {
      setSavingKey(null);
    }
  }

  return (
    <div className="mx-auto min-h-svh max-w-lg bg-[var(--vf-cream)] px-5 py-8">
      <button onClick={onBack} className="mb-4 text-sm text-neutral-500 hover:text-neutral-700">
        ← voltar
      </button>

      <h1 className="text-xl font-semibold" style={{ color: accentDark as string }}>
        {isKids ? '🧒' : '🌿'} {profile.nome}
      </h1>

      {fase.tipo === 'agendado' && (
        <div className="mt-4 rounded-2xl bg-white p-5 shadow-sm ring-1 ring-black/5">
          <p className="text-sm text-neutral-700">
            O protocolo desse ciclo começa em <strong>{formatDatePt(run.silimarina_start_date || run.start_date)}</strong>,
            sincronizado com a lua nova de {formatDatePt(run.moon_date)}.
          </p>
          <p className="mt-3 text-xs font-medium uppercase tracking-wide text-neutral-500">O que vem por aí</p>
          <ul className="mt-2 space-y-2 text-sm text-neutral-700">
            {items.map((item) => (
              <li key={item.key}>
                <span className="font-medium">{item.label}:</span> {item.instrucao}
              </li>
            ))}
          </ul>
        </div>
      )}

      {fase.tipo === 'em_andamento' && (
        <div className="mt-4">
          <p className="text-sm text-neutral-600">
            Dia {fase.diaAtual} de {fase.totalDias} · hoje é {formatDatePt(hoje)}
          </p>
          <div className="mt-3 space-y-3">
            {itensHoje.map((item) => {
              const done = checksHoje.get(item.key) || false;
              return (
                <button
                  key={item.key}
                  onClick={() => handleToggle(item)}
                  disabled={savingKey === item.key}
                  className={`flex w-full items-start gap-3 rounded-2xl p-4 text-left shadow-sm ring-1 transition ${
                    done ? 'bg-[var(--vf-green)]/10 ring-[var(--vf-green)]/30' : 'bg-white ring-black/5'
                  }`}
                >
                  <span
                    className={`mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full border-2 text-sm ${
                      done ? 'border-[var(--vf-green)] bg-[var(--vf-green)] text-white' : 'border-neutral-300'
                    }`}
                  >
                    {done ? '✓' : ''}
                  </span>
                  <span>
                    <span className={`block font-medium ${done ? 'text-neutral-500 line-through' : 'text-neutral-800'}`}>
                      {item.label}
                    </span>
                    <span className="block text-sm text-neutral-500">{item.instrucao}</span>
                  </span>
                </button>
              );
            })}
            {itensHoje.length === 0 && (
              <p className="text-sm text-neutral-500">Nenhum item programado pra hoje nesse perfil.</p>
            )}
          </div>
        </div>
      )}

      {fase.tipo === 'pronto_para_concluir' && !quizResult && (
        <CompletionQuiz
          onSubmit={async (transformacao, relato) => {
            const result = await completeRun(runId, transformacao, relato);
            setQuizResult(result);
          }}
        />
      )}

      {quizResult && <CompletionResult recomendacao={quizResult.recomendacao} cupom={quizResult.cupom_oferecido} />}

      {fase.tipo === 'concluido' && !quizResult && (
        <div className="mt-4 rounded-2xl bg-white p-5 text-center shadow-sm ring-1 ring-black/5">
          <p className="text-2xl">🌙</p>
          <p className="mt-2 text-sm text-neutral-600">
            Esse ciclo já foi concluído. A desparasitação natural é feita de 2 a 4 vezes por ano — a gente te avisa
            quando fizer sentido começar o próximo.
          </p>
        </div>
      )}
    </div>
  );
}

function CompletionQuiz({ onSubmit }: { onSubmit: (transformacao: Transformacao, relato: string) => Promise<void> }) {
  const [transformacao, setTransformacao] = useState<Transformacao | null>(null);
  const [relato, setRelato] = useState('');
  const [submitting, setSubmitting] = useState(false);

  return (
    <div className="mt-4 rounded-2xl bg-white p-5 shadow-sm ring-1 ring-black/5">
      <p className="text-2xl">🎉</p>
      <h2 className="mt-2 text-lg font-semibold text-[var(--vf-green-dark)]">Parabéns por completar o protocolo!</h2>
      <p className="mt-1 text-sm text-neutral-600">Conta pra gente: como foi a transformação?</p>

      <div className="mt-3 space-y-2">
        {TRANSFORMACAO_OPCOES.map((opcao) => (
          <button
            key={opcao.valor}
            onClick={() => setTransformacao(opcao.valor)}
            className={`w-full rounded-xl border px-4 py-2.5 text-left text-sm transition ${
              transformacao === opcao.valor
                ? 'border-[var(--vf-green)] bg-[var(--vf-green)]/10 font-medium text-[var(--vf-green-dark)]'
                : 'border-neutral-200 text-neutral-700 hover:border-neutral-300'
            }`}
          >
            {opcao.label}
          </button>
        ))}
      </div>

      <textarea
        value={relato}
        onChange={(e) => setRelato(e.target.value)}
        placeholder="Quer contar com suas palavras o que mudou? (opcional)"
        rows={3}
        className="mt-3 w-full rounded-lg border border-neutral-300 px-3 py-2 text-sm outline-none focus:border-[var(--vf-green)] focus:ring-2 focus:ring-[var(--vf-green)]/20"
      />

      <button
        disabled={!transformacao || submitting}
        onClick={async () => {
          if (!transformacao) return;
          setSubmitting(true);
          try {
            await onSubmit(transformacao, relato.trim());
          } finally {
            setSubmitting(false);
          }
        }}
        className="mt-4 w-full rounded-lg bg-[var(--vf-green-dark)] px-4 py-2.5 text-sm font-medium text-white transition hover:bg-[var(--vf-green)] disabled:opacity-60"
      >
        {submitting ? 'Enviando…' : 'Enviar'}
      </button>
    </div>
  );
}

function CompletionResult({ recomendacao, cupom }: { recomendacao: string; cupom: string | null }) {
  const precisaReforco = recomendacao === 'repetir_proximo_ciclo';

  return (
    <div className="mt-4 rounded-2xl bg-white p-5 shadow-sm ring-1 ring-black/5">
      <p className="text-2xl">{precisaReforco ? '🌱' : '💚'}</p>
      {precisaReforco ? (
        <>
          <h2 className="mt-2 text-lg font-semibold text-[var(--vf-green-dark)]">Constância é o que faz diferença</h2>
          <p className="mt-1 text-sm text-neutral-600">
            Muita gente sente o efeito completo só depois de repetir o protocolo em um segundo ciclo, sempre
            sincronizado com a lua nova. Pode fazer sentido considerar um novo ciclo em breve.
          </p>
          {cupom && (
            <div className="mt-3 rounded-xl bg-[var(--vf-green)]/10 p-3 text-center">
              <p className="text-sm text-neutral-700">Use o cupom no seu próximo protocolo:</p>
              <p className="mt-1 text-lg font-semibold tracking-wide text-[var(--vf-green-dark)]">{cupom}</p>
            </div>
          )}
        </>
      ) : (
        <>
          <h2 className="mt-2 text-lg font-semibold text-[var(--vf-green-dark)]">Que bom que sentiu diferença!</h2>
          <p className="mt-1 text-sm text-neutral-600">
            A desparasitação natural funciona melhor como rotina — o recomendado é repetir de 2 a 4 vezes por ano.
            A gente te avisa quando estiver perto da próxima lua nova.
          </p>
        </>
      )}
    </div>
  );
}
