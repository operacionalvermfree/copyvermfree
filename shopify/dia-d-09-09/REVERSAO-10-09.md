# Reversão 10/09 — agora é CONFERÊNCIA, não execução

Antes essa lista tinha duas coisas que não voltavam sozinhas. Resolvi as
duas criando **sucessores agendados** que ligam sozinhos às 00h00 de
quinta (`2026-09-10T03:00:00Z`). Ninguém precisa acordar de madrugada.

## Como funciona
O original expira quando o Dia D começa; o sucessor liga quando o Dia D
acaba. A janela vazia entre os dois é exatamente o Dia D, coberta pelos
descontos da campanha.

| o que | original (expira 09/09 03:00Z) | sucessor (liga 10/09 03:00Z) |
|---|---|---|
| Frete acima de R$ 399 | `1658793361627` | `1706030661851` |
| 10% · 3+ Kits | `1656398315739` | `1706030694619` |
| 15% · 5+ Kits | `1656400085211` | `1706030727387` |
| 20% · 8+ Kits | `1656400478427` | `1706030760155` |

Os sucessores replicam a configuração original: mesmos produtos, mesmas
quantidades mínimas, mesmo `combinesWith`, mesmo mínimo de R$ 399 e
mesmo destino (todos os países). Sem data de fim.

Os títulos precisaram ser diferentes (o Shopify exige título único) e
são todos apresentáveis ao cliente, porque título de desconto aparece
no checkout.

## O que fazer na quinta
Só **conferir** que os quatro sucessores estão `ACTIVE`. Nada a executar.

Depois disso, opcionalmente, apagar os quatro originais expirados para
não poluir o admin. Não tem pressa e não quebra nada deixá-los lá.

## Preço
Nada a fazer. A oferta final não mexe em preço — os 12/15/18 são
descontos de produto agendados. Isso saiu do plano por completo.
