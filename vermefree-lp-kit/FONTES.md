# FONTES.md — onde está cada fonte de verdade

> Este arquivo aponta para os dados reais. Ele **não substitui** a checagem ao vivo na loja/Drive — se algo aqui parecer desatualizado (preço, estoque, variant ID), confirmar direto na fonte antes de publicar copy.

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

---

## Marca / copy / compliance

- **Fonte única de tom de voz, ICP, regras ANVISA, catálogo e preços:** `CLAUDE.md` (raiz do repo).
- **Design system / convenções técnicas de LP:** `vermefree-lp-superprompt.md` (raiz do repo).
- **Mapa de LPs existentes:** `PAGINAS.md` (raiz do repo).

Se uma informação não estiver em nenhuma dessas fontes nem neste arquivo: **perguntar, não inventar.**
