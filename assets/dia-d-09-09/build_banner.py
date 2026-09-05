# -*- coding: utf-8 -*-
"""
Banner hero — Dia D VermeFree · quarta 09/09
============================================
Gera as 4 pecas obrigatorias (desktop/mobile, com texto e chapa limpa).

REGRA CENTRAL: nenhum frasco, rotulo ou embalagem e gerado por IA.
Os produtos entram como FOTO OFICIAL da Shopify, apenas recortada
(remocao de fundo) e reescalada. O fundo e uma chapa fotografica vazia
(parede creme + bancada de madeira, sem objetos e sem texto). Toda a
tipografia e desenhada com fontes reais (Montserrat), nunca "escrita"
por modelo generativo.

Entradas esperadas na pasta de trabalho:
  cut_adulto.png  cut_kids24.png  cut_oleo.png   -> recortes das fotos oficiais
  plate_d.png     plate_m.png                    -> chapas de fundo vazias
  fonts/m400.ttf  fonts/m600.ttf                 -> Montserrat Regular/SemiBold
  Montserrat-ExtraBold via fontconfig do sistema
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

RED = (196, 43, 43)        # #C42B2B  vermelho da acao
DRED = (126, 26, 26)       # #7E1A1A
CREAM = (253, 248, 243)    # #FDF8F3
INK = (43, 38, 33)
WHITE = (255, 255, 255)
MUTED = (104, 92, 82)

XB = '/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf'
SB = 'fonts/m600.ttf'
RG = 'fonts/m400.ttf'


def F(p, s):
    return ImageFont.truetype(p, s)


def wls(font, s, ls=0):
    """Largura de um texto com letter-spacing."""
    return sum(font.getlength(c) for c in s) + ls * (len(s) - 1)


def dls(d, x, y, s, font, fill, ls=0):
    """Desenha texto com letter-spacing; devolve o x final."""
    for c in s:
        d.text((x, y), c, font=font, fill=fill)
        x += font.getlength(c) + ls
    return x


def fit(path, s, maxw, start, ls=0, minsz=8):
    """Reduz o corpo ate o texto caber na coluna. Impede qualquer estouro."""
    sz = start
    while sz > minsz:
        f = F(path, sz)
        if wls(f, s, ls) <= maxw:
            return f, sz
        sz -= 2
    return F(path, minsz), minsz


def wrap(font, text, maxw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if font.getlength(t) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def horizon_frac(im):
    """Acha a linha parede/madeira pelo maior degrau de luminancia."""
    g = im.convert('L').resize((64, max(40, im.height // 12)))
    h = g.height
    rows = [sum(g.getpixel((x, y)) for x in range(64)) / 64.0 for y in range(h)]
    best = (int(h * 0.75), -1e9)
    for y in range(int(h * 0.45), int(h * 0.93)):
        d = sum(rows[y - 5:y]) / 5.0 - sum(rows[y:y + 5]) / 5.0
        if d > best[1]:
            best = (y, d)
    return best[0] / float(h)


def build_bg(path, W, H, horizon_px, wash=0.30):
    """Reescala parede e madeira separadamente para pousar a linha do
    horizonte exatamente onde a composicao pede."""
    p = Image.open(path).convert('RGB')
    pw, ph = p.size
    hf = horizon_frac(p)
    cut = int(ph * hf)
    wall = p.crop((0, 0, pw, cut)).resize((W, horizon_px), Image.LANCZOS)
    wood = p.crop((0, cut, pw, ph)).resize((W, H - horizon_px), Image.LANCZOS)
    bg = Image.new('RGB', (W, H))
    bg.paste(wall, (0, 0))
    bg.paste(wood, (0, horizon_px))
    return Image.blend(bg, Image.new('RGB', (W, H), CREAM), wash), hf


# ---------------------------------------------------------------- conceito
# Linguagem grafica adaptada da referencia aprovada (Mother Earth Day):
# corte diagonal entre bloco de cor e foto, faixas anguladas paralelas,
# triades de setas, headline empilhada em 3 linhas com a do meio na cor de
# acao, icone inline e botao pill. Paleta trocada para a identidade do
# Dia D: fundo claro/creme, VERMELHO como cor da acao, verde so nos rotulos.

def poly(base, pts, color, alpha, blur=0):
    """Preenche um poligono com cor solida em opacidade controlada."""
    m = Image.new('L', base.size, 0)
    ImageDraw.Draw(m).polygon(pts, fill=int(255 * alpha))
    if blur:
        m = m.filter(ImageFilter.GaussianBlur(blur))
    base.paste(Image.new('RGB', base.size, color), (0, 0), m)


def vbar(base, xt, w, lean, color, alpha, y0=None, y1=None, blur=0):
    """Faixa vertical inclinada — a 'barra diagonal' da referencia.
    xt = x no topo, lean = deslocamento horizontal ate a base."""
    H = base.height
    y0 = 0 if y0 is None else y0
    y1 = H if y1 is None else y1
    f0, f1 = y0 / float(H), y1 / float(H)
    poly(base, [(xt + lean * f0, y0), (xt + w + lean * f0, y0),
                (xt + w + lean * f1, y1), (xt + lean * f1, y1)], color, alpha, blur)


def tris(base, x, y, s, gap, color, alpha, n=3, lean=.30):
    """Triade de setas (>>>) — o acento de ritmo da referencia."""
    m = Image.new('L', base.size, 0)
    d = ImageDraw.Draw(m)
    w = s * .60
    for i in range(n):
        ox = x + i * (w + gap)
        d.polygon([(ox + s * lean, y), (ox + w + s * lean, y + s / 2.),
                   (ox + s * lean, y + s), (ox + s * lean + w * .42, y + s / 2.)],
                  fill=int(255 * alpha))
    base.paste(Image.new('RGB', base.size, color), (0, 0), m)


def leaf_img(h, color, vein):
    """Folha inline ao lado da headline — equivalente ao pinheiro da
    referencia, mas coerente com fitoterapia. Desenhada, nunca gerada."""
    W = max(6, int(h * .60))
    im = Image.new('RGBA', (W, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    n = 44
    pts = [(W / 2. + (W / 2.) * math.sin(math.pi * (i / float(n))) ** .85, (i / float(n)) * h)
           for i in range(n + 1)]
    pts += [(W / 2. - (W / 2.) * math.sin(math.pi * (i / float(n))) ** .85, (i / float(n)) * h)
            for i in range(n, -1, -1)]
    d.polygon(pts, fill=color + (255,))
    d.line((W / 2., h * .06, W / 2., h * .94), fill=vein + (210,), width=max(2, int(h * .045)))
    return im.rotate(-24, expand=True, resample=Image.BICUBIC)


def bottle_only(path):
    """Isola so o frasco central do Oleo de Alho (a foto oficial traz
    alhos e props ao redor). Nada e redesenhado: e recorte puro."""
    im = Image.open(path).convert('RGBA')
    a = im.getchannel('A')
    bb = a.getbbox()
    th = int((bb[3] - bb[1]) * 0.20)
    band = a.crop((bb[0], bb[1], bb[2], bb[1] + th))
    cols = [max(band.getpixel((x, y)) for y in range(band.height)) for x in range(band.width)]
    xs = [x for x, v in enumerate(cols) if v > 120]
    c = im.crop((max(0, bb[0] + min(xs) - 6), bb[1], min(im.width, bb[0] + max(xs) + 6), bb[3]))
    return c.crop(c.getchannel('A').getbbox())


def trimmed(path):
    im = Image.open(path).convert('RGBA')
    return im.crop(im.getchannel('A').getbbox())


def place(base, img, cx, baseline, th, shadow=0.30):
    """Assenta o produto na bancada com sombra de contato."""
    w = int(img.width * th / img.height)
    im = img.resize((w, th), Image.LANCZOS)
    sw, sh = int(w * 0.94), max(10, int(th * 0.13))
    m = Image.new('L', (sw, sh), 0)
    ImageDraw.Draw(m).ellipse((0, 0, sw - 1, sh - 1), fill=int(255 * shadow))
    m = m.filter(ImageFilter.GaussianBlur(sh * 0.34))
    base.paste(Image.new('RGB', (sw, sh), (92, 66, 44)), (int(cx - sw / 2), int(baseline - sh * 0.55)), m)
    base.paste(im, (int(cx - w / 2), int(baseline - th)), im)
    return (int(cx - w / 2), int(baseline - th), int(cx - w / 2) + w, int(baseline))


def pill(base, x, y, txt, fs, padx, pady):
    """Selo de urgencia com relogio desenhado (sem emoji, sem fonte externa)."""
    f = F(XB, fs)
    ls = fs * 0.10
    tw = wls(f, txt, ls)
    ic = int(fs * 1.15)
    h = int(fs * 1.55) + pady * 2
    w = int(tw) + padx * 2 + ic + int(fs * 0.55)
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=RED)
    cyc, cxc, rr = y + h // 2, x + padx + ic // 2, ic // 2
    d.ellipse((cxc - rr, cyc - rr, cxc + rr, cyc + rr), outline=WHITE, width=max(2, int(fs * 0.10)))
    lw = max(2, int(fs * 0.09))
    d.line((cxc, cyc, cxc, cyc - int(rr * 0.55)), fill=WHITE, width=lw)
    d.line((cxc, cyc, cxc + int(rr * 0.42), cyc + int(rr * 0.30)), fill=WHITE, width=lw)
    dls(d, x + padx + ic + int(fs * 0.55), y + pady + int(fs * 0.16), txt, f, WHITE, ls)
    return h, w


def cta(base, x, y, txt, fs, w=None, h=None):
    f = F(XB, fs)
    ls = fs * 0.02
    tw = wls(f, txt, ls)
    ar = int(fs * 0.85)
    if h is None:
        h = int(fs * 2.35)
    if w is None:
        w = int(tw) + int(fs * 3.0) + ar
    sh = Image.new('L', base.size, 0)
    ImageDraw.Draw(sh).rounded_rectangle((x, y + int(h * 0.14), x + w, y + h + int(h * 0.14)), radius=h // 2, fill=95)
    sh = sh.filter(ImageFilter.GaussianBlur(h * 0.17))
    base.paste(Image.new('RGB', base.size, (122, 52, 36)), (0, 0), sh)
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=RED)
    tx, ty = x + int((w - tw - ar - fs * 0.5) / 2), y + int((h - fs * 1.32) / 2)
    ex = dls(d, tx, ty, txt, f, WHITE, ls)
    cy, ax = y + h // 2, ex + int(fs * 0.55)
    lw, s = max(3, int(fs * 0.11)), int(fs * 0.24)
    d.line((ax, cy - s, ax + s, cy), fill=WHITE, width=lw)
    d.line((ax, cy + s, ax + s, cy), fill=WHITE, width=lw)
    return w, h


def badge(base, cx, cy, r):
    """Selo BRINDE (circulo + presente desenhado) sobre o Oleo de Alho."""
    ov = Image.new('RGBA', base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.ellipse((cx - r - int(r * 0.05), cy - r + int(r * 0.06), cx + r + int(r * 0.05), cy + r + int(r * 0.14)), fill=(90, 30, 30, 70))
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=RED + (255,))
    d.ellipse((cx - int(r * 0.86), cy - int(r * 0.86), cx + int(r * 0.86), cy + int(r * 0.86)), outline=(255, 255, 255, 150), width=max(2, int(r * 0.045)))
    gw, gh = int(r * 0.62), int(r * 0.46)
    gx, gy = cx - gw // 2, cy - int(r * 0.46)
    d.rounded_rectangle((gx, gy, gx + gw, gy + gh), radius=int(r * 0.07), fill=WHITE + (255,))
    d.line((cx, gy, cx, gy + gh), fill=RED + (255,), width=max(2, int(r * 0.075)))
    d.line((gx, gy + int(gh * 0.34), gx + gw, gy + int(gh * 0.34)), fill=RED + (255,), width=max(2, int(r * 0.075)))
    d.ellipse((cx - int(r * 0.30), gy - int(r * 0.19), cx - int(r * 0.02), gy + int(r * 0.05)), outline=WHITE + (255,), width=max(2, int(r * 0.07)))
    d.ellipse((cx + int(r * 0.02), gy - int(r * 0.19), cx + int(r * 0.30), gy + int(r * 0.05)), outline=WHITE + (255,), width=max(2, int(r * 0.07)))
    fb, _ = fit(XB, 'BRINDE', int(r * 1.44), int(r * 0.46), ls=int(r * 0.03))
    dls(d, cx - wls(fb, 'BRINDE', int(r * 0.03)) / 2, cy + int(r * 0.13), 'BRINDE', fb, WHITE, int(r * 0.03))
    base.paste(ov, (0, 0), ov)


def scrim_lr(base, x_full, x_end, alpha=0.88):
    """Veu creme da esquerda para a direita: garante contraste do texto
    sem apagar a foto do lado dos produtos."""
    W, H = base.size
    m = Image.new('L', (W, 1), 0)
    px = m.load()
    for x in range(W):
        v = alpha if x <= x_full else (0.0 if x >= x_end else alpha * (1 - (x - x_full) / float(x_end - x_full)) ** 1.7)
        px[x, 0] = int(255 * v)
    base.paste(Image.new('RGB', (W, H), CREAM), (0, 0), m.resize((W, H)))


def scrim_stops(base, stops):
    """Veu creme vertical por faixas [(y, alpha), ...] com interpolacao linear."""
    W, H = base.size
    m = Image.new('L', (1, H), 0)
    px = m.load()
    for y in range(H):
        a = stops[-1][1]
        for i in range(len(stops) - 1):
            y0, a0 = stops[i]
            y1, a1 = stops[i + 1]
            if y0 <= y <= y1:
                a = a0 + (a1 - a0) * ((y - y0) / float(max(1, y1 - y0)))
                break
        px[0, y] = int(255 * max(0.0, min(1.0, a)))
    base.paste(Image.new('RGB', (W, H), CREAM), (0, 0), m.resize((W, H)))


ADU = trimmed('cut_adulto.png')   # Protocolo Adulto — 4 frascos
KID = trimmed('cut_kids24.png')   # VermeFree Kids 2 a 4
OLE = bottle_only('cut_oleo.png')  # Oleo de Alho — o brinde

# --- Copy aprovada. Checklist ANVISA: sem cura/elimina/erradica/milagre,
#     sem medico, sem diagnostico, sem comparacao com farmacia, sem cupom. ---
H1, H2, H3 = 'DIA D', '10% OFF', 'SÓ HOJE'     # headline empilhada em 3 linhas
SUB = 'JÁ NO PREÇO, SEM CUPOM'                  # o diferencial, no lugar do subtitulo
BODY = 'Frete grátis sem valor mínimo e 1 Óleo de Alho de brinde no seu pedido.'
MICRO = '+ Manual da Desparasitação em PDF por e-mail.'
PT = 'QUARTA 09/09 · 24 HORAS'
CT = 'APROVEITAR O DIA D'


def desktop(txt=True):
    """2400x1000 — bloco creme a esquerda com corte diagonal, produtos a direita."""
    W, H, HZ = 2400, 1000, 772
    XT, XB_ = 1180, 1420          # x do corte no topo e na base
    LEAN = XB_ - XT
    bg = build_bg('plate_d.png', W, H, HZ).convert('RGB')

    # faixas anguladas sobre a foto (sob os produtos, para nao lavar o rotulo)
    vbar(bg, XT + 120, 300, LEAN, RED, .13)
    vbar(bg, XT + 470, 150, LEAN, CREAM, .30)
    vbar(bg, XT + 690, 54, LEAN, CREAM, .22)
    vbar(bg, XT + 880, 210, LEAN, CREAM, .16)
    vbar(bg, XT + 1090, 40, LEAN, RED, .20)

    # bloco de cor com aresta diagonal + filete vermelho (assinatura do conceito)
    poly(bg, [(0, 0), (XT, 0), (XB_, H), (0, H)], CREAM, .94)
    vbar(bg, XT, 14, LEAN, RED, 1.0)
    vbar(bg, XT + 42, 7, LEAN, RED, .55)
    vbar(bg, XT + 68, 4, LEAN, CREAM, .85)

    ah = int(H * .300)
    place(bg, ADU, 1660, 820, ah)
    place(bg, KID, 1880, 820, int(ah * .63))
    place(bg, OLE, 1448, 854, int(ah * .84))
    tris(bg, 1540, 168, 44, 17, CREAM, .85)
    tris(bg, 2118, 742, 40, 15, CREAM, .75)
    if not txt:
        return bg

    X, COL = 400, 760             # coluna dentro da area segura, a esquerda do corte
    ph, _ = pill(bg, X, 118, PT, 26, 28, 14)
    d = ImageDraw.Draw(bg)
    y = 118 + ph + 36
    f1, s1 = fit(XB, H1, COL, 80, ls=1)
    dls(d, X, y, H1, f1, INK, 1)
    y += int(s1 * 1.02)
    f2, s2 = fit(XB, H2, COL, 172, ls=-3)      # a linha de acao, em vermelho
    dls(d, X, y, H2, f2, RED, -3)
    y += int(s2 * 1.00)
    f3, s3 = fit(XB, H3, COL - 110, 80, ls=1)
    ex = dls(d, X, y, H3, f3, INK, 1)
    lf = leaf_img(int(s3 * .86), RED, CREAM)
    bg.paste(lf, (int(ex + s3 * .26), int(y + s3 * .10)), lf)
    y += int(s3 * 1.24)
    tris(bg, X, y, 26, 10, RED, .95)
    y += 40
    fsu, _ = fit(XB, SUB, COL, 28, ls=5)
    dls(d, X, y, SUB, fsu, RED, 5)
    y += 48
    fb = F(SB, 28)
    for ln in wrap(fb, BODY, COL):
        d.text((X, y), ln, font=fb, fill=INK)
        y += 40
    fm = F(RG, 24)
    for ln in wrap(fm, MICRO, COL):
        d.text((X, y), ln, font=fm, fill=MUTED)
        y += 33
    cta(bg, X, y + 22, CT, 30)
    badge(bg, 1420, 640, 58)
    return bg


def mobile(txt=True):
    """1080x1350 — composicao redesenhada: bloco creme no topo com aresta
    diagonal, produtos no meio sobre a bancada, bloco inferior para apoio+CTA."""
    W, H, HZ = 1080, 1350, 846
    bg = build_bg('plate_m.png', W, H, HZ).convert('RGB')
    vbar(bg, -40, 150, 260, CREAM, .26, 600, 1120)
    vbar(bg, 240, 60, 260, RED, .16, 600, 1120)
    vbar(bg, 700, 190, 260, CREAM, .22, 600, 1120)
    vbar(bg, 980, 44, 260, CREAM, .30, 600, 1120)

    poly(bg, [(0, 0), (W, 0), (W, 648), (0, 742)], CREAM, .94)
    poly(bg, [(0, 742), (W, 648), (W, 662), (0, 756)], RED, 1.0)
    poly(bg, [(0, 776), (W, 682), (W, 689), (0, 783)], RED, .55)
    poly(bg, [(0, 1068), (W, 1016), (W, H), (0, H)], CREAM, .93)
    poly(bg, [(0, 1068), (W, 1016), (W, 1028), (0, 1080)], RED, 1.0)

    ah = int(H * .245)
    place(bg, ADU, 536, 1010, ah)
    place(bg, KID, 858, 1010, int(ah * .60))
    place(bg, OLE, 206, 1032, int(ah * .79))
    tris(bg, 742, 792, 38, 14, CREAM, .85)
    if not txt:
        return bg

    COL = 940
    fp = F(XB, 25)
    pe = wls(fp, PT, 2.75) + int(25 * 1.12) + int(25 * .52) + 56
    ph, _ = pill(bg, int((W - pe) / 2), 70, PT, 25, 28, 13)
    d = ImageDraw.Draw(bg)
    y = 70 + ph + 34
    f1, s1 = fit(XB, H1, COL, 72, ls=1)
    dls(d, (W - wls(f1, H1, 1)) / 2, y, H1, f1, INK, 1)
    y += int(s1 * 1.02)
    f2, s2 = fit(XB, H2, COL, 178, ls=-3)
    dls(d, (W - wls(f2, H2, -3)) / 2, y, H2, f2, RED, -3)
    y += int(s2 * 1.00)
    f3, s3 = fit(XB, H3, COL - 120, 72, ls=1)
    lf = leaf_img(int(s3 * .86), RED, CREAM)
    sx = (W - (wls(f3, H3, 1) + s3 * .26 + lf.width)) / 2.
    ex = dls(d, sx, y, H3, f3, INK, 1)
    bg.paste(lf, (int(ex + s3 * .26), int(y + s3 * .10)), lf)
    y += int(s3 * 1.34)
    fsu, _ = fit(XB, SUB, COL, 26, ls=5)
    dls(d, (W - wls(fsu, SUB, 5)) / 2, y, SUB, fsu, RED, 5)
    badge(bg, 176, 786, 55)

    y = 1088
    fb = F(SB, 28)
    for ln in wrap(fb, BODY, 880):
        d.text(((W - fb.getlength(ln)) / 2, y), ln, font=fb, fill=INK)
        y += 40
    f = F(XB, 31)
    cw = int(wls(f, CT, 31 * .07)) + int(31 * 2.9) + int(31 * .80)
    cta(bg, int((W - cw) / 2), y + 18, CT, 31)
    return bg


def save(img, name, target_kb):
    """WebP de producao dentro do orcamento de peso + PNG de backup."""
    img.save(name + '.png', optimize=True)
    q = 92
    while q >= 40:
        img.save(name + '.webp', 'WEBP', quality=q, method=6)
        if os.path.getsize(name + '.webp') / 1024.0 <= target_kb:
            break
        q -= 4
    print(name, 'PNG %.0fKB' % (os.path.getsize(name + '.png') / 1024.0),
          'WEBP q%d %.1fKB' % (q, os.path.getsize(name + '.webp') / 1024.0))


if __name__ == '__main__':
    save(desktop(True), 'vermefree-diad-0909-desktop-2400x1000', 300)
    save(mobile(True), 'vermefree-diad-0909-mobile-1080x1350', 150)
    save(desktop(False), 'vermefree-diad-0909-desktop-chapa-limpa-2400x1000', 300)
    save(mobile(False), 'vermefree-diad-0909-mobile-chapa-limpa-1080x1350', 150)
