(function () {
  'use strict';

  if (window.__vfDiadBrinde) return;
  window.__vfDiadBrinde = true;
  if (window.Shopify && window.Shopify.designMode) return;
  if (window.location.pathname.indexOf('/checkout') === 0) return;

  var VARIANTE_BRINDE = 48968692891867;
  var PRODUTO_BRINDE  = 9400206262491;
  var PROTOCOLOS = [9345664614619, 9345665827035, 9345667399899, 9345668251867];
  var PROP = '_brinde';
  var VALOR = 'dia-d';

  var URL_CART   = '/cart';
  var URL_ADD    = '/cart/add.js';
  var URL_CHANGE = '/cart/change.js';

  var ocupado = false;
  var refazer = false;

  /* Janela do Dia D em horario de Brasilia (UTC-3), independente do fuso do
     visitante: desloco o epoch para o relogio de parede de Brasilia e leio
     os getters locais. */
  function naJanela() {
    var agora = new Date();
    var brt = new Date(agora.getTime() + agora.getTimezoneOffset() * 60000 - 10800000);
    return brt.getFullYear() === 2026 && brt.getMonth() === 8 && brt.getDate() === 9;
  }

  function ehOleo(item)      { return item.product_id === PRODUTO_BRINDE; }
  function ehProtocolo(item) { return PROTOCOLOS.indexOf(item.product_id) !== -1; }
  function ehBrinde(item)    {
    return ehOleo(item) && item.properties && item.properties[PROP] === VALOR;
  }

  function pedir(url, opcoes) {
    opcoes = opcoes || {};
    opcoes.credentials = 'same-origin';
    opcoes.headers = opcoes.headers || {};
    opcoes.headers['Accept'] = 'application/json';
    opcoes.headers['X-VF-Brinde'] = '1';
    return fetch(url, opcoes).then(function (r) {
      return r.ok ? r.json() : null;
    });
  }

  function lerCarrinho() { return pedir(URL_CART + '.js'); }

  function adicionar() {
    var corpo = { items: [{ id: VARIANTE_BRINDE, quantity: 1, properties: {} }] };
    corpo.items[0].properties[PROP] = VALOR;
    return pedir(URL_ADD, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(corpo)
    }).then(confirmar(function (cart) {
      return cart.items.some(ehBrinde);
    }));
  }

  function remover(linha) {
    return pedir(URL_CHANGE, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: linha.key, quantity: 0 })
    }).then(confirmar(function (cart) {
      return !cart.items.some(ehBrinde);
    }));
  }

  /* Só considero que mudou algo depois de reler o carrinho e confirmar.
     Isso e o que impede laco: se o add falhou (esgotado, 422), a condicao
     continua verdadeira mas nao ha reload, entao nao rodamos de novo. */
  function confirmar(teste) {
    return function (resposta) {
      if (!resposta) return false;
      return lerCarrinho().then(function (cart) {
        return !!(cart && cart.items && teste(cart));
      });
    };
  }

  function avaliar() {
    if (ocupado) { refazer = true; return; }
    ocupado = true;

    lerCarrinho().then(function (cart) {
      if (!cart || !cart.items) return false;

      var temProtocolo = cart.items.some(ehProtocolo);
      var oleos   = cart.items.filter(ehOleo);
      var brindes = cart.items.filter(ehBrinde);

      if (!naJanela()) {
        return brindes.length ? remover(brindes[0]) : false;
      }
      /* Cliente que ja tinha oleo por conta propria: nao adiciono outro.
         O BXGY zera o que ja esta la — que e exatamente "1 oleo de brinde". */
      if (temProtocolo && oleos.length === 0) return adicionar();
      if (!temProtocolo && brindes.length)    return remover(brindes[0]);
      return false;
    })
    .catch(function () { return false; })
    .then(function (mudou) {
      ocupado = false;
      if (mudou) {
        if (naPaginaDoCarrinho()) { window.location.reload(); return; }
      }
      if (refazer) { refazer = false; avaliar(); return; }
      marcarBrinde();
    });
  }

  function naPaginaDoCarrinho() {
    return window.location.pathname.split('?')[0].replace(/\/$/, '') === URL_CART;
  }

  /* O carrinho do tema renderiza cada linha como [data-cart-item][data-key].
     Uso a key vinda do /cart.js pra achar a linha certa e rotular. Se o tema
     mudar a marcacao, nada quebra: so nao rotula. */
  function marcarBrinde() {
    if (!naPaginaDoCarrinho()) return;
    lerCarrinho().then(function (cart) {
      if (!cart || !cart.items) return;
      cart.items.forEach(function (item) {
        if (!ehBrinde(item)) return;
        var linha = document.querySelector('[data-key="' + item.key + '"]');
        while (linha && !linha.hasAttribute('data-cart-item')) linha = linha.parentElement;
        if (!linha || linha.querySelector('.vf-brinde-tag')) return;

        linha.classList.add('vf-brinde-linha');
        var alvo = linha.querySelector('.vf-cart-item__title') || linha;
        var tag = document.createElement('span');
        tag.className = 'vf-brinde-tag';
        tag.textContent = '🎁 Brinde do Dia D · Grátis';
        alvo.parentNode.insertBefore(tag, alvo.nextSibling);

        if (item.original_line_price > item.final_line_price) {
          linha.querySelectorAll('.vf-cart-item__price, .vf-cart-item__price-mobile')
            .forEach(function (el) {
              if (el.querySelector('.vf-brinde-de')) return;
              var de = document.createElement('s');
              de.className = 'vf-brinde-de';
              de.textContent = dinheiro(item.original_line_price);
              el.insertBefore(de, el.firstChild);
            });
        }
      });
    }).catch(function () {});
  }

  function dinheiro(centavos) {
    return 'R$ ' + (centavos / 100).toFixed(2).replace('.', ',');
  }

  /* O tema recarrega a pagina depois de mexer no carrinho, entao o load ja
     cobre quase tudo. O wrapper abaixo pega os casos que nao recarregam
     (drawer, quantidade inline) sem depender de evento proprio do tema. */
  try {
    var fetchOriginal = window.fetch;
    window.fetch = function (entrada, init) {
      var url = (typeof entrada === 'string') ? entrada : (entrada && entrada.url) || '';
      var nosso = !!(init && init.headers && init.headers['X-VF-Brinde']);
      var mexeuNoCarrinho = /\/cart\/(add|change|update|clear)/.test(url);
      return fetchOriginal.apply(this, arguments).then(function (r) {
        if (mexeuNoCarrinho && !nosso && r.ok) setTimeout(avaliar, 0);
        return r;
      });
    };
  } catch (e) { /* silencio: o brinde nao pode quebrar a loja */ }

  ['cart:updated', 'cart:refresh', 'cart:update'].forEach(function (evt) {
    document.addEventListener(evt, function () { setTimeout(avaliar, 0); });
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', avaliar);
  } else {
    avaliar();
  }
})();
