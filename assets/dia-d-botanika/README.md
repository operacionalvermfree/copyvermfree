# DIA D BOTANIKA — Assets (07 e 08.08)

Peças da campanha **Dia D Botanika** — "8% OFF em todos os suplementos · Frete Grátis · Manual da Suplementação de brinde".
Identidade Botanika: **azul-marinho premium + dourado + branco**, monograma folha, produtos reais, estética clean/sofisticada.

## Arquivos finais (`/finais`)

| Peça | 1x (exato) | 2x (alta) | Timer? |
|---|---|---|---|
| Hero Desktop | `Botanika_DiaD_Hero_Desktop_1920x600.png` | `..._@2x_3840x1200.png` | sim — máscara reservada |
| Hero Mobile | `Botanika_DiaD_Hero_Mobile_1080x1350.png` | `..._@2x_2160x2700.png` | sim — máscara reservada |
| Tarja superior | `Botanika_DiaD_TarjaSuperior_1920x72.png` | `..._@2x_3840x144.png` | sim — "Termina em 00:00:00" à direita |
| Badge PDP (fundo transparente) | `Botanika_DiaD_Badge_PDP_600x600.png` | `..._@2x_1200x1200.png` | não |
| Tag de preço (fundo transparente) | `Botanika_DiaD_TagPreco_820x340.png` | `..._@2x_1640x680.png` | não |

## Área do timer (contador dinâmico)
As peças que exigem contador **não** desenham números fixos — reservam uma máscara para o timer do site.
- Desktop/Mobile: bloco `HORAS : MIN : SEG` com placeholder `00`. Sobrepor os dígitos dinâmicos no elemento `#timer-slot`.
- Tarja: placeholder `00:00:00` à direita, no `#timer-slot`.

## Reproduzir / editar (`/fonte`)
Composição feita em HTML/CSS/SVG + produtos reais (PNG recortado) e renderização em dimensão exata via Chromium/Playwright.
```
node render.js <arquivo.html> <largura> <altura> <saida.png> <escala> [transparent] [alturaViewport]
# ex.: node render.js desktop.html 1920 600 desktop_2x.png 2
# transparente (badge/tag): node render.js badge.html 600 600 badge_2x.png 2 transparent
# tarja (viewport alto p/ evitar trava do compositor): node render.js bar.html 1920 72 bar_2x.png 2 opaque 300
```
- Fonte: **Montserrat** (subconjunto latino embutido em `fonts/montserrat.css`).
- Produtos recortados em `prod/` (margem transparente removida).

## Pendências a confirmar com o Gabriel
1. **Frete:** a arte está com "Frete Grátis" **sem piso**. Confirmar se é sem valor mínimo ou acima de R$349.
2. **Identidade visual:** validar navy+dourado+branco e o monograma (recriado vetorialmente a partir dos rótulos).
3. **Tag de preço:** números são **ilustrativos** (de R$199,90 → R$183,91). Aplicar preços reais por SKU na PDP.

## Observações técnicas
- O fundo foi construído em CSS/SVG (mármore navy + veios/poeira dourada + eucalipto + vinheta). A geração no Higgsfield
  foi feita, mas o CDN de download ficou bloqueado pela política de egresso do ambiente; a recriação em código deixou
  texto e rótulos 100% nítidos (que é onde banners de IA costumam falhar).
- Cronograma: no ar 00h de 07/08, sai 23h59 de 08/08.
