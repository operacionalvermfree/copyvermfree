# Status do upload — tema Dia D (163879354587)

## No ar (21 arquivos, todos verificados por MD5)
sections/vf-announcement-bar.liquid      campanha 09/09
sections/vf-selos-ticker.liquid          campanha 09/09
sections/vf-kit-selector.liquid          campanha 09/09 + brinde com destaque
sections/vf-pdp-main.liquid              base Padrao + campanha (CSS extraido)
snippets/vf-pdp-main-css.liquid          NOVO - CSS da PDP (split por limite de API)
sections/main-cart.liquid                base Padrao + brindes do Dia D
layout/theme.liquid                      renders dos pop-ups + gate do 5OFF
config/settings_data.json                bloco da tarja + intervalo 4s
templates/index.json                     home de setembro + correcoes de claim
templates/cart.json                      previa do Dia D no carrinho
templates/product.kit-familia.json       + 2 secoes novas + previa + claims
snippets/vf-frete-progress.liquid        NOVO (+ gate: nao diz "falta R$ X" no dia)
snippets/vf-diagnostico-popup.liquid     NOVO
snippets/vf-whatsapp-float.liquid        NOVO
snippets/vf-bump-protocolo.liquid        NOVO (orfao)
snippets/vf-order-bump-2protocolo.liquid NOVO
sections/vf-pdp-benefits.liquid          NOVO
sections/vf-pdp-cross-familia.liquid     NOVO

## Falta subir (7)
templates/product.json
templates/product.kids-2-4.json
templates/product.kids-5-9.json
sections/vf-comparativo.liquid     (correcao de claim "+100 tipos")
snippets/vf-order-bump.liquid      (melhoria do Padrao)
snippets/vf-cart-recomendados.liquid  (orfao, paridade)
snippets/vf-upsell-oleo-popup.liquid  (orfao, paridade - CONFLITA com o brinde)

Conteudo pronto em aplicado/. Restaurar original = backup-original/.
