# Banner hero — Dia D · quarta 09/09

Peças do banner hero da home para a ação relâmpago de 24h (09/09, 00h00–23h59).

## Conceito

Linguagem gráfica adaptada da referência aprovada (banners "Mother Earth Day"): **corte diagonal** entre bloco de cor e foto, **faixas anguladas** paralelas, **tríades de setas**, **headline empilhada em três linhas** com a do meio na cor de ação, **ícone inline** e **botão pill**.

A paleta é a do Dia D, não a da referência: onde ela usa verde escuro chapado com destaque em verde-limão, aqui o bloco é **creme** e o destaque é **vermelho #C42B2B** — o "fundo claro/branco, tipografia pesada, vermelho como cor da ação" que a base já reconhece das edições anteriores. O verde continua onde deve: nos rótulos dos produtos, que é o que dá o contraste vermelho × verde.

Headline no formato da referência (`MOTHER / EARTH / DAY` → `DIA D / 10% OFF / SÓ HOJE`), com a linha do meio em vermelho e o dobro do corpo das outras — o 10% é o protagonista. O ícone inline é uma folha (fitoterapia), no lugar do pinheiro.

O slot do subtítulo da referência (`SAVE OUR PLANET`) recebe **`JÁ NO PREÇO, SEM CUPOM`** — é o diferencial da ação e o que reduz fricção.

## Arquivos entregues

| Peça | Peso | Link |
|---|---|---|
| **Desktop 2400×1000** (com texto) | 149 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/b5b9560b-ac5c-4624-a50b-406199c5df62.webp |
| **Mobile 1080×1350** (com texto) | 109 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/8d244f1c-783a-49e2-b686-f639cc018eb5.webp |
| **Chapa limpa desktop 2400×1000** | 98 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/59cb5d2a-a2e6-4d25-932d-44766cde5c37.webp |
| **Chapa limpa mobile 1080×1350** | 68 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/b976c9bd-0bf4-4b0d-b97e-b6895c5462df.webp |

Teto de peso: desktop < 300 KB, mobile < 150 KB. Todas passam com folga.

Os PNGs de backup são gerados pelo `build_banner.py` junto com os WebP; publico assim que o conceito estiver aprovado, para não deixar link de versão antiga circulando.

## Fotos de produto usadas (oficiais, da CDN da Shopify)

| Peça na arte | Arquivo original |
|---|---|
| Protocolo Adulto (4 frascos) — produto principal | `produto-card-1-adulto_901f4e4f-…png` |
| VermeFree Kids 2 a 4 anos — segundo produto | `produto-card-2-kids-2a4.png` |
| Óleo de Alho 500mg — **o brinde, na frente, com selo** | `01-PRINCIPAL-oleo-alho.png` |

Não usados: `produto-card-3-kids-5a9.png` e `produto-card-4-kit-familia-crop.png`.

### Nenhum frasco ou rótulo foi gerado por IA
As fotos oficiais entraram **só recortadas** (remoção de fundo) e reescaladas — pixel de rótulo é pixel da foto original. A IA gerou apenas a **chapa de fundo vazia** (parede creme + bancada de madeira clara, luz natural, folhagem nas bordas), sem nenhum objeto, produto, pessoa ou texto. Toda a tipografia e todos os elementos gráficos (corte diagonal, faixas, setas, folha, selo, pill, botão) são desenhados por código com fontes reais (Montserrat ExtraBold / SemiBold / Regular).

## Texto da arte

- **Selo:** `QUARTA 09/09 · 24 HORAS` (pill vermelho com relógio desenhado)
- **Headline:** `DIA D` / `10% OFF` (vermelho, dobro do corpo) / `SÓ HOJE` + folha
- **Subtítulo:** `JÁ NO PREÇO, SEM CUPOM`
- **Apoio:** `Frete grátis sem valor mínimo e 1 Óleo de Alho de brinde no seu pedido.`
- **Micro (só desktop):** `+ Manual da Desparasitação em PDF por e-mail.`
- **Selo no óleo:** `BRINDE`
- **CTA:** `APROVEITAR O DIA D`

Sem cupom, sem código, sem botão "copiar", sem preço riscado, sem "de/por".

## Especificação técnica verificada

- Desktop 2400×1000 (12:5). Coluna de texto em x 400–1160, sempre à esquerda do corte diagonal (que começa em x=1180 no topo). Produto mais à direita termina em x=1996, dentro da área segura de 1600 px. Faixas e setas decorativas ficam fora dela, nas laterais cortáveis.
- Mobile 1080×1350 (4:5) — composição redesenhada, não é crop: headline a 178 px contra 172 px no desktop, produto proporcionalmente menor.
- Contraste medido (WCAG, cor do texto vs fundo real): `10% OFF` e subtítulo em vermelho **5,29:1** · texto em tinta **14,25:1** · branco no vermelho do botão **5,63:1**.
- Tipografia toda auto-ajustada (`fit()`): mudar a copy não estoura a coluna.
- Chapas limpas saem com os blocos, faixas e produtos, **sem nenhuma tipografia** — para o tema escrever por cima e ainda ter contraste.

## Paleta

`#C42B2B` vermelho da ação · `#7E1A1A` vermelho escuro · `#FDF8F3` creme · `#2A2622` tinta.

## Como regerar

`build_banner.py` reconstrói as 4 peças de forma determinística a partir dos recortes dos produtos, das chapas de fundo e do Montserrat.
