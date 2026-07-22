# Histórico de copies — Lançamento VermeFree (abril–julho/2026)

> Fonte: conversa compartilhada (claude.ai) enviada pelo Gabriel, extraída em 22/07/2026.
> Cobre desde o pré-lançamento (abertura de carrinho, escassez de estoque) até a Semana da Lua Nova (13-17/07).
> Uso: referência de tom, formato e estrutura de campanhas já testadas. **As regras vigentes de compliance estão em `CLAUDE.md` — onde este histórico conflitar com o CLAUDE.md (ex.: menção ao Dr. William, claims biológicos sobre lua/parasitas, números de escassez inventados), o CLAUDE.md prevalece.**

---

## Contexto de negócio revelado neste histórico

- **Pré-lançamento (abril/2026):** 7 dias de carrinho aberto. 362 kits vendidos, R$ 132.240,37 de faturamento, base de 1.563 pessoas (alunos A Nova Saúde), taxa de conversão 23,16%, CAC R$ 3,41, ROAS 107x. Investimento de R$ 1.234,47 em API de WhatsApp.
- **Preços do pré-lançamento (parcelado 3x sem juros):** Adulto R$ 112,33 · Kids 2-4 R$ 90,00 · Kids 5-9 R$ 129,67 · Kit Família (-15%) R$ 282,20. *(Diferem dos preços à vista documentados no CLAUDE.md atual — preços mudam por campanha, sempre confirmar o valor vigente antes de publicar.)*
- **100 primeiros compradores:** cashback de 20% + frete grátis Brasil (efeito avalanche — quase 200 vendas nas primeiras horas).
- **Lançamento oficial:** live 20/05, formato apresentação + Q&A + abertura de carrinho, lote de 1.000 kits.
- **Dia D (07/07):** campanha de 24h — 10% OFF + frete grátis (sem valor mínimo) + bônus "Manual da Desparasitação".
- **Semana da Lua Nova (13-17/07):** 5% OFF + Manual da Desparasitação pros 100 primeiros pedidos + sorteio de 1 Kit Adulto entre quem comprar até 17/07. Abertura de pedidos à meia-noite de 13/07.
- **Cupons usados:** `5OFF` (5%, uso geral/recorrente), `PRIMEIRA5` (5%, só primeira compra), `ZEROTOXINAS10` / `ANOVASAUDE10` (10%, parcerias cruzadas — cupom dado "pelo Dr. William" a alunos de outros produtos do ecossistema).
- **Regra de mecânica de desconto:** desconto de campanha some do preço-base (não é cupom) pra empilhar com cupom de parceria sem conflito.
- **Frete grátis:** acima de R$ 399 (mesmo valor do CLAUDE.md atual).

⚠️ **Atenção:** este histórico mostra o Dr. William sendo citado nominalmente e como aval técnico em várias peças (ex.: "o Dr. William explicou que remédio comum mira só o verme adulto", API disparada do perfil pessoal dele, cupom "conseguido" por ele). **O CLAUDE.md vigente proíbe isso terminantemente, sem exceção.** Essa prática histórica não deve ser repetida — foi provavelmente por isso que a regra dura foi criada.

---

## Formato de API (disparo individual) — padrão consolidado

Estrutura de 5 blocos, usada em praticamente toda campanha:

```
DD/MM - HHh
Base: [nome da base]

{{1}} Gancho de abertura (emoji + frase curta)

{{2}} Oferta / contexto principal (o que está rolando, benefícios em bullets)

{{3}} Justificativa / urgência real ou prova social

{{4}} Reforço de benefícios ainda válidos + o que muda depois do prazo

{{5}} Toque em uma das opções abaixo com sua resposta:

BOTÃO: [ação principal, ex: "Quero garantir meu kit"]
BOTÃO: [captura indeciso, ex: "Quero ver os preços" / "Tenho uma dúvida"]
BOTÃO: [saída, ex: "Não tenho interesse" / "Agora não"]
```

Aprendizados sobre os botões:
- O botão do meio ("quero ver os preços" / "tenho uma dúvida") é o que **captura o lead morno** — não descartar.
- O botão de recusa serve pra **limpeza de base** (quem clica não recebe mais disparos daquela campanha).
- Se a plataforma limitar a 2 botões, cortar o de recusa antes do botão do meio (o do meio traz mais retorno operacional).

## Formato de mensagem de grupo

Mais solto que a API — tom de conversa, sauda ("Bom dia, gente"), fecha com convite a interagir ("qualquer dúvida chama aqui", pedido de reação com emoji pra medir interesse e gerar prova social pública).

## Formato de e-mail

- Assunto curto, muitas vezes com parênteses pra gerar curiosidade sem virar clickbait vazio (ex.: "Faltam 4 horas (e uma pergunta honesta)").
- Pré-cabeçalho reforça a oferta em 1 linha.
- Corpo dividido por `---` em blocos escaneáveis (o quê / por quê / prazo / CTA).
- Duas versões testadas: **longa** (storytelling, converte melhor em quem ainda tem dúvida) e **objetiva** (converte melhor em quem já decidiu e só precisa do link — "salva esse e-mail, abre amanhã e resolve em 3 minutos").

---

## Cadência de campanhas de lançamento/urgência (padrão de 24h-72h)

**Antecipação (dias antes):**
- T-7 a T-3: aviso institucional, sem revelar oferta completa (curiosidade > informação)
- Véspera manhã: reforço, ainda sem revelar tudo
- Véspera noite: revelação completa da oferta + pedido de reação/comprometimento público ("reage com 🔥 se for garantir")

**Dia da campanha (24h):**
- Abertura (madrugada/manhã cedo): sirene + oferta completa + prazo
- Meio da manhã: segmentação por ICP (ex. Adulto vs Kids)
- Meio-dia: prova social / dado
- Tarde: escassez (se real) ou benefício emocional (estado futuro / bifurcação)
- Início de noite: gancho família / ticket maior
- Noite: confronto direto da procrastinação ("o que te segura não é preço")
- Fechamento (última 1-2h): contagem regressiva curta, sem argumento novo, só o link

**Pós-campanha:**
- Agradecimento + fechamento simbólico (ex.: "esgotou")
- Transição pra lista de espera / próximo ciclo, com motivo concreto pra entrar (benefício exclusivo real, não vago)

## Padrão de comunicação em "modo perpétuo" (fora de campanha)

Depois de lançamento/campanha, o tom muda radicalmente: **sem contagem regressiva, sem "últimas unidades"**. Foco em benefício + conveniência + facilidade de compra (ex.: lembrete de frete grátis acima de R$399). Insistir em urgência falsa nesse momento queima a base.

---

## Alertas recorrentes que o próprio histórico já levantava (e que continuam valendo)

1. **Nunca inventar número de estoque/vendas.** Toda vez que apareceu um número de escassez ("39% restante", "61% vendidos", "X pedidos hoje"), a orientação foi: só usar se for real ou aproximação honesta. Número redondo demais ou "chutado" é o gatilho que mais queima credibilidade em base de saúde natural (público cético, já foi enganado antes).
2. **Depoimentos citados com iniciais/cidade** (ex. "M.R., SP") só podem ser usados se forem reais e com autorização. Caso contrário, usar depoimento anônimo genérico.
3. **Datas de prazo (próxima lua nova, fim de lote) precisam ser reais.** Prazo chutado que não se confirma depois queima a campanha seguinte.
4. **Claims biológicos fortes sobre mecanismo de parasitas/ciclo lunar** (ex. "é à noite que eles se movem e botam ovo", "atividade parasitária aumenta na lua cheia") são licença poética sem consenso científico — historicamente foram sinalizados como risco e suavizados. Com a regra ANVISA do CLAUDE.md atual, evitar completamente esse tipo de afirmação mecanicista.
5. **Claims associando sintomas específicos a diagnóstico** (ex. relacionar comportamento infantil a "hiperatividade por parasitose") geram risco de controvérsia e devem ser suavizados ou evitados.
6. **Promessas de disponibilidade da equipe** ("respondo até às 22h", "equipe de plantão") só podem entrar na copy se puderem ser cumpridas de fato.
