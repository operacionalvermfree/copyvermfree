# COMANDO-CRIAR-LP — colar em um chat novo

Equivalente ao fluxo que já existe pra Botanika (`botanika-lp-kit/COMANDO-CRIAR-LP.md`). Copiar o bloco abaixo, trocar só a URL/produto, colar num **chat novo** com acesso ao repo `operacionalvermfree/copyvermfree`.

```
Leia vermefree-lp-kit/COMO-USAR.md neste repo e siga-o à risca (ele manda ler antes, nesta ordem: CLAUDE.md, PAGINAS.md, vermefree-lp-superprompt.md, vermefree-lp-kit/FONTES.md e REPERTORIO-TECNICO.md). Use como régua git show origin/lp:linktree-vermefree/index.html [+ qualquer landing-<slug>/index.html já publicada — conferir PAGINAS.md]. Vou criar a LP do [nome do produto / URL na loja]. Responda só com (a) pasta, (b) identidade proposta e (c) referências — e aguarde meu ok.
```

## Por que esse formato (a/b/c + aguardar ok)

- **(a) pasta** — slug/pasta (`landing-<slug>/`) decidido e conferido contra `PAGINAS.md` *antes* de qualquer linha de HTML, pra nunca duplicar uma LP que já existe ou já foi tentada.
- **(b) identidade proposta** — resumo curto da assinatura visual/interativa específica desse produto. Regra dura do kit: nunca clonar 1:1 o código de outra LP já publicada — ver `REPERTORIO-TECNICO.md` seção 6 pra repertório de técnica por tom de marca.
- **(c) referências** — de onde vem cada dado real: preço e variant ID (Shopify/`FONTES.md`), composição e posologia (`CLAUDE.md` seção 5), claims permitidos (`CLAUDE.md` seção 4). Nunca inventar nenhum desses quatro.
- **Aguardar "ok" antes de gerar HTML** — pasta duplicada ou identidade errada custam uma resposta curta de correção nesse ponto; descobrir isso só depois da LP inteira pronta custa a LP inteira.

## Diferença em relação ao comando da Botanika

A Botanika já tem 8 LPs publicadas na branch `lp` pra usar como régua cruzada entre produtos. A VermeFree ainda não tem nenhuma `landing-<slug>/` publicada — a única peça já elevada com a técnica validada (Ken Burns, parallax de mouse, botão magnético, sheen, reveal-on-load, glass panel) é `linktree-vermefree/index.html`. Use-a como régua até a primeira LP de produto de verdade ser publicada.

**Toda vez que uma `landing-<slug>/` nova for publicada**, adicionar o `git show origin/lp:landing-<slug>/index.html` correspondente na lista de régua deste comando — a régua cresce junto com o catálogo, igual já acontece do lado Botanika.
