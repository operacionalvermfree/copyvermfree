# DIA D BOTANIKA — Assets v2 (07 e 08.08)

Refação completa com a **logo oficial** da Botanika, **paleta real da marca** (verde-limão · dourado · índigo),
**linha completa de produtos**, **foco na oferta (8% OFF) e no frete grátis** e **sem timer** nas imagens.

Entregue em **duas direções** para A/B:
- **`/finais/clara`** — premium editorial: fundo marfim, índigo + dourado + verde. Fresco, natural, sofisticado.
- **`/finais/escura`** — cinematográfica: esmeralda profundo + dourado, logo em creme, CTA dourado.

## Peças (cada uma em 1x exato + @2x em alta)

| Peça | Dimensão (1x) | @2x | Fundo |
|---|---|---|---|
| Hero Desktop | 1920×600 | 3840×1200 | opaco |
| Hero Mobile | 1080×1350 | 2160×2700 | opaco |
| Tarja superior | 1920×74 | 3840×148 | opaco |
| Badge PDP | 600×600 | 1200×1200 | **transparente** |
| Tag de preço | 820×340 | 1640×680 | **transparente** |

Nomeação: `Botanika_DiaD_<Peça>_<Claro|Escuro>_<WxH>.png` (e `@2x`).

## Decisões desta versão
- **Logo oficial** usada de verdade (wordmark + monograma), recolorida por peça (índigo/creme/dourado).
- **Todos os produtos** na cena (TETRA VIT D, Super Ômega 3, Hair, Tri[Mg], Super Vitamina C, Whey Balance, Creatina+Taurato, Sleep Inositol).
- **8% OFF** é o elemento dominante; **FRETE GRÁTIS** em destaque + **Manual de brinde**.
- **Sem contador** nas artes (o timer, se existir, entra via site por cima — mas nenhuma arte reserva/desenha timer).

## Reproduzir / editar (`/fonte`)
Composição em HTML/CSS/SVG com produtos reais (PNG) + logo oficial + Montserrat, renderizada em dimensão exata via Chromium/Playwright.
```
node render.js <arquivo.html> <larg> <alt> <saida.png> <escala> [transparent] [alturaViewport]
# ex.: node render.js desktop_v3.html 1920 600 out.png 2
# escuro gerado de claro:  python3 mkdark.py desktop_v3.html desktop_v3_dark.html
```
Paleta em variáveis CSS (`:root`) — trocar tema é trivial. Logos em `/fonte/brand`, produtos recortados em `/fonte/prod`.

## Pendências a confirmar com o Gabriel
1. **Frete:** artes com "Frete Grátis" **sem piso** — confirmar se é sem mínimo ou acima de R$349.
2. **Direção:** escolher **Clara** ou **Escura** (ou manter as duas por canal).
3. **Tag de preço:** números **ilustrativos** (R$199,90 → R$183,91) — aplicar preço real por SKU na PDP.

## Nota técnica (transparência)
As imagens de IA (Higgsfield/Nano Banana) foram usadas para explorar cenário, mas o CDN de download é bloqueado pela
política de egresso deste ambiente e o Higgsfield não expõe os bytes localmente. Para garantir **rótulos e texto 100%
nítidos** (onde banners de IA falham) e **entrega real de arquivos**, a composição final foi feita em código com os
produtos e a logo oficiais.
