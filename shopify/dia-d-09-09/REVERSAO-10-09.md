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
| Óleo · 3 frascos 15% | `1686134849755` | `1706031317211` |
| Óleo · 6 frascos 20% | `1686134948059` | `1706031415515` |

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

---

## Descontos que CONTINUAM rodando no Dia D (decisão consciente)

A auditoria encontrou cinco descontos ativos sem data de fim que ninguém
tinha mencionado. Dois foram pausados (os do óleo, acima). Estes três
ficam de pé, porque só beneficiam o cliente e não contradizem nada que
foi prometido:

| id | desconto | por que fica |
|---|---|---|
| `1706004283611` | Order Bump · 2º Protocolo 15% | dá mais desconto, não menos |
| `1701896650971` | Order Bump · 2º Protocolo 15% (com protocolo) | idem |
| `1704147189979` | 5% OFF · 2 Protocolos Adulto | 5% perde pros 12% da faixa |

⚠️ Os dois primeiros são **quase idênticos e estão ativos ao mesmo
tempo**. Parece duplicata acidental, e é independente do Dia D — vale
olhar depois da campanha.

## Por que os do óleo eram um problema de verdade
Eles apontam para a coleção `537943507163` "Óleo de Alho (desconto
volume)", que contém exatamente o óleo da campanha. Com eles ativos, um
carrinho com 6 óleos pegaria 20% — furando o teto de 18% que o Vitor
definiu como condição final de cada faixa.
