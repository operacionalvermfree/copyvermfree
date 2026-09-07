# Dia D 09/09/2026 — as quatro correções

Janela da ação: `2026-09-09T03:00:00Z` → `2026-09-10T02:59:59Z`
(quarta 09/09, 00h00 às 23h59 BRT). Fuso da loja confirmado: `America/Sao_Paulo`.

---

## Correção 1 · Empilhamento com o 10% do Dia D

Confirmado por `discountClasses` antes de mexer: os três de volume são
classe `PRODUCT` e o Dia D 10% é classe `ORDER`. A premissa estava certa —
o bloqueio era unilateral (o lado do Dia D já tinha `productDiscounts: true`).

| id | título | antes | depois |
|---|---|---|---|
| 1656398315739 | 10% OFF · 3+ Kits | `orderDiscounts: false` | `orderDiscounts: true` |
| 1656400085211 | 15% OFF · 5+ Kits | `orderDiscounts: false` | `orderDiscounts: true` |
| 1656400478427 | 20% OFF · 8+ Kits | `orderDiscounts: false` | `orderDiscounts: true` |

`productDiscounts: true` e `shippingDiscounts: true` preservados nos três.
Alteração **permanente** — ver plano de reversão.

### ⚠️ 8 unidades dão 28%, não 30%
Desconto de PEDIDO incide sobre o subtotal **já reduzido** pelo desconto de
produto. Não somam, compõem:

| faixa | conta | efetivo |
|---|---|---|
| 3+ | 1 − (0,90 × 0,90) | **19%** |
| 5+ | 1 − (0,85 × 0,90) | **23,5%** |
| 8+ | 1 − (0,80 × 0,90) | **28%** |

8 × Adulto = R$ 2.776 → sai **R$ 1.998,72** (28%). A 30% flat seria
R$ 1.943,20 — diferença de **R$ 55,52**. O card promete 30%.
Não dá pra chegar em 30% flat empilhando esses dois descontos.

Os três de volume valem só para Adulto, Kids 2-4 e Kids 5-9 —
**Kit Família não entra**, e nunca entrou.

## Correção 2 · Brinde limitado a 1
`1705126985947` · `usesPerOrderLimit`: `null` → `1`

## Correção 3 · Óleo fora do gatilho
`1705126985947` · `customerBuys.items.products`:

- antes: Adulto, Kids 2-4, Kids 5-9, Kit Família, **Óleo de Alho**
- depois: Adulto, Kids 2-4, Kids 5-9, Kit Família

`customerGets` intacto: 1 × Óleo de Alho a 100%.

---

## Correção 4 · Auto-adicionar o brinde

Arquivo: `snippets/vf-diad-brinde.liquid` (md5 `2a70194b5bef86ecd74a4d57677da006`)
+ uma linha `{%- render 'vf-diad-brinde' -%}` antes de `</body>` no `layout/theme.liquid`.

### Trava de data — dupla, de propósito
1. **Liquid** (`'now' | date`, fuso da loja = BRT): o script só é renderizado
   em 09/09 e 10/09. Nos outros dias não vai nem HTML.
2. **JS**: a *adição* só ocorre dentro de 09/09/2026 00:00:00–23:59:59 BRT,
   calculado com UTC−3 explícito (`getTimezoneOffset()` compensado), nunca
   com o fuso do navegador.

Fora da janela o script faz **uma** coisa: remove o brinde que ele mesmo
deixou. Isso protege quem montou o carrinho às 23h5x e voltou no dia 10 —
sem isso, ficaria com um óleo de R$ 67 que já não é mais grátis.

### Regras
| situação | ação |
|---|---|
| tem protocolo, não tem óleo | adiciona 1 óleo com `_brinde: "dia-d"` |
| não tem protocolo, tem brinde marcado | remove a linha |
| cliente já tinha óleo próprio (sem marcador) | não faz nada — o BXGY zera o que já está lá |
| fora da janela, tem brinde marcado | remove |
| óleo sem marcador | **nunca** removido |

### Anti-loop
Só considero que mudou algo depois de reler `/cart.js` e **confirmar** o
resultado. Se o add falhar (esgotado, 422), não há reload — logo não há
segunda tentativa. Falha de rede é engolida em silêncio.

### Onde está instalado
| tema | id | status |
|---|---|---|
| Dia D - Padrão | 163879354587 | ✅ snippet + theme.liquid, md5 conferido |
| VermFree Tema Padrão (MAIN) | 164523081947 | ❌ **bloqueado pela API** — instalar à mão |

A API recusa escrita em tema publicado (`live_theme / targets_live`).
Os arquivos prontos estão em `tema-principal/`.

---

## Reversão · quinta 10/09

### 1. ⚠️ PRIMEIRO: recriar o frete grátis acima de R$ 399
`1658793361627` tem `endsAt: 2026-09-09T03:00:00Z` e **não volta sozinho**.
A partir de quinta a loja fica sem frete grátis nenhum até a Semana do
Cliente (13/09). Estado original a recriar:

```
título:  Frete Grátis · Pedidos acima de R$ 399
tipo:    DiscountAutomaticFreeShipping
mínimo:  subtotal >= R$ 399,00 BRL
combina: orderDiscounts false · productDiscounts false · shippingDiscounts false
startsAt: imediato    endsAt: null
```

### 2. Reverter os três de volume
`orderDiscounts` de volta para `false` em 1656398315739, 1656400085211,
1656400478427 — **se** for essa a decisão. Vale reavaliar: o empilhamento é
provavelmente o comportamento desejado o ano todo, e voltar pra `false`
recria o bloqueio na próxima campanha com desconto de pedido.

### 3. Brinde no tema
Nada a fazer. A trava de data desliga sozinha: em 10/09 o snippet só limpa,
e a partir de 11/09 não renderiza mais nada. Confirmar no dia 11 que a
página não tem mais `__vfDiadBrinde` no HTML.

### 4. BXGY e 10% OFF
Expiram sozinhos em `2026-09-10T02:59:59Z`. Nada a fazer.
