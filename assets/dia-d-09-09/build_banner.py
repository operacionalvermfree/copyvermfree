# -*- coding: utf-8 -*-
"""
Banner hero — Dia D VermeFree · quarta 09/09  ·  versão cinematográfica
======================================================================
Gera as 4 pecas obrigatorias (desktop/mobile, com texto e chapa limpa).

METODO. A cena e GERADA por modelo generativo (pedestal de ardosia, luz-chave
dramatica, nevoa volumetrica, profundidade de campo), sempre VAZIA — sem
produto, sem pessoas, sem texto. A LINHA COMPLETA DE PRODUTOS e a foto real
do cliente (IMG_1479, os frascos lado a lado) com fundo removido, composta
na cena com o tratamento que faz um objeto parecer que esta mesmo ali:

  micro-contraste  UnsharpMask leve, para o rotulo aguentar a reducao
  relight          gradiente direcional casando com a luz-chave da chapa
  rim light        luz quente na borda do lado iluminado
  profundidade     a ponta oposta a luz recua: escurece e dessatura
  sombra projetada para o lado oposto a luz, achatada e borrada
  contato          faixa curta tirada da BASE do alfa, entao cada frasco
                   ganha a sua propria sombra de contato (a linha nao vira
                   um borrao unico)
  reflexo          copia espelhada com fade, no tampo polido

A chapa nao e medida a mao: `calib()` acha o topo do pedestal (maior queda
de luminancia varrendo o eixo Y), o centro/vao do pedestal (colunas claras
na faixa logo acima) e de que lado vem a luz (metade superior esquerda vs
direita). Assim trocar a chapa nao exige recalibrar nada a mao.

REGRA CENTRAL: nenhum frasco, rotulo ou embalagem e gerado, recriado ou
retocado. Relight e sombras sao operacoes fotometricas sobre os pixels
originais — brilho, matiz e mascara — nunca redesenho.

Entradas esperadas na pasta de trabalho:
  fam.png                   -> foto oficial da linha completa, fundo removido
  cine_d.png / cine_m.png   -> chapas de cena geradas, vazias
  fonts/m600.ttf            -> Montserrat SemiBold
  Montserrat-ExtraBold via fontconfig do sistema
"""
import os
from PIL import (Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance,
                 ImageChops, ImageStat)

RED = (198, 46, 46)          # fundo da pilula do CTA (texto creme por cima)
RED_T = (226, 74, 66)        # vermelho de TEXTO sobre o escuro: contraste 4.9:1
CREAM = (247, 242, 235)
WARM = (255, 214, 150)       # temperatura da luz-chave
DIM = (176, 168, 156)
GREEN = (34, 68, 44)         # verde da marca: botao do tema claro (9,6:1 com creme)
HAIR = (196, 188, 174)       # fio fino sobre o creme
INK = (26, 38, 30)           # verde-preto: o texto do tema claro
DIM_L = (96, 104, 92)        # olho do tema claro (4,8:1 sobre o creme)

# Os dois temas. Toda a diferenca entre a arte escura e a clara mora aqui:
# a composicao, a tipografia e a ordem dos blocos sao as mesmas. O tema
# escuro e dramatico (luz dura, sombra preta, reflexo forte); o claro e
# difuso (luz suave, sombra taupe curta, quase sem reflexo) — que e como
# um objeto se comporta de verdade num set claro.
DARK = dict(
    layout='cine',
    plate=('cine_d.png', 'cine_m.png'),
    ink=CREAM, dim=DIM, accent=RED_T, hair=(72, 78, 70), btn=RED,
    veil=(6, 9, 8), scrim_d=.74, scrim_m=.76,
    vig_d=.62, vig_m=.58,
    glow=(150, 160, 110), glow_a=74,
    lo=.68, hi=1.38, warm=.12, rim=235,
    depth=.55, depth_col=(18, 22, 20),
    shadow=(0, 0, 0), cast=.55, contact=.90, refl=.30,
)
LIGHT = dict(
    layout='ed',
    plate=('cine_dl.png', 'cine_ml.png'),
    ink=INK, dim=DIM_L, accent=RED, hair=HAIR, btn=GREEN,
    veil=(253, 250, 245), scrim_d=.58, scrim_m=.62,
    vig_d=0, vig_m=0,
    glow=None, glow_a=0,
    lo=.88, hi=1.14, warm=.05, rim=80,
    depth=.26, depth_col=(150, 152, 146),
    shadow=(88, 80, 70), cast=.34, contact=.60, refl=.15,
)

XB = '/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf'
SB = 'fonts/m600.ttf'


def F(p, s):
    return ImageFont.truetype(p, s)


def wls(f, s, ls=0):
    return sum(f.getlength(c) for c in s) + ls * (len(s) - 1)


def dls(d, x, y, s, f, fill, ls=0):
    for c in s:
        d.text((x, y), c, font=f, fill=fill)
        x += f.getlength(c) + ls
    return x


def fit(p, s, maxw, start, ls=0):
    """Reduz o corpo ate caber. Impede estouro de coluna."""
    z = start
    while z > 8:
        f = F(p, z)
        if wls(f, s, ls) <= maxw:
            return f, z
        z -= 2
    return F(p, 8), 8


def cover(img, W, H):
    s = max(W / float(img.width), H / float(img.height))
    r = img.resize((int(img.width * s + 1), int(img.height * s + 1)), Image.LANCZOS)
    x, y = (r.width - W) // 2, (r.height - H) // 2
    return r.crop((x, y, x + W, y + H))


def grade(im):
    return ImageEnhance.Color(ImageEnhance.Contrast(im).enhance(1.12)).enhance(1.10)


def calib(im):
    """Le a chapa: topo do pedestal, centro/vao dele e de que lado vem a luz.

    Retorna (y_topo, x_centro, vao, luz_da_direita), todos normalizados 0..1
    menos o booleano. Varre linhas finas medindo luminancia media: o topo do
    pedestal e onde a media despenca (tampo claro -> face escura).
    """
    g = im.convert('L')
    W, H = g.size
    st = max(2, H // 200)
    x0, x1 = int(W * .35), int(W * .98)
    pr = [(y, ImageStat.Stat(g.crop((x0, y, x1, y + st))).mean[0])
          for y in range(int(H * .30), int(H * .92), st)]
    best = None
    for i in range(5, len(pr) - 5):
        d = (sum(p[1] for p in pr[i - 5:i]) / 5. - sum(p[1] for p in pr[i:i + 5]) / 5.)
        if best is None or d > best[1]:
            best = (pr[i][0], d)
    band = g.crop((0, max(0, best[0] - st * 3), W, best[0]))
    cv = [ImageStat.Stat(band.crop((int(W * c / 60.), 0,
                                    int(W * (c + 1) / 60.), band.height))).mean[0]
          for c in range(60)]
    mx = max(cv)
    xs = [c for c in range(60) if cv[c] > mx * .5]
    lo = ImageStat.Stat(g.crop((0, 0, W // 4, H // 2))).mean[0]
    hi = ImageStat.Stat(g.crop((3 * W // 4, 0, W, H // 2))).mean[0]
    return (best[0] / float(H), (min(xs) + max(xs)) / 120.,
            (max(xs) - min(xs)) / 60., hi > lo)


def vignette(base, amt):
    """Fecha os cantos para concentrar a atencao no produto. No tema claro
    amt=0: escurecer canto de um set arejado so sujaria a foto."""
    if not amt:
        return
    W, H = base.size
    m = Image.new('L', (W, H), 0)
    ImageDraw.Draw(m).ellipse((-int(W * .28), -int(H * .34), int(W * 1.28), int(H * 1.34)), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(min(W, H) * .14)).point(lambda v: int(255 - (255 - v) * amt))
    base.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0), ImageChops.invert(m))


def glow(base, cx, cy, rx, ry, col, a):
    """Halo suave atras do produto, para separa-lo do fundo escuro. No tema
    claro nao existe: o produto ja se destaca por ser mais escuro que o set."""
    if col is None:
        return
    W, H = base.size
    m = Image.new('L', (W, H), 0)
    ImageDraw.Draw(m).ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=a)
    base.paste(Image.new('RGB', (W, H), col), (0, 0),
               m.filter(ImageFilter.GaussianBlur(max(rx, ry) * .48)))


def scrim(base, horiz, amt, hold, fade, col, rev=False):
    """Cortina escura sob o texto. A chapa e uma foto: sem isto o vermelho
    do subtitulo cai no facho de luz e o contraste despenca (medido: 2.5:1).
    Fica cheia ate `hold` e some ate `hold+fade`, entao nao vira caixa dura."""
    W, H = base.size
    n = W if horiz else H
    g = Image.new('L', (W, 1) if horiz else (1, H))
    for i in range(n):
        k = (n - 1 - i) if rev else i
        if k <= hold:
            v = amt
        else:
            v = amt * max(0., 1 - (k - hold) / float(fade)) ** 1.4
        g.putpixel((i, 0) if horiz else (0, i), int(255 * v))
    base.paste(Image.new('RGB', (W, H), col), (0, 0), g.resize((W, H)))


def chip(base, x, y, txt, fs, center_w=None):
    """Etiqueta vermelha do prazo. Texto creme sobre o vermelho da marca
    passa em contraste (4.7:1) onde o vermelho solto sobre a foto nao passava."""
    f = F(XB, fs)
    ls = fs * .10
    tw = wls(f, txt, ls)
    px, h = int(fs * .95), int(fs * 2.05)
    w = int(tw) + px * 2
    if center_w is not None:
        x = int((center_w - w) / 2)
    ov = Image.new('RGBA', base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.rounded_rectangle((x, y, x + w, y + h), radius=int(h * .30), fill=RED + (255,))
    dls(d, x + px, y + int((h - fs * 1.32) / 2), txt, f, CREAM + (255,), ls)
    base.alpha_composite(ov)
    return w, h


def place(base, hero, cx, by, ht, fr, th):
    """Assenta a linha de produtos na cena. `fr` = luz vem da direita.
    `th` traz a dureza da luz: no set escuro tudo e forte, no claro tudo
    e suave — mesma matematica, amplitudes diferentes."""
    w = int(hero.width * ht / hero.height)
    p = hero.resize((w, ht), Image.LANCZOS).filter(
        ImageFilter.UnsharpMask(radius=2, percent=55, threshold=3))

    g = Image.new('L', (w, 1))
    for x in range(w):
        t = x / float(max(1, w - 1))
        if not fr:
            t = 1 - t
        g.putpixel((x, 0), int(255 * (t ** 1.35)))
    g = g.resize((w, ht))
    rgb = p.convert('RGB')
    o = Image.composite(ImageEnhance.Brightness(rgb).enhance(th['hi']),
                        ImageEnhance.Brightness(rgb).enhance(th['lo']), g)
    o = Image.composite(Image.blend(o, Image.new('RGB', (w, ht), WARM), th['warm']), o,
                        g.point(lambda v: int(v * .85)))

    dg = Image.new('L', (w, 1))
    for x in range(w):
        t = x / float(max(1, w - 1))
        dg.putpixel((x, 0), int(255 * (t if fr else 1 - t)))
    dg = dg.resize((w, ht))
    o = Image.composite(o, Image.blend(ImageEnhance.Color(o).enhance(.72),
                                       Image.new('RGB', (w, ht), th['depth_col']),
                                       th['depth']), dg)

    o = o.convert('RGBA')
    o.putalpha(p.getchannel('A'))

    a = o.getchannel('A')
    edge = ImageChops.subtract(a, ImageChops.offset(a, -9 if fr else 9, 3)).filter(
        ImageFilter.GaussianBlur(2.4))
    lay = Image.new('RGBA', o.size, WARM + (0,))
    lay.putalpha(edge.point(lambda v: int(v * th['rim'] / 255)))
    o = Image.alpha_composite(o, lay)

    a = o.getchannel('A')
    W, H = base.size
    sh = th['shadow']

    sq = a.resize((int(w * 1.12), max(10, int(ht * .30))), Image.LANCZOS)
    dx = int(-w * .13) if fr else int(w * .13)
    l = Image.new('L', (W, H), 0)
    l.paste(sq, (int(cx - sq.width / 2 + dx), int(by - sq.height * .60)))
    base.paste(Image.new('RGB', (W, H), sh), (0, 0),
               l.filter(ImageFilter.GaussianBlur(40)).point(lambda v: int(v * th['cast'])))

    foot = a.crop((0, int(ht * .93), w, ht)).resize(
        (int(w * .99), max(7, int(ht * .040))), Image.LANCZOS)
    l2 = Image.new('L', (W, H), 0)
    l2.paste(foot, (int(cx - foot.width / 2), int(by - foot.height * .50)))
    base.paste(Image.new('RGB', (W, H), sh), (0, 0),
               l2.filter(ImageFilter.GaussianBlur(7)).point(lambda v: int(v * th['contact'])))

    rf = o.transpose(Image.FLIP_TOP_BOTTOM)
    mm = Image.new('L', (1, ht))
    for y in range(ht):
        mm.putpixel((0, y), int(255 * th['refl'] * max(0., 1 - (y / float(ht)) * 2.8)))
    rf.putalpha(ImageChops.multiply(rf.getchannel('A'), mm.resize((w, ht))))
    base.alpha_composite(rf.filter(ImageFilter.GaussianBlur(5)), (int(cx - w / 2), int(by)))

    base.alpha_composite(o, (int(cx - w / 2), int(by - ht)))
    return int(cx - w / 2), int(by - ht), int(cx + w / 2), int(by)


def cta(base, x, y, txt, fs, bg=RED):
    f = F(XB, fs)
    ls = fs * .08
    tw = wls(f, txt, ls)
    ar = int(fs * .78)
    h = int(fs * 2.5)
    w = int(tw) + int(fs * 3.0) + ar
    ov = Image.new('RGBA', base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=bg + (255,))
    ex = dls(d, x + int((w - tw - ar - fs * .5) / 2), y + int((h - fs * 1.3) / 2), txt, f, CREAM + (255,), ls)
    cy = y + h // 2
    ax = ex + int(fs * .55)
    lw, s = max(3, int(fs * .11)), int(fs * .22)
    d.line((ax, cy - s, ax + s, cy), fill=CREAM + (255,), width=lw)
    d.line((ax, cy + s, ax + s, cy), fill=CREAM + (255,), width=lw)
    base.alpha_composite(ov)
    return w, h


def hair(d, x, y, w, col, t=2):
    """Fio fino. O tema claro se estrutura com fios, nao com blocos de cor."""
    if w > 0:
        d.rectangle((x, y, x + w - 1, y + t - 1), fill=col + (255,))


def lockup(d, x, y, col, hair_col, n, s, span):
    """Lockup do desconto empilhado: o numero manda e o OFF encosta embaixo,
    com um fio ate a borda da coluna. Le como uma coisa so, nao duas linhas."""
    fn = F(XB, n)
    dls(d, x, y, '10%', fn, col + (255,), -n * .02)
    yo = y + int(n * .88)
    fo = F(XB, s)
    ox = dls(d, x, yo, 'OFF', fo, col + (255,), s * .02)
    hx = ox + int(s * .45)
    hair(d, hx, yo + int(s * .60), (x + span) - hx, hair_col, 3)
    return yo + int(s * .98)


def numbered(d, x, y, items, col, dim, hair_col, fs, gap, w):
    """Lista numerada com fio entre os itens — vocabulario de bula/editorial,
    no lugar dos marcadores redondos do tema escuro."""
    fn = F(XB, int(fs * .68))
    ind = int(fs * 2.2)
    for i, t in enumerate(items):
        d.text((x, y + int(fs * .20)), '%02d' % (i + 1), font=fn, fill=dim + (255,))
        ft, _ = fit(SB, t, w - ind, fs)
        d.text((x + ind, y), t, font=ft, fill=col + (255,))
        if i < len(items) - 1:
            hair(d, x, y + gap - int(gap * .26), w, hair_col, 1)
        y += gap
    return y


EYEBROW = 'VERMEFREE  ·  DIA D'
H1 = '10% OFF'
H2 = 'SÓ HOJE · QUARTA 09/09'
BULLETS = ['Já no preço, sem cupom.',
           'Frete grátis sem valor mínimo.',
           '1 Óleo de Alho de brinde no pedido.']
CT = 'APROVEITAR O DIA D'

FAM = Image.open('fam.png').convert('RGBA')
FAM = FAM.crop(FAM.getchannel('A').getbbox())
RATIO = FAM.width / float(FAM.height)


def desktop_cine(txt=True, th=DARK):
    """2400x1000 — a linha inteira no pedestal, texto na coluna da esquerda."""
    W, H = 2400, 1000
    src = Image.open(th['plate'][0]).convert('RGB')
    yt, xc, _sp, fr = calib(src)
    bg = grade(cover(src, W, H)).convert('RGBA')

    gw = 920                                   # cabe em 1180..2100
    gh = int(gw / RATIO)
    cx = max(1560, min(int(W * xc), 1640))
    by = min(max(int(H * yt) + 6, 640), 760)   # calib erra? a linha nao sai do lugar
    glow(bg, cx, by - int(gh * .55), int(gw * .60), int(gh * .78), th['glow'], th['glow_a'])
    box = place(bg, FAM, cx, by, gh, fr, th)
    vignette(bg, th['vig_d'])
    scrim(bg, True, th['scrim_d'], 900, 520, th['veil'])
    if not txt:
        return bg.convert('RGB'), box
    X, COL = 404, 780
    d = ImageDraw.Draw(bg)
    fe, _ = fit(XB, EYEBROW, COL, 24, 9)
    dls(d, X, 224, EYEBROW, fe, th['dim'] + (255,), 9)
    f1, s1 = fit(XB, H1, COL, 212, -4)
    dls(d, X, 280, H1, f1, th['ink'] + (255,), -4)
    y = 280 + int(s1 * 1.02)
    _, ch = chip(bg, X, y, H2, 30)
    y += ch + 30
    d.line((X, y, X + 96, y), fill=th['accent'] + (255,), width=5)
    y += 38
    fb = F(SB, 27)
    for t in BULLETS:
        d.ellipse((X, y + 11, X + 10, y + 21), fill=th['accent'] + (255,))
        d.text((X + 31, y), t, font=fb, fill=th['ink'] + (255,))
        y += 44
    cta(bg, X, y + 30, CT, 29)
    return bg.convert('RGB'), box


def mobile_cine(txt=True, th=DARK):
    """1080x1350 — redesenhado, nao recortado: oferta em cima, linha de
    produtos no pedestal, CTA embaixo."""
    W, H = 1080, 1350
    src = Image.open(th['plate'][1]).convert('RGB')
    yt, _xc, _sp, fr = calib(src)
    bg = grade(cover(src, W, H)).convert('RGBA')

    gw = 880
    gh = int(gw / RATIO)
    cx = 540
    by = min(max(int(H * yt) + 8, 900), 1000)  # idem: faixa, nao valor solto
    glow(bg, cx, by - int(gh * .55), int(gw * .60), int(gh * .82), th['glow'], th['glow_a'])
    box = place(bg, FAM, cx, by, gh, fr, th)
    vignette(bg, th['vig_m'])
    scrim(bg, False, th['scrim_m'], 520, 200, th['veil'])
    if not txt:
        return bg.convert('RGB'), box
    d = ImageDraw.Draw(bg)
    fe, _ = fit(XB, EYEBROW, 900, 26, 8)
    dls(d, (W - wls(fe, EYEBROW, 8)) / 2, 68, EYEBROW, fe, th['dim'] + (255,), 8)
    f1, s1 = fit(XB, H1, 920, 172, -4)
    dls(d, (W - wls(f1, H1, -4)) / 2, 112, H1, f1, th['ink'] + (255,), -4)
    y = 112 + int(s1 * 1.02)
    _, ch = chip(bg, 0, y, H2, 34, center_w=W)
    y += ch + 32
    fb = F(SB, 32)
    for t in BULLETS:
        d.text(((W - fb.getlength(t)) / 2, y), t, font=fb, fill=th['ink'] + (255,))
        y += 45
    f = F(XB, 38)
    cw = int(wls(f, CT, 38 * .08)) + int(38 * 3.0) + int(38 * .78)
    cta(bg, int((W - cw) / 2), 1152, CT, 38)
    return bg.convert('RGB'), box


def desktop_ed(txt, th):
    """2400x1000 — composicao espelhada: a linha de produtos ocupa a esquerda
    e o texto a direita, em coluna editorial."""
    W, H = 2400, 1000
    src = Image.open(th['plate'][0]).convert('RGB')
    yt, _xc, _sp, fr = calib(src)
    bg = grade(cover(src, W, H)).convert('RGBA')

    gw = 900
    gh = int(gw / RATIO)
    cx = 760
    by = min(max(int(H * yt) + 6, 640), 760)
    box = place(bg, FAM, cx, by, gh, fr, th)
    scrim(bg, True, th['scrim_d'], 780, 460, th['veil'], rev=True)
    if not txt:
        return bg.convert('RGB'), box

    X, COL = 1400, 600
    d = ImageDraw.Draw(bg)
    fe, _ = fit(XB, EYEBROW, COL, 23, 9)
    dls(d, X, 150, EYEBROW, fe, th['dim'] + (255,), 9)
    hair(d, X, 196, COL, th['hair'], 2)
    y = lockup(d, X, 228, th['ink'], th['hair'], 250, 104, COL)
    y += 26
    f2, _ = fit(XB, H2, COL, 30, 6)
    dls(d, X, y, H2, f2, th['accent'] + (255,), 6)
    y += 56
    hair(d, X, y, COL, th['hair'], 2)
    y = numbered(d, X, y + 34, BULLETS, th['ink'], th['dim'], th['hair'], 26, 50, COL)
    cta(bg, X, y + 26, CT, 28, th['btn'])
    return bg.convert('RGB'), box


def mobile_ed(txt, th):
    """1080x1350 — mesmo vocabulario: display centrado, corpo alinhado a
    esquerda, fios no lugar de blocos, botao no verde da marca."""
    W, H = 1080, 1350
    src = Image.open(th['plate'][1]).convert('RGB')
    yt, _xc, _sp, fr = calib(src)
    bg = grade(cover(src, W, H)).convert('RGBA')

    gw = 820
    gh = int(gw / RATIO)
    by = min(max(int(H * yt) + 8, 900), 1000)
    box = place(bg, FAM, 540, by, gh, fr, th)
    scrim(bg, False, th['scrim_m'], 470, 190, th['veil'])
    if not txt:
        return bg.convert('RGB'), box

    d = ImageDraw.Draw(bg)
    fe, _ = fit(XB, EYEBROW, 900, 24, 8)
    dls(d, (W - wls(fe, EYEBROW, 8)) / 2, 50, EYEBROW, fe, th['dim'] + (255,), 8)
    hair(d, W / 2 - 55, 92, 110, th['hair'], 2)

    n, sz = 176, 76
    f1 = F(XB, n)
    w1 = wls(f1, '10%', -n * .02)
    dls(d, (W - w1) / 2, 112, '10%', f1, th['ink'] + (255,), -n * .02)
    yo = 112 + int(n * .88)
    fo = F(XB, sz)
    wo = wls(fo, 'OFF', sz * .02)
    ox = (W - wo) / 2
    dls(d, ox, yo, 'OFF', fo, th['ink'] + (255,), sz * .02)
    hy = yo + int(sz * .60)
    hair(d, (W - w1) / 2, hy, int(ox - 26 - (W - w1) / 2), th['hair'], 3)
    hair(d, ox + wo + 26, hy, int((W + w1) / 2 - (ox + wo + 26)), th['hair'], 3)

    y = yo + int(sz * .98) + 22
    f2, _ = fit(XB, H2, 940, 30, 5)
    dls(d, (W - wls(f2, H2, 5)) / 2, y, H2, f2, th['accent'] + (255,), 5)
    y += 54
    hair(d, W / 2 - 55, y, 110, th['hair'], 2)
    numbered(d, 240, y + 34, BULLETS, th['ink'], th['dim'], th['hair'], 28, 46, 600)

    f = F(XB, 36)
    cw = int(wls(f, CT, 36 * .08)) + int(36 * 3.0) + int(36 * .78)
    cta(bg, int((W - cw) / 2), 1160, CT, 36, th['btn'])
    return bg.convert('RGB'), box


def desktop(txt=True, th=DARK):
    return desktop_ed(txt, th) if th['layout'] == 'ed' else desktop_cine(txt, th)


def mobile(txt=True, th=DARK):
    return mobile_ed(txt, th) if th['layout'] == 'ed' else mobile_cine(txt, th)


def save(img, name, target_kb):
    img.save(name + '.png', optimize=True)
    q = 90
    while q >= 38:
        img.save(name + '.webp', 'WEBP', quality=q, method=6)
        if os.path.getsize(name + '.webp') / 1024.0 <= target_kb:
            break
        q -= 4
    print(name, 'WEBP q%d %.1fKB' % (q, os.path.getsize(name + '.webp') / 1024.0))


if __name__ == '__main__':
    for tag, th in (('', DARK), ('-claro', LIGHT)):
        d, bx = desktop(True, th)
        m, bm = mobile(True, th)
        print(tag or '-escuro', 'grupo desktop', bx, 'grupo mobile', bm)
        save(d, 'vermefree-diad-0909-desktop%s-2400x1000' % tag, 300)
        save(m, 'vermefree-diad-0909-mobile%s-1080x1350' % tag, 150)
        save(desktop(False, th)[0],
             'vermefree-diad-0909-desktop%s-chapa-limpa-2400x1000' % tag, 300)
        save(mobile(False, th)[0],
             'vermefree-diad-0909-mobile%s-chapa-limpa-1080x1350' % tag, 150)
