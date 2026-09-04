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
