# -*- coding: utf-8 -*-
"""
Banner hero — Dia D VermeFree · quarta 09/09
============================================
Gera as 4 pecas obrigatorias (desktop/mobile, com texto e chapa limpa).

CONCEITO — adaptado da referencia aprovada (poster "GO STRONG · Serious Mass"):
produto flutuando e inclinado como heroi, fitas de marca envolvendo o produto
(umas por tras, outras por cima, que e o que cria a ilusao de embrulho),
ambiente com ceu em degrade e colina, assinatura manuscrita ao fundo, badge
de spec em caixa solida e botao pill no rodape.

Paleta trocada para a do Dia D: fitas e badges em VERMELHO #C42B2B em vez do
verde-limao da referencia. O verde da marca fica no rotulo do produto e na
colina — o contraste vermelho x verde e o que o briefing pede.

REGRA CENTRAL: o produto e a foto oficial do cliente apenas com o fundo
removido e reescalada. Nenhum frasco, rotulo ou embalagem e gerado,
recriado ou retocado. Nao ha fundo gerado por IA: ceu, colina, fitas,
badges e tipografia sao todos desenhados por codigo.

Entradas esperadas na pasta de trabalho:
  hero_cut.png                    -> foto oficial com fundo removido (RGBA)
  fonts/m400.ttf  fonts/m600.ttf  -> Montserrat Regular/SemiBold
  fonts/caveat.ttf                -> Caveat Bold (assinatura manuscrita)
  Montserrat-ExtraBold via fontconfig do sistema
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

RED = (196, 43, 43)        # #C42B2B  cor da acao
DRED = (150, 30, 30)       # borda das fitas
CREAM = (253, 248, 243)    # #FDF8F3
INK = (38, 34, 30)
GRN = (92, 130, 68)        # verde folha (colina, assinatura)
GRND = (58, 88, 44)        # verde escuro (colina da frente)
SKY_T = (216, 231, 222)    # topo do ceu
SKY_B = (253, 248, 243)    # horizonte

XB = '/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf'
SB, RG, SC = 'fonts/m600.ttf', 'fonts/m400.ttf', 'fonts/caveat.ttf'


def F(p, s):
    return ImageFont.truetype(p, s)


def wls(f, s, ls=0):
    return sum(f.getlength(c) for c in s) + ls * (len(s) - 1)


def dls(d, x, y, s, f, fill, ls=0):
    for c in s:
        d.text((x, y), c, font=f, fill=fill)
        x += f.getlength(c) + ls
    return x


def fit(p, s, maxw, start, ls=0, mn=8):
    """Reduz o corpo ate caber. Impede qualquer estouro de coluna."""
    z = start
    while z > mn:
        f = F(p, z)
        if wls(f, s, ls) <= maxw:
            return f, z
        z -= 2
    return F(p, mn), mn


def sky(W, H):
    """Degrade vertical do ceu."""
    g = Image.new('RGB', (1, H))
    for y in range(H):
        t = (y / float(H)) ** 0.85
        g.putpixel((0, y), tuple(int(SKY_T[k] + (SKY_B[k] - SKY_T[k]) * t) for k in range(3)))
    return g.resize((W, H)).convert('RGBA')


def hills(base, y0):
    """Duas colinas sobrepostas na base, feitas de elipses."""
    W, H = base.size
    for bbox, col in (((-int(W * .25), y0, int(W * 1.3), y0 + int(H * 1.5)), GRN),
                      ((-int(W * .45), y0 + int(H * .075), int(W * .88), y0 + int(H * 1.6)), GRND)):
        l = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(l).ellipse(bbox, fill=col + (255,))
        base.alpha_composite(l.filter(ImageFilter.GaussianBlur(1.2)))


def script(base, cx, cy, txt, size, alpha, ang):
    """Assinatura manuscrita ao fundo (Caveat), girada."""
    f = F(SC, size)
    s = Image.new('RGBA', (int(f.getlength(txt) + size * .6), int(size * 1.7)), (0, 0, 0, 0))
    ImageDraw.Draw(s).text((size * .3, 0), txt, font=f, fill=GRN + (alpha,))
    r = s.rotate(ang, expand=True, resample=Image.BICUBIC)
    base.alpha_composite(r, (int(cx - r.width / 2), int(cy - r.height / 2)))


def tape(base, cx, cy, L, T, ang, txt, fs, withtext=True):
    """Uma fita: banda com texto repetido, girada e composta."""
    s = Image.new('RGBA', (L, T), (0, 0, 0, 0))
    d = ImageDraw.Draw(s)
    d.rectangle((0, 0, L, T), fill=RED + (240,))
    e = max(2, int(T * .11))
    d.rectangle((0, 0, L, e), fill=DRED + (240,))
    d.rectangle((0, T - e, L, T), fill=DRED + (240,))
    if withtext:
        f = F(XB, fs)
        ls = fs * .17
        unit = wls(f, txt, ls) + fs * 1.5
        x = -unit
        while x < L:
            dls(d, x, (T - fs * 1.32) / 2, txt, f, (255, 241, 237, 255), ls)
            x += unit
    r = s.rotate(ang, expand=True, resample=Image.BICUBIC)
    base.alpha_composite(r, (int(cx - r.width / 2), int(cy - r.height / 2)))


def ramp_h(size, x0, x1):
    W, H = size
    m = Image.new('L', (W, 1), 0)
    px = m.load()
    for x in range(W):
        px[x, 0] = 0 if x <= x0 else (255 if x >= x1 else int(255 * (x - x0) / float(x1 - x0)))
    return m.resize((W, H))


def ramp_v(size, y0, y1, y2, y3):
    W, H = size
    m = Image.new('L', (1, H), 0)
    px = m.load()
    for y in range(H):
        if y <= y0 or y >= y3:
            v = 0.0
        elif y < y1:
            v = (y - y0) / float(y1 - y0)
        elif y <= y2:
            v = 1.0
        else:
            v = (y3 - y) / float(y3 - y2)
        px[0, y] = int(255 * v)
    return m.resize((W, H))


def tapes(base, specs, txt, mask):
    """Desenha um grupo de fitas e mascara para elas nao invadirem o texto.
    Sem isso as fitas atravessam a headline e matam a legibilidade."""
    lay = Image.new('RGBA', base.size, (0, 0, 0, 0))
    for cx, cy, L, T, a, fs in specs:
        tape(lay, cx, cy, L, T, a, TTXT, fs, txt)
    if mask is not None:
        lay.putalpha(ImageChops.multiply(lay.getchannel('A'), mask))
    base.alpha_composite(lay)


def product(base, img, cx, cy, h, ang):
    """Produto inclinado com sombra projetada."""
    w = int(img.width * h / img.height)
    p = img.resize((w, h), Image.LANCZOS).rotate(ang, expand=True, resample=Image.BICUBIC)
    sh = Image.new('RGBA', base.size, (0, 0, 0, 0))
    col = Image.new('RGBA', p.size, (64, 54, 40, 255))
    col.putalpha(p.getchannel('A').point(lambda v: int(v * .40)))
    sh.alpha_composite(col, (int(cx - p.width / 2 + 20), int(cy - p.height / 2 + 38)))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(28)))
    base.alpha_composite(p, (int(cx - p.width / 2), int(cy - p.height / 2)))
    return (int(cx - p.width / 2), int(cy - p.height / 2), int(cx + p.width / 2), int(cy + p.height / 2))


def gift(d, cx, cy, r, fg, bg):
    gw, gh = int(r * 1.15), int(r * .86)
    gx, gy = cx - gw // 2, cy - int(r * .30)
    d.rectangle((gx, gy, gx + gw, gy + gh), fill=fg)
    d.line((cx, gy, cx, gy + gh), fill=bg, width=max(2, int(r * .16)))
    d.line((gx, gy + int(gh * .34), gx + gw, gy + int(gh * .34)), fill=bg, width=max(2, int(r * .16)))
    d.ellipse((cx - int(r * .56), gy - int(r * .36), cx - int(r * .04), gy + int(r * .10)), outline=fg, width=max(2, int(r * .14)))
    d.ellipse((cx + int(r * .04), gy - int(r * .36), cx + int(r * .56), gy + int(r * .10)), outline=fg, width=max(2, int(r * .14)))


def badge_w(l1, l2, fs, ic=False):
    f1, f2 = F(XB, fs), F(XB, int(fs * .40))
    pad = int(fs * .44)
    iw = int(fs * 1.25) if ic else 0
    return int(max(wls(f1, l1, fs * .01), wls(f2, l2, fs * .10))) + pad * 2 + iw + (int(fs * .35) if ic else 0)


def badge(base, x, y, l1, l2, fs, ic=False):
    """Caixa solida de spec, no espirito do 'GAINER 2.73KG' da referencia."""
    f1, f2 = F(XB, fs), F(XB, int(fs * .40))
    pad = int(fs * .44)
    iw = int(fs * 1.25) if ic else 0
    w = badge_w(l1, l2, fs, ic)
    h = int(fs * 1.60) + pad * 2
    ov = Image.new('RGBA', base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.rectangle((x, y, x + w, y + h), fill=RED + (255,))
    tx = x + pad
    if ic:
        gift(d, x + pad + iw // 2, y + h // 2, int(iw * .46), CREAM + (255,), RED + (255,))
        tx = x + pad + iw + int(fs * .35)
    dls(d, tx, y + pad - int(fs * .10), l1, f1, CREAM + (255,), fs * .01)
    dls(d, tx, y + pad + int(fs * 1.02), l2, f2, (255, 214, 206, 255), fs * .10)
    base.alpha_composite(ov)
    return w, h


def cta(base, x, y, txt, fs):
    f = F(XB, fs)
    ls = fs * .07
    tw = wls(f, txt, ls)
    ar = int(fs * .80)
    h = int(fs * 2.45)
    w = int(tw) + int(fs * 2.9) + ar
    ov = Image.new('RGBA', base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=RED + (255,))
    tx = x + int((w - tw - ar - fs * .45) / 2)
    ex = dls(d, tx, y + int((h - fs * 1.30) / 2), txt, f, CREAM + (255,), ls)
    cy = y + h // 2
    ax = ex + int(fs * .52)
    lw, s = max(3, int(fs * .11)), int(fs * .23)
    d.line((ax, cy - s, ax + s, cy), fill=CREAM + (255,), width=lw)
    d.line((ax, cy + s, ax + s, cy), fill=CREAM + (255,), width=lw)
    base.alpha_composite(ov)
    return w, h


HERO = Image.open('hero_cut.png').convert('RGBA')
HERO = HERO.crop(HERO.getchannel('A').getbbox())

TTXT = 'DIA D · 10% OFF · SÓ HOJE'      # texto repetido nas fitas
H1, H2 = '10% OFF', 'SÓ HOJE'
SUB = 'JÁ NO PREÇO, SEM CUPOM'
CT = 'APROVEITAR O DIA D'


def desktop(txt=True):
    W, H = 2400, 1000
    bg = sky(W, H)
    hills(bg, int(H * .78))
    if txt:
        script(bg, 430, 180, 'Dia D', 430, 58, -7)
    mk = ramp_h((W, H), 1150, 1340)        # fitas so a partir da coluna do produto
    tapes(bg, [(1560, 250, 2600, 88, -19, 30), (1620, 690, 2600, 84, 9, 29),
               (1480, 110, 2600, 80, 23, 28)], txt, mk)     # atras do produto
    product(bg, HERO, 1700, 480, 760, -14)
    tapes(bg, [(1700, 780, 2600, 82, -8, 28), (1880, 370, 2600, 74, 4, 26)], txt, mk)  # na frente
    if not txt:
        return bg.convert('RGB')
    X, COL = 420, 880
    d = ImageDraw.Draw(bg)
    f1, s1 = fit(XB, H1, COL, 200, ls=-3)
    dls(d, X, 175, H1, f1, RED, -3)
    y = 175 + int(s1 * 1.00)
    f2, s2 = fit(XB, H2, 620, 112, ls=1)
    dls(d, X, y, H2, f2, INK, 1)
    y += int(s2 * 1.22)
    fs, _ = fit(XB, SUB, COL, 29, ls=5)
    dls(d, X, y, SUB, fs, RED, 5)
    y += 64
    w1, h1 = badge(bg, X, y, 'FRETE GRÁTIS', 'SEM VALOR MÍNIMO', 34)
    badge(bg, X + w1 + 26, y, 'BRINDE', '1 ÓLEO DE ALHO', 34, ic=True)
    cta(bg, X, y + h1 + 40, CT, 31)
    return bg.convert('RGB')


def mobile(txt=True):
    W, H = 1080, 1350
    bg = sky(W, H)
    hills(bg, int(H * .83))
    if txt:
        script(bg, 560, 60, 'Dia D', 300, 52, -7)
        script(bg, 540, 1250, 'Dia D', 250, 40, -5)
    mk = ramp_v((W, H), 430, 545, 1130, 1205)   # fitas so na faixa do produto
    tapes(bg, [(540, 560, 1600, 74, -20, 25), (540, 950, 1600, 72, 11, 25),
               (540, 720, 1600, 66, -4, 23)], txt, mk)
    product(bg, HERO, 580, 800, 650, -14)
    tapes(bg, [(540, 1020, 1600, 70, -9, 24), (540, 630, 1600, 62, 6, 22)], txt, mk)
    if not txt:
        return bg.convert('RGB')
    d = ImageDraw.Draw(bg)
    f1, s1 = fit(XB, H1, 900, 168, ls=-3)
    dls(d, (W - wls(f1, H1, -3)) / 2, 88, H1, f1, RED, -3)
    y = 88 + int(s1 * 1.00)
    f2, s2 = fit(XB, H2, 600, 104, ls=1)
    dls(d, (W - wls(f2, H2, 1)) / 2, y, H2, f2, INK, 1)
    y += int(s2 * 1.20)
    fs, _ = fit(XB, SUB, 880, 25, ls=5)
    dls(d, (W - wls(fs, SUB, 5)) / 2, y, SUB, fs, RED, 5)
    badge(bg, 44, 600, 'FRETE GRÁTIS', 'SEM VALOR MÍNIMO', 27)
    bw = badge_w('BRINDE', '1 ÓLEO DE ALHO', 27, True)
    badge(bg, W - 44 - bw, 880, 'BRINDE', '1 ÓLEO DE ALHO', 27, ic=True)
    f = F(XB, 32)
    cw = int(wls(f, CT, 32 * .07)) + int(32 * 2.9) + int(32 * .80)
    cta(bg, int((W - cw) / 2), 1216, CT, 32)
    return bg.convert('RGB')


def save(img, name, target_kb):
    img.save(name + '.png', optimize=True)
    q = 92
    while q >= 40:
        img.save(name + '.webp', 'WEBP', quality=q, method=6)
        if os.path.getsize(name + '.webp') / 1024.0 <= target_kb:
            break
        q -= 4
    print(name, 'WEBP q%d %.1fKB' % (q, os.path.getsize(name + '.webp') / 1024.0))


if __name__ == '__main__':
    save(desktop(True), 'vermefree-diad-0909-desktop-2400x1000', 300)
    save(mobile(True), 'vermefree-diad-0909-mobile-1080x1350', 150)
    save(desktop(False), 'vermefree-diad-0909-desktop-chapa-limpa-2400x1000', 300)
    save(mobile(False), 'vermefree-diad-0909-mobile-chapa-limpa-1080x1350', 150)
