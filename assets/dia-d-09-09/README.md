# Banner hero — Dia D · quarta 09/09

Peças do banner hero da home para a ação relâmpago de 24h (09/09, 00h00–23h59).

## Arquivos entregues

Hospedados no CDN (baixar e subir no tema/Shopify Files):

| Peça | Formato | Peso | Link |
|---|---|---|---|
| **Desktop 2400×1000** (com texto) | WebP | 144 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/f4863d11-3254-4be7-9fd0-4b55926399db.webp |
| Desktop 2400×1000 (backup) | PNG | 1,6 MB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/35cab55c-d6d5-4ec6-b0fa-269d7a672e8a.png |
| **Mobile 1080×1350** (com texto) | WebP | 109 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/f73ab3f2-f544-4f23-be36-d5abb79aacfd.webp |
| Mobile 1080×1350 (backup) | PNG | 1,1 MB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/b5f4f5fa-cd2b-4735-982c-398568323505.png |
| **Chapa limpa desktop 2400×1000** | WebP | 93 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/2aec257c-6c0e-4b85-82d6-a5c97e121cd2.webp |
| Chapa limpa desktop (backup) | PNG | 1,6 MB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/d0f1a0c9-ad70-48d0-b6db-9238f840a6b9.png |
| **Chapa limpa mobile 1080×1350** | WebP | 67 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/b1c52b41-66c3-4f79-a9ce-4350f821b304.webp |
| Chapa limpa mobile (backup) | PNG | 1,1 MB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/0621aeb4-3cae-4106-8ce6-943d73e37d4f.png |

Orçamento de peso pedido: desktop < 300 KB, mobile < 150 KB. **Todas as versões WebP ficaram abaixo da metade do teto** — o hero não vai atrasar o carregamento no único dia que importa.

## Fotos de produto usadas (oficiais, da CDN da Shopify)

| Peça na arte | Arquivo original |
|---|---|
| Protocolo Adulto (4 frascos) — produto principal | `produto-card-1-adulto_901f4e4f-…png` |
| VermeFree Kids 2 a 4 anos — segundo produto | `produto-card-2-kids-2a4.png` |
| Óleo de Alho 500mg — **o brinde, na frente, com selo** | `01-PRINCIPAL-oleo-alho.png` |

Não usados nesta arte: `produto-card-3-kids-5a9.png` e `produto-card-4-kit-familia-crop.png` (a composição pede um Kids só; o Kit Família ficaria redundante ao lado do Adulto).

### Nenhum frasco ou rótulo foi gerado por IA
As fotos oficiais entraram **só recortadas** (remoção de fundo) e reescaladas — pixel de rótulo é pixel da foto original. O único uso de IA foi a **chapa de fundo vazia** (parede creme + bancada de madeira clara, luz natural, sombras de folhagem nas bordas), gerada sem nenhum objeto, produto, pessoa ou texto. A tipografia toda é desenhada com fontes reais (Montserrat ExtraBold / SemiBold / Regular), nunca "escrita" por modelo generativo.

## Texto da arte

- **Selo:** `SÓ HOJE · QUARTA 09/09` (com relógio desenhado, pill vermelho)
- **Headline:** `10% OFF` gigante em vermelho + `em todo o site. Só hoje.`
- **Apoio:** `Já no preço, sem cupom. Frete grátis sem valor mínimo e 1 Óleo de Alho de brinde no seu pedido.`
- **Micro (só desktop):** `+ Manual da Desparasitação em PDF, por e-mail, para quem comprar.`
- **Selo no óleo:** `BRINDE`
- **CTA:** `Aproveitar o Dia D`

Sem cupom, sem código, sem botão "copiar", sem preço riscado, sem "de/por" — como pede o briefing.

## Especificação técnica verificada

- Desktop 2400×1000 (12:5); todo o conteúdo essencial entre x=400 e x=2000 (área segura de 1600 px). Elemento mais à direita: kit Kids termina em x=1994. As folhagens ficam fora da área segura, nas laterais cortáveis.
- Mobile 1080×1350 (4:5) — composição redesenhada, não é crop: headline proporcionalmente maior (210 px vs 180 px) e produto menor.
- Contraste medido (WCAG, cor do texto vs fundo real): headline 4,9:1 · sublinha 13,1:1 · apoio 12,8:1 / 10,4:1 · texto branco no vermelho #C42B2B 5,6:1. Tudo acima do mínimo para o corpo usado.
- Legibilidade a 320 px de largura: altura de caixa da headline ≈ 17 px no desktop e ≈ 45 px no mobile.
- As chapas limpas saem **com o degradê creme, sem nenhuma tipografia** — para o tema escrever por cima e ainda ter contraste.

## Paleta

`#C42B2B` vermelho da ação · `#7E1A1A` vermelho escuro · `#FDF8F3` creme · `#2A2622` tinta. O verde da marca fica onde deve: nos rótulos dos produtos, sem recolorir nada.

## Como regerar

`build_banner.py` reconstrói as 4 peças de forma determinística a partir dos recortes dos produtos, das chapas de fundo e do Montserrat. Toda a tipografia é auto-ajustada (`fit()`), então mudar a copy não estoura a coluna.
