# LP VermeFree — VSL + Quiz de Diagnóstico (recomendação, não diagnóstico)

> Prazo: sexta 25/09/2026. Página complementar ao pop-up de diagnóstico já existente no site — não compete com campanhas do mês, roda em paralelo.
> Status: **implementada e publicada como página + tema em rascunho no Shopify** (não publicada ao vivo ainda — falta o vídeo final da VSL e uma revisão humana antes de ir ao ar). Todo o texto e a lógica do quiz já estão funcionando.

---

## FASE 0 — Pop-up já no ar x LP nova: são complementares, não a mesma coisa

Abri o tema publicado da VermeFree no Shopify e li o código-fonte real do pop-up que já está no ar (`snippets/vf-diagnostico-popup.liquid`, renderizado em toda página do site via `theme.liquid`, exceto cart/checkout/account).

**O que o pop-up atual faz, de verdade:**
- Dispara ~4s depois de entrar em qualquer página, 1x a cada 5 dias (cookie).
- Pergunta 1: "Pra quem é?" → Adulto / Kids / Família.
- Pergunta 2 (varia pela resposta 1):
  - Adulto → "O que você mais quer sentir?" (leveza / disposição / sono) — **as três opções mandam pro mesmo lugar**, a página do Protocolo Adulto.
  - Kids → idade (2-4 ou 5-9) → página Kids certa.
  - Família → "o que mais pesa na rotina?" (3 ângulos) → todas mandam pro Kit Família.
- Resultado + captura de e-mail via formulário nativo do Shopify, oferece cupom 5OFF, redireciona pro produto.

**A lacuna real que encontrei:** o pop-up **nunca pergunta se a pessoa já fez o protocolo antes, nem há quanto tempo**. Ele sempre manda "Adulto" pro Protocolo Adulto — mesmo pra quem fez o protocolo há 3 semanas e deveria, pela lógica que você pediu, cair no Óleo de Alho. Essa pergunta de recorrência simplesmente não existe hoje em nenhum lugar do site.

**Risco de compliance que também encontrei (fora do escopo desta tarefa, só reportando):** o formulário de e-mail do pop-up atual não tem um checkbox de opt-in explícito — só o campo de e-mail com a frase "Sem spam." Isso é mais fraco do que o padrão de opt-in que você pediu pra esta LP. Vale o time de Conversão e Ticket revisar, mas não mexi nisso.

**Decisão: são complementares.**
- O pop-up é a rede de captura rápida (2 perguntas) que aparece em qualquer página do site.
- A LP é o destino de tráfego pago/orgânico dedicado: VSL de ~6min + quiz mais completo, que cobre o que o pop-up não cobre (recência de uso → roteia pra Óleo de Alho).
- Pra não dar dois diagnósticos diferentes pra mesma pessoa, a LP **reaproveita literalmente a mesma pergunta inicial e as mesmas opções/emojis** do pop-up ("Pra mim / pra nós adultos", "Pra meu filho", "Pra família toda") e a mesma divisão de idade Kids (2-4 / 5-9), e só ACRESCENTA a pergunta nova de recência dentro do ramo Adulto.
- O opt-in de e-mail da LP é explícito de verdade (checkbox obrigatório + campo `contact[accepts_marketing]` real do Shopify), corrigindo a lacuna que vi no pop-up.
- As tags de e-mail usam o prefixo `quiz-lp-*` (diferente do `quiz-*` do pop-up) e o link final da recomendação usa `utm_source=lp_vsl_quiz` (diferente do `utm_source=popup_diagnostico` do pop-up) — dá pra saber sempre qual dos dois gerou o contato/a venda, sem misturar métricas.

---

## FASE 1 — Roteiro completo da VSL (~6min, pronto pra gravar)

Tom: amiga que explica com calma, olhando pra câmera. Sem trilha de urgência, sem contagem regressiva, sem "só hoje".

### 1. Abertura (0:00–0:30)
> Oi. Se você chegou até aqui, você provavelmente tá com uma dúvida bem específica na cabeça — e não é "será que funciona". É outra: "isso aqui é pra mim, pro meu filho, ou pros dois?"
>
> Eu vou responder essa pergunta com calma nos próximos minutos. E no final, tem um quiz de menos de um minuto que te leva direto pro protocolo certo — sem você ter que adivinhar sozinha.

**[Cut-in]** texto "Adulto? Criança? Os dois?" sobreposto.

### 2. Contexto (0:30–1:30)
> Antes de entrar no como funciona, deixa eu te contar o que a desparasitação natural É — e o que ela NÃO é.
>
> Não é uma emergência. Não é "descobri que tenho verme, preciso tratar agora". É uma rotina — igual malhar, igual fazer aquele check-up anual. A recomendação é fazer de 2 a 4 vezes por ano.
>
> E tem um detalhe que faz parte da nossa forma de fazer: a gente sincroniza o início do protocolo com a lua nova. Não é papo místico prometendo resultado mágico — é só um jeito de criar um ritual, uma data fácil de lembrar, pra você não deixar a rotina de lado.

**[Cut-in]** calendário/ciclo lunar com "início do protocolo".

### 3. Como funciona — Protocolo Adulto (1:30–3:00)
> Vou te mostrar como é o protocolo adulto, os 4 frascos, um por um.

**[Cut-in: produto]** os 4 frascos na mão.

> O primeiro é a Silimarina. Ela começa ANTES dos outros — 15 dias antes da lua nova. É uma cápsula depois do café da manhã e uma depois do jantar. Esse começo adiantado é só pra preparar o terreno antes dos outros três entrarem.
>
> Aí, no dia da lua nova, entram os outros três juntos: a Tintura, que você dilui em água e toma 3 vezes ao dia, antes das refeições. O Óleo de Orégano, uma cápsula também 3 vezes ao dia, junto com a tintura. E a Ornitina, só 1 cápsula por dia, à noite, meia hora antes de deitar.

**[Cut-in]** linha do tempo — Dia -15 (Silimarina) → Dia 0/Lua Nova (Tintura + Orégano + Ornitina).

> Parece complicado escrito, mas na prática é só criar um lembrete no celular e seguir a ordem. Não tem mistério.

### 4. O Kids (3:00–4:00)
> Se é pro seu filho, o processo é bem mais simples — e diferente de propósito.

**[Cut-in: produto]** os 2 frascos líquidos do Kids.

> Kids são 2 frascos líquidos, e a dose é a mesma pra 2 a 4 anos e pra 5 a 9 anos — o que muda é a forma como a gente recomenda dar, pra facilitar a aceitação em cada fase. É diluído em água e tomado 3 vezes ao dia, também por 30 dias.
>
> Eu sei que toda mãe pergunta a mesma coisa: "a partir de que idade posso dar?". A partir de 2 anos.
>
> E sobre o sabor — é laranja, pensado pra criança aceitar sem drama. Dá pra dar puro ou, se ela tiver mais resistência, misturado em outra coisa gelada.
>
> Isso aqui não substitui uma emergência médica, viu? É rotina, cuidado, prevenção. Não é remédio de farmácia.

**[Cut-in]** "a partir de 2 anos" + ícone sabor laranja.

### 5. O depois (4:00–5:00)
> Agora a segunda dúvida que mais chega pra gente: "terminei o protocolo, e agora?"
>
> Entre um ciclo e outro — lembra, 2 a 4 vezes por ano — não é pra ficar parada. É aí que entra o Óleo de Alho Desodorizado: a manutenção mensal, uma cápsula por dia, nos meses em que você não tá fazendo o protocolo completo.

**[Cut-in: produto]** frasco do óleo de alho.

> Pensa assim: o protocolo dos 4 frascos é o cuidado grande, que você faz de tempos em tempos. O óleo de alho é o que segura a rotina no meio do caminho.

### 6. Expectativa honesta (5:00–5:30) — não é opcional
> Antes de eu te convidar pro quiz, preciso ser honesta com você sobre uma coisa.
>
> Isso aqui não é milagre. Não existe protocolo — nosso ou de qualquer marca — que resolve tudo em 3 dias ou garante o mesmo resultado pra todo mundo. O que existe é constância: fazer certinho, no seu tempo, e repetir a rotina ao longo do ano.
>
> Se você tá procurando uma solução instantânea, esse não é o produto certo pra você agora. Mas se você quer um cuidado natural, sério, que vira hábito — aí sim, eu acho que faz sentido a gente continuar essa conversa.

### 7. Fechamento (5:30–6:00)
> Beleza. Se depois de tudo isso você ainda tá em dúvida se é o protocolo Adulto, o Kids, os dois, ou já é hora do óleo de alho — não precisa decidir sozinha.
>
> Logo abaixo desse vídeo tem um quiz rápido, menos de 1 minuto, poucas perguntas. No final ele te mostra qual protocolo faz mais sentido pro seu caso, com a explicação do porquê.
>
> Responde aí embaixo. Te vejo do outro lado.

**[Cut-in]** seta apontando pro quiz abaixo do player.

**Checklist de compliance aplicado:** sem cura/eliminação/erradicação, sem "em X dias", sem comparação de superioridade com farmácia (só a frase-padrão da própria marca "não é remédio de farmácia"), sem promessa de emagrecimento, sem citar médico/influenciador, Dr. William não é citado, ninguém é diagnosticado, seção 6 presente e sem condicional.

---

## FASE 2 — Quiz e mapa de resposta completo

Máximo 3 perguntas em qualquer caminho (bem abaixo do limite de 5), pra não perder gente no meio.

**Pergunta 1 (sempre, idêntica ao pop-up):** "Pra quem é o protocolo?" → 🧍‍♀️ Pra mim/pra nós adultos · 🧒 Pra meu filho · 👨‍👩‍👧‍👦 Pra família toda

**Se "Pra meu filho" — Pergunta 2:** "Qual a idade do seu filho?" → 🧸 2 a 4 anos · 🎒 5 a 9 anos

**Se "Pra mim/adultos" — Pergunta 2 (NOVA, não existe no pop-up):** "Você já fez algum protocolo de desparasitação natural antes?" → 🌱 Não, é minha primeira vez · 🔁 Sim, já fiz antes

**Se "Sim, já fiz antes" — Pergunta 3 (NOVA):** "Há quanto tempo foi o seu último protocolo?" → 📅 Mais de 3 meses · 🕐 Menos de 3 meses

**Se "Pra família toda":** vai direto pra captura de e-mail (sem pergunta extra — a combinação já é suficiente pro Kit Família).

### Mapa de resposta (as 6 linhas pedidas)

| # | Perfil | Destino | Texto do resultado (recomendação, não diagnóstico) |
|---|---|---|---|
| 1 | Adulto, nunca fez | Protocolo Adulto | "Pelo que você contou, o Protocolo Adulto é o que faz mais sentido pra começar: são os 4 frascos que compõem a rotina completa de desparasitação natural, no seu primeiro ciclo." |
| 2 | Adulto, já fez, +3 meses | Protocolo Adulto | "Como já faz mais de 3 meses do seu último protocolo, esse é um bom momento pra recomeçar o ciclo — a recomendação é repetir a rotina completa de 2 a 4 vezes por ano." |
| 3 | Adulto, já fez, -3 meses | Óleo de Alho | "Como você fez o protocolo há pouco tempo, faz mais sentido agora apoiar a rotina com o Óleo de Alho — a manutenção mensal pra manter o cuidado entre um ciclo completo e outro." |
| 4 | Criança 2-4 anos | Kids 2-4 | "Pra essa faixa de idade, o VermeFree Kids 2 a 4 anos é o protocolo pensado certinho pro seu filho — líquido, com dose ajustada e fácil de aceitar." |
| 5 | Criança 5-9 anos | Kids 5-9 | "Pra essa faixa de idade, o VermeFree Kids 5 a 9 anos é o protocolo pensado certinho pro seu filho — líquido, com dose ajustada pra fase escolar." |
| 6 | Adulto E criança | Kit Família | "Como é pra adultos e crianças juntos, o Kit Família reúne os dois protocolos num só lugar — pra cuidar da rotina da casa inteira de uma vez." |

Cada resultado leva a um botão "Ver esse protocolo →" que aplica o cupom `5OFF` (mesmo cupom do pop-up, pra não criar mecânica nova) e abre a página real do produto certo, com `utm_source=lp_vsl_quiz&utm_medium=onsite&utm_campaign=quiz_diagnostico_lp`.

### Captura de e-mail com opt-in explícito
Aparece **antes** do resultado, em todos os 6 caminhos:
- Campo de e-mail obrigatório.
- Checkbox obrigatório (destacado visualmente, fundo amarelo): *"Aceito receber e-mails da VermeFree com novidades e cuidado natural pra família. Posso cancelar quando quiser."*
- O botão "Ver minha recomendação →" fica **desabilitado** até e-mail válido + checkbox marcado — não dá pra pular o opt-in.
- Ao confirmar, grava o contato no Shopify com `contact[accepts_marketing] = 1` (o campo real de consentimento de marketing do Shopify — mais forte que o pop-up atual, que não usa esse campo) e tags `quiz-lp-vsl`, `quiz-lp-<publico>`, `quiz-lp-<resultado>`.

---

## FASE 3 — Implementação (o que foi construído de verdade)

Implementei como página nativa do Shopify (mesma tecnologia do site: seção Liquid + template), não como arquivo solto, porque é assim que o site da VermeFree já funciona — a página fica no mesmo painel, editável pelo time, sem depender de outra plataforma.

**⚠️ Importante — não editei o tema publicado (ao vivo).** O sistema tem uma trava de segurança que bloqueia escrita direta no tema publicado — corretamente, porque isso poderia quebrar o site pra visitantes reais sem revisão. Segui o caminho certo: **dupliquei o tema em um tema-rascunho (não publicado)** e construí tudo lá.

**O que existe agora, pronto e funcional, no tema rascunho `VermFree — Draft LP VSL+Quiz (25/09)`:**
- `sections/vf-lp-vsl-quiz.liquid` — VSL no topo + quiz completo logo abaixo, com todo o texto e a lógica de roteamento das 6 combinações, mobile-first (o player vira 9:16 em telas pequenas, 16:9 a partir de 700px).
- `templates/page.vsl-quiz.json` — template que usa essa seção.
- `assets/vf-vsl-legendas.vtt` — legendas em português já escritas e sincronizadas com os timestamps do roteiro, conectadas ao `<track>` do vídeo.
- Página `Adulto ou Kids? Descubra seu protocolo` (`/pages/descubra-seu-protocolo`), criada como **rascunho (não publicada)**, apontando pro template acima.

**Vídeo:** ainda não existe o arquivo final (a Fase 1 pediu o roteiro pronto pra gravar, não um vídeo pronto). Deixei a seção pronta pra receber a URL do arquivo assim que for gravado — tem um campo "Vídeo (URL .mp4)" no editor de tema. Enquanto esse campo estiver vazio, a página mostra um aviso interno claro ("Vídeo em produção...") no lugar do player, pra ninguém publicar por engano sem o vídeo.

**Como revisar/editar:**
- Preview do tema rascunho (visual completo, inclusive com o quiz funcionando): abra o painel do Shopify → Loja Online → Temas → tema **"VermFree — Draft LP VSL+Quiz (25/09)"** → **Visualizar**. Ou direto: `https://vermefree.com.br/pages/descubra-seu-protocolo?preview_theme_id=164655497435` (só funciona logado no admin da loja).
- Editor visual: painel do tema rascunho → Personalizar → template da página `vsl-quiz` → seção "LP · VSL + Quiz" (lá dá pra colar a URL do vídeo final, trocar textos, etc. sem mexer em código).
- Página no admin: Loja Online → Páginas → "Adulto ou Kids? Descubra seu protocolo".

**Pra ir ao ar:** depois que o vídeo estiver gravado e revisado, o caminho mais seguro é pedir pra um dev copiar só os 3 arquivos novos (`sections/vf-lp-vsl-quiz.liquid`, `templates/page.vsl-quiz.json`, `assets/vf-vsl-legendas.vtt`) pro tema **publicado** e então publicar a página — em vez de publicar o tema-rascunho inteiro, que substituiria o tema ao vivo por completo e poderia perder qualquer mudança feita nele desde a duplicação.

---

## FASE 4 — Testes obrigatórios

**⚠️ Limitação que preciso ser transparente sobre:** o ambiente onde eu rodo bloqueia o acesso direto a `vermefree.com.br` e também ao domínio `myshopify.com` da loja (confirmei isso tentando abrir os dois de várias formas — todos retornaram bloqueio de rede por política do ambiente, não erro da loja). Ou seja, **eu não consegui abrir a página publicada/pré-visualização real com meu próprio navegador** pra clicar nela como um humano faria. Isso não é uma limitação da Shopify nem da página — é só uma restrição do ambiente onde eu processo essa tarefa. Um humano logado no admin da loja, no navegador normal, não tem esse bloqueio.

Pra compensar isso com rigor, extraí o HTML/CSS/JS **exatamente igual** ao que está no arquivo publicado no tema (não uma versão simplificada) e rodei em um navegador automatizado local, em viewport de celular (390×844, tamanho de iPhone), testando as seis combinações ponta a ponta:

| # | Caminho testado | Chegou na página certa? | Título do resultado bate com a tabela? | Opt-in bloqueava o botão até marcar? |
|---|---|---|---|---|
| 1 | Adulto → nunca fez | ✅ `protocolo-desparasitacao-adulto-vermefree` | ✅ | ✅ |
| 2 | Adulto → já fez → +3 meses | ✅ `protocolo-desparasitacao-adulto-vermefree` | ✅ | ✅ |
| 3 | Adulto → já fez → -3 meses | ✅ `oleo-de-alho-desodorizado-500mg` | ✅ | ✅ |
| 4 | Criança → 2 a 4 anos | ✅ `antiparasitario-infantil-natural-vermefree-kids-2-a-4-anos` | ✅ | ✅ |
| 5 | Criança → 5 a 9 anos | ✅ `antiparasitario-infantil-natural-vermefree-kids-5-a-9-anos` | ✅ | ✅ |
| 6 | Família (adulto + criança) | ✅ `kit-familia-vermefree-2-adultos-2-criancas` | ✅ | ✅ |

Em todos os 6: zero erros de JavaScript, o cupom `5OFF` e os parâmetros de UTM foram montados corretamente na URL final, e o registro que seria enviado ao Shopify veio com `contact[accepts_marketing]: "1"` **só depois** do checkbox marcado (testei também tentar enviar com e-mail preenchido mas checkbox desmarcado — o botão continuou desabilitado nos 6 casos).

**Confirmação: nenhum dos 6 resultados soa como diagnóstico.** Rodei um filtro automático procurando frases do tipo "você tem", "indica presença/infestação", "apresenta sinais" nos 6 textos de resultado — nenhuma ocorrência. Os 6 textos usam sempre a forma "pelo que você contou / faz mais sentido / é o protocolo pensado pra..." — recomendação de produto, nunca veredito de saúde.

**O que eu NÃO consegui testar por mim mesma (peço que o time confirme antes de publicar):**
- Assistir a VSL de verdade no celular com/sem som — porque o arquivo de vídeo ainda não existe (é o roteiro que estava pedido nesta fase, não a gravação). As legendas já estão escritas e conectadas; recomendo, assim que gravarem, only conferir se o tempo de fala bateu com os timestamps do `.vtt` (ajustar timestamps é rápido se a fala ficar mais rápida/lenta que o estimado).
- Clicar na página de verdade dentro do painel do Shopify (bloqueio do meu ambiente, explicado acima) — pedi que isso seja o único passo manual antes de publicar: abrir o link de preview do tema rascunho e passar pelo quiz uma vez.
- Conferir que a página não conflita visualmente/tecnicamente com o pop-up ao vivo: como são independentes (o pop-up é global via `theme.liquid`, a LP é uma página isolada) e a LP não foi tocada no tema publicado, não há como um conflitar com o outro em produção — mas o pop-up VAI continuar aparecendo por cima da LP também (ele dispara em qualquer página do site, exceto cart/checkout/account). Isso é esperado e não é um bug; se quiserem que a LP fique sem o pop-up por cima, dá pra adicionar a rota da LP na lista de exclusão do pop-up (`vf-diagnostico-popup.liquid`, variável `path`) — não fiz essa mudança porque webria mexer no tema publicado, fora do escopo que me foi dado sem confirmação.

---

## Link da página

- **Preview (tema rascunho, ainda não publicada):** `https://vermefree.com.br/pages/descubra-seu-protocolo?preview_theme_id=164655497435` (abrir logado no admin da loja)
- **Admin da página:** Shopify Admin → Loja Online → Páginas → "Adulto ou Kids? Descubra seu protocolo"
- **Tema rascunho:** "VermFree — Draft LP VSL+Quiz (25/09)"

## Pendências antes de ir ao ar
1. Gravar a VSL com o roteiro acima e subir o `.mp4` no campo "Vídeo (URL .mp4)" da seção (editor de tema).
2. Conferir/ajustar o timing das legendas (`assets/vf-vsl-legendas.vtt`) contra o áudio real.
3. Um humano abrir o preview e passar pelo quiz uma vez (meu ambiente não teve acesso pra fazer esse clique final).
4. Pedir a um dev pra copiar os 3 arquivos novos pro tema publicado e então publicar a página.
