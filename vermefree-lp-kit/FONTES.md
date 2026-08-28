# FONTES.md — onde está cada fonte de verdade

> Este arquivo aponta para os dados reais. Ele **não substitui** a checagem ao vivo na loja/Drive — se algo aqui parecer desatualizado (preço, estoque, variant ID), confirmar direto na fonte antes de publicar copy.

> Os 2 conflitos que existiam entre `PROMPT-AGENTE-LP-VENDA.md` e o resto do kit já foram resolvidos com o Gabriel (confirmado em 03/08): desconto do Óleo de Alho é **3=10%/6=15%** (o `CLAUDE.md` estava certo); convenção de arquivo é **`landing-<slug>/index.html`** (a já em uso em todo o kit). `PROMPT-AGENTE-LP-VENDA.md` já foi atualizado, sem mais ⚠️ pendente.

---

## Loja (Shopify)

- **Domínio:** `vermefree.com.br`
- **Checkout direto de carrinho:** `https://vermefree.com.br/cart/<VARIANT_ID>:<QTD>`
- **Cupom padrão de UGC/comunicação:** `5OFF` (5% off)
- **Frete grátis:** acima de R$399
- Regras completas de preço/desconto por volume/cupons de influencer: ver `CLAUDE.md`, seção 6.

### Variant IDs reais (confirmados via Shopify, produtos ACTIVE)

| Produto | Handle | Variant ID | Preço cheio |
|---|---|---|---|
| Protocolo Adulto | `protocolo-desparasitacao-adulto-vermefree` | `48772143415515` | R$347 |
| Kids 2 a 4 anos | `antiparasitario-infantil-natural-vermefree-kids-2-a-4-anos` | `48772145250523` | R$270 |
| Kids 5 a 9 anos | `antiparasitario-infantil-natural-vermefree-kids-5-a-9-anos` | `48772147085531` | R$389 |
| Kit Família (2 adultos + 2 crianças) | `kit-familia-vermefree-2-adultos-2-criancas` | `48772149739739` | R$1150 |
| Óleo de Alho Desodorizado 500mg | `oleo-de-alho-desodorizado-500mg` | `48968692891867` | R$67 |

Exemplo de link de checkout pronto (1 unidade do Protocolo Adulto):
`https://vermefree.com.br/cart/48772143415515:1`

> Há também 2 produtos em `DRAFT` na loja (`ExamCare`, `Manual da Suplementação`) — não usar em LP até virarem `ACTIVE` e serem documentados no `CLAUDE.md`.

---

## Google Drive — matéria-prima (bruto)

Conector Google Drive conectado. Estrutura criada em `VermeFree/LP-KIT/`:

| Pasta | ID | Uso |
|---|---|---|
| `VermeFree/` (raiz da marca) | `1_tkDGttuMwFWTBTN5V2mGpIHZ_j22jXz` | Pasta-mãe já existente no Drive da operação (também tem exports de pedidos, docs soltos). |
| `VermeFree/LP-KIT/` | `1-OsV1ntigh8Int0rgAReYLTbfpBp4zuG` | Raiz do material de apoio às LPs. |
| `VermeFree/LP-KIT/01_referencias-zips/` | `1t7jANDI4ngZFIJRcWYTGbz8cFPdejrKA` | Zips de referência técnica pesados (inspiração de LPs, não pra clonar). |
| `VermeFree/LP-KIT/02_referencias/` | `1Qkc4Hs8c9ZPDw9Fa_otttnhx3KgvhZfl` | Referências soltas (prints, links, benchmarks, briefings). |
| `VermeFree/LP-KIT/03_assets-produtos/` | `1IM5LtQQ-DRebwH4oVJjOU-qBvxML-cIa` | Assets em alta por produto (fotos, vídeos, rótulo). |
| `03_assets-produtos/protocolo-adulto/` | `1SF_dVXyVfug7SiWoluEXje1T_wCyTT_y` | Assets do Protocolo Adulto. |
| `03_assets-produtos/kids-2-4/` | `1dNWO3cWXlK7AyJQHcah9vovAO4bn65f9` | Assets do Kids 2 a 4 anos. |
| `03_assets-produtos/kids-5-9/` | `1-6x86eqX829SmJHnIGisPURI3yv7gDHh` | Assets do Kids 5 a 9 anos. |
| `03_assets-produtos/kit-familia/` | `1wZYcHY_jYFhy0TJmso5TANmlOx5vX-nb` | Assets do Kit Família. |
| `03_assets-produtos/oleo-de-alho/` | `1uuVBBO4MutcsvF5arlqUNP_-ESsJvFBP` | Assets do Óleo de Alho. |

Link direto: https://drive.google.com/drive/folders/1-OsV1ntigh8Int0rgAReYLTbfpBp4zuG

Essas pastas foram criadas vazias como fundação — popular com o material bruto (fotos de produto em alta, vídeos de UGC, zips de referência de outras LPs) conforme cada LP for construída.

### Biblioteca de referência técnica (getlayers / meez.design)

Em 31/07 o usuário subiu, dentro de `VermeFree/LP-KIT/`, uma pasta aninhada `LP-KIT/` com uma biblioteca de ~35 documentos de referência de design/animação de sites (catálogos técnicos do getlayers.com e do meez.design). **Já lida e destilada em `vermefree-lp-kit/REPERTORIO-TECNICO.md`** — consultar esse arquivo antes de reabrir qualquer coisa aqui.

| Pasta | ID |
|---|---|
| `LP-KIT/LP-KIT/` (raiz da biblioteca) | `1pppMHGEJfCQPDznbqnT9y7ZnMa1gde6q` |
| `01_getlayers/` | `1VrpLo9Eax_ctEeBtfGAaA0cXKDOzTij2` |
| `01_getlayers/Prompts/` | `1q67VqYyUbvEMOHyRms-_Wg8GWf-KBlPz` |
| `01_getlayers/Prompts/Templates/` | `1iLAXGOVeGbofYvniLgf2Dg777p4-qezp` |
| `01_getlayers/Prompts/3D Scenes/` | `1shNfMfZGX6qYeT2dBJLnGWej9BwBNFFk` |
| `01_getlayers/Zips/` | `1hA59ULLKm9WijeAKhXkuphb7myWn9696` |
| `01_getlayers/Zips/Backgrounds/` | `1zuhZ7FaoQRrpjArGqmSosEbqef-pgHGc` |
| `02_meez.design/` | `1C5nmIDunefVcukbYWxZBNTIpXQ_IN670` |
| `02_meez.design/WebSites/` | `1sMMKv41hB2lyQ9BZFYqK9jg_NchpaPOy` |
| `02_meez.design/WebSites/Prompts/` | `1bi3an5jfDEI1XX4NmkT7_6wMdZQB9Y4X` |
| `02_meez.design/Backgrounds/` | `1VsrJZrALZr5EhVQZqSJfakp_yTz-GskD` |
| `02_meez.design/Sections/` | `1NGBDEX_zyKdMTqnZqANxuWIHmc3Spahc` |

⚠️ **Problema conhecido:** os 8 `.docx` de descrição em `02_meez.design/Backgrounds/` (Nature, 3D, Nature nice, Person, Energy, Deep flowers, Flower Ground, 3D Sea) vieram todos corrompidos — todos retornam o mesmo conteúdo (o prompt do site "Alwayzz", que pertence a `Sections/Subscription Agency.docx`). Os vídeos `.mp4` estão intactos; só as descrições se perderam. Precisa re-exportar esses 8 docx no meez.design se quiser recuperar a informação — ver detalhes em `REPERTORIO-TECNICO.md`, seção 4.

---

## Marca / copy / compliance

- **Fonte única de tom de voz, ICP, regras ANVISA, catálogo e preços:** `CLAUDE.md` (raiz do repo).
- **Design system / convenções técnicas de LP:** `vermefree-lp-superprompt.md` (raiz do repo).
- **Mapa de LPs existentes:** `PAGINAS.md` (raiz do repo).
- **Dores/desejos/ganchos por SKU + anatomia completa de página + elementos de conversão obrigatórios das 5 LPs de venda:** `vermefree-lp-kit/PROMPT-AGENTE-LP-VENDA.md`.

Se uma informação não estiver em nenhuma dessas fontes nem neste arquivo: **perguntar, não inventar.**
