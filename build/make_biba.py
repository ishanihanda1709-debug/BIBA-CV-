import re, sys, os, shutil
SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT+'/assets', exist_ok=True)
h=open(SRC+'/index.html').read(); css=open(SRC+'/style.css').read(); js=open(SRC+'/app.js').read()

MAROON='#8B1E3F'; GOLD='#C9A05A'; GOLDL='#E3C27E'
cmap={'#E21B23':MAROON,'#e21b23':MAROON,'#B8141B':'#6B1530','#ffb020':GOLDL,'#ff8a3d':GOLD,'#fbfafa':'#FBF7F1','#141414':'#2A1A1E',
 '#736969':'#76655F','#907879':'#8A766C','#eae6e6':'#EDE3D6','#f8f5f5':'#F7F0E6','#f5f1f1':'#F5ECE0','#f4f0f0':'#F4ECE1','#f6f3f3':'#F6EFE5',
 '#f2ecec':'#F3E9DB','#ede7e7':'#ECE2D4','#e5e0e0':'#E8DCCB','#e7e1e1':'#E9DFD0','#e0dbdb':'#E3D6C4','#e1dcdc':'#E4D8C7','#e1c7c8':'#E3CDB8',
 '#d39fa1':GOLD,'#b88d8f':'#B89A7A','#bba3a4':'#C8B096','#ae9495':'#B09A86','#6a5859':'#7A5A4C','#f5f0f0':'#F5EDE1','#e2dddd':'#E5D9C8',
 '#0f1b3de8':'#2A1A1EE0','#e7ebff':'#F5ECE0','#fbf8ed':'#FBF3E4','#6d6767':'#76655F'}
def recolor(s):
    for k,v in cmap.items(): s=re.sub(re.escape(k)+r'(?![0-9A-Fa-f])',v,s,flags=re.I)
    return s

# ---------- CSS ----------
css=recolor(css)
css=css.replace("--serif:'DM Sans',Arial,sans-serif;--sans:'DM Sans',Arial,sans-serif","--serif:'Cormorant Garamond',Georgia,serif;--sans:'Jost',Arial,sans-serif;--gold:#C9A05A")
css=css.replace("/* CARS24 retheme */","/* BIBA retheme */")
css=css.replace(".held-speaker{",".held-kurta{").replace(".walking .held-speaker,.intro-car .held-speaker",".walking .held-kurta,.intro-car .held-kurta").replace(".motion-paused .held-speaker",".motion-paused .held-kurta").replace("@media(prefers-reduced-motion:reduce){.held-speaker","@media(prefers-reduced-motion:reduce){.held-kurta")
css=css.replace(".cars-cta",".biba-cta").replace("#building-boat","#building-biba")
css+="""
/* BIBA look: ivory, maroon, antique gold, serif display */
h1,h2,h3,h4,.metric-row strong,.footer-name,.game-card h3{font-weight:600;letter-spacing:-.01em}
.intro h1{letter-spacing:-.015em;line-height:1}
em{font-style:italic;color:var(--coral)}
.monogram{font-family:var(--serif);font-style:italic;font-weight:600;background:var(--coral);color:#F3DDB0}
.monogram span{color:var(--gold)}
.header{background:var(--paper);border-bottom:0;position:relative}
.header:after{content:'';position:absolute;left:0;right:0;bottom:-6px;height:6px;background:radial-gradient(circle at 50% 0,var(--gold) 2px,transparent 2.5px) 0 0/18px 6px repeat-x;opacity:.75}
.header nav a{letter-spacing:.06em;text-transform:uppercase;font-size:11px}
.nav-contact{border-radius:2px}
.eyebrow{letter-spacing:2.4px;color:#7A5A4C}
.hand-note{font-family:var(--serif);font-style:italic;color:var(--gold);font-weight:600;font-size:22px}
.stop-nav a.active{background:#F5ECE0;border-top-color:var(--coral)}
.chapter-head h2,.lab h2,.about h2{font-size:56px}
.metric-row strong{font-size:36px;color:var(--coral)}
.fit-grid article{background:#fff;border-color:#E8DCCB;border-top:3px solid var(--coral);border-radius:2px}
.fit-grid h3{font-size:27px}
.fit-proof span{border-radius:2px}
.fit-grid article.fit-honest{border-top-color:var(--gold)}
.biba-cta{border-radius:2px;background:var(--coral);background-image:radial-gradient(circle,#ffffff14 1.5px,transparent 2px);background-size:16px 16px}
.biba-cta p{font-family:var(--serif);font-size:24px;font-weight:600;font-style:italic}
.biba-cta .text-link:hover{color:#F3DDB0;border-color:#F3DDB0}
.lab{background:#F5ECE0}
.game-card{box-shadow:6px 8px 0 #E9DFD0;border-radius:2px}
.game-feedback{border-left-color:var(--coral)}
.contact{background:var(--coral);background-image:radial-gradient(circle,#ffffff12 1.5px,transparent 2px);background-size:18px 18px}
.contact h2 em,.contact h2>span{color:#F3DDB0}
.contact-bottom a:hover{color:#F3DDB0}
.text-link{letter-spacing:.04em}
.intro-screen{background:var(--coral);background-image:radial-gradient(circle,#ffffff12 1.5px,transparent 2px);background-size:20px 20px}
.intro-line{font-family:var(--serif);font-weight:600;letter-spacing:-.01em}
.intro-me #typeMe b{color:#F3DDB0;font-style:italic;font-weight:600}
.caret{background:#F3DDB0}
.intro-go{color:var(--coral);border-radius:2px;letter-spacing:.05em}
.intro-go:hover{background:#F3DDB0;color:#2A1A1E}
.intro-road{background:repeating-linear-gradient(90deg,#F3DDB077 0 18px,transparent 18px 36px)}
.toran circle{transform-box:fill-box;transform-origin:center}
.walking .held-kurta{animation:sway .5s ease-in-out infinite alternate}
.dupatta{transform-box:fill-box;transform-origin:top center}
.walking .dupatta,.intro-car .dupatta{animation:flutter .5s ease-in-out infinite alternate}
@keyframes flutter{from{transform:rotate(-3deg)}to{transform:rotate(4deg)}}
.motion-paused .dupatta{animation:none!important}
@media(prefers-reduced-motion:reduce){.dupatta{animation:none!important}}
.intro-car .kb{fill:#F3DDB0}.intro-car .ks{stroke:#F3DDB0}.intro-car .dupatta{fill:#D23C6E}
@media(max-width:700px){.chapter-head h2,.lab h2,.about h2{font-size:42px}.header nav a{font-size:10px}}
"""

# ---------- HTML ----------
h=recolor(h)
h=h.replace('family=DM+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800','family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Jost:wght@400;500;600;700')
# scene ground/road/bubble to warm tones
for a,b in [('#8fa6e8','#E8B08A'),('#3d56b5','#A65B3A'),('#dfe6ff','#FBEBDD'),('#5a6fc4','#B96E4C'),('#7f98e0','#D9966E'),('#6a82d8','#C97E5A'),('#f3f6ff','#FFF6EE'),('#7a6cf5','#C98A9A'),('#4a3fc0','#8E4A5E'),('#e9e6ff','#F7E6EA'),('#9a8ff7','#D7A3B0'),('#f6f4ff','#FCF4F6'),('#5c52c9','#9E5A6E'),('#6f64e6','#B06F82'),('#7d86a8','#9A8576'),('#e8edff','#F3E9DA'),('#cfd4e6','#E4D6C2'),('#b7c0e6','#DCC8AD'),('#2a3470','#5A2433')]: h=h.replace(a,b)

KURTA_GIRL='''<svg class="girl-kurta" x="-34" y="-112" width="73" height="126" viewBox="-50 -180 110 190" overflow="visible"><ellipse cx="4" cy="1" rx="31" ry="5" fill="#514331" opacity=".14"/><path d="M-20-118Q-40-183 1-179Q39-181 28-118L10-103Z" fill="#342d2d"/><path class="dupatta" d="M-9-124Q-34-96-27-46l7 2Q-24-92-1-120Z" fill="#C9A05A" opacity=".92"/><g class="leg leg-back"><path d="M0-63L-13-29-17-5" fill="none" stroke="#EADBC2" stroke-width="15" stroke-linecap="round"/><path d="M-23-8h16l5 10h-27q-3-9 6-10" fill="#8B1E3F" stroke="#6B1530" stroke-width="1.5"/></g><g class="leg leg-front"><path d="M13-63L18-31 25-6" fill="none" stroke="#F1E5D1" stroke-width="15" stroke-linecap="round"/><path d="M17-8h17l7 10H15q-2-9 2-10" fill="#8B1E3F" stroke="#6B1530" stroke-width="1.5"/></g><path class="ks" d="M-10-114L-26-85-12-71" fill="none" stroke="#8B1E3F" stroke-width="13" stroke-linecap="round"/><path d="M-12-71l7 5" stroke="#cc9870" stroke-width="9" stroke-linecap="round"/><path class="kb" d="M-9-126L15-126Q25-92 33-36Q5-27-27-36Q-18-92-9-126Z" fill="#8B1E3F"/><path d="M-27-36Q5-27 33-36" fill="none" stroke="#E3C27E" stroke-width="3.5"/><path d="M-1-126q6 9 11 0M4-118v14" fill="none" stroke="#E3C27E" stroke-width="1.8"/><g fill="#E3C27E"><circle cx="-6" cy="-92" r="1.4"/><circle cx="8" cy="-84" r="1.4"/><circle cx="20" cy="-70" r="1.4"/><circle cx="-12" cy="-62" r="1.4"/><circle cx="4" cy="-55" r="1.4"/><circle cx="22" cy="-50" r="1.4"/><circle cx="-16" cy="-46" r="1.4"/></g><rect x="-4" y="-137" width="13" height="16" rx="4" fill="#bd8768"/><ellipse cx="5" cy="-151" rx="19" ry="23" fill="#dca780"/><path d="M-15-153q-4-30 25-24 23 8 14 26-3-23-24-13l-15 17" fill="#342d2d"/><path d="M17-151l8 7-8 2" fill="#dca780"/><circle cx="15" cy="-153" r="1.6" fill="#342d2d"/><circle cx="17" cy="-163" r="1.3" fill="#8B1E3F"/><path d="M15-141q5 3 8-1" fill="none" stroke="#8a5248" stroke-width="1.4"/><circle cx="-2" cy="-137" r="2.6" fill="#E3C27E"/><path class="ks" d="M15-114l10 29 16-2" fill="none" stroke="#8B1E3F" stroke-width="12" stroke-linecap="round"/><g class="held-kurta"><path d="M47-92q0-8 5-8t3 5" fill="none" stroke="#7A5A4C" stroke-width="1.8" stroke-linecap="round"/><path d="M47-92L32-81H62Z" fill="none" stroke="#7A5A4C" stroke-width="1.8" stroke-linejoin="round"/><path d="M38-82L28-75 32-68 36-71 33-30Q47-25 61-30L58-71 62-68 66-75 56-82Q47-74 38-82Z" fill="#D23C6E" stroke="#9E1F4E" stroke-width="1"/><path d="M40-81Q47-72 54-81M47-75v14" fill="none" stroke="#F3D79A" stroke-width="1.6"/><path d="M33-35Q47-30 61-35" fill="none" stroke="#F3D79A" stroke-width="3"/><g fill="#F3D79A"><circle cx="40" cy="-58" r="1.3"/><circle cx="54" cy="-62" r="1.3"/><circle cx="46" cy="-48" r="1.3"/><circle cx="55" cy="-44" r="1.3"/><circle cx="39" cy="-42" r="1.3"/></g></g><path d="M40-87l7-5" stroke="#dca780" stroke-width="8" stroke-linecap="round"/><text class="note" x="72" y="-100" font-size="14" fill="#C9A05A">✦</text><text class="note" x="-48" y="-128" font-size="12" fill="#C9A05A">✦</text></svg>'''
h,n=re.subn(r'<svg class="girl-speaker".*?</svg>',lambda m:KURTA_GIRL,h,flags=re.S); assert n==2,n

# BIBA store building
def kurta(cx,y,fill,trim='#E3C27E'):
    return (f'<path d="M{cx-6} {y}l-8 5 3 6 3-2-2 25q10 4 20 0l-2-25 3 2 3-6-8-5q-6 6-12 0Z" fill="{fill}"/>'
            f'<path d="M{cx-6} {y+1}q6 7 12 0M{cx-9} {y+31}q9 4 18 0" fill="none" stroke="{trim}" stroke-width="1.5"/>'
            f'<path d="M{cx} {y-5}v5" stroke="#7A5A4C" stroke-width="1.4"/>')
sc=''.join(f'q{236/32:.3f} 9 {236/16:.3f} 0' for _ in range(16))
arch=lambda x,y,w,hh:f'M{x} {y+hh}v-{hh-w/2}a{w/2} {w/2} 0 0 1 {w} 0v{hh-w/2}Z'
toran=''.join(f'<circle cx="{1452+i*14.5:.1f}" cy="{86+ 0}" r="3.4" fill="{["#E0912F","#E3C27E"][i%2]}"/>' for i in range(0))
garland=''.join(f'<circle cx="{1500+i*11}" cy="{70+ (6*(1-((i-6)/6)**2)):.1f}" r="3" fill="{["#E0912F","#F0B23A"][i%2]}"/>' for i in range(13))
STORE=f'''<g class="building" id="building-biba"><rect x="1448" y="78" width="236" height="142" fill="#FBF3E6" stroke="#8B1E3F" stroke-width="2"/><rect x="1438" y="70" width="256" height="12" fill="#8B1E3F" stroke="#6B1530" stroke-width="2"/><path d="M1448 82h236v4H1448Z" fill="#C9A05A"/><path d="M1448 86{sc}V86Z" fill="#8B1E3F"/><path d="M1566 6l5 8-5 8-5-8Z" fill="#C9A05A"/><rect x="1498" y="22" width="136" height="46" rx="2" fill="#8B1E3F" stroke="#C9A05A" stroke-width="2.5"/><rect x="1504" y="28" width="124" height="34" fill="none" stroke="#E3C27E" stroke-width=".8"/><text x="1566" y="55" text-anchor="middle" font-family="Cormorant Garamond,Georgia,serif" font-size="30" font-weight="700" letter-spacing="7" fill="#F3DDB0">BIBA</text><g class="toran">{garland}</g><g fill="#FFF8EC" stroke="#8B1E3F" stroke-width="2"><path d="{arch(1464,104,44,52)}"/><path d="{arch(1522,104,44,52)}"/><path d="{arch(1580,104,44,52)}"/><path d="{arch(1638,104,34,52)}"/></g>{kurta(1486,126,"#D23C6E")}{kurta(1544,126,"#1F6F6B")}{kurta(1602,126,"#E0912F","#8B1E3F")}<path d="M1655 124v28" stroke="#C9A05A" stroke-width="2"/><rect x="1462" y="164" width="140" height="56" fill="#F7E7D4" stroke="#8B1E3F" stroke-width="2"/><path d="M1462 170h140" stroke="#C9A05A" stroke-width="2"/><circle cx="1490" cy="178" r="5" fill="#dca780"/><path d="M1484 184h12l9 34h-30Z" fill="#8B1E3F"/><path d="M1476 216h28" stroke="#E3C27E" stroke-width="2.5"/><path d="M1486 185q-6 14-4 30" stroke="#E3C27E" stroke-width="3" fill="none"/><g fill="#E9D3B6"><rect x="1520" y="196" width="22" height="7" rx="1"/><rect x="1520" y="189" width="22" height="7" rx="1" fill="#D23C6E"/><rect x="1520" y="182" width="22" height="7" rx="1" fill="#1F6F6B"/><rect x="1552" y="196" width="34" height="22" rx="1" fill="#F3DDB0" stroke="#C9A05A"/><text x="1569" y="210" text-anchor="middle" font-size="7" font-family="Jost,Arial" fill="#8B1E3F">NEW IN</text></g><path d="{arch(1614,160,52,60)}" fill="#8B1E3F" stroke="#6B1530" stroke-width="2"/><path d="{arch(1622,168,36,52)}" fill="#FBE9D0"/><path d="M1640 168v52" stroke="#C9A05A" stroke-width="1.5"/><text x="1566" y="4" class="sign" text-anchor="middle" dy="0"> </text></g>'''
i=h.find('<g class="building" id="building-boat">'); j=h.find('<g fill="#8fd0a8"',i)
h=h[:i]+'<!-- BIBA store -->\n'+STORE+h[j:]
h=h.replace('<!-- boAt store -->\n<!-- BIBA store -->','<!-- BIBA store -->')

# text swaps
R=[
('<meta name="description" content="Ishani Handa\'s journey from school and college to PhonePe, Masters\' Union and on to boAt, built around the Performance Marketing Manager (Marketplace Ads) role.">',
 '<meta name="description" content="Ishani Handa\'s journey from school and college to PhonePe, Masters\' Union and on to BIBA, built around the online marketplace business role.">'),
('<meta name="theme-color" content="'+MAROON+'">','<meta name="theme-color" content="#8B1E3F">'),
('Marketplace Ads · ROAS · ACOS · Share of Search','Myntra · Ajio · Amazon · Flipkart'),
('<small>MARKETPLACE PERFORMANCE</small>','<small>MARKETPLACE BUSINESS</small>'),
('<a href="#boat">boAt</a>','<a href="#biba">BIBA</a>'),
('MARKETPLACE ADS · PERFORMANCE · GROWTH','ONLINE MARKETPLACES · REVENUE · GROWTH'),
('<h1>Every rupee tested.<br>Every click <em>counted</em><span class="coral">.</span></h1>','<h1>Every listing sharp.<br>Every rupee <em>earning</em><span class="coral">.</span></h1>'),
('I run campaigns on the numbers that matter, from<br class="desktop-only"> placements and creative to ROAS, conversion and share of voice.',
 'I grow revenue on the numbers that matter, from<br class="desktop-only"> campaigns and pricing to conversion, margin and platform partners.'),
('every chapter<br>adds a little something','every chapter<br>adds a new thread'),
('A LITTLE WALK, THEN SOME MUSIC, THROUGH MY WORLD','A LITTLE WALK THROUGH MY WORLD, ENDING AT BIBA'),
('Masters’ Union and the boAt store, with Ishani walking to the current chapter, a boAt speaker in hand at the last stop',
 'Masters’ Union and the BIBA store, with Ishani walking to the current chapter, dressed in a kurta and carrying a new kurta to the last stop'),
('<a href="#boat" data-stop="4"><span>05</span><b>boAt</b><small>Marketplace ads fit</small></a>','<a href="#biba" data-stop="4"><span>05</span><b>BIBA</b><small>Marketplace fit</small></a>'),
('<span class="scope-note">Illustrative exercise · No real boAt data</span>','<span class="scope-note">Illustrative exercise · No real BIBA data</span>'),
('<h2>Your move,<br><em>marketplace marketer.</em></h2><p>A tiny marketplace-ads game.','<h2>Your move,<br><em>marketplace manager.</em></h2><p>A tiny marketplace game.'),
('At Masters’ Union, I’m taking that experience into new businesses, and next I’d like to take it to boAt.','At Masters’ Union, I’m taking that experience into new businesses, and next I’d like to take it to BIBA.'),
('I’m looking for a marketplace performance role where I own a category’s ad spend, fight for share of search, run a steady roadmap of tests, and move budget to whatever proves it returns.',
 'I’m looking for a marketplace role where I own revenue across platforms, keep the catalogue, pricing and stock in shape, plan promotions with platform partners, and back every call with the numbers.'),
('<h2>Ready to turn up<br>the <em>volume?</em><span>↗</span></h2>','<h2>Ready to grow BIBA<br>on every <em>platform?</em><span>↗</span></h2>'),
('So does a good playlist.','So does a good kurta.'),
]
for a,b in R:
    assert a in h,a[:60]; h=h.replace(a,b)

CH5='''<section class="chapter biba-chapter" id="biba" data-chapter="4"><div class="chapter-head"><p class="eyebrow">05 / THE NEXT CHAPTER</p><h2>BIBA.<br><em>Where I’d like to grow next.</em></h2><p class="chapter-dates">Online Marketplaces · Myntra, Ajio, Amazon, Flipkart · Lateral, 2–6 years</p><p class="lead">The role drives BIBA’s online marketplace business: strategy for revenue and profitability, platform relationships and promotions, catalogue, pricing, inventory and assortment, and the analysis behind them, working with merchandising, marketing, supply chain and finance. Here is the brief, and the proof I’d bring to it.</p></div>
<div class="fit-grid">
<article><span class="small-label">THE BRIEF · DRIVE THE MARKETPLACE BUSINESS ACROSS MYNTRA, AJIO, AMAZON, FLIPKART</span><h3>Revenue owned. Plan delivered.</h3><p>At PhonePe I owned revenue for a 30+ brand portfolio, delivering ₹2 Cr+ a month and 100% of the annual operating plan. A root-cause analysis showed which placements were yielding, and moving spend to them drove 10× growth in a key account: the same call as backing the styles and channels that sell.</p><div class="fit-proof"><span><b>₹2 Cr+</b> monthly revenue</span><span><b>100%</b> of AOP</span><span><b>10×</b> key-account growth</span></div></article>
<article><span class="small-label">THE BRIEF · SALES AND MARKETING STRATEGY FOR REVENUE AND PROFITABILITY</span><h3>Growth that keeps its margin.</h3><p>Took ROAS up to 4× for brands like Lakmé, Airtel and Country Delight by tracking CAC and end-funnel conversion, not just clicks. At Slay Pop Cult I priced for ~50% average margin. For Prolectro, our team set a 35% repeat-purchase gate before any expansion: growth only where the unit economics hold.</p><div class="fit-proof"><span><b>Up to 4×</b> ROAS</span><span><b>~50%</b> margin</span><span><b>35%</b> repeat gate</span></div></article>
<article><span class="small-label">THE BRIEF · PLATFORM RELATIONSHIPS, BUSINESS PLANNING, PROMOTIONS, VISIBILITY</span><h3>I’ve sat on the platform’s side of the table.</h3><p>PhonePe was the platform, and brands were my partners: 93% came back for repeat campaigns. For Amazon’s Great Indian Festival I delivered 10+ launches in 2 days, and cut launch turnaround from 2 days to 24 hours. I also secured 100% on-time delivery from 10+ agencies like GroupM and built the pitch decks that helped Sales close.</p><div class="fit-proof"><span><b>93%</b> brands retained</span><span><b>10+</b> sale launches in 2 days</span><span><b>10+</b> agencies</span></div></article>
<article><span class="small-label">THE BRIEF · CATALOGUE, LISTINGS, PRICING, INVENTORY, ASSORTMENT</span><h3>From SKU research to the shelf.</h3><p>At Slay Pop Cult I researched sellable SKUs, built a 4-market supplier base across Gujarat, Mumbai, Chandni Chowk and China, set prices and sold to 350+ customers for ₹3L+ in revenue. For Prolectro we planned the assortment itself: a ₹129 trial sachet, then multipacks built for the second purchase.</p><div class="fit-proof"><span><b>4</b> sourcing markets</span><span><b>350+</b> customers</span><span><b>₹3L+</b> revenue</span></div></article>
<article><span class="small-label">THE BRIEF · SALES, CONVERSION, MARKET TRENDS, CONSUMER BEHAVIOUR</span><h3>Reports that end in an action.</h3><p>Built a KPI dashboard and MIS on spend gaps that improved efficiency by 30% with zero errors. Hypothesis-driven A/B tests added 40% campaign efficiency, new formats took CTR from 0.2% to 1.5%, and carrying winners across categories lifted conversion in 5+ of them. A BBA in Marketing, with consumer behaviour at its core, and a 101-person survey behind Prolectro. Advanced Excel is where I work.</p><div class="fit-proof"><span><b>30%</b> efficiency, 0 errors</span><span><b>0.2% → 1.5%</b> CTR</span><span><b>5+</b> categories lifted</span></div></article>
<article><span class="small-label">THE BRIEF · MERCHANDISING, MARKETING, SUPPLY CHAIN, FINANCE</span><h3>Cross-functional by habit.</h3><p>At PhonePe I worked with design on new formats, with Data Science on segments for 10+ brands, and with Sales on pitches, and mentored new joiners for 6 months. Running Slay Pop Cult meant doing every seat myself: sourcing and stock, pricing and margins, and setting up the stall people bought from.</p><div class="fit-proof"><span><b>Design · Data · Sales</b></span><span><b>6 months</b> mentoring</span><span><b>Founder</b> ops</span></div></article>
<article><span class="small-label">GOOD TO HAVE · CONSUMER BRANDS AND SALE SEASONS</span><h3>Consumer-first, and festive-season tested.</h3><p>Two years running campaigns for consumer brands across beauty, telecom and D2C, including peak sale events like the Great Indian Festival. Before that, Foxymoron, where I shaped pitch and GTM direction for 5+ brands. And a Gen Z lifestyle brand of my own, where every rupee of revenue came from understanding what shoppers want to buy.</p><div class="fit-proof"><span><b>2 yrs</b> full-time</span><span><b>D2C</b></span><span><b>Sale events</b></span></div></article>
<article class="fit-honest"><span class="small-label">WHAT I’D RAMP UP ON</span><h3>Running seller panels, and the apparel playbook.</h3><p>My marketplace experience is from the platform side: I know how a platform plans visibility, promotions and partner KPIs from the inside. What’s new is the seller side of Myntra, Ajio, Amazon and Flipkart: catalogue uploads, size-wise inventory and sell-through, returns, and each platform’s trading model. In my first weeks I’d learn BIBA’s top styles by channel, the event calendar, and where margin is won or lost.</p><div class="fit-proof"><span><b>Same levers</b></span><span><b>New seller panels</b></span></div></article>
</div>
<div class="biba-cta"><p>Ready to grow BIBA, one platform at a time.</p><a class="text-link" href="#contact">Let’s talk <span>↗</span></a></div></section>'''
i=h.find('<section class="chapter cars-chapter"'); j=h.find('</section>',i)+len('</section>')
h=h[:i]+CH5+h[j:]
assert 'boAt' not in h, [m.start() for m in re.finditer('boAt',h)]
open(OUT+'/index.html','w').write(h)
open(OUT+'/style.css','w').write(css)

# ---------- JS ----------
js=js.replace("'ROAS · ACOS · SOV'","'GMV · Margin · Sell-through'").replace("'boat']","'biba']")
js=js.replace("option.style.background='#e7ebff'","option.style.background='#F5ECE0'")
js=js.replace('Hi boAt,','Hi BIBA,').replace('// Opening: "Hi boAt, I’m Ishani."','// Opening: "Hi BIBA, I’m Ishani."')
i=js.find('const rounds=['); j=js.find('];',i)+2
ROUNDS=r'''const rounds=[
 {title:'A sale is five days out on Myntra.',brief:'A big sale event is coming. You can fund deeper discounts and extra visibility, but not for the whole catalogue. Where does it go?',choices:[['Discount the whole catalogue evenly','It looks generous, but thin coverage on every style means none of them wins visibility, and margin drops on styles that would have sold anyway.'],['Back hero styles with full size depth','Pick the styles with proven conversion and enough stock across sizes, fund visibility and offers on them, and keep fresh styles ready to replace them as they sell out.'],['Push the slow movers hardest','Clearing old stock matters, but a sale is the best traffic of the season. Leading with your weakest styles wastes it.']],takeaway:'Back the styles you can actually ship.'},
 {title:'A kurta set is a hit. Sizes M and L are running out.',brief:'It is your top seller on Ajio this week, ads are running, and the core sizes will run out in four days. What do you do?',choices:[['Keep the ads running at full spend','You pay for traffic that lands on a broken size range. Shoppers bounce, conversion falls, and the listing loses rank just as it peaked.'],['Rebalance stock, redirect the spend','Work with supply chain to move stock in from slower channels or speed up a reorder. Meanwhile, move ad spend to similar styles with full sizes so the demand is not wasted.'],['Raise the price to slow sales down','It protects stock for now, but it chips away at conversion and rank on your best style, and it does not solve next week’s demand.']],takeaway:'Ads can’t sell what isn’t in stock.'},
 {title:'A platform asks for an extra 10% off.',brief:'Amazon wants BIBA to fund an extra 10% discount to feature it in a festive deal. Revenue would jump. What’s your answer?',choices:[['Say yes, the visibility is worth it','The spike in revenue can hide that every order now earns less, or even loses money once returns and fees come in.'],['Model the margin, then counter','Work out contribution after the discount, fees and returns with finance. Offer the deal on selected styles or a bundle where the numbers still work, and agree the visibility you get in return.'],['Decline, and protect the price','Margin stays safe, but you lose a top slot in the busiest week of the season, and the relationship with the platform team takes a hit.']],takeaway:'Grow revenue without giving away margin.'}
];'''
js=js[:i]+ROUNDS+js[j:]
js=js.replace('Watch total sales, not just ad sales. Win rank before the peak. Defend share of search where it counts. Move budget to what is incremental.',
 'Back the styles that sell and can ship. Keep sizes in stock before you buy traffic. Negotiate for visibility, but protect the margin.')
assert 'boAt' not in js
open(OUT+'/app.js','w').write(js)
open(OUT+'/assets/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#8B1E3F"/><text x="31" y="43" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-weight="700" font-size="30" fill="#F3DDB0">ih</text><path d="M50 9l4 6-4 6-4-6Z" fill="#C9A05A"/></svg>')
print('ok')
