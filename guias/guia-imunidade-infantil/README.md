# Guia da Imunidade Infantil — VermeFree kids

PDF-bônus entregue por e-mail pós-compra, junto com o **Manual da Desparasitação**.
Objetivo: acolher a mãe, educar sobre imunidade infantil e reforçar a rotina de
desparasitação natural — **sem vender e sem prometer resultado**.

## Arquivos
- `guia-imunidade-infantil.pdf` — arquivo final (A4 vertical, 9 páginas). É o que vai anexado no e-mail.
- `guia-imunidade-infantil.html` — fonte editável do layout. Para alterar o texto ou o design, edite este arquivo e regenere o PDF.

## Como regenerar o PDF
Renderizado via Chromium headless (mantém cores de fundo e quebra de página A4):

```bash
CHROME=$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome | head -1)
"$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=guia-imunidade-infantil.pdf guia-imunidade-infantil.html
```

## Estrutura (9 páginas)
1. **Capa** — "Guia da Imunidade Infantil", VermeFree kids, subtítulo acolhedor, selos.
2. **Abertura** — carta de mãe pra mãe.
3. **Por que a imunidade infantil pede atenção** — rotina, creche/escola, pets, ambiente (sem alarmismo).
4. **Como a desparasitação natural apoia o bem-estar** — lógica de rotina (2 a 4x/ano), linguagem segura.
5. **6 hábitos que fortalecem a imunidade** — sono, alimentação, hidratação, higiene, ar livre, constância.
6. **Como funciona o Protocolo Kids** — educativo: líquido, dose conforme a idade, início na lua nova, modo de uso geral.
7. **Sinais de bem-estar pra observar** — leveza, sono, apetite, disposição (enquadrado como bem-estar, nunca diagnóstico).
8. **Perguntas frequentes das mães** — 7 dúvidas reais.
9. **Encerramento** — reforço da rotina + convite suave à constância + 1 CTA leve.

## Identidade visual
Verde folha + verde escuro (primário), fundos off-white/bege, verde-limão de acento.
Estética "clean clínico natural / fitoterapia". Selos "Vegetal 100%" e "Metais Free".
Ilustração infantil suave na capa. Legível no celular.

## ✅ Checklist ANVISA (rodado no material)
- [x] Não promete cura / não usa "elimina/erradica/mata parasitas" / "em X dias"
- [x] Não cita Dr. William nem nenhum médico/influenciador como aval
- [x] Não diagnostica o leitor nem a criança ("seu filho tem verme")
- [x] Tom natural/acolhedor, não alarmista nem milagreiro
- [x] Usa linguagem segura ("auxilia na desparasitação", "rotina de limpeza natural", "contribui para o bem-estar")
- [x] Não compara com remédio/vermífugo de farmácia; não promete emagrecimento
- [x] Foco em rotina, constância, prevenção natural e sinais de bem-estar
- [x] 1 CTA claro e leve (encerramento)
- [x] Fala com o público real (mãe 30–50 que cuida da família)

> A única ocorrência de "trata doença" no material é a frase de **isenção** ("não diagnostica, **não trata doença** e não substitui..."), que é uma negação protetiva — compatível com a regra.
