# Teste do brinde do óleo (Dia D 09/09/2026)

Simula o `snippets/vf-diad-brinde.liquid` fora do navegador: carrinho falso,
`fetch` falso com a semântica real do `/cart/add.js` da Shopify (variante +
propriedades iguais somam na MESMA linha), `localStorage` falso compartilhado
entre "abas", e latência configurável pra provocar corrida.

## Rodar

    cd shopify/dia-d-09-09/aplicado
    python3 -c "
    import io,re
    s=io.open('vf-diad-brinde.liquid',encoding='utf-8').read()
    js=re.search(r'^<script>\n(.*?)\n</script>$', s, re.S|re.M).group(1)
    js=js.replace('{{ routes.cart_url }}','/cart').replace('{{ routes.cart_add_url }}','/cart/add').replace('{{ routes.cart_change_url }}','/cart/change')
    io.open('/tmp/brinde-puro.js','w',encoding='utf-8').write(js)"
    SC=/tmp node ../testes/brinde-oleo.test.js

Sai 0 se todos os cenários passarem, 1 se algum falhar.

## Por que ele existe

Os pedidos #3112 e #3113 saíram com DOIS frascos de óleo grátis numa linha só,
os dois carregando a propriedade `_brinde: dia-d` — prova de que foi o próprio
script que adicionou duas vezes, e não o cliente.

O cenário "DUAS ABAS simultâneas" reproduz exatamente isso: **falha na versão
anterior do snippet (2 óleos) e passa na atual (1 óleo)**. É o teste que
importa; os outros quatro são regressão.

## Limite

O ponto 3 do conserto — segurar o "Finalizar compra" — NÃO é coberto aqui:
depende de DOM e evento de submit reais. Precisa de teste no navegador.
