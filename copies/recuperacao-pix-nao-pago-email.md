# Recuperação — Pix Não Pago (E-mail / ActiveCampaign) · VermeFree

> Cliente de alta intenção: gerou o Pix, não pagou ainda. Objetivo: remover fricção de pagamento antes do código expirar. **Sem cupom em nenhum toque.** Variáveis: nome do cliente, produto, preço, link de pagamento/checkout.
> Este arquivo cobre os toques de e-mail (T1, T3, T4). Os toques de WhatsApp API (T1, T2, T4) estão em `recuperacao-pix-nao-pago-whatsapp-api.md`.

---

## T1 — 10min · "Seu Pix está te esperando"

**Assunto:** Seu Pix ainda está te esperando
**Assunto (variação A/B):** Falta só um passo pra finalizar seu pedido

**Pré-header:** Seu código Pix continua ativo — é só copiar e colar no seu banco.

**Corpo:**
```
Olá [NOME],

Vimos que você gerou o Pix do seu pedido — [PRODUTO] — mas ele ainda não caiu por aqui.

Às vezes o código trava por causa do app do banco, ou só falta finalizar o pagamento. Se foi isso, seu código continua ativo, é só copiar e colar:

[LINK/CÓDIGO PIX]

Pix costuma cair na hora, então em poucos minutos seu pedido já está confirmado.

Um abraço,
Equipe VermeFree
```

**CTA:** Finalizar meu Pix

---

## T3 — 3h · Benefício + código pode expirar

**Assunto:** Por que vale a pena finalizar agora
**Assunto (variação A/B):** Seu [PRODUTO] ainda está te esperando

**Pré-header:** O código Pix pode expirar em breve — finalize antes.

**Corpo:**
```
Olá [NOME],

Enquanto seu Pix não cai, seu pedido de [PRODUTO] (R$ [PREÇO]) continua reservado — mas o código pode expirar em breve.

Vale lembrar por que você começou esse pedido: o protocolo auxilia na desparasitação e apoia a rotina de limpeza natural, de forma natural e com constância — pra você (ou sua família) sentir o corpo mais leve, com mais disposição.

Se ainda faz sentido pra você, é só finalizar o Pix antes que expire:

[LINK]

Um abraço,
Equipe VermeFree
```

**CTA:** Finalizar meu pedido

---

## T4 — 20h · Última chance (expira, gerar novo Pix)

**Assunto:** Seu Pix está prestes a expirar
**Assunto (variação A/B):** Última chance de finalizar sem começar tudo de novo

**Pré-header:** Se o código expirou, é só gerar um novo — leva menos de 1 minuto.

**Corpo:**
```
Olá [NOME],

Esse é nosso último aviso sobre o Pix do seu pedido de [PRODUTO].

Se o código ainda está ativo, é só finalizar agora:

[LINK]

Se já expirou, sem problema — é só gerar um novo Pix, leva menos de 1 minuto e o pagamento cai na hora.

Depois disso, seu pedido sai da nossa lista de lembretes.

Um abraço,
Equipe VermeFree
```

**CTA:** Finalizar agora

---

## Checklist ANVISA (aplicado às 3 peças)

- [x] Sem claim proibido (cura/elimina/mata/erradica/100 tipos/milagre/garantido/em X dias) — nenhuma usa
- [x] Sem comparação com farmácia, sem promessa de emagrecimento
- [x] Sem citar Dr. William nem qualquer médico como aval
- [x] Não diagnostica o leitor
- [x] Tom empático, prestativo, leve — nunca desesperado nem acusatório (não presume erro do cliente, trata como "trava do app" ou "só faltou finalizar")
- [x] Sem cupom em nenhum toque, como definido pra este fluxo (alta intenção)
- [x] 1 CTA por e-mail

---

## Pendências para finalizar

1. **[PRODUTO], [PREÇO], [LINK/CÓDIGO PIX]** — variáveis dinâmicas do ActiveCampaign, preencher conforme integração com o checkout.
2. Confirmar com quem configura a automação o tempo real de expiração do código Pix (geralmente 30min–24h dependendo do gateway) — isso pode mudar a urgência real do T3 e T4.
