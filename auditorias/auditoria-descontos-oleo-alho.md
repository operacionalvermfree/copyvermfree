# Auditoria — Descontos do Óleo de Alho (order bump)

**Data:** 04/09/2026 · **Fonte:** dados reais da loja (Shopify Admin API) + prints da página de bump e do carrinho.
**Veredito:** a escada de volume do Óleo de Alho **não existe na prática**. 1, 3 e 6 frascos custam exatamente o mesmo por unidade (R$ 56,95). Além disso, há **conflito de regras** que faz o valor do checkout divergir do valor prometido na página.

---

## 1. O que a página promete

| Opção | "de" | Preço exibido | Preço/un | Desconto real |
|---|---|---|---|---|
| 1 frasco | R$ 67,00 | R$ 56,95 | **R$ 56,95** | 15% |
| 3 frascos · "MAIS ESCOLHIDO" | R$ 201,00 | R$ 170,85 | **R$ 56,95** | 15% |
| 6 frascos · "MELHOR CUSTO" | R$ 402,00 | R$ 341,70 | **R$ 56,95** | 15% |

**Os três níveis têm o mesmo preço unitário.** Comprar 6 não é "melhor custo" que comprar 1 — é o mesmo custo. A página inclusive já entrega isso escrito: o rótulo "R$ 56,95/un" aparece igual no card de 6 e no de 3.

Consequência de copy: os selos **"MELHOR CUSTO"** e **"Economize R$ 60,30"** são promessas que o próprio preço desmente. Quem faz a conta (e o ICP da VermeFree faz — é a mulher que lê rótulo) percebe.

---

## 2. Por que isso acontece — as regras ativas no Shopify

Existem **três** descontos automáticos ativos incidindo sobre o Óleo de Alho (preço cheio R$ 67,00):

| Regra | Tipo | Gatilho | % | Combina com outros descontos de produto? |
|---|---|---|---|---|
| `Óleo de Alho · 3 frascos - 15%` | Basic (coleção) | qtd ≥ 3 | **15%** | sim |
| `Óleo de Alho · 6 frascos - 15%` | Basic (coleção) | qtd ≥ 6 | **15%** | sim |
| `Order Bump · Óleo de Alho 15% (com protocolo no carrinho)` | **BxGy** | 1 protocolo no carrinho | **15% em 1 única unidade** (`usesPerOrderLimit: 1`) | **NÃO** |

### Erro 1 — o desconto de 3 frascos está com o % errado
Pelo CLAUDE.md, a regra de volume do Óleo é **3 frascos = 10% · 6 frascos = 15%**.
No Shopify, a regra de 3 frascos está configurada com **15%** — idêntica à de 6. Por isso a escada some: os dois degraus têm a mesma altura.

### Erro 2 — o bump dá 15% já no 1º frasco
O BxGy `Order Bump` concede 15% em **uma** unidade de Óleo sempre que houver um protocolo no carrinho. Como o bump só aparece nesse contexto, na prática **o frasco avulso já sai com 15%** — o mesmo desconto máximo da escada.

Resultado combinado dos erros 1 e 2: **1 = 3 = 6 = 15%**. Não há razão econômica nenhuma para o cliente subir de degrau.

---

## 3. Por que o desconto "não vai pro checkout"

O ponto crítico: o BxGy do bump está com **`combinesWith.productDiscounts = false`**.

Isso significa que ele **não convive** com os descontos de volume. Num carrinho com `1 protocolo + 3 óleos`, as duas regras são mutuamente exclusivas — o Shopify aplica **uma só**:

| Cenário | Desconto no óleo | Total dos 3 óleos |
|---|---|---|
| Vence a regra de **volume 3+** | 15% sobre 3 un = R$ 30,15 | **R$ 170,85** ← o que a página promete |
| Vence o **BxGy do bump** | 15% sobre **1 un** = R$ 10,05 | **R$ 190,95** ← R$ 20,10 a mais |

A página de bump exibe R$ 170,85 e afirma *"Desconto aplicado automaticamente no checkout"*. Se o BxGy for o vencedor da disputa, o checkout cobra **R$ 190,95**. É exatamente essa a divergência relatada.

Agravante: o preço R$ 170,85 aparece **já calculado na linha do carrinho** (print 2), sem linha de desconto separada. Isso indica que o número está sendo montado no front-end da página/tema, não vindo do motor de descontos do Shopify. O checkout recalcula do zero e pode chegar em outro valor — o cliente vê o preço subir na última tela, que é o pior lugar possível para uma surpresa de preço.

> **Verificar antes de fechar o diagnóstico:** rodar um checkout de teste real com `1 protocolo + 3 óleos` e conferir qual dos dois descontos o Shopify aplica. O conflito está provado pela configuração; qual regra vence é o que falta medir.

---

## 4. Riscos adicionais encontrados na varredura

1. **O bump expira em 09/09/2026** (`endsAt: 2026-09-09T03:00Z` = 09/09 00:00 BRT). A partir daí o card "1 frasco" passa a mostrar R$ 56,95 na página enquanto o checkout cobra R$ 67,00 — a mesma divergência, agora no frasco avulso.
2. ~~**Dois BxGy de brinde agendados**~~ — **verificado, sem problema.** `Dia D — 1 Óleo de Alho grátis` (09/09) e `Semana do Cliente — 2 Óleos grátis acima de R$600` (13–19/09) estão ambos com `productDiscounts: true`, ou seja, combinam com a escada de volume. Quem comprar 6 óleos e ganhar o brinde mantém os 20%.
3. **Estoque negativo** no Óleo de Alho (`inventoryQuantity: -224`) — venda a descoberto liberada. Fora do escopo desta auditoria, mas fica o registro.
4. **"4 items" no carrinho com 2 linhas** — é a contagem de unidades (3 óleos + 1 protocolo), não de produtos. Não é bug, mas confunde. Sugestão: "4 unidades · 2 produtos".

---

## 5. Correção proposta

### 5.1 Escada que realmente premia volume

| Opção | Desconto | Preço/un | Total | Economia |
|---|---|---|---|---|
| 1 frasco | — | R$ 67,00 | R$ 67,00 | — |
| 3 frascos | **15%** | R$ 56,95 | **R$ 170,85** | R$ 30,15 |
| 6 frascos | **20%** | R$ 53,60 | **R$ 321,60** | R$ 80,40 |

Cada degrau fica mais barato que o anterior — o selo "MELHOR CUSTO" passa a ser verdade, e o card de 3 (o mais escolhido) mantém exatamente o preço que já está no ar hoje (R$ 170,85), então não há perda percebida para quem já viu a oferta.

### 5.2 Ações no Shopify (ordem de execução)

1. **Pausar/excluir** o BxGy `Order Bump · Óleo de Alho 15%`. É a origem do conflito de checkout **e** do achatamento da escada. Sem ele, o frasco avulso volta a R$ 67 — que é justamente o que torna o pacote de 3 atraente.
2. **Alterar** `Óleo de Alho · 3 frascos` de 15% → mantém 15% (agora vira o 1º degrau real, já que o avulso volta a preço cheio).
3. **Alterar** `Óleo de Alho · 6 frascos` de 15% → **20%**, e renomear para `Óleo de Alho · 6 frascos - 20%`.
4. **Garantir** `combinesWith.productDiscounts = true` nas duas regras de volume (já está) e nos BxGy de brinde agendados.
5. **Alinhar o CLAUDE.md**: a seção 6 registra "Óleo de Alho: 3 = 10% · 6 = 15%". Atualizar para 3 = 15% · 6 = 20% assim que a mudança subir, para o copy não voltar a divergir da loja.

### 5.3 Ajuste na página do bump

- Fazer os preços virem do motor de descontos do Shopify, não de valor fixo no tema. Enquanto o número for calculado no front, qualquer mudança de regra recria a divergência.
- Trocar `1 frasco · R$ 56,95` por `1 frasco · R$ 67,00` (sem selo de economia).
- Se o preço "à vista" for desconto de pagamento (PIX), separar visualmente de desconto de volume. Hoje os dois estão fundidos no mesmo "Economize R$ X", o que torna impossível o cliente entender o que ganhou por quê.

---

## 6. Resumo em uma linha

Três regras de 15% empilhadas no mesmo produto zeraram a escada de volume (1 = 3 = 6 = R$ 56,95/un), e o BxGy do bump — marcado como não-combinável e limitado a 1 unidade — disputa com o desconto de volume no checkout, podendo cobrar R$ 190,95 onde a página prometeu R$ 170,85.


---

## 7. Status — alterações aplicadas em 04/09/2026

Executado via Shopify Admin API. Estado verificado após a mudança:

| Regra | Antes | Depois |
|---|---|---|
| `Order Bump · Óleo de Alho 15% (com protocolo no carrinho)` | ACTIVE · BxGy 15% em 1 un · `productDiscounts: false` | **DESATIVADO** |
| `Óleo de Alho · 3 frascos` | ACTIVE · 15% | ACTIVE · 15% *(inalterado — virou o 1º degrau real)* |
| `Óleo de Alho · 6 frascos - 15%` | ACTIVE · 15% | **`Óleo de Alho · 6 frascos - 20%` · ACTIVE · 20%** |

Sobraram **duas** regras incidindo no Óleo de Alho, ambas com `combinesWith.productDiscounts: true` e apontando para a coleção `Óleo de Alho (desconto volume)`. Não há mais nenhuma regra não-combinável no produto — o conflito de checkout está eliminado na origem.

**Escada agora vigente no checkout:**

| Opção | Desconto | Preço/un | Total | Economia |
|---|---|---|---|---|
| 1 frasco | — | R$ 67,00 | R$ 67,00 | — |
| 3 frascos | 15% | R$ 56,95 | R$ 170,85 | R$ 30,15 |
| 6 frascos | 20% | R$ 53,60 | R$ 321,60 | R$ 80,40 |

O CLAUDE.md (seção 6) foi atualizado para refletir a nova regra.

### ✅ Página do bump — corrigida em 04/09/2026 (tema "Copy of VermFree Tema Padrão")

Dois snippets foram reescritos no tema de cópia (`snippets/vf-order-bump.liquid` e `snippets/vf-oleo-desconto-aviso.liquid`). A mudança de fundo: **nenhum preço é mais escrito à mão**. Tudo é derivado em Liquid de `bump_product.price` (o preço real do produto na Shopify) mais duas constantes de escada no topo do arquivo:

```liquid
{%- assign OLEO_PCT_3 = 15 -%}
{%- assign OLEO_PCT_6 = 20 -%}
```

Se a escada mudar no admin, muda-se só essas duas linhas e a página inteira se reajusta — preço/un, valor cheio riscado, parcela, à vista, "Economize" e o rótulo do botão.

**O que o bump passa a renderizar:**

| Card | Cheio | Parcela | À vista | Por unidade | Economize |
|---|---|---|---|---|---|
| 1 frasco | — | 10x R$ 6,70 | R$ 67,00 | R$ 67,00 | — |
| 3 frascos | R$ 201,00 | 10x R$ 17,09 | **R$ 170,85** | R$ 56,95 | R$ 30,15 |
| 6 frascos | R$ 402,00 | 10x R$ 32,16 | **R$ 321,60** | R$ 53,60 | R$ 80,40 |

Mudanças de conteúdo, além dos números:

1. **Card "1 frasco"** perdeu o riscado e o selo "Economize" — sem o BxGy, o frasco avulso é preço cheio, e é justamente isso que dá sentido ao pacote de 3.
2. **Selo "MELHOR CUSTO"** no card de 6 passou a ser verdadeiro (R$ 53,60/un contra R$ 56,95/un do de 3).
3. **A parcela agora é calculada sobre o preço com desconto**, não sobre o cheio. O desconto por volume é automático e independe da forma de pagamento — a versão antiga exibia "10x R$ 20,15" (= R$ 201,50) para um pedido que a Shopify cobra R$ 170,85, o que subestimava a oferta no parcelado.
4. **Microcopy** do rodapé: "Desconto aplicado automaticamente no checkout · só nesta página" → "Desconto por volume aplicado automaticamente no checkout". O desconto não é exclusivo dessa página (é regra de loja), então a exclusividade era falsa.
5. **Faixa de aviso no carrinho** (`vf-oleo-desconto-aviso`) atualizada de 10%/15% para 15%/20%, também via constantes.

> **Premissa a confirmar:** a parcela usa divisão simples por 10 (`preço ÷ 10`, arredondado pra cima no centavo). A versão anterior tinha um acréscimo de ~0,3% embutido nos valores fixos (10x R$ 6,72 para um produto de R$ 67,00), provavelmente juros do gateway. Como essa regra não está documentada em lugar nenhum do tema, não a reproduzi. Se houver juros de parcelamento, basta ajustar a constante `PARCELAS` / a fórmula em um único ponto do arquivo.

### ⚠️ Pendente

**1. Publicar o tema.** As mudanças estão no tema de cópia (`Copy of VermFree Tema Padrão`, não publicado). O tema no ar (`VermFree Tema Padrão`) ainda tem os preços antigos. Revisar no preview e publicar.

**2. Não foi possível renderizar daqui.** A política de rede desta sessão bloqueia `vermefree.com.br`, então o teste foi estático: balanceamento de tags Liquid, ausência de variáveis sem `assign`, e conferência da aritmética em centavos. Vale abrir o preview do tema com um carrinho de teste (protocolo + óleo) antes de publicar.

**3. O cupom OLEO20 recria o problema.** O popup `vf-upsell-oleo-popup.liquid` (site-wide) oferece o Óleo com 15% OFF e manda o cliente para `/discount/OLEO20`. Esse cupom é um **código**, não um desconto automático — por isso não apareceu na varredura inicial:

| | |
|---|---|
| Título | Upsell Óleo de Alho 15% OFF (link pós-compra) |
| Valor | 15% no Óleo de Alho, **sem mínimo de quantidade** |
| Combina com descontos de produto? | **NÃO** (`productDiscounts: false`) |
| Vigência | 13/08 → 09/09/2026 |

É exatamente o mesmo padrão do BxGy que foi desativado, e depois da correção ele passa a **custar dinheiro ao cliente**: quem aplica OLEO20 e leva 6 frascos recebe 15% em vez de 20% — perde R$ 13,40 — porque o cupom bloqueia o desconto por volume. E, como não tem mínimo, ele reata o "1 frasco = R$ 56,95" que achatava a escada.

Não mexi nele: desativar um canal de oferta ativo é decisão de negócio, não de correção técnica. Opções, da mais simples à mais completa:
- **Desativar o OLEO20** e deixar o popup empurrar para o pacote de 3 (que já dá os mesmos 15%, com margem melhor por pedido).
- **Marcar o cupom como combinável** com descontos de produto — resolve a perda nos 6 frascos, mas empilha com o volume (15% + 20% no mesmo item).
- **Manter como está** até 09/09, quando ele expira sozinho.
