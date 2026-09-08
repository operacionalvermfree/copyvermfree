# Dia D 09/09 — oferta OFICIAL E FINAL

Fonte: mensagem do Vitor Gutierrez no grupo, 07/09 12:48.
"Considerem essa como a versão oficial e desconsiderem qualquer
percentual ou condição anterior."

Substitui o PDF de 07/09 e a descrição da task ClickUp `86ak8v6mh`.
**A task do ClickUp ainda descreve a oferta velha** (17%, teto de 22%,
faixa de 2 unidades) — precisa ser atualizada, senão quem escrever peça
a partir dela erra.

---

## Escada de desconto — CONFIGURADA

| faixa | % | id |
|---|---|---|
| site inteiro / 1 unidade | 12% | `1706029940955` |
| 3 unidades | 15% | `1706029973723` |
| 5 unidades | 18% | `1706030104795` |

As três são classe **PRODUCT**, cobrem os **5 produtos**, e valem só na
janela `2026-09-09T03:00:00Z` → `2026-09-10T02:59:59Z`.

**Não somam.** O Vitor foi explícito: "os percentuais de quantidade são a
condição final de cada faixa, ou seja, não é 12% + 15% ou 12% + 18%".
O Shopify aplica um único desconto de produto por linha, o de maior
valor pro cliente — que é exatamente esse comportamento.

O preço **NÃO** é alterado. Some a virada de madrugada que estava no
plano antigo, e some o risco de desconto vazar antes da hora.

## Resto da oferta — já estava configurado e continua valendo

| item | id | estado |
|---|---|---|
| Frete grátis sem mínimo | `1705126953179` | SCHEDULED |
| 1 Óleo de Alho em qualquer pedido | `1705126985947` | SCHEDULED, limite 1 |
| 1 Protocolo Infantil acima de R$ 700 | `1706010411227` | SCHEDULED, limite 1 |
| Faixas antigas 3+/5+/8+ | — | expiram em 09/09 03:00Z |

## Cupom das influenciadoras
Os cupons são classe ORDER. As faixas do Dia D agora são classe PRODUCT.
Classes diferentes **combinam**, então o 5% entra por cima:

| carrinho | conta | total |
|---|---|---|
| 1 un + cupom | 1 − (0,88 × 0,95) | **16,4%** |
| 3 un + cupom | 1 − (0,85 × 0,95) | **19,25%** |
| 5 un + cupom | 1 − (0,82 × 0,95) | **22,1%** |

⚠️ O Vitor escreve "faixa de 12% + cupom = mais 5%". Percentual sobre
percentual **compõe**, não soma: dá 16,4%, não 17%. A copy não pode
prometer o número somado.

## Fora do Shopify
- Manual da Desparasitação para todos → e-mail
- Guia da Imunidade + Guia da Suplementação p/ os 100 primeiros → e-mail
  + apuração manual. Shopify não tem gate de "N primeiros pedidos".
- Comissão 10% → 12% → ferramenta de afiliados

---

## ⚠️ O QUE PRECISA SER VERIFICADO ÀS 00h05 DE QUARTA

Não consigo alcançar a loja deste ambiente (rede bloqueada) e os
descontos só ficam ativos às 00h00. Então **uma coisa não foi testada**:

**As três faixas empilham entre si?** O desenho depende de o Shopify
aplicar só a melhor faixa por linha. É o comportamento clássico e é o
que o Vitor descreve, mas versões novas da API introduziram um sistema
de `tags` que permite empilhar produto+produto na mesma linha. Eu **não**
setei tags em nenhuma das três, justamente pra ficar no comportamento
clássico.

**Como verificar em 30 segundos:** carrinho com 5 unidades do Adulto.

- Certo: R$ 1.422,70 (18%)
- Errado: R$ 1.062,42 — significa que empilhou 12+15+18

**Se empilhou:** apagar `1706029973723` e `1706030104795` na hora. Todo
mundo fica com 12% e a campanha continua de pé enquanto se decide.
