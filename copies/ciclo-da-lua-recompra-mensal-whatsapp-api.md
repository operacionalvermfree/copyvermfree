# Ciclo da Lua — Recompra Mensal (WhatsApp API)

> Comunicação de recompra automatizada, disparada entre os dias 13 e 17 de cada mês, para clientes que já compraram o protocolo. Objetivo: preparar o cliente pra começar o próximo ciclo no timing certo da lua nova.

## O que preencher
- `{{1}}` — primeiro nome do cliente.
- `{{2}}` — data da próxima lua nova (atualizar todo mês).
- `{{3}}` — cupom de retorno (só na Versão Alternativa; ex.: "10% OFF com o VOLTA10").
- `[LINK]` — nas duas versões.

---

## 1. VERSÃO PRINCIPAL (disparo padrão mensal, sem cupom)

```
Nome sugerido do template: vermefree_ciclodalua_mensal_principal
Categoria: MARKETING

BODY:
Oi {{1}}! 🌙
A próxima lua nova é dia {{2}}.

Se você já sentiu como é bom manter a rotina de desparasitação natural em dia, esse é um bom momento pra começar o preparo do próximo ciclo.

A Silimarina começa 15 dias antes da lua — por isso vale garantir o kit com calma, sem correria de última hora.

FOOTER (opcional): Rotina se sustenta com constância, não com pressa.

BOTÃO (CTA URL): Preparar meu próximo ciclo → [LINK]
```

---

## 2. VERSÃO ALTERNATIVA (A/B — gatilho de janela + cupom de retorno)

> Uso pontual: só em meses específicos que você quiser puxar performance. Não usar todo mês — isso protegeria a percepção de valor da versão principal.

```
Nome sugerido do template: vermefree_ciclodalua_mensal_alt_cupom
Categoria: MARKETING

BODY:
Oi {{1}}! 🌙
Faltam poucos dias pra fase de preparo do seu próximo ciclo — a lua nova de {{2}} está chegando.

Pra facilitar sua volta esse mês, separei um mimo: {{3}}.

A Silimarina começa 15 dias antes da lua, então esse é o momento certo de garantir o kit.

FOOTER (opcional): Vale só essa janela, depois volta ao normal.

BOTÃO (CTA URL): Usar meu cupom de retorno → [LINK]
```

---

## 3. NOTAS DE IMPLEMENTAÇÃO

**Variáveis do template**
- `{{1}}` = primeiro nome do cliente.
- `{{2}}` = data da próxima lua nova — atualizar manualmente todo mês (calendário lunar não é fixo, varia ~29,5 dias).
- `{{3}}` = cupom de retorno — só preenchido/usado na Versão Alternativa.

**Categoria do template na Meta**
MARKETING nas duas versões (é uma mensagem promocional de recompra, não uma notificação transacional — não se enquadra em UTILITY).

**Timing**
- Disparo entre os dias **13 e 17 de cada mês**, sempre mirando ~15 dias antes da lua nova daquele mês (mesma lógica da Silimarina: início 15 dias antes do ciclo).
- Frequência: 1x por mês. Alternar: Versão Principal na maioria dos meses; Versão Alternativa só quando houver decisão pontual de puxar volume.

**Base de envio**
- Clientes que já compraram pelo menos 1 protocolo (base ativa de recompra), com opt-in de WhatsApp confirmado.
- Recomendado excluir quem comprou nos **últimos ~20-25 dias** antes do disparo, pra não empurrar recompra em cima de uma compra recente (mesmo raciocínio da exclusão do Dia D usada na campanha de Reativação/Recompra de agosto).
- Se houver segmentação por tempo desde a última compra (ex: 30-60 / 60-90 / 90+ dias), essa régua mensal pode substituir/absorver os disparos avulsos de recompra — vale alinhar com quem cuida do calendário de campanhas pra não duplicar envio no mesmo cliente no mesmo mês.

## 4. CHECKLIST ANVISA

- [x] Sem claim de cura / sem "elimina/erradica/mata" / sem "em X dias"
- [x] Não cita médico nem influenciador como aval
- [x] Não diagnostica o leitor
- [x] Tom natural/acolhedor, não alarmista nem milagreiro
- [x] Linguagem segura de desparasitação ("rotina de desparasitação natural", "auxilia", "ciclo")
- [x] Desconto como exceção (só na Versão Alternativa, não na principal)
- [x] 1 CTA claro por versão
- [x] Fala com mulher/mãe 30–50 que cuida da família (tom de constância e cuidado, sem pressão)
