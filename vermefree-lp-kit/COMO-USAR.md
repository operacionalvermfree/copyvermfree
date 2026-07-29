# Como usar o LP-KIT

## Antes de escrever qualquer linha de HTML

1. Leia, nesta ordem:
   - `CLAUDE.md` (raiz) — marca, tom de voz, regras de claim ANVISA, produtos, preços.
   - `PAGINAS.md` (raiz) — pra ver se essa LP já existe, em que status, e evitar duplicar slug.
   - `vermefree-lp-superprompt.md` (raiz) — design system e regras técnicas fixas.
   - `FONTES.md` (aqui) — checkout, variant IDs reais, pastas do Drive com referência/assets.
2. Confirme o produto e o slug da pasta (`landing-<slug>/`) antes de gerar qualquer arquivo.
3. Puxe a verdade do produto direto da loja/Drive — nunca invente preço, variant ID, composição ou dosagem.

## Regra de upload: o que vai pro GitHub vs. o que vai pro Drive

- **Direto no repo (GitHub), só o essencial e leve:**
  - O `index.html` final de cada LP.
  - Imagens/ícones realmente usados na LP, já otimizados.
  - Zips pequenos e essenciais (< 25MB) — ver `zips/README.md`.
- **Nunca commitar no repo:**
  - Assets brutos em alta resolução, vídeos, PSDs, zips grandes de referência.
  - Esse material bruto fica no **Google Drive** (`VermeFree/LP-KIT/`, ver `FONTES.md`) ou em **GitHub Release** (assets versionados grandes que precisam ficar linkáveis).
- Regra prática: se o arquivo sozinho já beira ou passa de 25MB, ele NÃO vai no commit. Sobe pro Drive (matéria-prima) ou vira Release asset, e o kit só guarda o link/ID.

## Fluxo de uma LP (do zero à publicação)

1. **Ler kit + assets** — este arquivo, `FONTES.md`, e a pasta do produto em `03_assets-produtos/<produto>/` no Drive.
2. **Confirmar pasta e identidade própria** — decidir `landing-<slug>/`, e decidir a assinatura visual/interativa única desse produto (nunca reaproveitar 1:1 o código de outra LP já publicada — ver repertório de técnica no `vermefree-lp-superprompt.md`).
3. **Puxar verdade do produto** — preço, variant ID, composição, posologia, claims permitidos: loja (Shopify) + `CLAUDE.md` + Drive.
4. **Construir o HTML autocontido** — sem build, sem dependência externa que quebre offline/Safari mobile.
5. **Validar** — `node --check` no JS inline da página + checagem de balanceamento de tags HTML antes de considerar pronto.
6. **Publicar** — commit em `landing-<slug>/index.html` na branch de publicação (ver `vermefree-lp-superprompt.md` para o nome da branch e o padrão de link raw.githack).
7. **Atualizar `PAGINAS.md`** — registrar slug, produto, status e link publicado.

## O que NÃO fazer

- Não clonar o HTML/CSS/JS de uma LP existente pra economizar tempo — cada produto precisa de identidade própria (ver repertório de técnica no superprompt, é inspiração, não template).
- Não subir asset bruto/pesado no repo "só pra não esquecer" — vai pro Drive.
- Não inventar variant ID, preço ou composição — sempre conferir em `FONTES.md` / loja / `CLAUDE.md`.
- Não usar claim proibido pela ANVISA (checklist completo no `CLAUDE.md`, seção 4 e 11).
