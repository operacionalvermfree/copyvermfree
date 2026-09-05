# -*- coding: utf-8 -*-
"""
Banner hero — Dia D VermeFree · quarta 09/09
============================================
Gera as 4 pecas obrigatorias (desktop/mobile, com texto e chapa limpa).

CONCEITO — adaptado da referencia aprovada (banners "Mother Earth Day"):
corte diagonal entre bloco de cor e bloco fotografico, faixas anguladas
paralelas, triades de setas, headline empilhada em 3 linhas com a do meio
na cor de acao, icone inline e botao pill. Paleta trocada para a do Dia D:
bloco creme, VERMELHO como cor da acao, verde so nos rotulos dos produtos.

REGRA CENTRAL: a foto do produto entra INTEIRA como bloco, apenas
reenquadrada e com grade leve de cor. Nao ha recorte de produto, nao ha
frasco flutuando e nao ha rotulo redesenhado ou gerado por IA. Toda a
tipografia e todos os elementos graficos sao desenhados por codigo com
fontes reais (Montserrat).

Entradas esperadas na pasta de trabalho:
  hero.jpg                        -> foto oficial do produto (bloco)
  fonts/m400.ttf  fonts/m600.ttf  -> Montserrat Regular/SemiBold
  Montserrat-ExtraBold via fontconfig do sistema
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

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



def cover(img, W, H, fy=.5):
    """Preenche WxH com a foto sem distorcer (crop central; fy move o corte)."""
    s = max(W / float(img.width), H / float(img.height))
    r = img.resize((int(img.width * s + 1), int(img.height * s + 1)), Image.LANCZOS)
    x = (r.width - W) // 2
    y = int((r.height - H) * fy)
    return r.crop((x, y, x + W, y + H))


def grade(im):
    """Grade leve para a foto casar com a paleta creme da peca."""
    im = ImageEnhance.Color(im).enhance(1.06)
    im = ImageEnhance.Contrast(im).enhance(1.05)
    return Image.blend(im, Image.new('RGB', im.size, (255, 246, 235)), 0.07)


def maskpoly(size, pts):
    m = Image.new('L', size, 0)
    ImageDraw.Draw(m).polygon(pts, fill=255)
    return m


def photo_block(base, path, pts, box, fy=.5):
    """Cola a foto DENTRO do poligono do bloco. A foto entra inteira,
    so reenquadrada — nada de recorte de produto, nada de rotulo redesenhado."""
    x, y, w, h = box
    ph = grade(cover(Image.open(path).convert('RGB'), w, h, fy))
    lay = Image.new('RGB', base.size, CREAM)
    lay.paste(ph, (x, y))
    m = maskpoly(base.size, pts)
    base.paste(lay, (0, 0), m)
    return m


def gift(d, cx, cy, r, fg, bg):
    gw, gh = int(r * 1.15), int(r * .86)
    gx, gy = cx - gw // 2, cy - int(r * .30)
    d.rounded_rectangle((gx, gy, gx + gw, gy + gh), radius=int(r * .12), fill=fg)
    d.line((cx, gy, cx, gy + gh), fill=bg, width=max(2, int(r * .14)))
    d.line((gx, gy + int(gh * .34), gx + gw, gy + int(gh * .34)), fill=bg, width=max(2, int(r * .14)))
    d.ellipse((cx - int(r * .56), gy - int(r * .36), cx - int(r * .04), gy + int(r * .10)), outline=fg, width=max(2, int(r * .13)))
    d.ellipse((cx + int(r * .04), gy - int(r * .36), cx + int(r * .56), gy + int(r * .10)), outline=fg, width=max(2, int(r * .13)))


TAG1, TAG2 = 'BRINDE', '1 Óleo de Alho no seu pedido'


def tag_w(fs):
    f1, f2 = F(XB, fs), F(SB, int(fs * .62))
    tw = max(wls(f1, TAG1, fs * .06), f2.getlength(TAG2))
    return int(int(fs * .85) * 2 + int(fs * 1.5) + fs * .7 + tw)


def tag(base, x, y, fs):
    """Etiqueta do brinde, colada sobre o bloco fotografico."""
    f1, f2 = F(XB, fs), F(SB, int(fs * .62))
    tw = max(wls(f1, TAG1, fs * .06), f2.getlength(TAG2))
    ic, pad = int(fs * 1.5), int(fs * .85)
    w, h = int(pad * 2 + ic + fs * .7 + tw), int(fs * 2.9)
    m = Image.new('L', base.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((x, y + int(h * .14), x + w, y + h + int(h * .14)), radius=int(h * .22), fill=105)
    base.paste(Image.new('RGB', base.size, (96, 34, 26)), (0, 0), m.filter(ImageFilter.GaussianBlur(h * .15)))
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((x, y, x + w, y + h), radius=int(h * .22), fill=RED)
    gift(d, x + pad + ic // 2, y + h // 2, int(ic * .52), WHITE, RED)
    tx = x + pad + ic + int(fs * .7)
    dls(d, tx, y + int(h * .20), TAG1, f1, WHITE, fs * .06)
    d.text((tx, y + int(h * .20) + int(fs * 1.16)), TAG2, font=f2, fill=(255, 226, 220))
    return w, h


ADU = trimmed('cut_adulto.png')   # Protocolo Adulto — 4 frascos
KID = trimmed('cut_kids24.png')   # VermeFree Kids 2 a 4
OLE = bottle_only('cut_oleo.png')  # Oleo de Alho — o brinde

# --- Copy aprovada. Checklist ANVISA: sem cura/elimina/erradica/milagre,
#     sem medico, sem diagnostico, sem comparacao com farmacia, sem cupom. ---
H1, H2, H3 = 'DIA D', '10% OFF', 'SÓ HOJE'     # headline empilhada em 3 linhas
SUB = 'JÁ NO PREÇO, SEM CUPOM'                  # o diferencial, no slot do subtitulo
BODY = 'Frete grátis sem valor mínimo e 1 Óleo de Alho de brinde no seu pedido.'
MICRO = '+ Manual da Desparasitação em PDF por e-mail.'
PT = 'QUARTA 09/09 · 24 HORAS'
CT = 'APROVEITAR O DIA D'
PHOTO = 'hero.jpg'


def desktop(txt=True):
    """2400x1000 — bloco creme a esquerda, bloco fotografico a direita,
    separados pelo corte diagonal."""
    W, H = 2400, 1000
    XT, XBt = 1100, 1340          # x do corte no topo e na base
    LEAN = XBt - XT
    bg = Image.new('RGB', (W, H), CREAM)

    pm = photo_block(bg, PHOTO, [(XT, 0), (W, 0), (W, H), (XBt, H)], (XT - 40, 0, W - XT + 40, H))

    # faixas anguladas SOBRE a foto, recortadas pelo bloco (assinatura do conceito)
    vbar(bg, XT + 180, 300, LEAN, CREAM, .20, clip=pm)
    vbar(bg, XT + 560, 110, LEAN, CREAM, .34, clip=pm)
    vbar(bg, XT + 740, 44, LEAN, CREAM, .24, clip=pm)
    vbar(bg, XT + 1010, 190, LEAN, RED, .14, clip=pm)

    # bloco de cor + filete vermelho na aresta
    poly(bg, [(0, 0), (XT, 0), (XBt, H), (0, H)], CREAM, 1.0)
    vbar(bg, XT, 15, LEAN, RED, 1.0)
    vbar(bg, XT + 44, 7, LEAN, RED, .55)
    vbar(bg, XT + 72, 4, LEAN, CREAM, .85)

    tris(bg, 1480, 150, 44, 17, CREAM, .90)
    tris(bg, 2160, 760, 40, 15, CREAM, .80)
    tag(bg, 1452, 806, 34)
    if not txt:
        return bg

    X, COL = 390, 690             # coluna a esquerda do corte (termina em 1080 < 1100)
    p_h, _ = pill(bg, X, 118, PT, 26, 28, 14)
    d = ImageDraw.Draw(bg)
    y = 118 + p_h + 36
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
    fb = F(SB, 27)
    for ln in wrap(fb, BODY, COL):
        d.text((X, y), ln, font=fb, fill=INK)
        y += 39
    fm = F(RG, 23)
    for ln in wrap(fm, MICRO, COL):
        d.text((X, y), ln, font=fm, fill=MUTED)
        y += 32
    cta(bg, X, y + 22, CT, 30)
    return bg


def mobile(txt=True):
    """1080x1350 — composicao redesenhada em tres faixas diagonais:
    bloco creme (texto) / bloco fotografico / bloco creme (apoio + CTA)."""
    W, H = 1080, 1350
    bg = Image.new('RGB', (W, H), CREAM)
    band = [(0, 640), (W, 570), (W, 990), (0, 1060)]
    bm = photo_block(bg, PHOTO, band, (0, 565, W, 500))

    vbar(bg, -40, 150, 260, CREAM, .24, 570, 1060, clip=bm)
    vbar(bg, 320, 54, 260, CREAM, .32, 570, 1060, clip=bm)
    vbar(bg, 760, 200, 260, RED, .14, 570, 1060, clip=bm)

    poly(bg, [(0, 640), (W, 570), (W, 584), (0, 654)], RED, 1.0)
    poly(bg, [(0, 674), (W, 604), (W, 611), (0, 681)], RED, .55)
    poly(bg, [(0, 1060), (W, 990), (W, 1004), (0, 1074)], RED, 1.0)

    tris(bg, 64, 700, 36, 13, CREAM, .90)
    tag(bg, int((W - tag_w(30)) / 2), 872, 30)
    if not txt:
        return bg

    COL = 940
    fp = F(XB, 25)
    pe = wls(fp, PT, 2.75) + int(25 * 1.12) + int(25 * .52) + 56
    p_h, _ = pill(bg, int((W - pe) / 2), 58, PT, 25, 28, 13)
    d = ImageDraw.Draw(bg)
    y = 58 + p_h + 30
    f1, s1 = fit(XB, H1, COL, 68, ls=1)
    dls(d, (W - wls(f1, H1, 1)) / 2, y, H1, f1, INK, 1)
    y += int(s1 * 1.02)
    f2, s2 = fit(XB, H2, COL, 170, ls=-3)
    dls(d, (W - wls(f2, H2, -3)) / 2, y, H2, f2, RED, -3)
    y += int(s2 * 1.00)
    f3, s3 = fit(XB, H3, COL - 120, 68, ls=1)
    lf = leaf_img(int(s3 * .86), RED, CREAM)
    sx = (W - (wls(f3, H3, 1) + s3 * .26 + lf.width)) / 2.
    ex = dls(d, sx, y, H3, f3, INK, 1)
    bg.paste(lf, (int(ex + s3 * .26), int(y + s3 * .10)), lf)
    y += int(s3 * 1.30)
    fsu, _ = fit(XB, SUB, COL, 26, ls=5)
    dls(d, (W - wls(fsu, SUB, 5)) / 2, y, SUB, fsu, RED, 5)

    y = 1104
    fb = F(SB, 27)
    for ln in wrap(fb, BODY, 880):
        d.text(((W - fb.getlength(ln)) / 2, y), ln, font=fb, fill=INK)
        y += 39
    f = F(XB, 31)
    cw = int(wls(f, CT, 31 * .07)) + int(31 * 2.9) + int(31 * .80)
    cta(bg, int((W - cw) / 2), y + 16, CT, 31)
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
