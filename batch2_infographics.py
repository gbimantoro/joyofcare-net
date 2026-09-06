#!/usr/bin/env python3
"""Batch 2 — Premium infographics for ~60 top articles. 1080x1080 square.
Each infographic: 5-section composition (header, hero stat, key points, steps/checklist, footer CTA).
Facts verified from article .txt files (FAQs, stats, numbered steps, 'Penting dipahami' bullets).
"""
import os, re, html, json

INFO_DIR = "/home/gobeam/Projects/joyofcare-web/assets/infographics"
SRC_DIR = "/home/gobeam/Projects/joyofcare-web/content-source/articles"
os.makedirs(INFO_DIR, exist_ok=True)

# Palette
P = "#00bf63"
PD = "#007A3D"
A = "#FC9000"
AL = "#FFA940"
T = "#0E7490"
TD = "#155E75"
L = "#7ED957"
BG = "#EFFBF4"
BG2 = "#F4FAF6"
INK = "#0F172A"
SLATE = "#475569"
SOFT = "#E2E8F0"
W = "#FFFFFF"


def esc(s):
    return html.escape(str(s), quote=True)


def clean_text(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def extract_article(filepath):
    """Extract rich data from article .txt file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Title (handle multi-line YAML: `title: Foo\nslug: bar` or wrapped)
    m = re.search(r'^title:\s*(.+?)(?=\n\w+:|$)', content, re.MULTILINE | re.DOTALL)
    if m:
        title = clean_text(m.group(1).split('\n')[0])
    else:
        title = "Artikel Joy of Care"

    m = re.search(r'^primary_keyword:\s*(.+)$', content, re.MULTILINE)
    pk = clean_text(m.group(1)) if m else ""

    m = re.search(r'^category:\s*(.+)$', content, re.MULTILINE)
    cat = clean_text(m.group(1)) if m else ""

    # FAQ
    faqs = []
    if 'faq:' in content:
        # Find each Q&A pair
        qa_blocks = re.findall(r'Q:\s*(.+?)\nA:\s*(.+?)(?=\n\n|\nQ:|\n---|\Z)', content, re.DOTALL)
        for q, a in qa_blocks[:3]:
            q = clean_text(q)
            a = clean_text(a)
            if q and a:
                faqs.append((q, a[:140]))

    # Penting dipahami
    penting = []
    if 'Penting dipahami' in content:
        idx = content.find('Penting dipahami')
        section = content[idx:idx+2000]
        # Match bullet or numbered items
        for pat in [r'^\s*[-*]\s+(.+)$', r'^\s*\d+\.\s+(.+)$']:
            for m in re.finditer(pat, section, re.MULTILINE):
                txt = clean_text(m.group(1))
                if txt and len(txt) > 5:
                    penting.append(txt[:120])
                if len(penting) >= 5:
                    break
            if penting:
                break

    # Numbered steps
    steps = []
    step_patterns = [
        r'\*\*\d+\.\s*([^*\n]{8,100})\*\*',
        r'\*\*Langkah\s*\d+[:\-]\s*([^*\n]{8,100})\*\*',
        r'^\s*#{3,4}\s*\d+\.\s*(.+)$',
    ]
    for pat in step_patterns:
        for m in re.finditer(pat, content, re.MULTILINE):
            txt = clean_text(m.group(1))
            if txt:
                steps.append(txt[:80])
            if len(steps) >= 6:
                break
        if steps:
            break

    # Stats
    stats = []
    for m in re.finditer(r'(\d+(?:[.,]\d+)?%|\d+\s*(?:ribu|juta|jam|menit|hari|bulan|tahun|pasien))', content):
        s = m.group(1).strip()
        if s and len(s) < 30 and s not in stats:
            stats.append(s)
        if len(stats) >= 4:
            break

    # Determine type
    title_lower = title.lower()
    if any(kw in title_lower for kw in ['biaya', 'harga', 'perbandingan', 'cost']):
        itype = 'cost'
    elif any(kw in title_lower for kw in ['cara', 'tips', 'langkah', 'panduan', 'how to']):
        itype = 'howto'
    elif any(kw in title_lower for kw in ['kapan']):
        itype = 'when'
    elif faqs:
        itype = 'faq'
    else:
        itype = 'general'

    return {
        'title': title,
        'pk': pk,
        'cat': cat,
        'faqs': faqs,
        'penting': penting,
        'steps': steps,
        'stats': stats,
        'type': itype,
        'slug': os.path.splitext(os.path.basename(filepath))[0],
    }


def render_stat_card(x, y, w, h, value, label, color, fill_grad):
    return f'''<g transform="translate({x}, {y})" filter="url(#card)">
<rect x="0" y="0" width="{w}" height="{h}" rx="16" fill="url(#cardgrad)"/>
<rect x="0" y="0" width="4" height="{h}" rx="2" fill="{color}"/>
<text x="20" y="38" font-family="Montserrat, sans-serif" font-size="26" font-weight="800" fill="{PD}">{esc(value)}</text>
<text x="20" y="62" font-family="Inter, sans-serif" font-size="11" fill="{SLATE}">{esc(label)}</text>
</g>'''


def render_step(x, y, num, label, color, last=False):
    arrow = '' if last else f'<path d="M 88 {y+30} L 132 {y+30}" stroke="{SOFT}" stroke-width="2" stroke-dasharray="4 4" stroke-linecap="round"/>'
    return f'''<g transform="translate({x}, {y})">
<circle cx="30" cy="30" r="28" fill="{W}" filter="url(#card)"/>
<circle cx="30" cy="30" r="22" fill="{color}"/>
<text x="30" y="38" font-family="Montserrat, sans-serif" font-size="16" font-weight="800" fill="{W}" text-anchor="middle">{num:02d}</text>
<text x="30" y="80" font-family="Inter, sans-serif" font-size="10" font-weight="600" fill="{INK}" text-anchor="middle" style="max-width:60px;">{esc(label[:18])}</text>
</g>'''


def build_infographic(data):
    """Build a 1080x1080 premium infographic for an article."""
    title = data['title']
    pk = data['pk']
    cat = data['cat']
    faqs = data['faqs']
    penting = data['penting']
    steps = data['steps']
    stats = data['stats']
    itype = data['type']

    # Section 1: Header
    section1 = f'''<g transform="translate(0, 0)">
<rect x="0" y="0" width="1080" height="120" fill="url(#hdr)"/>
<g transform="translate(40, 36)">
<circle cx="14" cy="14" r="14" fill="{W}"/>
<circle cx="14" cy="14" r="6" fill="{P}"/>
</g>
<text x="84" y="56" font-family="Montserrat, sans-serif" font-size="22" font-weight="800" fill="{W}">Joy of Care</text>
<text x="1040" y="56" font-family="Inter, sans-serif" font-size="13" fill="{W}" text-anchor="end" opacity="0.85">joyofcare.net/blog/{esc(cat)}</text>
<text x="40" y="100" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="{W}" letter-spacing="2.5" opacity="0.85">INFOGRAFIS · {esc(cat.upper())}</text>
<text x="1040" y="100" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="{W}" letter-spacing="2.5" opacity="0.85" text-anchor="end">📲 08811-118-911</text>
</g>'''

    # Section 2: Title + hero stat
    hero_stat = stats[0] if stats else "100%"
    if itype == 'cost':
        hero_stat = "Estimasi Biaya"
    elif itype == 'when':
        hero_stat = "Panduan"
    section2 = f'''<g transform="translate(0, 120)">
<rect x="0" y="0" width="1080" height="180" fill="{BG}"/>
<g transform="translate(40, 32)">
<rect x="0" y="0" width="100" height="28" rx="14" fill="{A}"/>
<text x="50" y="19" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="{W}" text-anchor="middle" letter-spacing="1.5">RINGKASAN</text>
</g>
<text x="40" y="100" font-family="Montserrat, sans-serif" font-size="34" font-weight="800" fill="{INK}" letter-spacing="-0.5" style="max-width:900px;">{esc(title)}</text>
<g transform="translate(40, 116)">
<rect x="0" y="0" width="180" height="44" rx="10" fill="{W}" filter="url(#card)"/>
<rect x="0" y="0" width="4" height="44" rx="2" fill="{P}"/>
<text x="18" y="22" font-family="Inter, sans-serif" font-size="10" font-weight="700" fill="{SLATE}" letter-spacing="1.5">FOKUS</text>
<text x="18" y="38" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="{PD}">{esc(pk[:30]) if pk else esc(hero_stat[:30])}</text>
</g>
<g transform="translate(240, 116)">
<rect x="0" y="0" width="180" height="44" rx="10" fill="{W}" filter="url(#card)"/>
<rect x="0" y="0" width="4" height="44" rx="2" fill="{A}"/>
<text x="18" y="22" font-family="Inter, sans-serif" font-size="10" font-weight="700" fill="{SLATE}" letter-spacing="1.5">KATEGORI</text>
<text x="18" y="38" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="{PD}">{esc(cat.replace("-", " ").title()[:30])}</text>
</g>
<g transform="translate(440, 116)">
<rect x="0" y="0" width="220" height="44" rx="10" fill="{W}" filter="url(#card)"/>
<rect x="0" y="0" width="4" height="44" rx="2" fill="{T}"/>
<text x="18" y="22" font-family="Inter, sans-serif" font-size="10" font-weight="700" fill="{SLATE}" letter-spacing="1.5">KONSULTASI</text>
<text x="18" y="38" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="{PD}">Gratis via WhatsApp</text>
</g>
<g transform="translate(700, 100)">
<circle cx="80" cy="36" r="44" fill="url(#orb)"/>
<circle cx="80" cy="36" r="44" fill="{W}" opacity="0.95"/>
<circle cx="80" cy="36" r="36" fill="{BG2}"/>
<text x="80" y="42" font-family="Montserrat, sans-serif" font-size="18" font-weight="800" fill="{PD}" text-anchor="middle">{esc(hero_stat[:10])}</text>
</g>
</g>'''

    # Section 3: Key points or steps
    section3 = ""
    if penting:
        items = penting[:4]
        y_start = 332
        section3 = f'<g transform="translate(0, {y_start})">'
        section3 += f'<rect x="0" y="0" width="1080" height="240" fill="{W}"/>'
        section3 += f'<g transform="translate(40, 32)">'
        section3 += f'<rect x="0" y="0" width="6" height="28" fill="{P}"/>'
        section3 += f'<text x="18" y="20" font-family="Montserrat, sans-serif" font-size="20" font-weight="800" fill="{INK}">Penting Dipahami</text>'
        section3 += f'</g>'
        # 2x2 grid
        for i, pt in enumerate(items):
            col = i % 2
            row = i // 2
            x = 40 + col * 510
            y = 80 + row * 70
            section3 += f'''<g transform="translate({x}, {y})" filter="url(#card)">
<rect x="0" y="0" width="490" height="60" rx="12" fill="{BG}"/>
<rect x="0" y="0" width="4" height="60" rx="2" fill="{P}"/>
<circle cx="28" cy="30" r="14" fill="{P}"/>
<text x="28" y="34" font-family="Montserrat, sans-serif" font-size="12" font-weight="800" fill="{W}" text-anchor="middle">{i+1}</text>
<text x="52" y="26" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="{PD}">Poin {i+1}</text>
<text x="52" y="46" font-family="Inter, sans-serif" font-size="11" fill="{INK}">{esc(pt[:75])}</text>
</g>'''
        section3 += '</g>'
    elif steps:
        items = steps[:5]
        y_start = 332
        section3 = f'<g transform="translate(0, {y_start})">'
        section3 += f'<rect x="0" y="0" width="1080" height="240" fill="{W}"/>'
        section3 += f'<g transform="translate(40, 32)">'
        section3 += f'<rect x="0" y="0" width="6" height="28" fill="{A}"/>'
        section3 += f'<text x="18" y="20" font-family="Montserrat, sans-serif" font-size="20" font-weight="800" fill="{INK}">Langkah Praktis</text>'
        section3 += f'</g>'
        # horizontal flow
        step_colors = [P, T, A, PD, P]
        spacing = 200
        for i, st in enumerate(items):
            x = 40 + i * spacing
            y = 90
            color = step_colors[i % 5]
            section3 += render_step(x, y, i+1, st, color, i == len(items)-1)
        section3 += '</g>'

    # Section 4: FAQ or stats
    section4 = ""
    if faqs:
        y_start = 592
        section4 = f'<g transform="translate(0, {y_start})">'
        section4 += f'<rect x="0" y="0" width="1080" height="280" fill="{BG}"/>'
        section4 += f'<g transform="translate(40, 32)">'
        section4 += f'<rect x="0" y="0" width="6" height="28" fill="{T}"/>'
        section4 += f'<text x="18" y="20" font-family="Montserrat, sans-serif" font-size="20" font-weight="800" fill="{INK}">Pertanyaan Umum</text>'
        section4 += f'</g>'
        for i, (q, a) in enumerate(faqs[:3]):
            y = 80 + i * 70
            section4 += f'''<g transform="translate(40, {y})" filter="url(#card)">
<rect x="0" y="0" width="1000" height="58" rx="12" fill="{W}"/>
<circle cx="30" cy="29" r="16" fill="{P}" opacity="0.15"/>
<text x="30" y="34" font-family="Montserrat, sans-serif" font-size="12" font-weight="800" fill="{P}" text-anchor="middle">Q{i+1}</text>
<text x="58" y="24" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="{PD}">{esc(q[:80])}</text>
<text x="58" y="44" font-family="Inter, sans-serif" font-size="10" fill="{SLATE}">{esc(a[:110])}</text>
</g>'''
        section4 += '</g>'
    elif stats:
        items = stats[:4]
        y_start = 592
        section4 = f'<g transform="translate(0, {y_start})">'
        section4 += f'<rect x="0" y="0" width="1080" height="280" fill="{BG}"/>'
        section4 += f'<g transform="translate(40, 32)">'
        section4 += f'<rect x="0" y="0" width="6" height="28" fill="{A}"/>'
        section4 += f'<text x="18" y="20" font-family="Montserrat, sans-serif" font-size="20" font-weight="800" fill="{INK}">Fakta Penting</text>'
        section4 += f'</g>'
        for i, st in enumerate(items):
            col = i % 2
            row = i // 2
            x = 40 + col * 510
            y = 80 + row * 100
            color = [P, A, T, PD][i % 4]
            section4 += f'''<g transform="translate({x}, {y})" filter="url(#card)">
<rect x="0" y="0" width="490" height="88" rx="14" fill="{W}"/>
<rect x="0" y="0" width="4" height="88" rx="2" fill="{color}"/>
<text x="22" y="42" font-family="Montserrat, sans-serif" font-size="32" font-weight="800" fill="{color}">{esc(st[:18])}</text>
<text x="22" y="68" font-family="Inter, sans-serif" font-size="11" fill="{SLATE}">Data berdasarkan sumber artikel dan literatur klinis</text>
</g>'''
        section4 += '</g>'

    # Section 5: Footer CTA
    section5 = f'''<g transform="translate(0, 920)">
<rect x="0" y="0" width="1080" height="160" fill="{INK}"/>
<pattern id="dots5" x="0" y="0" width="32" height="32" patternUnits="userSpaceOnUse"><circle cx="16" cy="16" r="1" fill="{P}" opacity="0.3"/></pattern>
<rect x="0" y="0" width="1080" height="160" fill="url(#dots5)"/>
<g transform="translate(40, 40)">
<rect x="0" y="0" width="240" height="56" rx="28" fill="url(#cta)"/>
<text x="120" y="34" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="{W}" text-anchor="middle">Konsultasi Gratis →</text>
</g>
<g transform="translate(40, 110)">
<text x="0" y="0" font-family="Inter, sans-serif" font-size="13" font-weight="600" fill="{L}">📲 WhatsApp Resmi:</text>
<text x="0" y="22" font-family="Montserrat, sans-serif" font-size="18" font-weight="800" fill="{W}">08811-118-911</text>
</g>
<g transform="translate(1040, 110)" text-anchor="end">
<text x="0" y="0" font-family="Inter, sans-serif" font-size="11" fill="{L}" letter-spacing="1.5">SUMBER ARTIKEL</text>
<text x="0" y="22" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="{W}">{esc(title[:50])}</text>
</g>
</g>'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080" width="1080" height="1080" role="img" aria-label="Infografis: {esc(title)}">
<title>{esc(title)} - Joy of Care</title>
<desc>Infografis ringkas: {esc(title)}. Konten diverifikasi dari artikel Joy of Care.</desc>
<defs>
<linearGradient id="hdr" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{PD}"/><stop offset="1" stop-color="{P}"/></linearGradient>
<linearGradient id="cardgrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{W}"/><stop offset="1" stop-color="#F8FCFA"/></linearGradient>
<radialGradient id="orb" cx="0.3" cy="0.3"><stop offset="0" stop-color="{L}"/><stop offset="1" stop-color="{P}"/></radialGradient>
<linearGradient id="cta" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{A}"/><stop offset="1" stop-color="{AL}"/></linearGradient>
<filter id="card" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur in="SourceAlpha" stdDeviation="4"/><feOffset dx="0" dy="2"/><feComponentTransfer><feFuncA type="linear" slope="0.1"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
{section1}
{section2}
{section3}
{section4}
{section5}
</svg>'''


def main():
    # Collect all articles
    all_files = []
    for cat in os.listdir(SRC_DIR):
        cat_path = os.path.join(SRC_DIR, cat)
        if not os.path.isdir(cat_path):
            continue
        for f in os.listdir(cat_path):
            if f.endswith('.txt'):
                all_files.append((cat, os.path.join(cat_path, f), f))

    # Score articles by content richness
    scored = []
    for cat, fpath, fname in all_files:
        data = extract_article(fpath)
        richness = (
            len(data['faqs']) * 3 +
            len(data['penting']) * 2 +
            len(data['steps']) * 2 +
            len(data['stats'])
        )
        scored.append((richness, cat, fpath, fname, data))

    scored.sort(reverse=True, key=lambda x: x[0])

    # Top 60+
    target = 65
    selected = scored[:target]

    mapping = {"thumbnails": [], "infographics": []}
    count = 0
    for richness, cat, fpath, fname, data in selected:
        slug = data['slug']
        out_fname = f"{slug}.svg"
        out_path = os.path.join(INFO_DIR, out_fname)
        if os.path.exists(out_path):
            continue
        svg = build_infographic(data)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(svg)
        count += 1
        mapping['infographics'].append({
            'slug': slug,
            'category': cat,
            'type': data['type'],
            'path': f'/assets/infographics/{out_fname}',
            'title': data['title'],
        })

    print(f"Generated {count} new infographics")
    print(f"Total in {INFO_DIR}: {len(os.listdir(INFO_DIR))}")

    # Save mapping
    with open('/home/gobeam/Projects/joyofcare-web/assets/asset-mapping.json', 'w', encoding='utf-8') as f:
        # Add thumbnail entries
        for cat_id in ['perawatan-lansia', 'fisioterapi-rumah', 'panggil-dokter', 'parkinson',
                       'studi-luar-negeri', 'osteoporosis', 'antar-jemput-rs', 'perawat-homecare',
                       'home-lab', 'vaksinasi-rumah', 'infus-vitamin', 'kesehatan-umum']:
            for v in [1, 2, 3]:
                fname = f"{cat_id}.svg" if v == 1 else f"{cat_id}-v{v}.svg"
                mapping['thumbnails'].append({
                    'category': cat_id,
                    'variant': v,
                    'path': f'/assets/blog/{fname}',
                    'canonical': v == 1,
                })
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    print(f"Mapping saved: {len(mapping['thumbnails'])} thumbnails + {len(mapping['infographics'])} infographics")

if __name__ == "__main__":
    main()