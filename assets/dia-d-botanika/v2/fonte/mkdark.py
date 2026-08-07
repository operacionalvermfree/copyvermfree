import sys, re
inf, outf = sys.argv[1], sys.argv[2]
s = open(inf).read()
# palette vars
s = s.replace("--ivory1:#ffffff","--ivory1:#123a34").replace("--ivory2:#f6f2e7","--ivory2:#0d2b2a").replace("--ivory3:#efe8d6","--ivory3:#0a1f22").replace("--ivory4:#e6dcc4","--ivory4:#06110f")
s = s.replace("--ink:#33372f","--ink:#e7ebe2")
s = s.replace("--indigo:#2b357e","--indigo:#f4efe0")
s = s.replace("--kick:#b48a35","--kick:#e7c877")
# spot glow -> gold
s = s.replace("rgba(255,255,255,.9)","rgba(231,200,120,.28)").replace("rgba(255,255,255,.85)","rgba(231,200,120,.26)")
s = s.replace("rgba(255,255,255,0) 70%","rgba(231,200,120,0) 70%")
# paper multiply -> screen gold
s = s.replace("mix-blend-mode:multiply","mix-blend-mode:screen")
s = s.replace("radial-gradient(rgba(120,110,80,.08) 1px","radial-gradient(rgba(231,200,120,.10) 1px")
# vignette dark
s = re.sub(r"rgba\(120,105,70,\.1[46]\) 100%","rgba(2,10,9,.72) 100%",s)
# floor dark
s = s.replace("rgba(206,192,160,0)","rgba(4,14,12,0)").replace("rgba(198,183,150,.35)","rgba(3,10,9,.55)").replace("rgba(198,183,150,.4)","rgba(3,10,9,.55)")
# frame gold brighter
s = s.replace("rgba(196,154,69,.45)","rgba(214,176,92,.55)").replace("rgba(196,154,69,.22)","rgba(214,176,92,.28)")
# watermark mono -> gold, more visible
s = s.replace("brand/mono_lime.png","brand/mono_gold.png").replace("opacity:.06;pointer-events:none","opacity:.11;pointer-events:none")
# product shadows dark
s = s.replace("rgba(40,46,30,.28)","rgba(0,0,0,.55)").replace("rgba(60,60,40,.4)","rgba(0,0,0,.6)")
# logo cream
s = s.replace("brand/wordmark_indigo.png","brand/wordmark_cream.png")
# CTA -> gold, dark text
s = s.replace("linear-gradient(135deg,#2f3a86,#232c66)","linear-gradient(135deg,#e6c874,#c99a3c)")
s = s.replace("color:#fff;font-weight:800;font-size:21px","color:#10201c;font-weight:800;font-size:21px")  # desktop cta
s = s.replace("color:#fff;font-weight:800;font-size:36px","color:#10201c;font-weight:800;font-size:36px")  # mobile cta
s = s.replace("box-shadow:0 14px 26px rgba(35,44,102,.3)","box-shadow:0 14px 26px rgba(120,90,30,.4)")
s = s.replace("box-shadow:0 16px 30px rgba(35,44,102,.32)","box-shadow:0 16px 30px rgba(120,90,30,.42)")
s = s.replace(".cta a .arw{color:#e7c877",".cta a .arw{color:#10201c")
open(outf,"w").write(s)
print("wrote",outf)
