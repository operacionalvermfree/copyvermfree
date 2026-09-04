# Shopify · pop-up de captura de e-mail (VermeFree)

Mudança decidida na reunião de **04/09** (Vitor, Gabriel, Pedro): eliminar a fricção
do pop-up inicial — sai o quiz de 3 etapas, fica só a captura de e-mail em troca do
cupom **5OFF**, e a visitante cai na **home**.

⚠️ Vale **só para a VermeFree**. A Botanika não é tocada.

## Arquivos

| Caminho | O que é |
|---|---|
| `snippets/vf-diagnostico-popup.liquid` | Versão nova (tela única). É o que foi publicado nos temas. |
| `backups/vf-diagnostico-popup.ORIGINAL.liquid` | Conteúdo original (quiz de 3 etapas), salvo antes de alterar. |

O **nome do arquivo foi mantido** de propósito: `layout/theme.liquid` chama
`{%- render 'vf-diagnostico-popup' -%}`. Renomear quebraria o render.
Renomear depois, com calma, junto com a chamada no layout.

## Checksums (MD5)

| Versão | Tamanho | MD5 |
|---|---|---|
| Original (quiz) | 18.926 B | `86484ae461d1201576013af3cbcc14b5` |
| Nova (captura)  | 7.153 B  | `4922d253bc862edd85cbd86f4f26ac5c` |

## Estado por tema

| Tema | gid | Papel | Situação |
|---|---|---|---|
| Gap Frete Gratis | 164712808667 | unpublished | ✅ **aplicado** |
| VermFree Tema Padrão | 164523081947 | **MAIN (no ar)** | ⛔ **pendente** — escrita em tema publicado é bloqueada |
| Copy of VermFree Tema Padrão | 164706451675 | unpublished | pop-up antigo (tema órfão — avaliar exclusão) |
| Semana do Cliente | 164610474203 | unpublished | pop-up antigo |
| Semana do Cliente - rascunho | 164712906971 | unpublished | pop-up antigo |
| VermFree — Draft LP VSL+Quiz (25/09) | 164655497435 | unpublished | pop-up antigo |
| Dia D Kids | 164572430555 | unpublished | pop-up antigo **em variante própria** (skin vermelha + faixa "Dia D Kids · só hoje") |

Temas sem o pop-up: Tema OFICIAL, Dia D - Padrão, Semana da Lua Nova - Padrão.

## O que a versão nova preserva

- `/discount/5OFF?redirect=…` no submit (é o que aplica o cupom na sessão) —
  destino agora é a **home**: `%2F%3Futm_source%3Dpopup_email%26utm_medium%3Donsite%26utm_campaign%3Dcaptura`
- Captura via `{% form 'customer' %}` (`contact[email]`), AJAX, estado "Enviando..."
- Cookie `vf_diag_popup`, snooze 5 dias / 30 dias se converteu, gatilho ~4s
- Não aparece em `/cart`, `/checkout`, `/account`; não empilha com `vf_oleopop_shown`
- Fecha com ESC, overlay e X
- `@media (max-width: 480px)` mantido

## Tags

O formulário grava `contact[tags]` = **`quiz-diagnostico,popup-email`**.

`quiz-diagnostico` foi **mantida de propósito**: é a única dessas tags com dependência
conhecida — o segmento Shopify *"Pop-up Diagnóstico (quiz)"*
(`customer_tags CONTAINS 'quiz-diagnostico'`).

As tags de ramificação do quiz (`quiz-adulto`, `quiz-kids`, `quiz-familia`,
`quiz-leveza`, `quiz-disposicao`, `quiz-sono`, `quiz-prevencao`) deixam de ser
gravadas — nenhum segmento Shopify e nenhuma automação do ActiveCampaign depende
delas hoje. **Confirmar com a Sarah** antes de considerar encerrado.

---

# Promo · Frete Grátis sem mínimo (05–06/09/2026)

Decidido com o Gabriel: frete grátis **sem mínimo**, sábado 05 e domingo 06/09.
Como não há mínimo, **não existe gap** — a barra de progresso vira *reforço* da
promo em vez de contador ("faltam R$ X" sairia mentindo).

Tudo só no tema **Gap Frete Gratis** (gid 164712808667).

## Desconto no Shopify

| | |
|---|---|
| Título | Frete Grátis · Fim de Semana 05-06/09 (sem mínimo) |
| ID | `gid://shopify/DiscountAutomaticNode/1705321136347` |
| Tipo | automático, frete grátis |
| Mínimo | **nenhum** |
| Janela | 05/09 00:00 → 06/09 23:59:59 (Brasília) |
| Status na criação | SCHEDULED |
| Combina com | descontos de produto ✔ · de pedido ✔ |

## Arquivos do tema

| Arquivo | MD5 antes | MD5 depois |
|---|---|---|
| `snippets/vf-frete-progress.liquid` | `7642bb23cf07443001755a9b2a5ae936` | `398c1ef5076ef3cded1d6749863a8e72` |
| `sections/vf-announcement-bar.liquid` | `84512c6d1495733b9631ea282179d2de` | `41b1fe1d42508773cadf0bd081e34073` |

Originais em `backups/`.

## ⚠️ A janela está escrita em TRÊS lugares

Mexeu em um, mexer nos três — senão a loja anuncia uma coisa e o checkout cobra outra:

1. o desconto automático no Shopify (acima);
2. `snippets/vf-frete-progress.liquid` → `PROMO_INICIO` / `PROMO_FIM` (epoch UTC
   `1788577200` / `1788749999`);
3. `sections/vf-announcement-bar.liquid` → `ann_today == '2026-09-05' or '2026-09-06'`
   e `ann_promo_end = '2026-09-07T00:00:00-03:00'`.

## Como cada peça se comporta

**Barra de frete** (`vf-frete-progress`): dentro da janela mostra "Frete grátis
liberado — em qualquer pedido, só neste fim de semana" com a barra cheia. Fora
da janela volta sozinha ao comportamento normal de R$399. Também limpei CSS
morto que já estava lá (`.vf-frete--nudge`, `.vf-frete__cta*`).

**Tarja de anúncio** (`vf-announcement-bar`): reaproveitei o mecanismo de promo
que já existia (foi feito pro frete grátis de 30-31/07 e estava com data vencida).
Só troquei as datas. Nos dias 05 e 06/09 ela fica vermelha, com
"🚨 FRETE GRÁTIS SEM MÍNIMO — acaba em <contador>". Fora disso, volta às
4 mensagens rotativas de sempre.

`preview_promo` (checkbox no editor) força o visual pra conferir antes. Conferi
que ele está **desligado** no `settings_data.json` — a tarja não aparece agora.

## ⛔ Pendência crítica: 5OFF x frete grátis não combinam

O cupom **5OFF** está com `combinesWith.shippingDiscounts = false`. O pop-up de
captura aplica o 5OFF sozinho na sessão. Resultado no fim de semana: **quem pegar
o cupom pelo pop-up não recebe o frete grátis** — a loja anuncia "frete grátis em
tudo" e o checkout cobra frete.

Correção: virar `shippingDiscounts` para `true` no 5OFF. Decisão de margem
(5% + frete grátis empilhados) — precisa de aval antes.

Os descontos automáticos de volume (10/15/20% Kits) e o do Óleo já estão com
`shippingDiscounts: true`, então esses combinam normalmente.
