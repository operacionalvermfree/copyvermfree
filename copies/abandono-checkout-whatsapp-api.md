# Abandono de Checkout — WhatsApp API (4 Toques) · VermeFree

> Público: quem iniciou a compra mas não concluiu o checkout. Objetivo: trazer de volta pra finalizar, com dois caminhos — retomar a compra (link) ou falar com atendimento. Excluir da régua quem já finalizou a compra (checar antes de CADA disparo, não só no início).

## O que preencher
- `{{1}}` = primeiro nome
- `{{2}}` = produto/kit que ficou no carrinho (se disponível)
- `{{3}}` = link de retomada do checkout (rastreável)
- `{{4}}` = cupom do Toque 4 (código + % + prazo)

---

## TOQUE 1 — 30 min · Lembrete pessoal (⚠️ Template HSM — business-initiated)

```
Nome sugerido do template: vermefree_checkout_toque1_lembrete
Categoria: MARKETING
Tipo: Template HSM (obrigatório — disparo fora da janela de 24h, iniciado pela marca)

BODY:
Oi {{1}}! Vi que você separou {{2}} mas não chegou a finalizar.
Ainda quer continuar de onde parou?

BOTÃO 1 (CTA URL): Retomar minha compra → {{3}}
BOTÃO 2 (Quick Reply): Falar com atendimento
```

**Variáveis usadas:** `{{1}}`, `{{2}}`, `{{3}}`

---

## TOQUE 2 — 6h · Quebra de objeção + prova social

```
Nome sugerido do template: vermefree_checkout_toque2_objecao
Categoria: MARKETING
Tipo: Template HSM (ver nota abaixo sobre janela de 24h)

BODY:
Oi {{1}}, passando rapidinho: a desparasitação natural é uma rotina, não um susto — funciona melhor quando você começa com calma, no seu tempo.

Quem já fez o protocolo costuma contar que sentiu mais leveza e constância. Resultados podem variar de pessoa pra pessoa.

Se tiver alguma dúvida sobre {{2}}, é só chamar a gente.

BOTÃO 1 (CTA URL): Retomar minha compra → {{3}}
BOTÃO 2 (Quick Reply): Falar com atendimento
```

**Variáveis usadas:** `{{1}}`, `{{2}}`, `{{3}}`

---

## TOQUE 3 — 24h · Urgência gentil

```
Nome sugerido do template: vermefree_checkout_toque3_urgencia
Categoria: MARKETING
Tipo: Template HSM (ver nota abaixo sobre janela de 24h)

BODY:
Oi {{1}}, seu carrinho com {{2}} continua aberto — mas as unidades não ficam reservadas pra sempre.

Se quiser continuar de onde parou, é rapidinho.

BOTÃO 1 (CTA URL): Retomar minha compra → {{3}}
BOTÃO 2 (Quick Reply): Falar com atendimento
```

**Variáveis usadas:** `{{1}}`, `{{2}}`, `{{3}}`

---

## TOQUE 4 — 48h · Oferta final (cupom, prazo curto)

```
Nome sugerido do template: vermefree_checkout_toque4_final
Categoria: MARKETING
Tipo: Template HSM (ver nota abaixo sobre janela de 24h)

BODY:
Oi {{1}}, essa é a última vez que eu te chamo sobre {{2}} 🌿

Preparei um cupom especial pra fechar: {{4}}. Vale só até amanhã.

BOTÃO 1 (CTA URL): Usar cupom e retomar agora → {{3}}
BOTÃO 2 (Quick Reply): Falar com atendimento
```

**Variáveis usadas:** `{{1}}`, `{{2}}`, `{{3}}`, `{{4}}`

---

## NOTAS DE IMPLEMENTAÇÃO

**Opt-in:** só entram na régua contatos que aceitaram receber WhatsApp da VermeFree.

**Sobre a janela de 24h:** o Toque 1 sempre precisa ser template HSM aprovado (é o primeiro contato, fora da janela de sessão). Se o cliente **responder** ao Toque 1 — inclusive clicando no botão "Falar com atendimento" — abre-se a janela de conversa livre de 24h, e os toques seguintes PARA AQUELE CONTATO podem virar mensagem de sessão livre (sem precisar de template aprovado). Se ele não responder, os Toques 2, 3 e 4 continuam sendo business-initiated e também precisam ser templates HSM aprovados pela Meta — por isso os três já vêm marcados como template aqui, prontos pra submissão.

**Exclusão da régua:** checar o status do pedido antes de **cada** disparo (não só na entrada da régua) — se o cliente finalizar a compra entre um toque e outro, a régua deve parar imediatamente pra esse contato, em qualquer ponto da sequência.

**Timing:** os intervalos (30 min / 6h / 24h / 48h) contam a partir do momento do abandono do checkout, não a partir do toque anterior.

**Mensuração de vendas recuperadas:**
- `{{3}}` deve ser um link de retomada com parâmetro de rastreio único por contato (idealmente amarrado ao ID do checkout/carrinho abandonado), pra atribuir a venda mesmo que ela feche direto pelo link.
- `{{4}}` (cupom do Toque 4) deve ser exclusivo dessa régua, pra atribuir separadamente as vendas fechadas por causa da oferta final.
- Com os dois sinais (clique no link rastreado + uso do cupom), dá pra medir tanto recuperação "espontânea" (toques 1–3) quanto recuperação por incentivo (toque 4).

**Botão "Falar com atendimento":** configurar como quick reply que aciona o transbordo pro time humano e, ao mesmo tempo, conta como resposta do cliente — abrindo a janela de 24h a partir daí.

## CHECKLIST ANVISA

- [x] Sem claim de cura / sem "elimina/erradica/mata" / sem "em X dias"
- [x] Não cita médico nem influenciador
- [x] Não diagnostica o leitor
- [x] Tom natural/acolhedor, sem culpa nem alarme (nenhum toque usa "sumiu"/"cadê você")
- [x] Linguagem segura de desparasitação ("rotina", "leveza", "constância")
- [x] Cupom só no Toque 4, como exceção com prazo curto
- [x] Cada toque com 1 CTA principal (retomar compra), mais o caminho alternativo de atendimento
- [x] Fala com mulher/mãe 30–50 que cuida da família
