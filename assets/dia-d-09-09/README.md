# Banner hero — Dia D · quarta 09/09

Peças do banner hero da home para a ação relâmpago de 24h (09/09, 00h00–23h59).

## Conceito

Linguagem gráfica adaptada da segunda referência aprovada (pôster "GO STRONG · Serious Mass"):

- **Produto flutuando**, recortado e inclinado, como herói central da peça
- **Fitas de marca** envolvendo o produto — bandas anguladas com texto repetido, umas passando por trás e outras por cima, que é o que cria a ilusão de embrulho
- **Ambiente**: céu em degradê + colina verde na base
- **Assinatura manuscrita** em verde suave ao fundo, cortada pela borda
- **Badge de spec**: caixa sólida com duas linhas de tipografia pesada
- **Rodapé** com botão pill

Paleta trocada para a do Dia D: as fitas e os badges são **vermelho #C42B2B** (cor da ação) em vez do verde-limão da referência. O verde da marca fica onde deve — no rótulo do produto e na colina. O contraste vermelho × verde é o que o briefing pede.

Texto das fitas: `DIA D · 10% OFF · SÓ HOJE`, repetido, no lugar do `GO STRONG`.

## Arquivos entregues

| Peça | Peso | Link |
|---|---|---|
| **Desktop 2400×1000** (com texto) | 169 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/06071407-9a44-45da-b817-1ea956de87ea.webp |
| **Mobile 1080×1350** (com texto) | 132 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/ccd07ddf-f31f-4cb2-95c2-37c3230c1f0a.webp |
| **Chapa limpa desktop 2400×1000** | 90 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/3716dab2-98b2-41f3-aef9-6bb91149ace7.webp |
| **Chapa limpa mobile 1080×1350** | 69 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/17aba93e-500e-4ad6-a314-19add8a2d408.webp |

Teto: desktop < 300 KB, mobile < 150 KB. Todas passam.

Nas chapas limpas as fitas saem **sem o texto repetido** — bandas vermelhas lisas — junto com a remoção de toda a tipografia.

## Foto usada

Foto oficial enviada pelo cliente: **`IMG_1463.jpg`**, recortada por segmentação.

Escolhida por medição da qualidade do recorte entre quatro candidatas: 768×1390 de área útil, borda de transição de ~2,1 px, **zero buracos internos** e silhueta de objeto único. A pior das candidatas (`IMG_1322`) deu 9,6 px de borda e 3 buracos — descartada. As fotos anteriores, dos cards da Shopify, tinham fundo de madeira com props em volta, e é daí que vinha o recorte ruim.

### Nada de produto foi gerado ou redesenhado por IA
Nenhum frasco, rótulo ou embalagem é gerado, recriado ou retocado — só recorte de fundo e reescala. Não há fundo gerado por IA: céu, colina, fitas, badges e tipografia são todos desenhados por código. Fontes reais (Montserrat ExtraBold/SemiBold/Regular + Caveat para a assinatura).

## Texto da arte

- **Headline:** `10% OFF` (vermelho, 200 px no desktop) / `SÓ HOJE`
- **Subtítulo:** `JÁ NO PREÇO, SEM CUPOM`
- **Badge 1:** `FRETE GRÁTIS` / `SEM VALOR MÍNIMO`
- **Badge 2:** `BRINDE` / `1 ÓLEO DE ALHO` (com ícone de presente)
- **Fitas:** `DIA D · 10% OFF · SÓ HOJE`
- **CTA:** `APROVEITAR O DIA D`

Sem cupom, sem código, sem preço riscado, sem "de/por".

## Especificação técnica verificada

- Desktop 2400×1000 (12:5) e mobile 1080×1350 (4:5), composições independentes.
- **Máscara nas fitas.** Sem ela as fitas atravessavam a headline. No desktop elas só aparecem a partir de x=1150 (com fade até 1340), emergindo de trás do texto; no mobile, só entre y=430 e y=1205. Verificado: **zero pixel de fita** à esquerda da área segura no desktop e zero acima da headline.
- Produto: bbox 1405–1995 no desktop, dentro da área segura de 1600 px. As fitas correm até a borda direita de propósito — são decorativas e podem ser cortadas.
- Contraste medido (WCAG): `10% OFF` vermelho sobre o céu **4,52:1** (tipografia de 200 px, bem acima do mínimo de 3:1 para texto grande) · `SÓ HOJE` em tinta **13,42:1** · creme sobre o vermelho dos badges e do botão **5,34:1**.

## Paleta

`#C42B2B` vermelho da ação · `#961E1E` vermelho escuro das bordas de fita · `#FDF8F3` creme · `#5C8244` verde folha · `#3A582C` verde escuro · `#26221E` tinta.

## Como regerar

`build_banner.py` reconstrói as 4 peças a partir de `hero_cut.png` (o recorte) e das fontes. Trocar o produto é trocar esse arquivo.
