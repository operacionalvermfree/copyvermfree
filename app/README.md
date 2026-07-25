# Meu Protocolo VermeFree

Mini-app (PWA) para clientes que compraram na VermeFree acompanharem o cronograma
da desparasitação natural, sincronizado com a lua nova — cápsula/dose do dia,
progresso do ciclo e, ao final, um quiz de transformação com recomendação de
recompra quando fizer sentido.

## Como funciona

- **Acesso**: a cliente entra com e-mail + número do pedido. Isso é validado
  contra a tabela `compra_aprovada` (já alimentada pelo Shopify) no Supabase do
  projeto **VermeFree**. Não existe cadastro de senha.
- **Onboarding**: o app já sugere os perfis (adulto / kids) a partir dos
  produtos comprados, e mostra de volta as respostas do quiz de pré-checkout
  (sintomas, histórico) — sem pedir de novo o que a cliente já respondeu no
  Shopify.
- **Cronograma**: a data da próxima lua nova é calculada localmente (sem API
  externa), e cada protocolo (Adulto ou Kids) é agendado a partir dela, com a
  janela de dias de cada item calculada a partir da posologia real dos rótulos
  (ver `CLAUDE.md`, seção 5, na raiz do repositório).
- **Checklist diário**: mostra só os itens daquele dia especificamente para
  aquele perfil (ex: só a Silimarina nos 15 dias antes da lua nova; tintura +
  óleo + ornitina depois).
- **Conclusão**: ao passar do último dia, a cliente responde como sentiu a
  transformação. Se a resposta indicar pouca/nenhuma diferença, o app sugere
  repetir no próximo ciclo com o cupom `5OFF` — sempre com linguagem segura
  (sem prometer cura, sem diagnosticar, ver checklist de claims no `CLAUDE.md`).

## Stack

- Vite + React + TypeScript + Tailwind v4
- Backend: Supabase (projeto `VermeFree`, id `xwusvksjnwydliicjveu`)
  - Tabelas: `app_customers`, `app_profiles`, `app_protocol_runs`,
    `app_daily_checks`, `app_quiz_responses` (todas com RLS habilitado, sem
    policies — só acessíveis via Edge Function com service role).
  - Edge Function única `protocol-api` (`supabase/functions/protocol-api`),
    roteada por `action` no corpo do POST: `verify-purchase`, `get-state`,
    `save-profiles`, `toggle-check`, `complete-run`.
- PWA instalável (manifest + service worker via `vite-plugin-pwa`).

## Rodando localmente

```bash
cp .env.example .env   # preencha com a URL e a anon/publishable key do projeto
npm install
npm run dev
```

## Deploy

`npm run build` gera um `dist/` estático — pode ir para Vercel, Netlify,
Cloudflare Pages ou qualquer hosting estático. As variáveis de ambiente
`VITE_SUPABASE_URL` e `VITE_SUPABASE_ANON_KEY` precisam estar configuradas no
provedor de hosting.

## Limitações da v1 / próximos passos sugeridos

- O link de acesso ao app hoje precisa ser compartilhado manualmente (ex: no
  e-mail de confirmação de compra ou por WhatsApp). Um próximo passo natural é
  automatizar esse envio assim que o pedido é aprovado.
- A recomendação de recompra usa sempre o cupom `5OFF` (documentado no
  `CLAUDE.md`). Se quiserem um cupom específico de recompra pós-protocolo,
  é só trocar a constante em `supabase/functions/protocol-api/index.ts`.
- Duração dos itens do protocolo adulto (Tintura, Óleo de Orégano, Ornitina)
  foi padronizada em 15 dias para ficar sincronizada com o frasco de Ornitina
  (15 cáps, 1/dia) e Óleo (45 cáps, 3/dia) — a Tintura (150ml a 9ml/dia) dura
  perto disso. Kids usa os 30 dias explícitos do rótulo.
