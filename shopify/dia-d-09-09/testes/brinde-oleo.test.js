const vm = require('vm');
const fs = require('fs');
const CODE = fs.readFileSync(process.env.SC + '/brinde-puro.js', 'utf8');

const OLEO = 9400206262491, VAR_OLEO = 48968692891867, ADULTO = 9345664614619;

function novoMundo(cartRef, storage, pathname, latencia) {
  let n = 0;
  const key = (variant, props) => variant + ':' + JSON.stringify(props || {});
  function fetchFake(url, opts) {
    opts = opts || {};
    const body = opts.body ? JSON.parse(opts.body) : null;
    return new Promise(res => setTimeout(() => {
      if (url.startsWith('/cart/add')) {
        const it = body.items[0];
        const k = key(it.id, it.properties);
        let linha = cartRef.items.find(l => l.key === k);
        if (linha) linha.quantity += it.quantity;            // Shopify soma linha igual
        else cartRef.items.push({ key: k, product_id: it.id === VAR_OLEO ? OLEO : ADULTO,
                                  quantity: it.quantity, properties: it.properties || {} });
      } else if (url.startsWith('/cart/change')) {
        const linha = cartRef.items.find(l => l.key === body.id);
        if (linha) { linha.quantity = body.quantity;
                     if (body.quantity === 0) cartRef.items = cartRef.items.filter(l => l.key !== body.id); }
      }
      res({ ok: true, json: () => Promise.resolve(JSON.parse(JSON.stringify(cartRef))) });
    }, latencia));
  }
  const doc = { readyState: 'complete', addEventListener(){}, querySelector: () => null,
                querySelectorAll: () => [], createElement: () => ({ setAttribute(){}, appendChild(){}, style:{} }) };
  const win = { location: { pathname, reload(){ win.__reloads = (win.__reloads||0)+1; } },
                Shopify: {}, fetch: fetchFake, localStorage: storage, setTimeout, Promise, Date, JSON, console };
  win.window = win;
  const ctx = vm.createContext(Object.assign(win, { document: doc }));
  vm.runInContext(CODE, ctx);
  return ctx;
}

function storageFake() {
  const m = new Map();
  return { getItem: k => (m.has(k) ? m.get(k) : null), setItem: (k,v) => m.set(k,String(v)), removeItem: k => m.delete(k) };
}
const oleos = c => c.items.filter(l => l.product_id === OLEO).reduce((a,l)=>a+l.quantity,0);
const linhasOleo = c => c.items.filter(l => l.product_id === OLEO).length;
const espera = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  let falhas = 0;
  const check = (nome, ok, detalhe) => { console.log((ok?'✅':'❌') + ' ' + nome + (detalhe?'  → '+detalhe:'')); if(!ok) falhas++; };

  // 1) protocolo sem oleo, fora do carrinho → adiciona exatamente 1
  let cart = { items: [{ key:'a', product_id: ADULTO, quantity:1, properties:{} }] };
  novoMundo(cart, storageFake(), '/products/protocolo', 5);
  await espera(400);
  check('1 protocolo, sem óleo → adiciona 1 brinde', oleos(cart)===1 && linhasOleo(cart)===1, 'óleos='+oleos(cart));

  // 2) estado do pedido #3112: 1 linha de brinde com quantidade 2, FORA do carrinho
  cart = { items: [{ key:'a', product_id: ADULTO, quantity:3, properties:{} },
                   { key: VAR_OLEO+':{"_brinde":"dia-d"}', product_id: OLEO, quantity:2, properties:{_brinde:'dia-d'} }] };
  novoMundo(cart, storageFake(), '/products/protocolo', 5);
  await espera(400);
  check('#3112 (linha brinde qtd 2) fora do carrinho → corta pra 1', oleos(cart)===1, 'óleos='+oleos(cart));

  // 3) brinde + oleo do cliente (2 linhas) → sobra so o brinde
  cart = { items: [{ key:'a', product_id: ADULTO, quantity:1, properties:{} },
                   { key: VAR_OLEO+':{"_brinde":"dia-d"}', product_id: OLEO, quantity:1, properties:{_brinde:'dia-d'} },
                   { key: VAR_OLEO+':{}', product_id: OLEO, quantity:3, properties:{} }] };
  novoMundo(cart, storageFake(), '/products/oleo', 5);
  await espera(600);
  const brindeSobrou = cart.items.some(l => l.product_id===OLEO && l.properties._brinde==='dia-d');
  check('brinde + 3 óleos do cliente → sobra 1, e é o brinde', oleos(cart)===1 && brindeSobrou, 'óleos='+oleos(cart)+' linhas='+linhasOleo(cart));

  // 4) sem protocolo, com brinde → remove o brinde
  cart = { items: [{ key: VAR_OLEO+':{"_brinde":"dia-d"}', product_id: OLEO, quantity:1, properties:{_brinde:'dia-d'} }] };
  novoMundo(cart, storageFake(), '/products/oleo', 5);
  await espera(400);
  check('sem protocolo → remove o brinde', oleos(cart)===0, 'óleos='+oleos(cart));

  // 5) A CORRIDA: duas abas, mesmo localStorage, mesmo carrinho, ao mesmo tempo
  cart = { items: [{ key:'a', product_id: ADULTO, quantity:1, properties:{} }] };
  const st = storageFake();
  novoMundo(cart, st, '/products/protocolo', 40);
  novoMundo(cart, st, '/cart', 40);
  await espera(900);
  check('DUAS ABAS simultâneas → 1 óleo só (era o bug de #3112/#3113)', oleos(cart)===1, 'óleos='+oleos(cart));

  console.log(falhas ? '\n❌ ' + falhas + ' falha(s)' : '\n✅ todos os cenários passaram');
  process.exit(falhas ? 1 : 0);
})();
