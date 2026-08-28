# REPERTORIO-TECNICO.md — catálogo destilado da biblioteca getlayers/meez.design

> Matéria-prima bruta: `VermeFree/LP-KIT/LP-KIT/` no Drive (ver `FONTES.md` para os IDs de pasta). Este arquivo é o resumo técnico de ~35 documentos de referência de design/animação de sites — pra não precisar reabrir tudo no Drive toda vez que for construir uma LP.
>
> **Repertório de inspiração, nunca template pra colar.** Nenhum desses sites tem qualquer relação com VermeFree (são agências, apps, moda, tênis, bebida, etc. fictícios usados só como catálogo de técnica). O valor está na técnica de interação/motion, não no conteúdo. Ver seção 6 pra recomendação de quais técnicas combinam com o tom natural/consultivo da marca.

---

## 0. Sistema de tokens/botão validado em código real (Botanika, 8 LPs publicadas)

> Diferente do resto deste arquivo (prompts especulativos do getlayers/meez.design), isto veio de **código-fonte real e publicado**: as 8 LPs de produto da Botanika (`BotanikaHub/Botanika-Desing`, branch `lp`), lidas via `raw.githubusercontent.com` em 03/08. É o mesmo "template de tokens" reaproveitado nas 8 (só recolorindo hex por produto) — por isso vale mais confiança que os prompts do getlayers/meez. Já testado na prática: usado pra elevar `linktree-vermefree/index.html`.

**Tokens (adaptar cores pra paleta de cada marca, manter a estrutura):**
```css
--bg / --bg2      /* dois tons de fundo próximos, nunca um só sólido */
--grad            /* 2 cores da marca em diagonal, 115-120deg */
--glass           /* branco a ~4.5% opacidade, pra cards translúcidos */
--line            /* cor de acento a ~15-30% opacidade, pra bordas sutis */
--ease            /* cubic-bezier(.2,.7,.2,1) — "overshoot suave", não linear */
--radius: 22-24px (cards) · --radius-sm: 15-16px (ícones/chips) · botões sempre 100px (pílula)
```

**Botão CTA (o padrão de maior retorno visual, replicado nas 8 LPs sem variação):**
- Pílula (`border-radius:100px`), fundo em `var(--grad)`.
- Sombra em duas camadas: glow colorido difuso por fora (`0 12-14px 34px -12px rgba(cor-acento,.7)`) **+** inset de brilho por dentro (`inset 0 1px 0 rgba(255,255,255,.35-.4)`) — dá efeito "pílula de vidro 3D".
- Hover: só intensifica a sombra (não muda cor) — `transition:transform .25-.3s var(--ease), box-shadow .3s var(--ease)`.
- `:active{transform:scale(.97)}` (feedback de "pressionar") — variante mais simples que `translateY(-2px)` no hover.
- Sheen opcional: `::after` com gradiente branco enviesado (`skewX(-18deg)`) que varre o botão via `@keyframes` só no `:hover`.
- Botão magnético (opcional, desktop-only): no `mousemove`, desloca o próprio botão em fração da distância do cursor ao centro (`*.18-.35` em x, `*.28-.4` em y via `translate()`), volta a 0 no `mouseleave`. **Sempre** atrás de `matchMedia('(hover:hover) and (pointer:fine)')` e `prefers-reduced-motion` — nunca em mobile/touch.

**Header/identidade:** pílula flutuante (`margin:12px auto`, `border-radius:100px`, `backdrop-filter:blur(14px)`), não barra full-width. Logo = wordmark tipográfico + um "pip" — ponto circular pequeno com `background:var(--grad)` e `box-shadow` glow — em vez de depender de arquivo de imagem.

**Loader de entrada:** tela cheia com wordmark + contador `000→100` (fonte display com gradiente via `background-clip:text`) + barra fina. JS incrementa por `setInterval` com números aleatórios (não é progresso real de rede) e sempre tem **timeout de segurança** (`setTimeout` de 1.8-3s) pra garantir que a página nunca fica travada atrás do loader. Sempre checar `prefers-reduced-motion` (pula direto pro conteúdo) e ter fallback `<noscript>` que esconde o loader se JS não rodar.

**O que NÃO portar pra página de tela única (bio-link, sem scroll de produto):** ScrollTrigger/Lenis, canvas/WebGL de fundo, parallax por seção, countdown de escassez, marquee de ingredientes — todo esse aparato pressupõe uma LP de venda longa. Ver seção 6 abaixo pra critério equivalente aplicado ao repertório getlayers/meez.

---

## 1. Cenas 3D de fundo procedurais (`01_getlayers/Prompts/3D Scenes/`)

Todas as 6 cenas compartilham o **mesmo esqueleto de engenharia** (vale reaproveitar como base genérica, trocando só geometria/paleta/deformação):

- Three.js r0.143.0 via importmap CDN (unpkg) — sem bundler, HTML autocontido.
- 3 `EffectComposer`s (torus / bloom / final) trocando `camera.layers` por frame.
- Um `FinalPass` (shader customizado) somando fundo + "chamas de canto" animadas (função `warp3d` compartilhada) + as texturas dos outros composers.
- Scroll mapeado 0→1 com **double-lerp** (dois estágios de damping) pra suavizar o "mergulho" de câmera.
- Cursor em "world-space void": unproject do NDC no plano z=0 pra repelir/atrair partículas próximas.
- Camada opcional de "poeira ambiente" (motes) presa à câmera, com função `warp()` GLSL própria.

| Cena | Visual | Técnica de destaque | Uso sugerido |
|---|---|---|---|
| **Storm** | Orbe de plasma pulsante, gradiente carmesim→magenta→dourado, ~50k pontos | Distribuição em esfera por Marsaglia + viés radial; gradiente 3 estágios via `smoothstep` | Hero de impacto/urgência — não combina com tom calmo da marca |
| **Cosmic Dust** | Poeira cósmica âmbar/ferrugem à deriva, minimalista (940 pontos) | Wrap infinito via `fract()`; fade-in com smootherstep | A mais serena das 6 — possível fundo de seção "constância/rotina" se recolorida em verde/bege |
| **Elliptical Galaxy** | Céu de 79 galáxias elípticas, núcleo dourado, 90k estrelas | Padrão de "clusters" (N frames + M pontos distribuídos entre eles); scroll só (sem cursor) | Fundo passivo de seção editorial, sem necessidade de interação |
| **Starfield Close** | Túnel de estrelas verde-menta/jade/osso, cintilação | Wrap 1-eixo via `mod()`; paleta discreta por índice (0/1/2) | Recolorido em tons verdes bate com a paleta VermeFree — mas é WebGL pesado pra uma LP de conversão |
| **Flow Wave** | Mar de partículas ondulando (noise Simplex), verde-esmeralda | SphereGeometry densa remapeada pra "sheet" plano; 2 oitavas de `snoise` (FBM simplificado) | Paleta já é verde — mais próxima visualmente da marca, mas ainda é WebGL caro |
| **Tunnel** | Wormhole índigo→ciano com paredes ondulando | Remapeamento esfera→cilindro via trigonometria; múltiplas camadas de `snoise` | Efeito "uau" mas fora do tom natural/honesto da marca |

**Recomendação geral:** WebGL procedural pesado (Three.js + shaders) tem alto custo de manutenção/performance. Só vale a pena numa LP da VermeFree se for a *assinatura única* de um produto específico (ex: Kit Família) — nunca como padrão repetido entre LPs.

---

## 2. Templates completos de site (`01_getlayers/Prompts/Templates/`)

| Site | Nicho fictício | Técnica de destaque | Stack | Relevância pra VermeFree |
|---|---|---|---|---|
| **Flowstate** | App de foco/deep-work | Simulação de fluido WebGL reagindo ao mouse + cursor automático que nunca deixa o fundo estático; texto revela palavra-a-palavra | WebGL puro + Lenis | Efeito pesado demais; grid rem-adaptativo é reaproveitável |
| **Loopstack** | Marca genérica (footer hero) | Cursor customizado duplo (anel + pill com lerp); reveal letra-a-letra do wordmark; vídeo de fundo com gradiente | CSS + JS vanilla | Estrutura de "tela única, CTA único" pode servir pra uma LP de oferta pontual (ex: cupom Lua Nova) |
| **Soda** | Bebida (lata 3D) | Produto 3D via `<model-viewer>` inclinando com o mouse; repulsão de decorativos pelo cursor; troca de variante coreografada com GSAP | GSAP + `<model-viewer>` | Padrão de "seletor de variante/sabor" é direto aplicável ao Protocolo Adulto vs. Kids vs. Kit Família |
| **Baseline** | Clube de tênis (institucional) | Loader com barra de progresso; grid 100% rem-adaptativo (fórmula documentada); reveal de linha via clip-mask; seções "recortadas" com `border-radius` + margem negativa | Spring helper JS próprio + Lenis | **Mais aplicável ao tom da marca** — estrutura editorial/institucional, sem WebGL pesado |
| **Laocoön** | Escultura/arte (cinematográfico) | Câmera 3D orbitando 360° o objeto central conforme scroll; shader de fundo com paleta migrando ao longo da página; partículas de faísca | Three.js + shader custom | Técnica de câmera orbital é interessante pra "produto herói" (ex: kit de frascos), mas o efeito geral é caro |
| **Lumora** | Estúdio de design (institucional) | **Liquid reveal via canvas 2D** (antes/depois pintado pelo cursor, sem WebGL); loader com contador 000→100; count-up de estatísticas disparado por scroll | Canvas 2D + spring helper + Lenis | **Muito aplicável** — liquid reveal sem WebGL é leve e pode mostrar "antes/depois" do protocolo; count-up serve pra depoimentos/números |

---

## 3. Sites/seções completos (`02_meez.design/WebSites/Prompts/` + `02_meez.design/Sections/`)

| Site | Nicho fictício | Estrutura/seções | Estilo | Relevância pra VermeFree |
|---|---|---|---|---|
| **Wellness Companion** ("Vitaforge Daily") | App de wellness/quiz | Mockup de tela única (quiz de seleção + botão de voz + slide-to-confirm) | "Liquid glass" em componentes, fundo desfocado | Padrão de quiz interativo pode virar página de "qual protocolo é ideal pra você" |
| **Travel Journal** | App de viagem | Cards de destino full-bleed + nav bar flutuante | "Liquid glass", tipografia grande semi-transparente | Baixa relevância direta |
| **Cross-Border** / **Cargo Group** ("CARGOX GROUP") | Logística B2B | Hero com vídeo + mapa-múndi animado (rotas SVG) + stats + formulário | Preto/amarelo vibrante, Barlow Condensed | Baixa relevância de nicho, mas o padrão de "mapa com rotas animadas" é reaproveitável pra uma seção "ingredientes de N países"/"protocolo em N passos" |
| **Coffee Rewards** | App de fidelidade (café) | Perfil com stats, "liquid glass" avançado via `feDisplacementMap` (refração real) | Escuro/quente, Neue Haas Unica | Efeito de vidro líquido avançado é vistoso, mas alto custo de implementação |
| **"prmpt"** (PROMPT.docx) | Moda/streetwear (drop) | Scroll-driven: vídeo com scrub por cursor → painel desliza revelando galeria de produtos | Preto/branco, `mix-blend-mode: exclusion` | Estética editorial extrema, não combina com tom acolhedor da marca |
| **Subscription Agency** ("Alwayzz") | Agência criativa | Navbar com drawer fullscreen, linhas decorativas pulsantes, marquee de serviços/logos | Preto/branco, Inter + Source Serif itálica | Estrutura de "trusted by" com marquee é reaproveitável pra prova social |
| **Wellbeing OS** ("flowpath") | SaaS produtividade/bem-estar | Hero fullscreen com vídeo, dropdowns no hover, "liquid glass" | Fonte custom, glass | Nicho "wellbeing" é próximo — vale olhar a paleta/tom |
| **Stillmind** ("Lumora" — site diferente do template Lumora acima) | App de mindfulness | 4 vídeos em crossfade selecionáveis, overlay com animação de respiração, modo escuro condicional | Instrument Serif itálico, glass | Conceito de "trocar cenário de fundo" (Golden Hour/Still Water/etc.) poderia virar "trocar produto" na VermeFree |
| **Celestial Renewal** ("Serene") | Beleza/wellness de luxo | Hero com vídeo + seção de citação com parallax (nuvens entrando lateralmente) | Azul-petróleo escuro, Dancing Script + Instrument Serif | **Tom "wellness natural"** é o mais próximo de todos os exemplos — parallax de lerp é técnica leve e reaproveitável |
| **Creative Portfolio** ("Viktor") | Portfólio pessoal | Vídeos crossfade selecionáveis, indicador "available" pulsante, tipografia extrema (200px) | Preto/branco + rosa, Figtree | Baixa relevância de nicho |
| **CozyPaws** | Pet shop e-commerce | Hero sem scroll: heading central + card de produto + card de vídeo/review sobrepostos + 3 imagens com overlays | Verde-menta + laranja, Inter + DM Serif Display | **E-commerce de bem-estar/consumo direto** — estrutura de hero com card de produto + review é bem próxima do que uma LP de produto VermeFree precisa |
| **Wellness Balance** ("TerraElix") | Suplementos à base de plantas | Headline com reveal palavra-por-palavra, imagem de produto flutuante, carrossel automático de 4 cards, contador "+14K" | DM Sans + Inter, foto full-screen | **O mais próximo de todos em nicho** (suplemento natural) — código-fonte HTML completo disponível como referência de estrutura |
| **Tech-Forward** ("NeuralKinetics") | Fintech/tech | Vídeo de fundo centralizado, animações sequenciais Framer Motion | Preto/branco extremo, Inter 300 | Baixa relevância |
| **Vision Reveal** ("Studio"/Nora Kessler) | Portfólio criativo | Spotlight que segue o mouse via canvas + CSS mask; splash inicial de blocos que se abrem | Cinza claro + creme, Inter | Efeito de "spotlight reveal" poderia destacar um ingrediente/selo específico ao passar o mouse |

**Os 4 mais relevantes pro tom/nicho da VermeFree, em ordem:** Wellness Balance (TerraElix) → Celestial Renewal (Serene) → CozyPaws → Wellbeing OS (flowpath). Vale reabrir esses no Drive quando for desenhar a primeira LP de verdade.

---

## 4. Assets brutos disponíveis no Drive (não processados aqui, só catalogados)

### Zips de cenas 3D (`01_getlayers/Zips/Backgrounds/`) — pesados, 12–60MB cada
`glass-flower.zip` · `metal-human.zip` · `hills.zip` · `flower-arc.zip` · `purple-desert.zip` · `flower-field.zip` · `material-hills.zip` · `sea-storm.zip`

### Vídeos de fundo (`02_meez.design/Backgrounds/`) — 8 mp4, 2.6–44MB cada
`ms-nature.mp4` · `ms-3d.mp4` · `ms-nature-nice.mp4` · `ms-person.mp4` · `ms-energy.mp4` · `ms-dark-flowers.mp4` · `ms-flower-ground.mp4` · `ms-3d-sea.mp4`

> ⚠️ **Os 8 arquivos .docx de descrição que deveriam acompanhar esses vídeos vieram todos corrompidos** — todos retornam o mesmo conteúdo (o prompt do "Alwayzz", que é na verdade o arquivo `Subscription Agency.docx` de `02_meez.design/Sections/`), em vez de descrever cada vídeo. Prints/nomes de arquivo dão uma pista do conteúdo (natureza, 3D, pessoa, energia, flores, etc.) mas a descrição/prompt de geração de cada um se perdeu. **Precisa re-exportar esses 8 docx no meez.design e resubir** se quiser recuperar a informação; os vídeos em si (.mp4) estão intactos.

Também existe um snippet de referência de embed confirmado (`embed_ms-nature.mp4.docx` e os outros 7 pares): `<video autoplay muted loop playsinline poster="...">` — padrão simples de embed de vídeo de fundo, sem problema.

---

## 5. Onde isso vive no Drive

Ver tabela completa de IDs em `FONTES.md`, seção "Google Drive — matéria-prima". Estrutura (nova, veio de uma reorganização feita pelo usuário em 31/07):

```
VermeFree/LP-KIT/LP-KIT/
├── 01_getlayers/
│   ├── Prompts/
│   │   ├── Templates/     → 6 docx (seção 2 acima)
│   │   └── 3D Scenes/     → 6 docx (seção 1 acima)
│   └── Zips/
│       └── Backgrounds/   → 8 zips de asset 3D bruto (seção 4)
└── 02_meez.design/
    ├── WebSites/
    │   └── Prompts/       → 5 docx (parte da seção 3)
    ├── Backgrounds/       → 8 mp4 + docx quebrados (seção 4)
    └── Sections/          → 10 docx (parte da seção 3)
```

---

## 6. Recomendação de aplicação para as LPs da VermeFree

Dado o tom "natural, sério e honesto, sem alarmismo nem milagre" (CLAUDE.md, seção 3) e a régua de claim ANVISA, a leitura de todo esse repertório sugere:

- **Atualizado em 28/08** — o Gabriel pediu explicitamente um nível WebGL/3D de verdade (trouxe prompts completos de Flow Wave, Laocoön e Baseline como referência técnica) depois de considerar a primeira versão da LP do Protocolo Adulto abaixo do nível esperado. Ver seção 7 abaixo pro padrão validado que resultou disso — WebGL contido ao hero (nunca a página inteira), com fallback CSS, pausa fora da viewport e ajuste de partículas/pixelRatio pra mobile, deixou de ser "evitar por padrão" e virou a assinatura esperada de hero pra LPs de venda.
- Os efeitos WebGL/3D mais pesados de fora do padrão validado (Flowstate, Soda, as 6 cenas 3D de fundo genéricas do getlayers) continuam exigindo critério — avaliar peso mobile antes de aplicar como estão, mesmo assim.
- **Priorizar** técnicas leves e editoriais: reveal de texto por palavra/linha via clip-mask (Loopstack, Baseline, Lumora), grid rem-adaptativo, liquid reveal via canvas 2D (Lumora — bom pra "antes/depois" do protocolo), count-up de estatísticas em scroll (Lumora), parallax simples com lerp (Celestial Renewal).
- **Estruturas de referência mais próximas do nicho:** Wellness Balance (TerraElix), Celestial Renewal (Serene), CozyPaws, Wellbeing OS — olhar essas primeiro ao desenhar a estrutura de seções de uma LP de produto.
- Sempre a mesma regra do `vermefree-lp-superprompt.md`: usar como inspiração pra montar uma identidade própria por produto, nunca clonar 1:1.

---

## 7. "Jornada" — voo imersivo por dentro do corpo (Three.js, WebGL, testado em código real)

> Nasceu de três prompts completos que o Gabriel trouxe em 28/08 (recriações verbatim de sites reais — "Flow Wave" um campo de partículas Three.js, "Laocoön" um cavalo de bronze cinematográfico, "Baseline" um site institucional de tênis com grid rem-adaptativo). A instrução foi clara: **usar como inspiração de técnica, nunca clonar o conteúdo** (tênis/bronze não têm nada a ver com a marca). Esta seção passou por duas versões dentro da mesma LP (`landing-protocolo-adulto/index.html`) antes de chegar na que ficou — registrado porque o histórico ensina tanto quanto o resultado final:

- **v1 (Campo Lunar):** um campo de partículas verde brilhante recolorido do shader "Flow Wave", só no hero. Feedback do Gabriel: "recolorir o conceito da referência não é criar algo novo pra nossa marca" — a ambição pedida era vermes 3D de verdade, não uma paisagem abstrata.
- **v2 (Problema + Hero separados):** vermes 3D procedurais (`InstancedMesh` de cápsulas) numa seção "problema" isolada, seguida por uma seção "hero" separada com o Campo Lunar. Feedback: ainda parecia "duas seções", não uma experiência imersiva única — e faltavam fotos reais do produto.
- **v3/final (Jornada única):** as duas cenas viraram UMA só — um túnel intestinal (cilindro visto por dentro, `side:BackSide`) com vermes 3D grudados na parede, e a câmera voa por dentro dele conforme a pessoa rola. A cor do túnel migra de infestado (vermelho/marrom) pra limpo (verde/bronze da marca) ao longo do voo, e os vermes desaparecem na mesma transição — a limpeza acontece na frente dos olhos, não por corte de seção. É essa versão que fica documentada abaixo.

**Arquitetura — `position:sticky`, não duas seções `100vh`:** a seção `.jornada` tem `height:260vh`; dentro dela, `.jornada-stage` é `position:sticky;top:0;height:100svh` — a cena fica "pinada" na tela enquanto a pessoa rola os 260vh, e o progresso 0→1 usado por tudo (cor, câmera, vermes, qual dos 3 "beats" de texto está ativo) vem de `-sectionRect.top / (sectionRect.height - innerHeight)`. Isso substitui o esquema anterior de duas seções `min-height:100svh` empilhadas — permite a transição de cor acontecer **durante** o voo, não num corte entre seções.

**Túnel:** `CylinderGeometry` rotacionado (eixo ao longo de Z), material `ShaderMaterial` com `side:THREE.BackSide` (a câmera fica *dentro*, então as faces de fora precisam ser as visíveis), parede deformada por Simplex noise (mesma função `snoise` já catalogada, reaproveitada) simulando respiração/peristalse. `scene.background` e `scene.fog.color` precisam ser atualizados a cada frame junto com a cor do túnel — sem isso a abertura no fim do túnel aparece como um buraco preto sólido, quebrando a ilusão (bug real, encontrado e corrigido nessa sessão).

**Vermes na parede:** mesma técnica de `InstancedMesh` de cápsulas da v2, mas agora com a matemática de posição em coordenadas cilíndricas (ângulo + posição ao longo do eixo do túnel) em vez de espaço livre — cada verme rasteja ao longo da parede em vez de flutuar solto. A opacidade/escala de cada verme é multiplicada por um fator `alive` que cai a zero conforme o progresso avança — é assim que eles "somem" na limpeza.

**3 beats de texto** (`.beat`, `opacity` cross-fade via classe `is-active`) por cima da cena, trocando em faixas do progresso (0–30% problema, 30–68% transição, 68–100% marca/CTA) — em vez de 2 seções de conteúdo, é 1 cena com 3 "cartões" de texto se revezando.

**Salvaguardas obrigatórias (todas testadas):**
- Fundo CSS sólido (`.jornada-stage{background:...}`) sempre atrás do canvas — se o CDN do Three.js falhar ou o navegador não suportar WebGL, a página nunca fica quebrada, só sem o efeito (nesse caso o beat 1 fica fixo visível via JS).
- `IntersectionObserver` na seção inteira: o loop de `requestAnimationFrame` só roda enquanto a jornada está visível.
- Detecção simples de mobile (`innerWidth < 700`): reduz a malha do túnel, o número de vermes/segmentos e o `pixelRatio`.
- `prefers-reduced-motion: reduce` pula o WebGL inteiro.

**⚠️ Bug real e importante — `position:sticky` quebrado por `overflow-x:hidden`:** o kit inteiro usa `html,body{overflow-x:hidden}` como regra fixa (convenção #2 do `vermefree-lp-superprompt.md`, pra nunca ter scroll horizontal no Safari mobile). Isso **quebra `position:sticky`** nos dois navegadores testados (Chromium/swiftshader) — porque `overflow-x:hidden` sozinho força `overflow-y:auto` (regra da spec CSS: só um eixo setado como não-`visible` faz o outro virar `auto`), e isso muda a "ancestral de rolagem" que o sticky usa como referência. Sintoma: o elemento sticky rola junto com o pai, como se fosse `position:static`, sem erro nenhum no console. **Correção:** `overflow-x:hidden; overflow-x:clip;` na mesma regra (a segunda linha vence em navegador que suporta `clip`; `hidden` fica de fallback). Testado e confirmado que resolve os dois (sticky funciona E não aparece scroll horizontal). Qualquer LP futura que use `position:sticky` (pra qualquer coisa "pinada" durante um trecho de rolagem, não só WebGL) precisa dessa troca — não é específico dessa cena.

**Como testar isso localmente antes de publicar (o sandbox de LP bloqueia unpkg/jsdelivr/cdnjs, mas libera `registry.npmjs.org`):**
```
npm install three@0.160.0   # baixa via npm, permitido
# aponte um importmap de teste pros arquivos em node_modules/three (build/)
# via um servidor local (python3 -m http.server) + screenshot via Playwright
# só depois de confirmar que renderiza, troca o importmap pra
# https://unpkg.com/three@0.160.0/... no arquivo publicado de verdade
```
Sem isso, um bug de shader ou de `position:sticky` falha em silêncio (canvas preto, ou elemento simplesmente não gruda) e não tem como saber sem essa etapa — os dois bugs reais desta seção só apareceram no screenshot, nunca na leitura do código.

**Cores usadas (Linha Adulto, `CLAUDE.md` §10):** infestado = `#3a0f08`/`#160604`, limpo = `#1f3d1f`/`#14241a`, glow infestado = `#c85a3a`, glow limpo (bronze) = `#C9A876`.

**Fotos reais de produto:** puxadas ao vivo da Shopify (`mcp__Shopify__get-product`), não geradas — o kit completo (`produto-card-1-adulto`) e as 4 fotos individuais de frasco (`pdp-adulto-01-oregano-frontal`, `-05-tintura-gota`, `-06-ornitina`, `-07-silimarina`) já existiam cadastradas no produto ativo e nunca tinham sido usadas em nenhuma LP até essa sessão — vale conferir o produto na Shopify antes de gerar qualquer imagem nova de "produto", a foto de verdade quase sempre já existe.

**Outro bug real encontrado e corrigido nessa mesma sessão** (vale registrar pra não repetir): `transform-origin:center` não funciona em elementos SVG sem `transform-box:fill-box` — pegou os marcadores da linha do tempo lunar (seção "como funciona" da mesma LP).
