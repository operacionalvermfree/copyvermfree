# Dia D v2 — troca de preços às 00h00 (NÃO EXECUTADA)

O 12% passa a ser **embutido no preço**. Isso não é agendável no Shopify:
alguém (ou uma rotina) precisa rodar a virada às **00h00 de 09/09** e a
volta às **00h00 de 10/09**, horário de Brasília.

## ⚠️ As duas coisas são acopladas
No mesmo instante em que o preço cai, o desconto automático de 12%
(`gid://shopify/DiscountAutomaticNode/1705238298843`) precisa ser
**desativado**. Se os dois ficarem de pé juntos, o cliente paga
12% no preço + 12% no pedido = **22,6% de desconto**.

## Virada — 09/09 00h00 BRT

| produto | variante | preço hoje | preço no Dia D | compareAt no Dia D |
|---|---|---|---|---|
| Protocolo Adulto | 48772143415515 | 347,00 | **305,36** | 347,00 |
| Kids 2 a 4 | 48772145250523 | 270,00 | **237,60** | 270,00 |
| Kids 5 a 9 | 48772147085531 | 389,00 | **342,32** | 389,00 |
| Kit Família | 48772149739739 | 1.150,00 | **1.012,00** | 1.150,00 |
| Óleo de Alho | 48968692891867 | 67,00 | **58,96** | 67,00 |

+ desativar `1705238298843` (Dia D — 12% OFF, desconto de pedido).

## Volta — 10/09 00h00 BRT
Restaurar **exatamente** os valores da coluna "preço hoje" e os
`compareAtPrice` originais abaixo. Anotados porque dois estão errados
hoje e a volta precisa ser fiel, não "corrigida":

| variante | price original | compareAtPrice original |
|---|---|---|
| 48772143415515 | 347.00 | **337.00** ⚠️ menor que o preço |
| 48772145250523 | 270.00 | 270.00 (igual ao preço, não mostra de/por) |
| 48772147085531 | 389.00 | null |
| 48772149739739 | 1150.00 | **846.60** ⚠️ menor que o preço |
| 48968692891867 | 67.00 | null |

⚠️ Adulto e Kit Família têm `compareAtPrice` MENOR que o preço. Isso é
dado errado que já existia antes de qualquer coisa que eu fiz — o Shopify
não mostra "de/por" nesse estado. Não corrigi porque não é escopo desta
tarefa, mas vale olhar depois.

## Efeito colateral que some sozinho
Com o 12% no preço, não existe mais desconto de PEDIDO no Dia D. Logo o
cupom de 5% das influenciadoras (classe ORDER) aplica limpo por cima —
o bloqueio de "dois descontos de pedido" desaparece sem gambiarra.

Composição real: 5% sobre o preço já reduzido → 1 − (0,88 × 0,95) = **16,4%**,
não 17%. Percentuais compõem, não somam.
