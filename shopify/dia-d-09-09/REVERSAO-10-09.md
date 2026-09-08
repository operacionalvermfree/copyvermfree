# Reversão — quinta 10/09, 00h00 BRT

Ordem importa. O item 1 é o que quebra a loja se for esquecido.

---

## 1. ⚠️ Frete grátis acima de R$ 399 — RECRIAR
`1658793361627` tem `endsAt: 2026-09-09T03:00:00Z` e **não volta sozinho**.
Sem isso a loja fica sem frete grátis nenhum até a Semana do Cliente (13/09).

```
título:   Frete Grátis · Pedidos acima de R$ 399
tipo:     DiscountAutomaticFreeShipping
mínimo:   subtotal >= R$ 399,00 BRL
combina:  orderDiscounts false · productDiscounts false · shippingDiscounts false
startsAt: imediato     endsAt: null
```

## 2. ⚠️ Faixas de volume — DEVOLVER `endsAt: null`
As três estão ACTIVE hoje com `endsAt` marcado para o início do Dia D.
Às 03:00Z de 09/09 elas viram EXPIRED e **não voltam sozinhas**.

| id | faixa | ação |
|---|---|---|
| 1656398315739 | 10% · 3+ | `endsAt: null` |
| 1656400085211 | 15% · 5+ | `endsAt: null` |
| 1656400478427 | 20% · 8+ | `endsAt: null` |

Mecanismo **testado em 07/09** num desconto descartável: um desconto
EXPIRED volta a ACTIVE assim que o `endsAt` vira `null`. O status é
derivado das datas, não é estado preso.

Os três já estão com `combinesWith.orderDiscounts: false`, que é o
estado original da loja. Não mexer nisso na volta.

## 3. Preços — DESFAZER a virada
Ver `OFERTA-V2-PRECOS.md`. Restaurar `price` e `compareAtPrice` exatos,
incluindo os dois `compareAtPrice` que já estavam errados antes.

## 4. Reativar o desconto automático de 12%?
**Não.** `1705238298843` tem `endsAt` em 10/09 02:59:59Z e expira sozinho.
Se a virada de preço acontecer, ele terá sido desativado antes — e não
deve voltar.

## 5. Expira sozinho, nada a fazer
- `1706014933211` · 5% · 2 unidades (só 09/09)
- `1705126953179` · Frete grátis sem mínimo
- `1705126985947` · Brinde óleo de alho
- `1706010411227` · Brinde Kids acima de R$ 700

## 6. Tema
O snippet do brinde se desliga sozinho pela trava de data. Confirmar no
dia 11 que o HTML não tem mais `__vfDiadBrinde`.
