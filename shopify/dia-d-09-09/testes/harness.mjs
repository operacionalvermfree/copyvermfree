import fs from 'fs';
const SRC = fs.readFileSync('/tmp/brinde.js','utf8');

const OIL_P=9400206262491, OIL_V=48968692891867;
const PROTO=[9345664614619,9345665827035,9345667399899,9345668251867];

function makeItem(pid, {gift=false, qty=1, key=null}={}) {
  return { key: key||(pid+':'+Math.random().toString(36).slice(2,8)), product_id: pid,
           variant_id: pid===OIL_P?OIL_V:pid+1, quantity: qty,
           properties: gift? {_brinde:'dia-d'} : null,
           original_line_price: 6700, final_line_price: gift?0:6700 };
}

async function run(nome, {itens, dataISO, addFalha=false, path='/cart'}) {
  let cart = { items: itens.slice() };
  const log = [];
  let reloaded = false;

  const fakeFetch = async (url, init={}) => {
    const body = init.body ? JSON.parse(init.body) : null;
    if (url.endsWith('/cart.js')) return { ok:true, json: async()=>JSON.parse(JSON.stringify(cart)) };
    if (url.includes('/cart/add')) {
      log.push('ADD ' + JSON.stringify(body.items[0]));
      if (addFalha) return { ok:false, json: async()=>null };
      const it = makeItem(OIL_P, {gift: body.items[0].properties?._brinde==='dia-d'});
      cart.items.push(it);
      return { ok:true, json: async()=>({}) };
    }
    if (url.includes('/cart/change')) {
      log.push('REMOVE ' + body.id);
      cart.items = cart.items.filter(i=>i.key!==body.id);
      return { ok:true, json: async()=>JSON.parse(JSON.stringify(cart)) };
    }
    return { ok:false, json: async()=>null };
  };

  const listeners = {};
  const doc = {
    readyState:'complete',
    addEventListener:(e,f)=>{(listeners[e]=listeners[e]||[]).push(f);},
    querySelector:()=>null, querySelectorAll:()=>[], createElement:()=>({}),
  };
  const win = {
    fetch: fakeFetch,
    Shopify: {},
    location: { pathname: path, reload: ()=>{reloaded=true;} },
    __vfDiadBrinde: undefined,
  };

  // Date fixa (o script le getTimezoneOffset do ambiente; forco UTC via TZ)
  const real = Date;
  const fixed = new real(dataISO);
  global.Date = class extends real {
    constructor(...a){ return a.length? new real(...a) : new real(fixed.getTime()); }
    static now(){ return fixed.getTime(); }
  };

  const fn = new Function('window','document','fetch','setTimeout','console','Date', SRC);
  fn(win, doc, fakeFetch, (f)=>f(), console, global.Date);

  await new Promise(r=>setImmediate(()=>setImmediate(()=>setImmediate(()=>setImmediate(r)))));
  global.Date = real;

  const oleos = cart.items.filter(i=>i.product_id===OIL_P).length;
  const brindes = cart.items.filter(i=>i.product_id===OIL_P && i.properties?._brinde==='dia-d').length;
  console.log(`${nome}\n   acoes=[${log.join(' | ')||'nenhuma'}]  oleos=${oleos} brindes=${brindes} reload=${reloaded}`);
}

const DENTRO = '2026-09-09T12:00:00Z';   // 09h BRT do dia 09
const INICIO = '2026-09-09T03:00:30Z';   // 00:00:30 BRT do dia 09
const FIM    = '2026-09-10T02:59:00Z';   // 23:59 BRT do dia 09
const FORA_A = '2026-09-09T02:59:00Z';   // 23:59 BRT do dia 08
const FORA_D = '2026-09-10T03:30:00Z';   // 00:30 BRT do dia 10

await run('1  1 Protocolo Adulto, dentro da janela        ', {itens:[makeItem(PROTO[0])], dataISO:DENTRO});
await run('2  1 Kids 2-4, dentro da janela                ', {itens:[makeItem(PROTO[1])], dataISO:DENTRO});
await run('3  So brinde no carrinho (protocolo removido)  ', {itens:[makeItem(OIL_P,{gift:true})], dataISO:DENTRO});
await run('4  Cliente ja tinha 1 oleo proprio + protocolo ', {itens:[makeItem(OIL_P),makeItem(PROTO[0])], dataISO:DENTRO});
await run('5  2 oleos proprios, sem protocolo             ', {itens:[makeItem(OIL_P),makeItem(OIL_P)], dataISO:DENTRO});
await run('6  4 protocolos                                ', {itens:PROTO.map(p=>makeItem(p)), dataISO:DENTRO});
await run('7  Ja tem protocolo + brinde (estado estavel)  ', {itens:[makeItem(PROTO[0]),makeItem(OIL_P,{gift:true})], dataISO:DENTRO});
await run('8  FORA: vespera 08/09 23:59, so protocolo     ', {itens:[makeItem(PROTO[0])], dataISO:FORA_A});
await run('9  FORA: 10/09 00:30, carrinho com brinde velho', {itens:[makeItem(PROTO[0]),makeItem(OIL_P,{gift:true})], dataISO:FORA_D});
await run('10 Borda 00:00:30 BRT do dia 09                ', {itens:[makeItem(PROTO[0])], dataISO:INICIO});
await run('11 Borda 23:59 BRT do dia 09                   ', {itens:[makeItem(PROTO[0])], dataISO:FIM});
await run('12 add falha (esgotado) — nao pode dar reload  ', {itens:[makeItem(PROTO[0])], dataISO:DENTRO, addFalha:true});
await run('13 fora da pagina do carrinho (PDP)            ', {itens:[makeItem(PROTO[0])], dataISO:DENTRO, path:'/products/x'});
