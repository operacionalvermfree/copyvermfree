# Live Educativa de Quinta — Divulgação (3 canais) · VermeFree

> Template reutilizável pra divulgação da Live de Quinta. Live educativa: protocolo de desparasitação natural, posologia (como se faz), sincronia com a lua nova (com leveza) e kit infantil (VermeFree Kids). Foco em educar e tirar dúvida — venda vem como consequência, sem pitch pesado.

## O que preencher
- `{{DATA}}` — data da live (quinta-feira)
- `{{HORARIO}}` — horário
- `{{PLATAFORMA_LINK}}` — onde acontece + link (ex.: Instagram @vermefree)
- `{{TEMA}}` — tema/título da live
- `{{1}}` — primeiro nome (WhatsApp API)

---

## 1. WHATSAPP API

### Convite (com antecedência)

```
Nome sugerido do template: vermefree_live_quinta_convite
Categoria: MARKETING

BODY:
Oi {{1}}! Quinta-feira ({{DATA}}) tem live educativa sobre {{TEMA}} 🌿
Vou explicar como funciona o protocolo, a posologia certinha e como funciona o kit infantil.

FOOTER (opcional): {{HORARIO}} · {{PLATAFORMA_LINK}}

BOTÃO (CTA URL): Ativar lembrete → {{PLATAFORMA_LINK}}
```

### Lembrete (no dia, próximo ao horário)

```
Nome sugerido do template: vermefree_live_quinta_lembrete
Categoria: MARKETING

BODY:
Oi {{1}}, começa daqui a pouco! 🎥
{{HORARIO}}, sobre {{TEMA}}.

BOTÃO (CTA URL): Entrar na live → {{PLATAFORMA_LINK}}
```

**Variáveis usadas:** `{{1}}`, `{{DATA}}`, `{{HORARIO}}`, `{{PLATAFORMA_LINK}}`, `{{TEMA}}`

---

## 2. E-MAIL

**Assunto:** Quinta tem live: {{TEMA}}
**Assunto (variação A/B):** Vamos tirar suas dúvidas sobre desparasitação natural

**Pré-header:** {{DATA}} às {{HORARIO}} — ativa o lembrete.

**Corpo:**
```
Olá,

Quinta-feira ({{DATA}}, às {{HORARIO}}) a gente se encontra numa live educativa sobre {{TEMA}}.

Vou explicar com calma: como funciona o protocolo, a posologia (como se faz, na prática) e como funciona o kit infantil, o VermeFree Kids.

Sem enrolação, sem pitch de venda — é uma conversa pra tirar dúvida e te ajudar a entender o porquê de cada etapa da rotina.

Um abraço,
Equipe VermeFree
```

**CTA (botão único):** Ativar lembrete e assistir

---

## 3. GRUPO/BROADCAST

```
🎥 Quinta tem live educativa: {{TEMA}}

{{DATA}}, às {{HORARIO}} — {{PLATAFORMA_LINK}}

Vou explicar como funciona o protocolo, a posologia certinha e como funciona o kit infantil. Só isso, sem pitch de venda.

👉 Ativa o lembrete e aparece lá
```

---

## NOTAS PARA SARAH

- **Convite (WhatsApp API + e-mail + grupo):** disparar com **antecedência** (sugestão: 2 a 3 dias antes da live, e reforço na véspera se fizer sentido no calendário).
- **Lembrete (WhatsApp API):** disparar **no dia da live**, próximo ao horário de início (ex.: 1h antes e/ou minutos antes de começar).
- Preencher `{{DATA}}`, `{{HORARIO}}`, `{{PLATAFORMA_LINK}}` e `{{TEMA}}` a cada semana/edição da live — nenhum desses campos foi inventado aqui, ficam como placeholder pra reuso.
- Mensagem de grupo pode ser reenviada em mais de um grupo/broadcast sem adaptação — é genérica o suficiente.

## CHECKLIST ANVISA

- [x] Sem claim de cura / sem "elimina/erradica/mata" / sem "em X dias"
- [x] Não cita médico nem influenciador
- [x] Não diagnostica
- [x] Tom educativo/acolhedor
- [x] Linguagem segura de desparasitação ("protocolo", "rotina", "posologia", "leveza")
- [x] Data/horário/link presentes (campos preenchíveis: `{{DATA}}`, `{{HORARIO}}`, `{{PLATAFORMA_LINK}}`)
- [x] 1 CTA claro por peça
- [x] Fala com mulher/mãe 30–50
