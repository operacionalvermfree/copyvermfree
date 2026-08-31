# Funil Perpétuo de Recompra — Pós-Compra · VermeFree

> Automação de reativação (quem já comprou). 3 toques — D+30, D+45, D+90 — cada um em WhatsApp API (HSM) + E-mail. Tom: consultivo, acolhedor, sem culpa. Depois do Toque 3, o cliente entra no winback trimestral (fora de escopo aqui).

## O que preencher
- `{{nome}}` — primeiro nome.
- `{{data}}` — prazo final do cupom no Toque 3 (72h a partir do disparo).

---

## WHATSAPP API

### MSG 1 — D+30 · Reconexão
```
Categoria: UTILITY

Oi {{nome}}! Faz um mês que você começou seu protocolo — como você tá se sentindo? 🌿
A desparasitação natural funciona bem quando vira rotina, no ritmo da lua nova (2 a 4x por ano).
Se quiser já ir se organizando pro próximo ciclo, separei 10% OFF com o cupom BEMVINDO10 pra quando fizer sentido pra você.
Quer que eu te avise quando a próxima lua nova chegar? 💬
```

### MSG 2 — D+45 · Reforço com prova social
```
Categoria: MARKETING

Oi {{nome}}! Olha só o que a gente ouve direto de quem já faz o protocolo com a gente: "me sinto muito mais leve, o intestino regulou de verdade". 🌿
Se você também quer voltar pro ritmo da lua nova, o cupom BEMVINDO10 (10% OFF) ainda tá valendo pra você.
Bora retomar? 👉 [LINK]
```

### MSG 3 — D+90 · Última chamada (sem culpa)
```
Categoria: MARKETING

Oi {{nome}}! Faz um tempinho que a gente não fala sobre o seu próximo ciclo — sem problema, cada corpo tem seu ritmo. 🌿
Se fizer sentido retomar agora, abrimos uma janela de 15% OFF com o cupom RECOMPRA15, válida até {{data}}.
Se não for a hora, tá tudo bem — a gente te espera por aqui quando fizer sentido pra você. 💬
```

---

## E-MAIL

### E-MAIL 1 — D+30 · Reconexão

**Assunto:** 🌿 Como você tá se sentindo, {{nome}}?
**Prévia (preview text):** Um mês desde o seu protocolo — bora conversar sobre isso

**Corpo:**
```
Olá, {{nome}},

Já faz um mês desde que você começou seu protocolo com a gente. Queríamos saber: como você tem se sentido? Mais leve, o intestino funcionando melhor, aquela sensação de corpo limpo por dentro?

A desparasitação natural funciona assim — não é evento único, é rotina. O ideal é repetir o ciclo de 2 a 4 vezes por ano, sempre no ritmo da lua nova, pra manter a constância que faz a diferença de verdade.

Se quiser já se programar pro seu próximo ciclo, deixamos 10% OFF reservado com o cupom BEMVINDO10 — sem pressa, é só pra quando fizer sentido pra você.

Um abraço,
Equipe VermeFree
```

**CTA (botão único):** Preparar meu próximo ciclo
**Cupom:** BEMVINDO10 — 10% OFF, uso livre (sem prazo neste toque)
**Rodapé:** Oferta pontual, por tempo limitado. Frete grátis acima de R$399.

### E-MAIL 2 — D+45 · Reforço com prova social

**Assunto:** 🌿 "Me sinto muito mais leve" — quem já sentiu
**Prévia (preview text):** Relatos de quem já voltou pro ritmo da lua nova

**Corpo:**
```
Olá, {{nome}},

Uma coisa que a gente ouve bastante de quem mantém a rotina de desparasitação natural em dia: "sinto o intestino funcionando melhor" e "acordo com mais disposição, sem aquela sensação de peso". Não é milagre — é constância, feita no ritmo certo, ciclo após ciclo.

Resultados variam de pessoa pra pessoa, claro. Mas se o seu corpo já te mostrou o que uma rotina de cuidado natural pode fazer, esse é um bom momento pra voltar a ela.

O cupom BEMVINDO10 (10% OFF) continua reservado pra você — é só retomar quando estiver pronta.

Um abraço,
Equipe VermeFree
```

**CTA (botão único):** Quero voltar ao meu ritmo
**Cupom:** BEMVINDO10 — 10% OFF, uso livre (sem prazo neste toque)
**Rodapé:** Oferta pontual, por tempo limitado. Frete grátis acima de R$399.

### E-MAIL 3 — D+90 · Última chamada (sem culpa)

**Assunto:** 🌿 Uma janela de 3 dias, sem pressa nenhuma
**Prévia (preview text):** 15% OFF até {{data}}, se e quando fizer sentido pra você

**Corpo:**
```
Olá, {{nome}},

Já faz um tempo desde o seu último contato com o seu ciclo de desparasitação natural — e tudo bem, cada família tem o próprio ritmo pra voltar à rotina.

Se esse for um bom momento pra retomar, abrimos uma janela pontual de 15% OFF com o cupom RECOMPRA15, válida até {{data}}. Vale tanto pra repetir o protocolo (adulto, kids ou kit família) quanto pra manter em dia com o Óleo de Alho entre um ciclo e outro.

Se ainda não for a hora, sem problema nenhum — seguimos por aqui, com você, prontos pra quando fizer sentido.

Um abraço,
Equipe VermeFree
```

**CTA (botão único):** Retomar meu protocolo
**Cupom:** RECOMPRA15 — 15% OFF, válido até {{data}} (72h a partir do disparo)
**Rodapé:** Oferta pontual, por tempo limitado. Frete grátis acima de R$399.

---

## Notas para Sarah

- Depois do Toque 3 (D+90), o cliente sai desta automação e entra no winback trimestral — copy desse fluxo não está incluída aqui.
- `{{data}}` no Toque 3 precisa ser calculada dinamicamente (disparo + 72h) na automação, não é valor fixo.
- Toques 1 e 2 usam o mesmo cupom (BEMVINDO10, 10% OFF) sem prazo apertado — a urgência só entra no Toque 3, com o RECOMPRA15.
- Produto sugerido varia pelo histórico do cliente: quem comprou Adulto/Kids/Kit Família → retomar o mesmo protocolo; quem já está dentro do ritmo → Óleo de Alho como manutenção entre ciclos (pode ser testado como order bump nos CTAs de e-mail, se a Sarah quiser).

## CHECKLIST ANVISA

- [x] Nenhuma peça usa "cura", "trata doença", "elimina/mata/erradica os vermes/parasitas" ou "mais de 100 tipos"
- [x] Nenhuma peça promete "milagre", "garantido" ou "resultado em X dias"
- [x] Nenhuma comparação com remédio/vermífugo de farmácia
- [x] Nenhuma promessa de emagrecimento
- [x] Nenhuma peça diagnostica o leitor ("você tem verme")
- [x] Nenhum médico ou influenciador citado como aval clínico
- [x] Linguagem segura usada em todas as peças ("auxilia na desparasitação", "rotina de limpeza natural", "bem-estar", "leveza", "constância", "no ritmo da lua nova")
- [x] Tom acolhedor em todos os toques, inclusive no D+90 — nenhuma peça usa culpa ("sumiu", "você abandonou", "cadê você"); todas deixam a porta aberta sem cobrança
- [x] Desconto sempre como oportunidade pontual, nunca como "sempre tem promoção"
- [x] 1 CTA claro por peça
- [x] WhatsApp curto e pessoal (até 4 linhas); e-mail estruturado, com assunto, prévia, corpo e CTA
