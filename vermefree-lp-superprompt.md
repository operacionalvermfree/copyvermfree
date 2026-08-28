# vermefree-lp-superprompt.md — Design System & Regras Técnicas de LP

> Ler antes de construir qualquer landing page. Cobre a parte **técnica/design** (como a página é feita). Pra tom de voz, claims e catálogo, ver `CLAUDE.md`. Pra fluxo de trabalho e onde buscar assets, ver `vermefree-lp-kit/`.

---

## 1. Contexto fixo

- **Empresa/marca:** VermeFree
- **Repositório:** `operacionalvermfree/copyvermfree`
- **Loja (checkout):** `https://vermefree.com.br` · cupom padrão `5OFF` · frete grátis acima de **R$399**
- **Branch de publicação das LPs:** `lp`
- **Link publicado:** `https://raw.githack.com/operacionalvermfree/copyvermfree/lp/landing-<slug>/index.html`
- **Checkout direto:** `https://vermefree.com.br/cart/<VARIANT_ID>:<QTD>` — variant IDs reais em `vermefree-lp-kit/FONTES.md`

## 2. Convenções fixas (não negociáveis)

1. **Uma pasta por produto:** `landing-<slug>/index.html`. HTML autocontido — sem build, sem bundler, sem dependência de arquivo externo do repo (CSS/JS inline ou no mesmo arquivo).
2. **Tem que funcionar no Safari mobile ao vivo** (via raw.githack, sem servidor próprio): sempre incluir `html { overflow-x: hidden; }` e evitar qualquer recurso que dependa de HTTPS local/CORS especial.
3. **Cada produto tem identidade visual e interativa própria.** Nunca clonar ou copiar código 1:1 de outra LP já publicada. O repertório de técnica abaixo é inspiração/repertório — não é template pra colar.
4. **Validar antes de publicar:**
   - `node --check` no(s) bloco(s) de JS inline (extrair pra um `.js` temporário se precisar rodar o check, mas o arquivo final continua autocontido).
   - Conferir balanceamento de tags HTML (abre/fecha bate).
5. **Nunca colocar identificador de modelo de IA** (nome do modelo, versão, etc.) em commit, PR, código-fonte ou comentário.
6. **1 CTA claro por peça**, seguindo a régua de claim do `CLAUDE.md` (nunca "elimina/erradica/cura", nunca citar Dr. William Araujo, nunca diagnosticar o leitor).
7. **Elementos de conversão obrigatórios numa LP de venda por produto** (detalhado em `vermefree-lp-kit/PROMPT-AGENTE-LP-VENDA.md`): seleção invertida de potes (maior kit/mais economia ancorando no topo), pop-up de diagnóstico ANVISA-safe (nunca diagnostica, só sugere protocolo a partir de bem-estar/rotina), selos + garantia de 7 dias (confirmada, ver `CLAUDE.md` §6).

## 3. Repertório de técnica (inspiração — nunca copiar 1:1)

Usar como banco de referência pra decidir a assinatura de cada LP, misturando com critério (não empilhar tudo numa página só):

- Grid `rem` adaptativo.
- Spring helper em JS puro (animações com física leve, sem lib externa).
- Reveals com `clip-path` + blur-up ao entrar em viewport.
- Loader com contador numérico na entrada da página.
- Assinatura em `<canvas>` própria — partículas, fios ou ondas reagindo ao mouse.
- Hero em "liquid reveal" (transição orgânica de entrada).
- `<model-viewer>` pra elemento 3D do produto.
- Pipeline Three.js procedural: 3 composers + `FinalPass` + simplex noise + motes (partículas ambiente) + scroll com double-damping.
- UX de commerce: toggle de kit/variante, count-up de preço/desconto, botões magnéticos, tilt+glow em cards de produto, barra de compra fixa no mobile.

**Catálogo real e destilado:** `vermefree-lp-kit/REPERTORIO-TECNICO.md` documenta ~35 referências técnicas reais (getlayers.com + meez.design) lidas e resumidas — com técnica de destaque, stack e uma recomendação explícita de quais combinam com o tom natural/consultivo da marca (evitar WebGL pesado tipo fluid-sim/Three.js como padrão; priorizar reveals de texto via clip-mask, liquid reveal em canvas 2D, grid rem-adaptativo, count-up em scroll). Consultar esse arquivo antes de escolher a assinatura de uma LP nova.

## 4. Fluxo de uma LP

0. Se for uma das 5 LPs de venda por produto (protocolo-adulto, kids-2-4, kids-5-9, kit-familia, oleo-de-alho): ler também `vermefree-lp-kit/PROMPT-AGENTE-LP-VENDA.md` — tem a ficha completa (ganchos, dores, desejos, variant ID, anatomia de página) de cada uma.
1. Ler `vermefree-lp-kit/` (kit + assets do produto no Drive) e `PAGINAS.md`.
2. Confirmar pasta (`landing-<slug>/`) e decidir a identidade própria dessa LP (paleta pode puxar da identidade visual do `CLAUDE.md` seção 10, mas a assinatura interativa/estrutural precisa ser única).
3. Puxar a verdade do produto — preço, variant ID, composição, posologia, claim permitido — na loja e no Drive (ver `FONTES.md`).
4. Construir o HTML autocontido com a assinatura única.
5. Validar (`node --check` + balanço de tags).
6. Publicar em `landing-<slug>/index.html` na branch `lp`.
7. Atualizar `PAGINAS.md` (status + link).

## 5. Identidade visual de referência (herdada do CLAUDE.md, seção 10)

- **Paleta oficial** — ver `CLAUDE.md` §10 pra hex completo. Linha Adulto (Adulto, Kits mistos, Kit Família, Óleo de Alho): verde claro `#C0DE96` + verde escuro `#5E8C43`, preto `#1A1A1A`, branco, dourado/bronze `#C9A876` de acento premium, gradiente escuro `#1f3d1f`→`#14241a` pra peças cinematográficas/dark, verde-suave `#E8F5E4` pra blocos alternativos claros. Linha **Kids tem paleta própria** (vívida: verde `#009933`, magenta, laranja, azul royal) — nunca misturar as duas linhas numa mesma LP.
- ⚠️ **Referência ainda incompleta** — o Gabriel vai trazer imagens de inspiração antes de qualquer LP fechar a identidade visual definitiva. Não travar uma LP nova só nesses hex sem conferir se chegaram imagens novas em `vermefree-lp-kit/FONTES.md` / Drive.
- Selos de rótulo disponíveis: "Vegetal 100%", "Metais Free".
- UGC de referência: vertical 9:16, caseiro, luz natural, sem marca d'água.

Cada LP pode variar tom/composição dentro da paleta da sua linha (Adulto ou Kids) — mas a paleta-base de cada linha não muda entre produtos dela, pra manter reconhecimento de marca.
