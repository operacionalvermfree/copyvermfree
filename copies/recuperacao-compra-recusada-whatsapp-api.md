# Recuperação — Compra Recusada (WhatsApp API) · VermeFree

> Cartão recusado. Objetivo: reassegurar e oferecer alternativa fácil (Pix aprova na hora / outro cartão). Cupom leve só no último toque. `{{1}}` = nome, nunca abre nem fecha a mensagem.
> Este arquivo cobre os toques de WhatsApp API (T1, T2, T4). O toque de e-mail T3 está em `recuperacao-compra-recusada-email.md`.

---

## T1 — 15min · Tranquilizar

```
Nome sugerido do template: vermefree_recusada_t1_probleminha
Categoria: MARKETING (ou UTILITY, se a conta permitir — é sobre um pedido já iniciado, não uma oferta nova)

BODY:
Oi {{1}}, tivemos um probleminha com seu pagamento — acontece bastante, não se preocupe. Seu pedido continua reservado, é só tentar de novo.

FOOTER (opcional): (nenhum)

BOTÃO (CTA URL): Tentar novamente → [LINK]
```

---

## T2 — 3h · Pix como alternativa fácil

```
Nome sugerido do template: vermefree_recusada_t2_pix
Categoria: MARKETING (ou UTILITY)

BODY:
Oi {{1}}, se o cartão continuar recusando, dá pra pagar por Pix — aprova na hora. É só escanear o QR ou colar o código no app do seu banco.

FOOTER (opcional): Rápido e sem burocracia

BOTÃO (CTA URL): Pagar com Pix → [LINK]
```

---

## T4 — 36h · Última chance + cupom leve

```
Nome sugerido do template: vermefree_recusada_t4_cupom
Categoria: MARKETING

BODY:
Oi {{1}}, esse é nosso último lembrete sobre seu pedido. Separei um cupom pra te ajudar: 5OFF (5% de desconto).

FOOTER (opcional): Última chance de usar o cupom

BOTÃO (CTA URL): Usar cupom e finalizar → [LINK]
```

---

## Checklist ANVISA (aplicado às 3 peças)

- [x] Sem claim proibido (cura/elimina/mata/erradica/100 tipos/milagre/garantido/em X dias) — nenhuma usa
- [x] Sem comparação com farmácia, sem promessa de emagrecimento
- [x] Sem citar Dr. William nem qualquer médico como aval
- [x] Não diagnostica o leitor
- [x] Tom empático, tranquilizador — nunca acusatório
- [x] Cupom só no T4
- [x] 1 CTA por peça

---

## Antes de submeter pra aprovação Meta

- Preencher `[LINK]` nas 3 peças.
- `{{1}}` puxa o primeiro nome do contato — confirmar que a base tem esse campo preenchido.
- Mesma observação do arquivo de e-mail: usei o cupom `5OFF` no T4 — trocar por `VOLTA5` se Gabriel preferir reservar o `5OFF` pra outro contexto.
