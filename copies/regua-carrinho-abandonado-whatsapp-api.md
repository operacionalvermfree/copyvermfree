# Régua de Carrinho Abandonado — WhatsApp API (Meta Business) · VermeFree

> 4 templates HSM, tom de atendimento humano do início ao fim (equipe respondendo, não robô disparando). Só o Toque 4 tem cupom. O Toque 2 é desenhado pra puxar resposta do cliente — texto aberto + botões de resposta rápida, já que tocar num botão também conta como mensagem do cliente e abre a janela de 24h de conversa livre.
>
> Formato pensado pra submissão de aprovação Meta: nome sugerido, categoria, cabeçalho (se houver), corpo com variável `{{1}}` (nome), rodapé e botões. `{{1}}` nunca abre nem fecha a mensagem, como exige a Meta.

---

## TOQUE 1 — 30min após abandono
**Ângulo:** lembrete curto, tom de quem está checando de verdade (não robô).

```
Nome sugerido do template: vermefree_carrinho_toque1_lembrete
Categoria: MARKETING

CORPO:
Oi {{1}}! Aqui é da equipe VermeFree 🌿
Vi que você começou um pedido com a gente e não chegou a finalizar. Ficou alguma dúvida?
Seu carrinho continua salvo, do jeitinho que você deixou.

BOTÃO (CTA URL): Voltar pro meu carrinho → [LINK CARRINHO]
```

---

## TOQUE 2 — 6h após abandono
**Ângulo:** abrir espaço pra dúvida — pergunta aberta, pensada pra gerar resposta e abrir a janela de 24h.

```
Nome sugerido do template: vermefree_carrinho_toque2_duvida
Categoria: MARKETING

CORPO:
Oi {{1}}, tudo bem?
Fiquei pensando aqui se ficou alguma dúvida sobre o protocolo — dose, forma de uso, o que esperar nos primeiros dias. Pode me perguntar, é rapidinho :)

BOTÕES (Resposta rápida):
- Tenho uma dúvida
- Só estou olhando ainda
```

> Nota pra Sarah: os dois botões de resposta rápida servem exatamente pra isso — mesmo quem não digita nada, ao tocar em qualquer um dos dois, já conta como mensagem do cliente e abre a janela de 24h pra conversa livre. Vale configurar as duas respostas automáticas de continuidade (uma puxando a dúvida específica, outra reforçando benefício sem pressionar).

---

## TOQUE 3 — 24h após abandono
**Ângulo:** prova + reforço — composição do kit, quem já usou.

```
Nome sugerido do template: vermefree_carrinho_toque3_reforco
Categoria: MARKETING
Cabeçalho: [IMAGEM DO KIT — se disponível; ver nota abaixo]

CORPO:
Oi {{1}}! Passando aqui pra reforçar.
O protocolo que você separou é feito à base de plantas selecionadas, pensado pra apoiar a rotina de limpeza intestinal de forma natural — e já faz parte da rotina de muita gente que busca isso sem recorrer à química pesada.
Se quiser, te conto mais sobre como funciona.

BOTÃO (Resposta rápida): Quero saber mais
```

> Nota pra Sarah: se tivermos foto oficial do kit em boa qualidade, esse é o toque certo pra usar cabeçalho de imagem no template (a Meta permite `HEADER: IMAGE` em templates aprovados). Se não tiver imagem pronta, sobe só com texto — o corpo já funciona sem ela.

---

## TOQUE 4 — 48h após abandono (último toque)
**Ângulo:** fechamento com cupom/desconto — único toque com oferta.

```
Nome sugerido do template: vermefree_carrinho_toque4_cupom
Categoria: MARKETING

CORPO:
Oi {{1}}! Esse é nosso último lembrete sobre o seu carrinho aqui na VermeFree 🌿
Pra te ajudar a fechar, separei um cupom: [CUPOM CARRINHO], com [%]% de desconto — válido só pelas próximas horas.

RODAPÉ (opcional): Responda SAIR se não quiser mais receber esses avisos.

BOTÃO (CTA URL): Usar cupom e finalizar pedido → [LINK CARRINHO]
```

---

## Pendências para finalizar

1. **[CUPOM CARRINHO] e [%]** (Toque 4) — cupom de carrinho abandonado da VermeFree ainda sem percentual definido (aguardando confirmação do Gabriel, tarefa 86ajr1dmr). Preencher antes de submeter o template pra aprovação — a Meta não permite editar o corpo de um template já aprovado sem submeter de novo.
2. **[LINK CARRINHO]** (Toques 1 e 4) — confirmar se é possível gerar link de checkout direto (carrinho já preenchido) ou se será link genérico da loja.
3. **Imagem do kit** (Toque 3) — sinalizar se há foto oficial disponível em boa qualidade pra usar como cabeçalho de mídia; se não houver, o template sobe só com texto.
4. **Categoria Meta** — classifiquei os 4 como MARKETING (nenhum é sobre pedido já confirmado, então não se qualificam como UTILITY). Vale confirmar com quem for submeter, já que a Meta pode reclassificar na revisão — e envio muito frequente de MARKETING pro mesmo número pode afetar a qualidade/limite de envio da conta.
