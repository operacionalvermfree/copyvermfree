# Recuperação — Pix Não Pago (WhatsApp API) · VermeFree

> Cliente de alta intenção: gerou o Pix, não pagou ainda. Objetivo: ajudar a finalizar antes do código expirar. **Sem cupom em nenhum toque.** `{{1}}` = nome, nunca abre nem fecha a mensagem.
> Este arquivo cobre os toques de WhatsApp API (T1, T2, T4). O toque de e-mail T3 está em `recuperacao-pix-nao-pago-email.md`.

---

## T1 — 10min

```
Nome sugerido do template: vermefree_pix_t1_lembrete
Categoria: MARKETING (ou UTILITY, se a conta permitir — é lembrete de pagamento em aberto, não oferta)

BODY:
Oi {{1}}! Vi que você gerou o Pix do seu pedido, mas ele ainda não caiu por aqui. Seu código continua ativo — é só copiar e colar no app do seu banco.

FOOTER (opcional): Pix costuma confirmar na hora

BOTÃO (CTA URL): Finalizar meu Pix → [LINK]
```

---

## T2 — 1h · Reforço + gerar novo código

```
Nome sugerido do template: vermefree_pix_t2_reforco
Categoria: MARKETING (ou UTILITY)

BODY:
Oi {{1}}, ainda dá tempo de finalizar seu Pix! Se o código já expirou, me chama aqui que eu gero outro pra você rapidinho.

FOOTER (opcional): É rápido, leva menos de 1 minuto

BOTÃO (CTA URL): Finalizar agora → [LINK]
```

---

## T4 — 20h · Última chance

```
Nome sugerido do template: vermefree_pix_t4_ultima_chance
Categoria: MARKETING (ou UTILITY)

BODY:
Oi {{1}}, seu Pix está prestes a expirar. Se ainda não caiu, é só finalizar agora — ou responda aqui que eu gero um novo código pra você.

FOOTER (opcional): Última chance antes de sair da nossa lista de lembretes

BOTÃO (CTA URL): Finalizar agora → [LINK]
```

---

## Checklist ANVISA (aplicado às 3 peças)

- [x] Sem claim proibido (cura/elimina/mata/erradica/100 tipos/milagre/garantido/em X dias) — nenhuma usa
- [x] Sem comparação com farmácia, sem promessa de emagrecimento
- [x] Sem citar Dr. William nem qualquer médico como aval
- [x] Não diagnostica o leitor
- [x] Tom empático, prestativo — nunca desesperado nem acusatório
- [x] Sem cupom em nenhum toque
- [x] 1 CTA por peça

---

## Antes de submeter pra aprovação Meta

- Preencher `[LINK]` nas 3 peças.
- `{{1}}` puxa o primeiro nome do contato — confirmar que a base tem esse campo preenchido.
- T2 e T4 convidam o cliente a responder pedindo um código novo — isso abre a janela de 24h de conversa livre, então vale ter alguém (ou automação) de prontidão pra gerar o novo Pix quando a pessoa responder.
