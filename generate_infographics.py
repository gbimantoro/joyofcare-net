#!/usr/bin/env python3
"""Generate infographics for ~112 articles (2/3 of 168) based on article content.
Extracts key data from 'Penting dipahami', numbered steps, and FAQ sections.
"""
import os
import re
import html

# Brand palette
BRAND = {
    "primary": "#00bf63",
    "primary_dark": "#007A3D",
    "accent": "#FC9000",
    "accent_light": "#FFA940",
    "teal": "#0E7490",
    "light": "#7ED957",
    "bg_light": "#EFFBF4",
    "bg_white": "#F4FAF6",
    "text_dark": "#1A1A2E",
    "text_muted": "#475569",
    "white": "#FFFFFF",
}

ARTICLES_DIR = "/home/gobeam/Projects/joyofcare-web/content-source/articles"
OUT_DIR = "/home/gobeam/Projects/joyofcare-web/assets/infographics"

os.makedirs(OUT_DIR, exist_ok=True)

def escape_xml(text):
    return html.escape(text, quote=True)

def extract_infographic_data(filepath):
    """Extract structured data from article for infographic generation."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title from frontmatter
    title_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Artikel"

    # Extract primary_keyword
    kw_match = re.search(r'^primary_keyword:\s*(.+)$', content, re.MULTILINE)
    primary_kw = kw_match.group(1).strip() if kw_match else ""

    # Extract category
    cat_match = re.search(r'^category:\s*(.+)$', content, re.MULTILINE)
    category = cat_match.group(1).strip() if cat_match else ""

    # Extract "Penting dipahami" bullets
    penting_section = []
    if "Penting dipahami" in content:
        idx = content.find("Penting dipahami")
        section = content[idx:idx+2000]
        bullets = re.findall(r'[-*]\s*(.+)', section)
        # Clean HTML tags and entities
        clean_bullets = []
        for b in bullets[:5]:
            b = re.sub(r'<[^>]+>', '', b)  # Remove HTML tags
            b = html.unescape(b)  # Decode entities
            b = b.strip()
            if b:
                clean_bullets.append(escape_xml(b))
        penting_section = clean_bullets

    # Extract numbered steps
    steps = []
    step_patterns = [
        r'\*\*\d+\.\s*([^*]+)\*\*',
        r'\*\*Langkah \d+[:\-]\s*([^*]+)\*\*',
        r'<h3>\d+\.\s*(.+)</h3>',
    ]
    for pattern in step_patterns:
        matches = re.findall(pattern, content)
        if matches:
            steps = []
            for m in matches[:6]:
                m = re.sub(r'<[^>]+>', '', m)
                m = html.unescape(m)
                steps.append(escape_xml(m.strip()))
            break

    if not steps:
        bold_matches = re.findall(r'\*\*([^*]{10,80})\*\*', content)
        steps = []
        for m in bold_matches[:6]:
            if not m.startswith(('Penting', 'Highlights', 'Key', 'Cara', 'Tips')):
                m = re.sub(r'<[^>]+>', '', m)
                m = html.unescape(m)
                steps.append(escape_xml(m.strip()))

    # Extract FAQ questions
    faqs = []
    faq_section = re.search(r'FAQ.*?(?=\n\n|\n[A-Z]|$)', content, re.DOTALL | re.IGNORECASE)
    if faq_section:
        faq_text = faq_section.group(0)
        q_matches = re.findall(r'Q:\s*(.+)', faq_text)
        a_matches = re.findall(r'A:\s*(.+)', faq_text)
        for q, a in zip(q_matches[:3], a_matches[:3]):
            q = re.sub(r'<[^>]+>', '', q)
            q = html.unescape(q)
            a = re.sub(r'<[^>]+>', '', a)
            a = html.unescape(a)
            faqs.append((escape_xml(q.strip()), escape_xml(a.strip()[:120])))

    # Extract key stats/numbers
    stats = []
    stat_patterns = [
        r'(\d+(?:\.\d+)?%)\s*(?:pasien|pengguna|kasus|keberhasilan)',
        r'(?:lebih dari|sekitar|approx)\.?\s*(\d+(?:\.\d+)?\s*(?:ribu|juta|persen|%))',
        r'(\d+(?:\.\d+)?)\s*(?:tahun|bulan|minggu|hari)\s*(?:pengalaman|proses|pemulihan)',
    ]
    for pattern in stat_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        stats.extend(matches[:3])

    # Determine infographic type based on content
    infographic_type = "general"
    if any(kw in title.lower() for kw in ['biaya', 'harga', 'perbandingan', 'cost']):
        infographic_type = "cost_comparison"
    elif any(kw in title.lower() for kw in ['cara', 'tips', 'langkah', 'panduan', 'how to']):
        infographic_type = "step_by_step"
    elif any(kw in title.lower() for kw in ['apa', 'apa itu', 'apa yang', 'kenapa', 'mengapa', 'apa saja']):
        infographic_type = "awareness"
    elif any(kw in title.lower() for kw in ['kapan', 'kapan harus', 'when']):
        infographic_type = "decision_guide"
    elif penting_section:
        infographic_type = "key_points"

    return {
        "title": escape_xml(title),
        "primary_kw": escape_xml(primary_kw),
        "category": category,
        "penting": penting_section,
        "steps": steps,
        "faqs": faqs,
        "stats": stats[:3],
        "type": infographic_type,
        "slug": os.path.splitext(os.path.basename(filepath))[0],
    }

def make_header(w, h, title, cat):
    """Generate the common header with defs."""
    primary = BRAND["primary"]
    dark = BRAND["primary_dark"]
    accent = BRAND["accent"]
    accent_light = BRAND["accent_light"]
    teal = BRAND["teal"]
    bg = BRAND["bg_light"]
    bg2 = BRAND["bg_white"]
    text = BRAND["text_dark"]
    muted = BRAND["text_muted"]
    white = BRAND["white"]

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Infografis: {title} - JoyofCare">
  <title>{title} - Joy of Care</title>
  <desc>Infografis ringkas untuk artikel {title} dari JoyofCare.</desc>

  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <linearGradient id="primaryGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{primary}"/>
      <stop offset="100%" stop-color="{dark}"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent}"/>
      <stop offset="100%" stop-color="{accent_light}"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{white}"/>
      <stop offset="100%" stop-color="#F8FCFA"/>
    </linearGradient>
    <linearGradient id="stepGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{primary}"/>
      <stop offset="100%" stop-color="{teal}"/>
    </linearGradient>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="4"/>
      <feOffset dx="0" dy="3"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.1"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="6"/>
      <feOffset dx="0" dy="4"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.15"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <!-- Arrow marker for step flows -->
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{primary}"/>
    </marker>
    <marker id="arrowheadTeal" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{teal}"/>
    </marker>
    <marker id="arrowheadAccent" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{accent}"/>
    </marker>
    <marker id="arrowheadDark" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{dark}"/>
    </marker>
  </defs>

  <rect width="{w}" height="{h}" fill="url(#bgGrad)"/>

  <!-- Top Brand Bar -->
  <rect x="0" y="0" width="{w}" height="80" fill="{primary}"/>
  <text x="60" y="52" font-family="Montserrat, sans-serif" font-size="28" font-weight="700" fill="{white}">Joy of Care</text>
  <text x="{w-60}" y="52" font-family="Inter, sans-serif" font-size="14" fill="{white}" opacity="0.9" text-anchor="end">joyofcare.net</text>

  <!-- Title Area -->
  <g transform="translate(60, 110)">
    <rect x="0" y="0" width="200" height="36" rx="18" fill="{accent}"/>
    <text x="100" y="24" font-family="Inter, Montserrat, sans-serif" font-size="12" font-weight="700" fill="{white}" text-anchor="middle" letter-spacing="1">INFOGRAFIS</text>
    <text x="0" y="90" font-family="Montserrat, Inter, sans-serif" font-size="36" font-weight="800" fill="{text}" style="max-width:960px;">{title}</text>
  </g>
'''

def make_footer(w, h, title, cat):
    """Generate the common footer with CTA and brand."""
    primary = BRAND["primary"]
    dark = BRAND["primary_dark"]
    accent = BRAND["accent"]
    accent_light = BRAND["accent_light"]
    white = BRAND["white"]
    text = BRAND["text_dark"]
    muted = BRAND["text_muted"]

    footer_y = h - 100
    return f'''  <!-- CTA Footer -->
  <g transform="translate(60, {footer_y})">
    <rect x="0" y="0" width="960" height="80" rx="16" fill="url(#primaryGrad)" filter="url(#shadow)"/>
    <text x="480" y="32" font-family="Montserrat, sans-serif" font-size="20" font-weight="700" fill="{white}" text-anchor="middle">Butuh Bantuan Lebih Lanjut?</text>
    <text x="480" y="58" font-family="Inter, sans-serif" font-size="14" fill="{white}" opacity="0.9" text-anchor="middle">Konsultasi Gratis via WhatsApp 📲 08811-118-911</text>
  </g>

  <!-- Bottom Brand -->
  <g transform="translate(60, {h-60})">
    <circle cx="14" cy="14" r="14" fill="{primary}"/>
    <text x="42" y="13" font-family="Montserrat, sans-serif" font-size="18" font-weight="700" fill="{dark}">Joy</text>
    <text x="72" y="13" font-family="Montserrat, sans-serif" font-size="18" font-weight="400" fill="{text}">of Care</text>
    <text x="42" y="30" font-family="Inter, sans-serif" font-size="12" fill="{muted}">Sumber: {title} | Kategori: {cat}</text>
  </g>
</svg>'''

def make_content(data, w, h):
    """Generate content section based on infographic type."""
    title = data["title"]
    cat = data["category"]
    penting = data["penting"]
    steps = data["steps"]
    faqs = data["faqs"]
    stats = data["stats"]
    infotype = data["type"]

    primary = BRAND["primary"]
    dark = BRAND["primary_dark"]
    accent = BRAND["accent"]
    accent_light = BRAND["accent_light"]
    teal = BRAND["teal"]
    bg = BRAND["bg_light"]
    bg2 = BRAND["bg_white"]
    text = BRAND["text_dark"]
    muted = BRAND["text_muted"]
    white = BRAND["white"]

    content_y = 160
    left_margin = 60
    content = ""

    if infotype == "cost_comparison" and (penting or stats):
        content += f'''    <!-- Stat Highlights -->
    <g transform="translate({left_margin}, {content_y})">
'''
        if stats:
            for i, stat in enumerate(stats[:3]):
                x = i * 320
                content += f'''      <g transform="translate({x}, 0)" filter="url(#cardShadow)">
        <rect x="0" y="0" width="300" height="140" rx="16" fill="url(#cardGrad)"/>
        <text x="150" y="45" font-family="Montserrat, sans-serif" font-size="36" font-weight="800" fill="{primary}" text-anchor="middle">{escape_xml(stat)}</text>
        <text x="150" y="85" font-family="Inter, sans-serif" font-size="14" fill="{muted}" text-anchor="middle">Berdasarkan data klinis & survei</text>
        <text x="150" y="115" font-family="Inter, sans-serif" font-size="13" fill="{text}" text-anchor="middle">Konsultasi untuk estimasi akurat</text>
      </g>
'''
        content += '''    </g>
'''
        content_y += 160

    elif infotype == "step_by_step" and steps:
        content += f'''    <!-- Steps Flow -->
    <g transform="translate({left_margin}, {content_y})">
'''
        step_colors = [primary, teal, accent, dark, primary, teal]
        arrow_markers = ["arrowhead", "arrowheadTeal", "arrowheadAccent", "arrowheadDark", "arrowhead", "arrowheadTeal"]
        for i, step in enumerate(steps[:5]):
            x = i * 200
            color = step_colors[i]
            marker = arrow_markers[i]
            content += f'''      <g transform="translate({x}, 0)">
        <circle cx="50" cy="50" r="45" fill="{white}" stroke="{color}" stroke-width="3"/>
        <circle cx="50" cy="50" r="35" fill="{color}"/>
        <text x="50" y="58" font-family="Montserrat, sans-serif" font-size="22" font-weight="800" fill="{white}" text-anchor="middle">{i+1}</text>
        <text x="50" y="120" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="{text}" text-anchor="middle" style="max-width:160px;">{step[:40]}{'...' if len(step) > 40 else ''}</text>
'''
            if i < len(steps[:5]) - 1:
                content += f'''        <path d="M 100 50 Q 125 50 125 50" stroke="{color}" stroke-width="3" fill="none" stroke-dasharray="8,4" marker-end="url(#{marker})"/>
'''
            content += '''      </g>
'''
        content += '''    </g>
'''
        content_y += 180

    elif infotype == "awareness" and penting:
        content += f'''    <!-- Key Points -->
    <g transform="translate({left_margin}, {content_y})">
'''
        for i, point in enumerate(penting[:4]):
            row = i // 2
            col = i % 2
            x = col * 480
            y = row * 150
            content += f'''      <g transform="translate({x}, {y})" filter="url(#cardShadow)">
        <rect x="0" y="0" width="450" height="130" rx="16" fill="url(#cardGrad)"/>
        <circle cx="40" cy="40" r="20" fill="{primary}" opacity="0.15"/>
        <text x="40" y="46" font-family="Montserrat, sans-serif" font-size="20" font-weight="700" fill="{primary}" text-anchor="middle">{i+1}</text>
        <text x="80" y="40" font-family="Montserrat, sans-serif" font-size="16" font-weight="700" fill="{text}">Poin Kunci {i+1}</text>
        <text x="80" y="70" font-family="Inter, sans-serif" font-size="13" fill="{muted}" style="max-width:350px;">{point[:80]}{'...' if len(point) > 80 else ''}</text>
        <text x="80" y="100" font-family="Inter, sans-serif" font-size="12" fill="{accent}" font-weight="600">Baca detail di artikel &rarr;</text>
      </g>
'''
        content += '''    </g>
'''
        content_y += 320

    elif infotype == "decision_guide":
        content += f'''    <!-- Decision Checklist -->
    <g transform="translate({left_margin}, {content_y})">
      <text x="0" y="0" font-family="Montserrat, sans-serif" font-size="22" font-weight="700" fill="{text}">Kapan Harus Konsultasi?</text>
'''
        checks = penting[:6] if penting else [
            "Gejala muncul > 2 minggu",
            "Mengganggu aktivitas harian",
            "Obat bebas tidak membaik",
            "Ada riwayat keluarga",
            "Usia > 60 tahun",
            "Pasca operasi/cedera",
        ]
        for i, check in enumerate(checks):
            y = 35 + i * 40
            content += f'''      <g transform="translate(0, {y})">
        <rect x="0" y="0" width="30" height="30" rx="6" fill="{primary}"/>
        <text x="15" y="21" font-family="Montserrat, sans-serif" font-size="16" font-weight="700" fill="{white}" text-anchor="middle">✓</text>
        <text x="45" y="21" font-family="Inter, sans-serif" font-size="14" fill="{text}">{escape_xml(check)}</text>
      </g>
'''
        content += '''    </g>
'''
        content_y += 300

    else:
        # General: mix of stats, key points, steps
        if stats:
            content += f'''    <!-- Quick Stats -->
    <g transform="translate({left_margin}, {content_y})">
'''
            for i, stat in enumerate(stats[:3]):
                x = i * 320
                content += f'''      <g transform="translate({x}, 0)" filter="url(#cardShadow)">
        <rect x="0" y="0" width="300" height="120" rx="16" fill="url(#cardGrad)"/>
        <text x="150" y="40" font-family="Montserrat, sans-serif" font-size="28" font-weight="800" fill="{primary}" text-anchor="middle">{escape_xml(stat)}</text>
        <text x="150" y="75" font-family="Inter, sans-serif" font-size="13" fill="{muted}" text-anchor="middle">Fakta Cepat</text>
      </g>
'''
            content += '''    </g>
'''
            content_y += 140

        if penting:
            content += f'''    <!-- Penting Dipahami -->
    <g transform="translate({left_margin}, {content_y})">
      <text x="0" y="0" font-family="Montserrat, sans-serif" font-size="20" font-weight="700" fill="{text}">Penting Dipahami</text>
'''
            for i, point in enumerate(penting[:4]):
                y = 35 + i * 50
                content += f'''      <g transform="translate(0, {y})">
        <circle cx="12" cy="12" r="12" fill="{primary}"/>
        <text x="35" y="17" font-family="Inter, sans-serif" font-size="13" fill="{text}" style="max-width:900px;">{point}</text>
      </g>
'''
            content += '''    </g>
'''
            content_y += 220 + len(penting[:4]) * 50

    # FAQ section if available
    if faqs:
        content += f'''    <!-- FAQ -->
    <g transform="translate({left_margin}, {content_y})">
      <text x="0" y="0" font-family="Montserrat, sans-serif" font-size="20" font-weight="700" fill="{text}">Pertanyaan Umum</text>
'''
        for i, (q, a) in enumerate(faqs):
            y = 35 + i * 80
            content += f'''      <g transform="translate(0, {y})" filter="url(#cardShadow)">
        <rect x="0" y="0" width="960" height="70" rx="12" fill="url(#cardGrad)"/>
        <text x="20" y="25" font-family="Inter, sans-serif" font-size="13" font-weight="600" fill="{primary}">Q: {q[:60]}{'...' if len(q) > 60 else ''}</text>
        <text x="20" y="50" font-family="Inter, sans-serif" font-size="12" fill="{muted}">A: {a[:80]}{'...' if len(a) > 80 else ''}</text>
      </g>
'''
        content += '''    </g>
'''
        content_y += 35 + len(faqs) * 80 + 20

    return content


def generate_infographic(data):
    """Generate complete SVG infographic."""
    w, h = 1080, 1350
    title = data["title"]
    cat = data["category"]

    header = make_header(w, h, title, cat)
    content = make_content(data, w, h)
    footer = make_footer(w, h, title, cat)

    return header + content + footer


def main():
    # Collect all article files
    article_files = []
    for cat_dir in os.listdir(ARTICLES_DIR):
        cat_path = os.path.join(ARTICLES_DIR, cat_dir)
        if os.path.isdir(cat_path):
            for f in os.listdir(cat_path):
                if f.endswith('.txt'):
                    article_files.append((cat_dir, os.path.join(cat_path, f)))

    print(f"Found {len(article_files)} articles")

    # Select ~112 articles (2/3) - prioritize those with rich content
    scored = []
    for cat, fpath in article_files:
        data = extract_infographic_data(fpath)
        richness = len(data["penting"]) * 2 + len(data["steps"]) + len(data["faqs"]) * 2 + len(data["stats"])
        scored.append((richness, cat, fpath, data))

    scored.sort(reverse=True, key=lambda x: x[0])

    # Take top 112
    target = min(112, len(scored))
    selected = scored[:target]

    print(f"Generating infographics for {target} articles...")

    generated = 0
    for richness, cat, fpath, data in selected:
        slug = data["slug"]
        fname = f"{slug}-infografis.svg"
        fpath_out = os.path.join(OUT_DIR, fname)

        # Skip if already exists
        if os.path.exists(fpath_out):
            continue

        svg = generate_infographic(data)
        with open(fpath_out, "w", encoding="utf-8") as f:
            f.write(svg)
        generated += 1
        if generated % 20 == 0:
            print(f"  Generated {generated}...")

    print(f"\nDone! Generated {generated} new infographics.")
    print(f"Total in {OUT_DIR}: {len(os.listdir(OUT_DIR))}")

if __name__ == "__main__":
    main()