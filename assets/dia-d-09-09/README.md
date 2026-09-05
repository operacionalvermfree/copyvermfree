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
| **Desktop 2400×1000** (com texto) | 136 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/14e6c128-77e4-4171-bba8-0df17203eee0.webp |
| **Mobile 1080×1350** (com texto) | 97 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/3ce57fa1-f875-4c5f-aeab-281bb59d8c81.webp |
| **Chapa limpa desktop 2400×1000** | 89 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/3df09af2-46cd-475c-a66a-bde7c29593dd.webp |
| **Chapa limpa mobile 1080×1350** | 59 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/a78d5b73-2bfb-413f-9646-820354b91f1d.webp |

Teto de peso: desktop < 300 KB, mobile < 150 KB. Todas passam com folga.

Os PNGs de backup são gerados pelo `build_banner.py` junto com os WebP; publico assim que o conceito estiver aprovado, para não deixar link de versão antiga circulando.

## Foto usada

Foto oficial enviada pelo cliente: **`1-IMG_1319.jpg`** (5184×3456), a mesma no desktop e no mobile para manter a leitura consistente entre as duas peças.

Escolhida por medição, não por preferência: é horizontal (1.50), o produto ocupa 43% do quadro e se estende por toda a largura, e é a de maior presença de verde de rótulo entre as horizontais — o perfil de um line-up de produtos, que é o que assenta num bloco largo.

**A foto entra inteira, como bloco.** Só é reenquadrada (crop central para preencher o polígono) e recebe uma grade leve de cor para casar com o creme da peça. Não há recorte de produto, não há frasco flutuando, não há borda de segmentação — que foi o problema das versões anteriores.

### Nada de produto foi gerado ou redesenhado por IA
Nenhum frasco, rótulo ou embalagem é gerado, recriado ou retocado. Nesta versão não há sequer chapa de fundo gerada por IA: o fundo é bloco de cor chapado e o resto é a fotografia real. Toda a tipografia e todos os elementos gráficos (corte diagonal, faixas, setas, folha, etiqueta, pill, botão) são desenhados por código com fontes reais (Montserrat ExtraBold / SemiBold / Regular).

### O brinde
O Óleo de Alho aparece na foto do line-up e ganha presença própria com uma **etiqueta vermelha sólida** sobre o bloco fotográfico: ícone de presente + `BRINDE` + `1 Óleo de Alho no seu pedido`. Resolve o "mostre o frasco" sem precisar recortar nada.

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

- Desktop 2400×1000 (12:5). Coluna de texto em x 390–1080, sempre à esquerda do corte diagonal (que começa em x=1100 no topo). Etiqueta do brinde termina em x=1895, dentro da área segura de 1600 px. Faixas e setas decorativas ficam fora dela, nas laterais cortáveis.
- Mobile 1080×1350 (4:5) — composição redesenhada em três faixas diagonais, não é crop: headline a 170 px contra 160 px no desktop.
- Contraste medido (WCAG): `10% OFF` e subtítulo em vermelho **5,34:1** · texto em tinta **14,38:1** · branco no vermelho do botão **5,63:1**. O texto agora assenta em bloco creme chapado, não sobre foto — por isso os números melhoraram.
- Tipografia toda auto-ajustada (`fit()`): mudar a copy não estoura a coluna.
- Chapas limpas saem com os blocos, faixas e produtos, **sem nenhuma tipografia** — para o tema escrever por cima e ainda ter contraste.

## Paleta

`#C42B2B` vermelho da ação · `#7E1A1A` vermelho escuro · `#FDF8F3` creme · `#2A2622` tinta.

## Como regerar

`build_banner.py` reconstrói as 4 peças de forma determinística a partir de `hero.jpg` e do Montserrat. Trocar a foto é trocar esse arquivo.
