# Recuperação — Compra Recusada (E-mail / ActiveCampaign) · VermeFree

> Cartão recusado. Objetivo: reassegurar (acontece, não é culpa do cliente) e oferecer alternativa fácil (Pix aprova na hora / outro cartão). Cupom leve só no último toque. Variáveis: nome do cliente, produto, preço, link de pagamento/checkout.
> Este arquivo cobre os toques de e-mail (T1, T3, T4). Os toques de WhatsApp API (T1, T2, T4) estão em `recuperacao-compra-recusada-whatsapp-api.md`.

---

## T1 — 15min · "Tivemos um probleminha"

**Assunto:** Tivemos um probleminha com seu pagamento
**Assunto (variação A/B):** Seu pedido quase saiu — só faltou isso

**Pré-header:** Acontece bastante, e é rápido de resolver.

**Corpo:**
```
Olá [NOME],

Vimos que seu pagamento do pedido [PRODUTO] não foi aprovado. Não se preocupe — isso acontece bastante, às vezes é só um bloqueio momentâneo do cartão ou um dado digitado errado.

Seu pedido continua reservado. É só tentar de novo:

[LINK]

Se preferir, também dá pra pagar por Pix, que aprova na hora.

Um abraço,
Equipe VermeFree
```

**CTA:** Tentar novamente

---

## T3 — 12h · Benefício + Pix como caminho fácil

**Assunto:** O jeito mais fácil de finalizar seu pedido
**Assunto (variação A/B):** Ainda dá tempo de garantir seu [PRODUTO]

**Pré-header:** Pix aprova na hora — sem depender do seu cartão.

**Corpo:**
```
Olá [NOME],

Seu pedido de [PRODUTO] (R$ [PREÇO]) ainda está reservado, esperando só a confirmação do pagamento.

Se o cartão continuar dando problema, o Pix costuma ser o caminho mais fácil — aprova na hora, sem burocracia.

Vale lembrar por que você começou esse pedido: o protocolo auxilia na desparasitação e apoia a rotina de limpeza natural, de forma natural e com constância — pra você (ou sua família) sentir o corpo mais leve, com mais disposição.

[LINK]

Um abraço,
Equipe VermeFree
```

**CTA:** Finalizar com Pix

---

## T4 — 36h · Última chance + cupom leve

**Assunto:** Última chance + um empurrãozinho pra fechar
**Assunto (variação A/B):** Separei um cupom pra você finalizar seu pedido

**Pré-header:** Cupom 5OFF — só pra ajudar a fechar seu pedido de [PRODUTO].

**Corpo:**
```
Olá [NOME],

Esse é nosso último e-mail sobre o seu pedido de [PRODUTO].

Pra te ajudar a fechar, separei um cupom: 5OFF, com 5% de desconto.

[LINK]

Depois disso, seu pedido sai da nossa lista de lembretes — mas a porta continua aberta pra quando fizer sentido pra você.

Um abraço,
Equipe VermeFree
```

**CTA:** Usar cupom e finalizar

---

## Checklist ANVISA (aplicado às 3 peças)

- [x] Sem claim proibido (cura/elimina/mata/erradica/100 tipos/milagre/garantido/em X dias) — nenhuma usa
- [x] Sem comparação com farmácia, sem promessa de emagrecimento
- [x] Sem citar Dr. William nem qualquer médico como aval
- [x] Não diagnostica o leitor
- [x] Tom empático, tranquilizador — nunca acusatório ("não se preocupe", "acontece bastante", nunca insinua erro do cliente)
- [x] Cupom só no T4, como definido pra este fluxo
- [x] 1 CTA por e-mail

---

## Pendências para finalizar

1. **[PRODUTO], [PREÇO], [LINK]** — variáveis dinâmicas do ActiveCampaign.
2. **Cupom 5OFF vs VOLTA5** — usei `5OFF` por ser o cupom padrão de comunicação já documentado no `CLAUDE.md`. O `VOLTA5` é descrito como cupom de recompra (cliente que já comprou antes), o que não é bem o caso aqui (compra ainda não concluída) — mas se Gabriel preferir reservar o `5OFF` pra outros contextos, é só trocar o código no T4.
