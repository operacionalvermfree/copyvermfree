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
import os
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


ADU = trimmed('cut_adulto.png')
KID = trimmed('cut_kids24.png')
OLE = bottle_only('cut_oleo.png')

# --- Copy aprovada (checklist ANVISA: sem cura/elimina/erradica/milagre,
#     sem medico, sem diagnostico, sem comparacao com farmacia) ---
HEAD1 = '10% OFF'
HEAD2a = 'em todo o site. '
HEAD2b = 'So hoje.'.replace('So', 'Só')
SUP = ('Já no preço, sem cupom. Frete grátis sem valor mínimo '
       'e 1 Óleo de Alho de brinde no seu pedido.')
MICRO = '+ Manual da Desparasitação em PDF, por e-mail, para quem comprar.'
PILLTXT = 'SÓ HOJE · QUARTA 09/09'
CTATXT = 'Aproveitar o Dia D'


def desktop(with_text=True):
    W, H, HZ = 2400, 1000, 772
    bg, hf = build_bg('plate_d.png', W, H, HZ)
    bg = bg.convert('RGB')
    scrim_lr(bg, 980, 1600, 0.88)          # tambem na chapa limpa: o tema escreve por cima
    ah = int(H * 0.335)
    place(bg, ADU, 1585, 820, ah)          # Protocolo Adulto (4 frascos)
    place(bg, KID, 1865, 820, int(ah * 0.63))   # VermeFree Kids 2 a 4
    place(bg, OLE, 1345, 852, int(ah * 0.80))   # Oleo de Alho — o brinde, na frente
    if not with_text:
        return bg
    X, COL = 400, 790                      # coluna dentro da area segura (400..2000)
    ph, _ = pill(bg, X, 180, PILLTXT, 27, 30, 15)
    d = ImageDraw.Draw(bg)
    f1, s1 = fit(XB, HEAD1, COL, 196, ls=-2)
    y = 180 + ph + 34
    dls(d, X, y, HEAD1, f1, RED, -2)
    y += int(s1 * 1.16)
    f2, s2 = fit(XB, HEAD2a + HEAD2b, COL, 62, ls=-1)
    dls(d, dls(d, X, y, HEAD2a, f2, INK, -1), y, HEAD2b, f2, RED, -1)
    y += int(s2 * 1.62)
    fs = F(SB, 30)
    for ln in wrap(fs, SUP, COL):
        d.text((X, y), ln, font=fs, fill=INK)
        y += 42
    y += 6
    fm = F(RG, 25)
    for ln in wrap(fm, MICRO, COL):
        d.text((X, y), ln, font=fm, fill=MUTED)
        y += 34
    cta(bg, X, y + 26, CTATXT, 32)
    badge(bg, 1296, 596, 58)
    return bg


def mobile(with_text=True):
    W, H, HZ = 1080, 1350, 846
    bg, hf = build_bg('plate_m.png', W, H, HZ)
    bg = bg.convert('RGB')
    scrim_stops(bg, [(0, 0.70), (430, 0.70), (610, 0.0), (830, 0.0), (920, 0.62), (1350, 0.62)])
    ah = int(H * 0.255)
    place(bg, ADU, 530, 900, ah)
    place(bg, KID, 835, 900, int(ah * 0.60))
    place(bg, OLE, 213, 928, int(ah * 0.78))
    if not with_text:
        return bg
    COL = 940
    fp = F(XB, 26)
    pw_est = wls(fp, PILLTXT, 2.6) + int(26 * 1.15) + int(26 * 0.55) + 60
    ph, _ = pill(bg, int((W - pw_est) / 2), 88, PILLTXT, 26, 30, 14)
    d = ImageDraw.Draw(bg)
    f1, s1 = fit(XB, HEAD1, COL, 210, ls=-2)
    y = 88 + ph + 30
    dls(d, (W - wls(f1, HEAD1, -2)) / 2, y, HEAD1, f1, RED, -2)
    y += int(s1 * 1.14)
    f2, s2 = fit(XB, HEAD2a + HEAD2b, COL, 54, ls=-1)
    x2 = (W - wls(f2, HEAD2a + HEAD2b, -1)) / 2
    dls(d, dls(d, x2, y, HEAD2a, f2, INK, -1), y, HEAD2b, f2, RED, -1)
    badge(bg, 170, 700, 58)
    y = 985
    fs = F(SB, 31)
    for ln in wrap(fs, SUP, 900):
        d.text(((W - fs.getlength(ln)) / 2, y), ln, font=fs, fill=INK)
        y += 44
    f = F(XB, 34)
    cwid = int(wls(f, CTATXT, 34 * 0.02)) + int(34 * 3.0) + int(34 * 0.85)
    cta(bg, int((W - cwid) / 2), y + 22, CTATXT, 34)
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
