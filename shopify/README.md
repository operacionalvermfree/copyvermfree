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
| Status | **ACTIVE** (ativado em 04/09 21:12 BRT) |
| Combina com | descontos de produto ✔ · de pedido ✔ |

## Arquivos do tema

| Arquivo | MD5 antes | MD5 depois |
|---|---|---|
| `snippets/vf-frete-progress.liquid` | `7642bb23cf07443001755a9b2a5ae936` | `398c1ef5076ef3cded1d6749863a8e72` |
| `sections/vf-announcement-bar.liquid` | `84512c6d1495733b9631ea282179d2de` | `41b1fe1d42508773cadf0bd081e34073` |

Originais em `backups/`.

## Tudo ativado — o gatilho é publicar o tema

Decisão do Gabriel: nada de trava de data no tema. Quem controla o quando é a
publicação do "Gap Frete Gratis". Enquanto ele estiver no ar, a promo aparece.

**Mas atenção ao que é do TEMA e ao que é da LOJA:**

| Peça | Escopo | Ligado por |
|---|---|---|
| Barra de frete e tarja vermelha | tema | publicar o Gap Frete Gratis |
| Desconto de frete grátis | **loja inteira** | está ACTIVE agora, em qualquer tema |

O desconto **não** é do tema. Ele já está valendo no tema que está no ar agora
e vale até domingo 06/09 23:59:59, independente de qual tema esteja publicado.

Interruptores, se precisar desligar:
- barra: `PROMO_FRETE_GRATIS = false` em `snippets/vf-frete-progress.liquid`;
- tarja: desmarcar "🔴 Modo promo" no editor da seção;
- contador: campo "Fim da promo" no editor — em branco, anuncia sem contador
  (melhor que data vencida, que zera e fica "00:00:00");
- desconto: mudar a data de fim em Descontos.

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

## 5OFF x frete grátis — resolvido

O cupom **5OFF** estava com `combinesWith.shippingDiscounts = false`. Como o
pop-up aplica o 5OFF sozinho na sessão, quem pegasse o cupom **não** receberia o
frete grátis: a loja anunciaria "frete grátis em tudo" e o checkout cobraria.

Virado para `true` em 04/09. Agora 5% e frete grátis empilham. Para reverter, é
só voltar o campo para `false` no cupom 5OFF.

Os automáticos de volume (10/15/20% Kits) e o do Óleo já estavam com
`shippingDiscounts: true`.
