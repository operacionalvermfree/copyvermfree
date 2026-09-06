# Banner hero — Dia D · quarta 09/09

Versão **cinematográfica premium, com a linha completa de produtos**. Peças do banner hero da home para a ação relâmpago de 24h (09/09, 00h00–23h59).

## Método

1. **A cena é gerada** por modelo generativo: pedestal de ardósia polida, luz-chave dramática, névoa volumétrica, atmosfera esmeralda caindo pro preto, profundidade de campo. Gerada **vazia** — sem produto, sem pessoas, sem texto.
2. **Os produtos são a foto real** (`IMG_1479`, a linha inteira lado a lado), com fundo removido e compostos na cena com o tratamento que faz um objeto parecer que está mesmo ali:
   - **micro-contraste** (UnsharpMask leve) para o rótulo aguentar a redução;
   - **relight** direcional casando com a luz-chave da chapa;
   - **luz de recorte** quente na borda do lado iluminado;
   - **profundidade**: a ponta oposta à luz recua — escurece e dessatura;
   - **sombra projetada** achatada para o lado oposto à luz;
   - **sombra de contato** tirada da BASE da máscara alfa, então **cada frasco ganha a sua própria sombra** (a fileira não vira um borrão único);
   - **reflexo** espelhado com fade no tampo polido.
3. **A tipografia** é Montserrat real desenhada por código, com auto-fit (mudar a copy nunca estoura a coluna).

A chapa não é medida à mão: `calib()` acha o topo do pedestal (maior queda de luminância varrendo o eixo Y), o centro/vão dele e de que lado vem a luz. Trocar a chapa não exige recalibrar nada.

## Arquivos entregues

| Peça | Peso | Link |
|---|---|---|
| **Desktop 2400×1000** (com texto) | 132,5 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/0da3c6a6-fa63-4522-8684-e84511ca68b8.webp |
| **Mobile 1080×1350** (com texto) | 88,2 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/a3e09600-7d96-4bc8-9ff0-9001abcf35ab.webp |
| **Chapa limpa desktop** | 98,9 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/a142502b-1cc9-4840-ab53-dfa65775c8cb.webp |
| **Chapa limpa mobile** | 55,0 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_3DxKyMs0lPMnTsxEPVz0TBl1Jco/773f6445-34e2-4d98-9469-043c140cf4e6.webp |

Teto do briefing: desktop < 300 KB, mobile < 150 KB. Todas passam com folga.

## Verificações medidas (não estimadas)

O build imprime estes números a cada rodada, comparando a peça com texto contra a chapa limpa (a diferença entre as duas **é** o texto, então a caixa é exata):

| | Desktop | Mobile |
|---|---|---|
| Dimensão | 2400×1000 | 1080×1350 |
| Caixa do texto | x 403–1178 · y 231–829 | x 174–904 · y 76–1248 |
| Dentro da área segura de 1600 px (x 400–2000) | ✅ | ✅ (peça inteira) |
| Contraste do título (creme) | 17,05:1 | 16,68:1 |
| Contraste da etiqueta de prazo | 17,19:1 | 16,58:1 |
| Contraste dos bullets | 17,52:1 | 15,69:1 |
| Linha de produtos | x 1180–2099 · y 281–707 | x 101–979 · y 583–990 |

Mínimo WCAG AA para texto pequeno é 4,5:1 — todas as peças passam com larga folga.

**Duas correções vieram dessa medição, não do olho:**
- o subtítulo em vermelho caía dentro do facho de luz no mobile e media **2,5:1** (reprovado). Virou **etiqueta vermelha com texto creme** — o vermelho da marca continua presente e o contraste passa;
- entrou uma **cortina escura** (`scrim`) sob o bloco de texto, cheia até certo ponto e sumindo em degradê, para o texto nunca depender de onde a névoa da chapa caiu.

## Legibilidade a 320 px

Mobile foi redesenhado, não recortado. A 320 px de largura o headline renderiza a ~50 px e os bullets a ~9,5 px. O bloco de oferta ficou **acima** dos produtos (antes as linhas caíam em cima do pedestal) e o CTA embaixo.

## Produtos usados

**`IMG_1479.jpg`** — a foto oficial do cliente com **a linha completa** lado a lado: as duas tinturas líquidas grandes, o frasco médio e a fileira de potes de cápsulas. Recorte medido: 1816×841 px úteis, borda de ~2,1 px, sem buracos internos.

### Nada de produto foi gerado ou redesenhado por IA
Nenhum frasco, rótulo ou embalagem é gerado, recriado ou retocado. A IA gerou apenas a **cena vazia** (pedestal, luz, névoa, fundo). Relight, profundidade e sombras são operações fotométricas sobre os pixels originais da foto — brilho, matiz e máscara — nunca redesenho.

## Texto da arte

- **Olho:** `VERMEFREE · DIA D` (letterspaced, discreto)
- **Headline:** `10% OFF` em creme
- **Etiqueta:** `SÓ HOJE · QUARTA 09/09` — pílula vermelha, texto creme
- **Bullets:** `Já no preço, sem cupom.` · `Frete grátis sem valor mínimo.` · `1 Óleo de Alho de brinde no pedido.`
- **CTA:** `APROVEITAR O DIA D`

Sem cupom, sem código, sem preço riscado, sem "de/por". O Manual da Desparasitação (o benefício mais fraco) ficou de fora para não diluir os três primeiros — cabe no e-mail de confirmação.

## Nota sobre identidade

Esta versão é **escura**, o que contraria o "fundo claro/branco" das edições anteriores do Dia D. Foi decisão consciente: cinematográfico premium pede escuro e atmosférico. O vermelho da ação continua na etiqueta de prazo, nos marcadores e no botão. É uma decisão de marca que cabe ao cliente confirmar.

## Como regerar

`build_banner.py` reconstrói as 4 peças a partir de:

- `fam.png` — a linha completa de produtos, fundo removido (RGBA);
- `cine_d.png` / `cine_m.png` — as chapas de cena geradas, vazias;
- `fonts/m600.ttf` — Montserrat SemiBold (o ExtraBold vem do fontconfig do sistema).
