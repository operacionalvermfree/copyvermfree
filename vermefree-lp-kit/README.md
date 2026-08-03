# vermefree-lp-kit/

Base de conhecimento técnica para construir landing pages (LPs) da VermeFree — pasta irmã da `CLAUDE.md` (que cobre marca/copy) e focada no lado **engenharia/design das LPs**.

> Este kit é a **técnica destilada**. A matéria-prima bruta (zips de referência, prints, vídeos, assets de produto em alta) mora no Google Drive — ver `FONTES.md`.

## O que tem aqui

| Arquivo | Pra quê serve |
|---|---|
| `COMANDO-CRIAR-LP.md` | **Comando pronto pra colar num chat novo** e começar uma LP (equivalente ao fluxo já usado na Botanika). |
| `COMO-USAR.md` | Fluxo de trabalho pra criar uma LP nova: o que ler antes, onde subir asset pesado vs. leve, passo a passo. |
| `FONTES.md` | Onde está cada fonte de verdade: loja/checkout, variant IDs reais, pastas do Drive (com IDs/links). |
| `REPERTORIO-TECNICO.md` | Catálogo destilado de ~35 referências reais de técnica/animação de LP (getlayers.com + meez.design), já lidas e resumidas com recomendação de aplicação ao tom da marca. |
| `prompts/00-INDEX.md` | Índice de prompts reutilizáveis pra gerar blocos de LP (hero, prova social, FAQ, oferta, etc.). |
| `zips/README.md` | Regra de upload de zip pequeno/essencial direto no repo. |

## Como isso se encaixa

- `CLAUDE.md` (raiz) → manda ler este kit + `PAGINAS.md` + `vermefree-lp-superprompt.md` antes de qualquer LP.
- `vermefree-lp-superprompt.md` (raiz) → design system e regras técnicas fixas (grid, animação, convenções de pasta, validação).
- `PAGINAS.md` (raiz) → mapa vivo de quais LPs existem, status e link publicado.
- `vermefree-lp-kit/` (aqui) → como trabalhar e onde buscar matéria-prima.

## Convenções fixas (não mudam por LP)

- Uma pasta por produto: `landing-<slug>/index.html` — HTML autocontido, sem build/bundler.
- Tem que funcionar no Safari mobile ao vivo: sempre `html { overflow-x: hidden }`.
- Cada produto tem identidade visual própria — nunca clonar/copiar código 1:1 de outra LP.
- Validar antes de publicar: `node --check` no JS inline + conferir balanço de tags HTML.
- Nunca colocar identificador de modelo de IA em commit, PR ou código.
- Checkout sempre via link direto de carrinho: `https://vermefree.com.br/cart/<VARIANT_ID>:<QTD>` (ver IDs reais em `FONTES.md`).
