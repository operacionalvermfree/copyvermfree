import { useMemo, useState } from 'react';
import { useSession } from '../context/SessionContext';
import type { ProfileInput, TipoPerfil } from '../lib/types';

type Row = ProfileInput & { rowId: string };

let rowSeq = 0;
function newRowId() {
  rowSeq += 1;
  return `row-${rowSeq}`;
}

const SINTOMAS_LABELS: Record<string, string> = {
  Sintomas: 'O que você notou',
  Histórico: 'Histórico com desparasitação',
};

export default function Onboarding() {
  const { state, saveProfiles } = useSession();
  const customer = state?.customer;
  const produtos = customer?.produtos;

  const sugestoesIniciais = useMemo<Row[]>(() => {
    const rows: Row[] = [];
    if (produtos && (produtos.adulto > 0 || produtos.familia > 0)) {
      rows.push({ rowId: newRowId(), tipo: 'adulto', nome: 'Eu' });
    }
    if (produtos && (produtos.kids_2_4 > 0 || produtos.familia > 0)) {
      rows.push({ rowId: newRowId(), tipo: 'kids', nome: '', faixa_etaria: '2-4' });
    }
    if (produtos && produtos.kids_5_9 > 0) {
      rows.push({ rowId: newRowId(), tipo: 'kids', nome: '', faixa_etaria: '5-9' });
    }
    if (!rows.length) {
      rows.push({ rowId: newRowId(), tipo: 'adulto', nome: 'Eu' });
    }
    return rows;
  }, [produtos]);

  const [rows, setRows] = useState<Row[]>(sugestoesIniciais);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  function updateRow(rowId: string, patch: Partial<Row>) {
    setRows((prev) => prev.map((r) => (r.rowId === rowId ? { ...r, ...patch } : r)));
  }

  function addRow(tipo: TipoPerfil) {
    setRows((prev) => [
      ...prev,
      tipo === 'adulto'
        ? { rowId: newRowId(), tipo: 'adulto', nome: '' }
        : { rowId: newRowId(), tipo: 'kids', nome: '', faixa_etaria: '2-4' },
    ]);
  }

  function removeRow(rowId: string) {
    setRows((prev) => prev.filter((r) => r.rowId !== rowId));
  }

  async function handleSubmit() {
    setError(null);
    const perfisValidos = rows.filter((r) => r.nome.trim().length > 0);
    if (!perfisValidos.length) {
      setError('Dá um nome pra cada perfil antes de continuar (pode ser só "Eu" ou o nome da criança).');
      return;
    }
    setSubmitting(true);
    try {
      await saveProfiles(
        perfisValidos.map((r) => ({ tipo: r.tipo, nome: r.nome.trim(), faixa_etaria: r.faixa_etaria })),
      );
    } catch {
      setError('Não conseguimos salvar agora. Tenta de novo em instantes.');
    } finally {
      setSubmitting(false);
    }
  }

  const quiz = customer?.quiz_checkout;
  const quizEntries = quiz ? Object.entries(quiz).filter(([k]) => k !== 'Contraindicações' && k !== 'Respondido em') : [];

  return (
    <div className="mx-auto min-h-svh max-w-lg bg-[var(--vf-cream)] px-5 py-8">
      <h1 className="text-xl font-semibold text-[var(--vf-green-dark)]">
        Oi{customer?.nome ? `, ${customer.nome.split(' ')[0]}` : ''}! Vamos montar seu protocolo.
      </h1>
      <p className="mt-2 text-sm text-neutral-600">
        Cada protocolo é sincronizado com a lua nova. É só nos dizer quem vai fazer, e a gente monta o cronograma
        certinho.
      </p>

      {quizEntries.length > 0 && (
        <div className="mt-5 rounded-2xl bg-white p-4 shadow-sm ring-1 ring-black/5">
          <p className="text-xs font-medium uppercase tracking-wide text-neutral-500">No checkout, você contou:</p>
          <ul className="mt-2 space-y-1 text-sm text-neutral-700">
            {quizEntries.map(([k, v]) => (
              <li key={k}>
                <span className="font-medium">{SINTOMAS_LABELS[k] || k}:</span> {v}
              </li>
            ))}
          </ul>
          <p className="mt-2 text-xs text-neutral-500">Não precisa preencher de novo — já está tudo aqui. 🙂</p>
        </div>
      )}

      <div className="mt-6 space-y-3">
        {rows.map((row) => (
          <div key={row.rowId} className="rounded-2xl bg-white p-4 shadow-sm ring-1 ring-black/5">
            <div className="flex items-center justify-between">
              <span
                className={
                  row.tipo === 'kids'
                    ? 'rounded-full bg-[var(--vf-kids)]/15 px-2.5 py-1 text-xs font-medium text-[var(--vf-kids-dark)]'
                    : 'rounded-full bg-[var(--vf-green)]/10 px-2.5 py-1 text-xs font-medium text-[var(--vf-green-dark)]'
                }
              >
                {row.tipo === 'kids' ? '🧒 Protocolo Kids' : '🌿 Protocolo Adulto'}
              </span>
              <button
                type="button"
                onClick={() => removeRow(row.rowId)}
                className="text-xs text-neutral-400 hover:text-neutral-600"
              >
                remover
              </button>
            </div>

            <div className="mt-3 grid grid-cols-1 gap-3 sm:grid-cols-2">
              <div>
                <label className="mb-1 block text-xs font-medium text-neutral-600">
                  {row.tipo === 'kids' ? 'Nome da criança' : 'Nome'}
                </label>
                <input
                  value={row.nome}
                  onChange={(e) => updateRow(row.rowId, { nome: e.target.value })}
                  placeholder={row.tipo === 'kids' ? 'ex: Théo' : 'Eu'}
                  className="w-full rounded-lg border border-neutral-300 px-3 py-2 text-sm outline-none focus:border-[var(--vf-green)] focus:ring-2 focus:ring-[var(--vf-green)]/20"
                />
              </div>
              {row.tipo === 'kids' && (
                <div>
                  <label className="mb-1 block text-xs font-medium text-neutral-600">Faixa etária</label>
                  <select
                    value={row.faixa_etaria}
                    onChange={(e) => updateRow(row.rowId, { faixa_etaria: e.target.value })}
                    className="w-full rounded-lg border border-neutral-300 px-3 py-2 text-sm outline-none focus:border-[var(--vf-green)] focus:ring-2 focus:ring-[var(--vf-green)]/20"
                  >
                    <option value="2-4">2 a 4 anos</option>
                    <option value="5-9">5 a 9 anos</option>
                  </select>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>

      <div className="mt-3 flex gap-2">
        <button
          type="button"
          onClick={() => addRow('adulto')}
          className="rounded-full border border-[var(--vf-green)] px-3 py-1.5 text-xs font-medium text-[var(--vf-green-dark)] hover:bg-[var(--vf-green)]/5"
        >
          + adicionar adulto
        </button>
        <button
          type="button"
          onClick={() => addRow('kids')}
          className="rounded-full border border-[var(--vf-kids)] px-3 py-1.5 text-xs font-medium text-[var(--vf-kids-dark)] hover:bg-[var(--vf-kids)]/5"
        >
          + adicionar criança
        </button>
      </div>

      {error && <p className="mt-4 text-sm text-red-600">{error}</p>}

      <button
        type="button"
        onClick={handleSubmit}
        disabled={submitting}
        className="mt-6 w-full rounded-lg bg-[var(--vf-green-dark)] px-4 py-3 text-base font-medium text-white transition hover:bg-[var(--vf-green)] disabled:opacity-60"
      >
        {submitting ? 'Montando cronograma…' : 'Começar meu protocolo'}
      </button>
    </div>
  );
}
