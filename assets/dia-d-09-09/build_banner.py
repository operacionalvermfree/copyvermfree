# -*- coding: utf-8 -*-
"""
Banner hero — Dia D VermeFree · quarta 09/09  ·  versão cinematográfica
======================================================================
Gera as 4 pecas obrigatorias (desktop/mobile, com texto e chapa limpa).

METODO. As versoes anteriores desenhavam a cena a mao em codigo, e o teto
disso e "amador". Aqui a cena e GERADA por modelo generativo (pedestal de
ardosia, luz-chave dramatica, nevoa volumetrica, profundidade de campo),
sempre VAZIA — sem produto, sem pessoas, sem texto. O produto e a foto
real do cliente com fundo removido, composta na cena com o tratamento
que faz um objeto parecer que esta mesmo ali:

  relight     gradiente direcional casando com a luz-chave da chapa
  rim light   luz quente na borda do lado iluminado
  sombra      projetada para o lado oposto a luz, achatada e borrada
  contato     sombra curta e escura na base, que "prega" o objeto no chao
  reflexo     copia espelhada com fade, no tampo polido

A luz de cada chapa foi medida antes: no desktop vem da DIREITA, no
mobile da ESQUERDA. O parametro `fr` (from_right) propaga isso para
relight, rim e direcao da sombra.

REGRA CENTRAL: nenhum frasco, rotulo ou embalagem e gerado, recriado ou
retocado. Relight e sombras sao operacoes fotometricas sobre os pixels
originais — brilho, matiz e mascara — nunca redesenho.

Entradas esperadas na pasta de trabalho:
  hero_cut.png              -> foto oficial com fundo removido (RGBA)
  cine_d.png / cine_m.png   -> chapas de cena geradas, vazias
  fonts/m600.ttf            -> Montserrat SemiBold
  Montserrat-ExtraBold via fontconfig do sistema
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops

RED = (198, 46, 46)
CREAM = (247, 242, 235)
WARM = (255, 214, 150)     # temperatura da luz-chave
DIM = (176, 168, 156)

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


def vignette(base, amt):
    """Fecha os cantos para concentrar a atencao no produto."""
    W, H = base.size
    m = Image.new('L', (W, H), 0)
    ImageDraw.Draw(m).ellipse((-int(W * .28), -int(H * .34), int(W * 1.28), int(H * 1.34)), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(min(W, H) * .14)).point(lambda v: int(255 - (255 - v) * amt))
    base.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0), ImageChops.invert(m))


def glow(base, cx, cy, r):
    """Halo suave atras do produto, para separa-lo do fundo escuro."""
    W, H = base.size
    m = Image.new('L', (W, H), 0)
    ImageDraw.Draw(m).ellipse((cx - r, cy - int(r * .78), cx + r, cy + int(r * .78)), fill=74)
    base.paste(Image.new('RGB', (W, H), (150, 160, 110)), (0, 0), m.filter(ImageFilter.GaussianBlur(r * .55)))


def place(base, hero, cx, by, ht, fr):
    """Assenta o produto na cena. `fr` = luz vem da direita."""
    w = int(hero.width * ht / hero.height)
    p = hero.resize((w, ht), Image.LANCZOS)

    # --- relight: gradiente na direcao da luz-chave ---
    g = Image.new('L', (w, 1))
    for x in range(w):
        t = x / float(max(1, w - 1))
        if not fr:
            t = 1 - t
        g.putpixel((x, 0), int(255 * (t ** 1.35)))
    g = g.resize((w, ht))
    rgb = p.convert('RGB')
    o = Image.composite(ImageEnhance.Brightness(rgb).enhance(1.38),
                        ImageEnhance.Brightness(rgb).enhance(.68), g)
    o = Image.composite(Image.blend(o, Image.new('RGB', (w, ht), WARM), .12), o,
                        g.point(lambda v: int(v * .85)))
    o = o.convert('RGBA')
    o.putalpha(p.getchannel('A'))

    # --- rim light: borda quente do lado iluminado ---
    a = o.getchannel('A')
    edge = ImageChops.subtract(a, ImageChops.offset(a, -9 if fr else 9, 3)).filter(ImageFilter.GaussianBlur(2.4))
    lay = Image.new('RGBA', o.size, WARM + (0,))
    lay.putalpha(edge.point(lambda v: int(v * 235 / 255)))
    o = Image.alpha_composite(o, lay)

    a = o.getchannel('A')
    W, H = base.size

    # --- sombra projetada, para o lado oposto a luz ---
    sq = a.resize((int(w * 1.35), max(10, int(ht * .30))), Image.LANCZOS)
    dx = int(-w * .46) if fr else int(w * .46)
    l = Image.new('L', (W, H), 0)
    l.paste(sq, (int(cx - sq.width / 2 + dx), int(by - sq.height * .60)))
    base.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0),
               l.filter(ImageFilter.GaussianBlur(40)).point(lambda v: int(v * .60)))

    # --- sombra de contato: curta e escura, prega o objeto no chao ---
    ct = a.resize((int(w * .94), max(8, int(ht * .055))), Image.LANCZOS)
    l2 = Image.new('L', (W, H), 0)
    l2.paste(ct, (int(cx - ct.width / 2), int(by - ct.height * .55)))
    base.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0),
               l2.filter(ImageFilter.GaussianBlur(9)).point(lambda v: int(v * .88)))

    # --- reflexo no tampo polido ---
    rf = o.transpose(Image.FLIP_TOP_BOTTOM)
    mm = Image.new('L', (1, ht))
    for y in range(ht):
        mm.putpixel((0, y), int(255 * .30 * max(0., 1 - (y / float(ht)) * 2.8)))
    rf.putalpha(ImageChops.multiply(rf.getchannel('A'), mm.resize((w, ht))))
    base.alpha_composite(rf.filter(ImageFilter.GaussianBlur(5)), (int(cx - w / 2), int(by)))

    base.alpha_composite(o, (int(cx - w / 2), int(by - ht)))


def cta(base, x, y, txt, fs):
    f = F(XB, fs)
    ls = fs * .08
    tw = wls(f, txt, ls)
    ar = int(fs * .78)
    h = int(fs * 2.5)
    w = int(tw) + int(fs * 3.0) + ar
    ov = Image.new('RGBA', base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=RED + (255,))
    ex = dls(d, x + int((w - tw - ar - fs * .5) / 2), y + int((h - fs * 1.3) / 2), txt, f, CREAM + (255,), ls)
    cy = y + h // 2
    ax = ex + int(fs * .55)
    lw, s = max(3, int(fs * .11)), int(fs * .22)
    d.line((ax, cy - s, ax + s, cy), fill=CREAM + (255,), width=lw)
    d.line((ax, cy + s, ax + s, cy), fill=CREAM + (255,), width=lw)
    base.alpha_composite(ov)
    return w, h


EYEBROW = 'VERMEFREE  ·  DIA D'
H1 = '10% OFF'
H2 = 'SÓ HOJE · QUARTA 09/09'
BULLETS = ['Já no preço, sem cupom.',
           'Frete grátis sem valor mínimo.',
           '1 Óleo de Alho de brinde no pedido.']
CT = 'APROVEITAR O DIA D'

HERO = Image.open('hero_cut.png').convert('RGBA')
HERO = HERO.crop(HERO.getchannel('A').getbbox())


def desktop(txt=True):
    """2400x1000 — luz da DIREITA, produto no pedestal, texto no negro a esquerda."""
    W, H = 2400, 1000
    bg = grade(cover(Image.open('cine_d.png').convert('RGB'), W, H)).convert('RGBA')
    glow(bg, 1800, 430, 300)
    place(bg, HERO, 1800, 655, 560, fr=True)
    vignette(bg, .62)
    if not txt:
        return bg.convert('RGB')
    X, COL = 400, 800
    d = ImageDraw.Draw(bg)
    fe, _ = fit(XB, EYEBROW, COL, 24, 9)
    dls(d, X, 232, EYEBROW, fe, DIM + (255,), 9)
    f1, s1 = fit(XB, H1, COL, 212, -4)
    dls(d, X, 288, H1, f1, CREAM + (255,), -4)
    y = 288 + int(s1 * 1.02)
    f2, _ = fit(XB, H2, COL, 30, 6)
    dls(d, X, y, H2, f2, RED + (255,), 6)
    y += 62
    d.line((X, y, X + 96, y), fill=RED + (255,), width=5)
    y += 40
    fb = F(SB, 27)
    for t in BULLETS:
        d.ellipse((X, y + 11, X + 10, y + 21), fill=RED + (255,))
        d.text((X + 31, y), t, font=fb, fill=CREAM + (255,))
        y += 44
    cta(bg, X, y + 32, CT, 29)
    return bg.convert('RGB')


def mobile(txt=True):
    """1080x1350 — luz da ESQUERDA, produto baixo e centrado, texto acima."""
    W, H = 1080, 1350
    bg = grade(cover(Image.open('cine_m.png').convert('RGB'), W, H)).convert('RGBA')
    glow(bg, 540, 690, 270)
    place(bg, HERO, 540, 918, 530, fr=False)
    vignette(bg, .58)
    if not txt:
        return bg.convert('RGB')
    d = ImageDraw.Draw(bg)
    fe, _ = fit(XB, EYEBROW, 900, 22, 8)
    dls(d, (W - wls(fe, EYEBROW, 8)) / 2, 108, EYEBROW, fe, DIM + (255,), 8)
    f1, s1 = fit(XB, H1, 900, 190, -4)
    dls(d, (W - wls(f1, H1, -4)) / 2, 158, H1, f1, CREAM + (255,), -4)
    y = 158 + int(s1 * 1.02)
    f2, _ = fit(XB, H2, 900, 27, 5)
    dls(d, (W - wls(f2, H2, 5)) / 2, y, H2, f2, RED + (255,), 5)
    fb = F(SB, 25)
    yy = 1010
    for t in BULLETS:
        d.text(((W - fb.getlength(t)) / 2, yy), t, font=fb, fill=CREAM + (255,))
        yy += 38
    f = F(XB, 30)
    cw = int(wls(f, CT, 2.4)) + 90 + 23
    cta(bg, int((W - cw) / 2), yy + 26, CT, 30)
    return bg.convert('RGB')


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
    save(desktop(True), 'vermefree-diad-0909-desktop-2400x1000', 300)
    save(mobile(True), 'vermefree-diad-0909-mobile-1080x1350', 150)
    save(desktop(False), 'vermefree-diad-0909-desktop-chapa-limpa-2400x1000', 300)
    save(mobile(False), 'vermefree-diad-0909-mobile-chapa-limpa-1080x1350', 150)
