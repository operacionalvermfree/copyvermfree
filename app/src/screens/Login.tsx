import { useState } from 'react';
import type { FormEvent } from 'react';
import { useSession } from '../context/SessionContext';
import { ApiError } from '../lib/api';

export default function Login() {
  const { login } = useSession();
  const [email, setEmail] = useState('');
  const [idCompra, setIdCompra] = useState('');
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setSubmitting(true);
    setError(null);
    try {
      await login(email.trim(), Number(idCompra.trim()));
    } catch (err) {
      if (err instanceof ApiError && err.status === 404) {
        setError('Não encontramos esse pedido com esse e-mail. Confira os dois dados e tente de novo.');
      } else {
        setError('Não conseguimos verificar seu pedido agora. Tenta novamente em instantes.');
      }
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div className="flex min-h-svh flex-col items-center justify-center bg-[var(--vf-cream)] px-6 py-10">
      <div className="w-full max-w-sm">
        <div className="mb-8 text-center">
          <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-[var(--vf-green-dark)]">
            <span className="text-2xl">🌿</span>
          </div>
          <h1 className="text-2xl font-semibold text-[var(--vf-green-dark)]">Meu Protocolo VermeFree</h1>
          <p className="mt-2 text-sm text-neutral-600">
            Acompanhe sua desparasitação natural, sincronizada com a lua nova, dia a dia.
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4 rounded-2xl bg-white p-6 shadow-sm ring-1 ring-black/5">
          <div>
            <label className="mb-1 block text-sm font-medium text-neutral-700">E-mail da compra</label>
            <input
              type="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="voce@email.com"
              className="w-full rounded-lg border border-neutral-300 px-3 py-2.5 text-base outline-none focus:border-[var(--vf-green)] focus:ring-2 focus:ring-[var(--vf-green)]/20"
            />
          </div>
          <div>
            <label className="mb-1 block text-sm font-medium text-neutral-700">Número do pedido</label>
            <input
              type="text"
              inputMode="numeric"
              required
              value={idCompra}
              onChange={(e) => setIdCompra(e.target.value)}
              placeholder="ex: 2217"
              className="w-full rounded-lg border border-neutral-300 px-3 py-2.5 text-base outline-none focus:border-[var(--vf-green)] focus:ring-2 focus:ring-[var(--vf-green)]/20"
            />
            <p className="mt-1 text-xs text-neutral-500">Está no e-mail de confirmação da sua compra.</p>
          </div>

          {error && <p className="text-sm text-red-600">{error}</p>}

          <button
            type="submit"
            disabled={submitting}
            className="w-full rounded-lg bg-[var(--vf-green-dark)] px-4 py-2.5 text-base font-medium text-white transition hover:bg-[var(--vf-green)] disabled:opacity-60"
          >
            {submitting ? 'Verificando…' : 'Entrar no meu protocolo'}
          </button>
        </form>

        <p className="mt-6 text-center text-xs text-neutral-500">
          Só clientes VermeFree têm acesso. Dúvidas? Chama a gente no WhatsApp.
        </p>
      </div>
    </div>
  );
}
