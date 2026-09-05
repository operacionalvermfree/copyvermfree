# Banner hero — Dia D · quarta 09/09

Versão **cinematográfica premium**. Peças do banner hero da home para a ação relâmpago de 24h (09/09, 00h00–23h59).

## Mudança de método

As versões anteriores eram desenhadas à mão em código — polígonos chapados, degradês calculados, colinas de elipse. Isso tem teto, e o teto é "amador". Esta versão troca o método:

1. **A cena é gerada** por modelo generativo: pedestal de ardósia polida, luz-chave dramática, névoa volumétrica, atmosfera esmeralda caindo pro preto, profundidade de campo. Gerada **vazia** — sem produto, sem pessoas, sem texto.
2. **O produto é a foto real**, com fundo removido, composto na cena com o tratamento que faz um produto parecer que está mesmo ali: **relight** direcional casando com a luz da cena, **luz de recorte** quente na borda iluminada, **sombra projetada** para o lado oposto à luz, **sombra de contato** curta e escura na base, e **reflexo** no tampo polido com fade.
3. **A tipografia** é Montserrat real desenhada por código.

A luz de cada chapa foi medida antes de compor: no desktop vem da direita, no mobile da esquerda. Sombra e relight seguem cada uma.

## Arquivos entregues

| Peça | Peso | Link |
|---|---|---|
| **Desktop 2400×1000** (com texto) | 135 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/53a62f38-90bc-4de8-bf42-204a355b8982.webp |
| **Mobile 1080×1350** (com texto) | 88 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/2959aefc-df12-4d8c-932e-fd0ff5cee0b1.webp |
| **Chapa limpa desktop** | 106 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/d80d8dcd-c869-4593-a696-b1f40c81c6bd.webp |
| **Chapa limpa mobile** | 61 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/1e9c7a69-1825-4d7c-b3d2-399c8fef96c0.webp |

Teto: desktop < 300 KB, mobile < 150 KB. Todas passam com folga.

## Produto usado — PENDENTE DE TROCA

Hero atual: **`IMG_1463.jpg`**, escolhida por qualidade de recorte (2,1 px de borda, zero buracos internos, contra 9,6 px e 3 buracos da pior candidata).

**O frasco é a Silimarina** — um dos quatro componentes do Protocolo Adulto, não o kit e não o Óleo de Alho. Para um hero de promoção do site inteiro, o certo é o Protocolo Adulto completo. Falta o cliente indicar qual arquivo é. Trocar é trocar `hero_cut.png`.

### Nada de produto foi gerado ou redesenhado por IA
Nenhum frasco, rótulo ou embalagem é gerado, recriado ou retocado. A IA gerou apenas a **cena vazia**. O relight e as sombras são operações fotométricas sobre os pixels originais — brilho, matiz e máscara — nunca redesenho.

## Texto da arte

- **Olho:** `VERMEFREE · DIA D` (letterspaced, discreto)
- **Headline:** `10% OFF` em creme
- **Subtítulo:** `SÓ HOJE · QUARTA 09/09` em vermelho, com filete
- **Bullets:** `Já no preço, sem cupom.` · `Frete grátis sem valor mínimo.` · `1 Óleo de Alho de brinde no pedido.`
- **CTA:** `APROVEITAR O DIA D`

Sem cupom, sem código, sem preço riscado, sem "de/por".

## Nota sobre identidade

Esta versão é **escura**, o que contraria o "fundo claro/branco" das edições anteriores do Dia D. Foi decisão consciente: cinematográfico premium pede escuro e atmosférico. O vermelho da ação continua no subtítulo, nos marcadores e no botão. É uma decisão de marca que cabe ao cliente confirmar.

## Como regerar

`build_banner.py` reconstrói as 4 peças a partir de `hero_cut.png` (produto recortado), `cine_d.png` / `cine_m.png` (cenas) e Montserrat.
