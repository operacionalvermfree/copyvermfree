# Campanha de Depoimentos/UGC — "Conta pra gente" · VermeFree

> Objetivo: incentivar clientes a enviarem depoimento em vídeo (1–1,5 min) ou texto sobre a experiência com a VermeFree. Primeiras 30 participantes ganham um benefício em troca. Todo conteúdo recebido será usado depois em conteúdo/prova social/anúncios, sempre com autorização de uso de imagem.

## O que preencher
- `{{DATA_INICIO}}` — data de início da campanha (pendente com o Gabriel).
- `{{BRINDE}}` — benefício das 30 primeiras: kit / desconto / condição especial (pendente com o Gabriel).
- `{{1}}` — primeiro nome (WhatsApp API).
- `[LINK]` — link do formulário de participação.

---

## 1. MENSAGEM-CONVITE

### Versão WhatsApp API

```
Nome sugerido do template: vermefree_ugc_convite
Categoria: MARKETING

BODY:
Oi {{1}}! Você toparia contar como foi sua experiência com a VermeFree? 🎥
Procuro as 30 primeiras pra participar — em troca, {{BRINDE}}.

FOOTER (opcional): Vagas abrem em {{DATA_INICIO}}

BOTÃO (CTA URL): Quero participar → [LINK]
```

### Versão E-mail

**Assunto:** Quero ouvir sua experiência com a VermeFree
**Assunto (variação A/B):** Você topa contar sua rotina pra gente? (30 vagas)

**Pré-header:** As 30 primeiras ganham {{BRINDE}}.

**Corpo:**
```
Olá,

Queremos ouvir de verdade como tem sido sua rotina com a VermeFree — o que mudou, o que você sentiu, como foi pra você.

Estamos procurando as 30 primeiras pessoas que topem gravar um vídeo curto (1 a 1,5 min) ou escrever um depoimento em texto contando essa experiência.

Em troca, quem participar ganha {{BRINDE}}.

As vagas abrem em {{DATA_INICIO}} — é por ordem de chegada.

Um abraço,
Equipe VermeFree
```

**CTA (botão único):** Quero contar minha experiência

---

## 2. COPY DA PÁGINA DA CAMPANHA

**Headline:** Conta pra gente como foi sua experiência

**Subhead:** Buscamos as 30 primeiras pessoas que topem compartilhar sua rotina com a VermeFree — em vídeo curto ou em texto. Em troca, você ganha {{BRINDE}}.

**Como participar (3 passos):**
1. Grave um vídeo de 1 a 1,5 min (ou escreva um texto curto) contando sua experiência — use o roteiro-guia como apoio, não precisa decorar nada.
2. Envie pelo formulário desta página, junto com a autorização de uso de imagem/conteúdo.
3. Pronto! Se você for uma das 30 primeiras, garante {{BRINDE}}.

**O que você ganha:** {{BRINDE}}

**Vagas e prazo:** 30 vagas, por ordem de chegada. Abertura em {{DATA_INICIO}}.

**FAQ curta:**
- **Preciso aparecer no vídeo?** Não é obrigatório — pode ser só sua voz, ou você pode enviar em texto.
- **Meu depoimento vai aparecer onde?** Pode ser usado em conteúdo da marca, redes sociais e anúncios, sempre com a sua autorização.
- **Posso enviar depois das 30 vagas?** Pode, mas o benefício ({{BRINDE}}) vale só pras 30 primeiras.
- **Preciso falar de algum resultado específico?** Não — fale da sua experiência real com a rotina, com suas palavras e no seu tempo.

---

## 3. ROTEIRO-GUIA PRO DEPOIMENTO (1–1,5 min)

**Estrutura sugerida (não precisa decorar, é só um apoio):**

1. **Como era antes** — como era sua rotina ou o que te fez buscar uma desparasitação natural.
2. **O que mudou** — como foi usar o protocolo, o que passou a fazer na rotina.
3. **Como você se sente hoje** — leveza, constância, bem-estar.

**Orientações importantes pra participante (incluir na página/formulário):**
- Fale com suas próprias palavras, com naturalidade — não precisa de um roteiro decorado.
- Fale de **bem-estar, leveza, rotina e constância**.
- **Não fale** de "cura", "eliminar/matar vermes", "resultado garantido" ou "em X dias" — a VermeFree é uma rotina natural, não uma promessa desse tipo.
- **Não cite** nenhum médico, profissional de saúde ou influenciador como aval do protocolo.
- Resultados podem variar de pessoa pra pessoa — fica à vontade pra mencionar isso, se fizer sentido pra você.

---

## 4. AUTORIZAÇÃO DE USO DE IMAGEM/CONTEÚDO (LGPD)

Microcopy pra exibir no formulário, com checkbox de aceite obrigatório antes do envio:

```
Ao enviar seu depoimento (vídeo, áudio, foto ou texto), você autoriza a VermeFree a usar esse conteúdo — sua imagem e/ou voz e/ou texto — em conteúdos da marca, redes sociais e anúncios, sem custo adicional. Se um dia você quiser que a gente retire seu conteúdo do ar, é só chamar a gente — resolvemos rapidinho.
```

---

## 5. NOTAS PARA SARAH

- Confirmar com o Gabriel os valores de `{{BRINDE}}` e `{{DATA_INICIO}}` antes de publicar qualquer peça.
- O formulário de envio precisa ter: campo de upload (vídeo) OU campo de texto longo (pra quem preferir escrever), e o checkbox de autorização de uso de imagem como obrigatório antes de permitir o envio.
- Recomendado revisar cada depoimento recebido antes de publicar/usar em anúncio — mesmo com o roteiro-guia, a participante fala livre, então vale conferir se nenhum claim proibido (cura, eliminação, garantia, "em X dias", menção a médico) passou antes de ir pro ar.
- Contagem das 30 vagas precisa ficar visível/atualizada (mesmo que manual) pra não gerar frustração em quem chegar depois do limite.
- Depoimento em texto pode entrar pelo mesmo formulário do vídeo — só trocar o tipo de campo, sem precisar de página separada.

## 6. CHECKLIST ANVISA

- [x] Sem claim de cura / sem "elimina/erradica/mata" / sem "em X dias"
- [x] Roteiro do depoimento orienta a participante a NÃO fazer claim proibido
- [x] Não cita médico nem influenciador
- [x] Não diagnostica
- [x] Tom natural/acolhedor
- [x] Linguagem segura de desparasitação
- [x] Autorização de imagem (LGPD) presente
- [x] Benefício como exceção/convite especial (30 primeiras, não "sempre tem")
- [x] 1 CTA claro por peça
- [x] Fala com mulher/mãe 30–50
