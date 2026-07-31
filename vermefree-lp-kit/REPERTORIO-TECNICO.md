# REPERTORIO-TECNICO.md — catálogo destilado da biblioteca getlayers/meez.design

> Matéria-prima bruta: `VermeFree/LP-KIT/LP-KIT/` no Drive (ver `FONTES.md` para os IDs de pasta). Este arquivo é o resumo técnico de ~35 documentos de referência de design/animação de sites — pra não precisar reabrir tudo no Drive toda vez que for construir uma LP.
>
> **Repertório de inspiração, nunca template pra colar.** Nenhum desses sites tem qualquer relação com VermeFree (são agências, apps, moda, tênis, bebida, etc. fictícios usados só como catálogo de técnica). O valor está na técnica de interação/motion, não no conteúdo. Ver seção 6 pra recomendação de quais técnicas combinam com o tom natural/consultivo da marca.

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

- **Evitar** os efeitos WebGL/3D mais pesados (Flowstate, Soda, Laocoön, as 6 cenas 3D de fundo) como padrão — combinam mais com marcas tech/luxo/bebida do que com o posicionamento consultivo/acolhedor da marca, e pesam no carregamento mobile (público-alvo é mãe pesquisando no celular).
- **Priorizar** técnicas leves e editoriais: reveal de texto por palavra/linha via clip-mask (Loopstack, Baseline, Lumora), grid rem-adaptativo, liquid reveal via canvas 2D (Lumora — bom pra "antes/depois" do protocolo), count-up de estatísticas em scroll (Lumora), parallax simples com lerp (Celestial Renewal).
- **Estruturas de referência mais próximas do nicho:** Wellness Balance (TerraElix), Celestial Renewal (Serene), CozyPaws, Wellbeing OS — olhar essas primeiro ao desenhar a estrutura de seções de uma LP de produto.
- Sempre a mesma regra do `vermefree-lp-superprompt.md`: usar como inspiração pra montar uma identidade própria por produto, nunca clonar 1:1.
