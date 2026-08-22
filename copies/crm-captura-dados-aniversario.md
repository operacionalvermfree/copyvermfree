# Captura de Dados CRM — Cadastro de Aniversário

> Fluxo de captura de dados pra segmentação e relacionamento futuro. Prioridade 1: data de aniversário. Troca de valor: mimo no mês do aniversário. Automação a ser montada por Sarah + Clint.

## O que preencher
- `{{1}}` — primeiro nome do cliente (WhatsApp).
- `[LINK]` — na mensagem-convite (WhatsApp e e-mail).

---

## 1. MENSAGEM-CONVITE

### Versão WhatsApp API

```
Nome sugerido do template: vermefree_crm_convite_aniversario
Categoria: MARKETING

BODY:
Oi {{1}}! 🎂
Queremos guardar a data do seu aniversário pra te mandar um mimo especial no seu mês.

Leva menos de 1 minuto pra completar seu cadastro.

BOTÃO (CTA URL): Completar meu cadastro → [LINK]
```

### Versão E-mail

**Assunto:** Queremos lembrar do seu aniversário 🎂
**Assunto (variação A/B):** Um mimo esperando por você no seu mês

**Pré-header:** Leva menos de 1 minuto pra completar.

**Corpo:**
```
Olá,

Queremos guardar a data do seu aniversário pra te mandar um mimo especial quando o seu mês chegar.

É rápido: faltam só alguns dados pra completar seu cadastro com a gente.

Um abraço,
Equipe VermeFree
```

**CTA (botão único):** Completar meu cadastro

---

## 2. COPY DA PÁGINA/FORMULÁRIO DE CAPTURA

**Headline:** Guarda um mimo pra você no seu mês 🎂

**Subhead:** Complete seu cadastro em menos de 1 minuto e ganhe uma surpresa especial da VermeFree no mês do seu aniversário.

**Campos do formulário:**

1. **Data de aniversário** *(prioridade 1, obrigatório)*
   - Label: "Sua data de aniversário"
   - Placeholder: "DD/MM"
   - Microcopy: "Só o dia e o mês — pra te mandar o mimo certinho, sem precisar saber sua idade."

2. **Primeiro nome** *(obrigatório só se ainda não tiver na base)*
   - Label: "Seu nome"
   - Placeholder: "Como você gosta de ser chamada?"

3. **Cidade e estado** *(opcional)*
   - Label: "Cidade e estado"
   - Placeholder: "Ex.: Belo Horizonte, MG"
   - Microcopy: "Opcional — ajuda a gente a entender melhor onde nossas clientes estão."

4. **Cuida da saúde de crianças em casa?** *(opcional, sim/não)*
   - Label: "Você cuida da rotina de saúde de crianças em casa?"
   - Opções: Sim / Não
   - Microcopy: "Só pra te mandar conteúdo e ofertas que façam sentido pra sua família — não pedimos nenhum dado da criança."

5. **Produto de interesse** *(opcional, seleção única)*
   - Label: "O que mais te interessa hoje?"
   - Opções: Protocolo Adulto · Protocolo Kids · Kit Família · Só quero saber mais, por enquanto

**Texto do botão:** Quero meu mimo de aniversário

**Nota de privacidade (LGPD)**, abaixo do botão, fonte pequena:
```
Ao enviar, você concorda em receber comunicações da VermeFree. Usamos seus dados só pra isso — carinho, novidades e ofertas pensadas pra você. Nada de spam, nada de compartilhar com terceiros.
```

**Mensagem de sucesso (pós-envio):**
```
Prontinho! 🎉
Já guardamos sua data. Quando o seu mês chegar, a gente aparece com um mimo especial.
```

---

## 3. NOTAS PARA SARAH/CLINT

**Lista final de campos sugeridos:**
| Campo | Prioridade | Obrigatório? | Formato |
|---|---|---|---|
| Data de aniversário | 1 (essencial) | Sim | DD/MM (sem ano — não precisamos da idade exata, e evita fricção/dado sensível desnecessário) |
| Primeiro nome | Alta | Só se ainda não existir na base (pular campo se já tiver) | Texto livre |
| Cidade/Estado | Baixa | Não | Texto livre ou dropdown de UF |
| Cuida de crianças em casa? | Média | Não | Boolean (Sim/Não) |
| Produto de interesse | Baixa | Não | Seleção única |

**Observações de integração:**
- Manter o formulário em no máximo 5 campos (o essencial é o aniversário — o resto é bônus, não trava conversão).
- Se o CRM já tiver o primeiro nome do contato, pular esse campo automaticamente (pré-preencher ou ocultar) pra reduzir atrito.
- Campo "cuida de crianças em casa?" é só uma tag booleana no cadastro do responsável — **não cria perfil da criança nem coleta nome/data de nascimento de menor**. Usar exclusivamente pra segmentar comunicação Kids pra quem já é mãe/cuidadora.
- O mimo de aniversário **não é liberado no momento do cadastro** — é entregue no mês do aniversário do cliente (a automação de disparo do cupom é separada dessa captura; esse formulário só coleta o dado).
- Sugestão de gatilho: dispara o mimo (cupom pontual) alguns dias antes ou no início do mês de aniversário, puxando a data DD/MM cadastrada aqui.
- Formulário de aniversário funciona bem tanto como link solto (via WhatsApp/e-mail) quanto embutido em fluxo pós-compra — mas este documento cobre só o convite standalone pedido no briefing.

---

## 4. Checklist ANVISA/marca

- [x] Sem claim de cura / sem "elimina/erradica/mata" / sem "em X dias"
- [x] Não cita médico nem influenciador
- [x] Não diagnostica o leitor
- [x] Tom natural/acolhedor
- [x] Linguagem segura de desparasitação (não há claim de produto nesta peça — é captura de dados, mas o tom segue a mesma linha)
- [x] Mimo posicionado como exceção pontual do mês de aniversário, não "sempre tem promoção"
- [x] Nota de privacidade (LGPD) presente, em tom leve
- [x] Formulário curto (até 5 campos), 1 CTA claro
- [x] Fala com mulher/mãe 30–50 que cuida da família
