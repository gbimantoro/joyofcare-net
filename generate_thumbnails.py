#!/usr/bin/env python3
"""Generate thumbnail variants for all 12 JoyofCare blog categories.
Each category gets 3 variants: Brand Hero, Benefit Scene, Process Steps.
Total: 36 new SVGs at 1200x630.
"""
import os

# Brand palette (logo-truth colors)
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

CATEGORIES = {
    "perawatan-lansia": {
        "name": "Perawatan Lansia",
        "short": "Lansia",
        "icons": ["👴", "🏠", "💚", "🩺", "🤝"],
        "benefits": ["Mandiri", "Nyaman", "Aman", "Dikenal"],
        "steps": ["Assessment", "Rencana", "Perawatan", "Pantau"],
        "trust": ["500+ Pasien", "Tim Geriatri", "Dinkes Terdaftar"],
    },
    "fisioterapi-rumah": {
        "name": "Fisioterapi Rumah",
        "short": "Fisio",
        "icons": ["🏃", "💪", "🏠", "🩹", "🎯"],
        "benefits": ["Pulih Cepat", "Tanpa Ribet", "Personal", "Terukur"],
        "steps": ["Evaluasi", "Program", "Latihan", "Progres"],
        "trust": ["Ahli Fisio", "Sertifikat", "Alat Modern"],
    },
    "panggil-dokter": {
        "name": "Panggil Dokter",
        "short": "Dokter",
        "icons": ["🩺", "🏠", "💊", "🚗", "⏰"],
        "benefits": ["Cepat", "Lengkap", "Hemat", "Tenang"],
        "steps": ["Booking", "Kunjungan", "Diagnosis", "Resep"],
        "trust": ["Dokter Spesialis", "SIP Terverifikasi", "24/7 Ready"],
    },
    "parkinson": {
        "name": "Parkinson",
        "short": "Parkinson",
        "icons": ["🧠", "🤝", "🏃", "💊", "🏠"],
        "benefits": ["Stabil", "Mandiri", "Dukungan", "Teratur"],
        "steps": ["Assessment", "Obat", "Fisio", "Kontrol"],
        "trust": ["Konsultan Saraf", "Protokol EPDA", "Homecare"],
    },
    "studi-luar-negeri": {
        "name": "Studi Luar Negeri",
        "short": "Study Abroad",
        "icons": ["✈️", "🩺", "📋", "💉", "🌏"],
        "benefits": ["Lengkap", "Cepat", "Valid", "Diterima"],
        "steps": ["Cek Syarat", "Medical", "Vaksin", "Surat"],
        "trust": ["Kemenkes", "Imigrasi", "Univ Global"],
    },
    "osteoporosis": {
        "name": "Osteoporosis",
        "short": "Osteoporosis",
        "icons": ["🦴", "💊", "🏃", "🥛", "🛡️"],
        "benefits": ["Tulang Kuat", "Cegah Patah", "Aktif", "Tenang"],
        "steps": ["Scan BMD", "Obat", "Nutrisi", "Latihan"],
        "trust": ["Spesialis Tulang", "Guideline IOF", "Infus Rumah"],
    },
    "antar-jemput-rs": {
        "name": "Antar Jemput RS",
        "short": "TransCare",
        "icons": ["🚑", "🏥", "🏠", "👨‍⚕️", "🛡️"],
        "benefits": ["Aman", "Nyaman", "Tepat Waktu", "Lengkap"],
        "steps": ["Jadwal", "Jemput", "Perjalanan", "Antar"],
        "trust": ["Ambulance ICU", "Perawat Pendamping", "GPS Tracking"],
    },
    "perawat-homecare": {
        "name": "Perawat Homecare",
        "short": "Perawat",
        "icons": ["👩‍⚕️", "💊", "🩹", "📋", "❤️"],
        "benefits": ["Profesional", "Penasihat", "Pendamping", "24 Jam"],
        "steps": ["Screening", "Matching", "Perawatan", "Laporan"],
        "trust": ["STR Terverifikasi", "Pengalaman RS", "Soft Skill"],
    },
    "home-lab": {
        "name": "Home Lab",
        "short": "Lab Darah",
        "icons": ["🩸", "🔬", "🏠", "📱", "⚡"],
        "benefits": ["Mudah", "Cepat", "Akurat", "Hemat"],
        "steps": ["Pesan", "Jemput", "Proses", "Hasil"],
        "trust": ["Lab Akreditasi", "Alat Modern", "Hasil Digital"],
    },
    "vaksinasi-rumah": {
        "name": "Vaksinasi Rumah",
        "short": "Vaksin",
        "icons": ["💉", "🛡️", "👨‍👩‍👧‍👦", "🏠", "📅"],
        "benefits": ["Lengkap", "Aman", "Nyaman", "Terjadwal"],
        "steps": ["Konsul", "Pilih", "Suntik", "Catat"],
        "trust": ["Vaksin Resmi", "Cold Chain", "Bidan/Dokter"],
    },
    "infus-vitamin": {
        "name": "Infus Vitamin",
        "short": "Infus",
        "icons": ["💧", "⚡", "🏠", "🩺", "✨"],
        "benefits": ["Prima", "Cepat", "Custom", "Refresh"],
        "steps": ["Cek Kebutuhan", "Formula", "Infus", "Monitor"],
        "trust": ["Dokter Resep", "Steril", "IV Certified"],
    },
    "kesehatan-umum": {
        "name": "Kesehatan Umum",
        "short": "Umum",
        "icons": ["🩺", "💊", "🏠", "📋", "👨‍⚕️"],
        "benefits": ["Lengkap", "Mudah", "Terpercaya", "Berkala"],
        "steps": ["Keluhan", "Cek Up", "Diagnosis", "Terapi"],
        "trust": ["Dokter Umum", "Rujukan Spesialis", "Kontinuitas"],
    },
}

import html

def escape_xml(text):
    """Escape XML special characters."""
    return html.escape(text, quote=True)

def make_svg(cat_id, variant, data):
    """Generate SVG for a category variant."""
    name = escape_xml(data["name"])
    short = escape_xml(data["short"])
    benefits = [escape_xml(b) for b in data["benefits"]]
    steps = [escape_xml(s) for s in data["steps"]]
    trust = [escape_xml(t) for t in data["trust"]]
    primary = BRAND["primary"]
    dark = BRAND["primary_dark"]
    accent = BRAND["accent"]
    accent_light = BRAND["accent_light"]
    teal = BRAND["teal"]
    light = BRAND["light"]
    bg = BRAND["bg_light"]
    bg2 = BRAND["bg_white"]
    text = BRAND["text_dark"]
    muted = BRAND["text_muted"]
    white = BRAND["white"]

    # Variant-specific content
    if variant == 1:
        # Brand Hero - existing style: left content, right illustration
        title_line1 = name
        title_line2 = escape_xml("di Rumah" if "di Rumah" not in data["name"] else "Joy of Care")
        subtitle = escape_xml(f"Layanan {data['name']} Profesional & Terpercaya")
        bullets = benefits[:3]
        cta = escape_xml("Konsultasi Gratis →")
        tag = escape_xml(f"{len([f for f in os.listdir(f'/home/gobeam/Projects/joyofcare-web/content-source/articles/{cat_id}') if f.endswith('.txt')])} Artikel")

        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img" aria-label="Kategori {name} - JoyofCare">
  <title>{name} - Joy of Care</title>
  <desc>Thumbnail kategori blog {name} dari JoyofCare.</desc>

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
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="8"/>
      <feOffset dx="0" dy="6"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.18"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <pattern id="dots" x="0" y="0" width="40" height="40" patternUnits="userSpaceOnUse">
      <circle cx="20" cy="20" r="1.5" fill="{primary}" opacity="0.18"/>
    </pattern>
  </defs>

  <rect width="1200" height="630" fill="url(#bgGrad)"/>
  <rect width="1200" height="630" fill="url(#dots)"/>
  <circle cx="1080" cy="140" r="190" fill="{primary}" opacity="0.12"/>
  <circle cx="140" cy="530" r="150" fill="{accent}" opacity="0.08"/>

  <g transform="translate(80, 90)">
    <rect x="0" y="0" width="280" height="44" rx="22" fill="{primary}"/>
    <text x="140" y="29" font-family="Inter, Montserrat, sans-serif" font-size="14" font-weight="700" fill="{white}" text-anchor="middle" letter-spacing="2">KATEGORI BLOG</text>

    <text x="0" y="125" font-family="Montserrat, Inter, sans-serif" font-size="68" font-weight="800" fill="{text}">{title_line1}</text>
    <text x="0" y="195" font-family="Montserrat, Inter, sans-serif" font-size="56" font-weight="800" fill="{dark}">{title_line2}</text>

    <text x="0" y="245" font-family="Inter, sans-serif" font-size="20" font-weight="500" fill="{muted}">{subtitle}</text>

    <g transform="translate(0, 290)">
'''
        for i, b in enumerate(bullets):
            svg += f'''      <g transform="translate(0, {i*35})">
        <circle cx="10" cy="10" r="5" fill="{primary}"/>
        <text x="30" y="16" font-family="Inter, sans-serif" font-size="16" fill="{text}">{b}</text>
      </g>
'''
        svg += f'''    </g>

    <g transform="translate(0, 410)">
      <rect x="0" y="0" width="270" height="46" rx="23" fill="url(#accentGrad)" filter="url(#shadow)"/>
      <text x="135" y="29" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="{white}" text-anchor="middle">{cta}</text>
    </g>
  </g>

  <g transform="translate(850, 300)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="180" fill="{white}" opacity="0.95"/>
    <circle cx="0" cy="0" r="150" fill="url(#bgGrad)"/>
    <text x="0" y="10" font-family="Montserrat, sans-serif" font-size="72" text-anchor="middle" fill="url(#primaryGrad)">{short}</text>
    <circle cx="0" cy="60" r="40" fill="url(#primaryGrad)"/>
    <text x="0" y="70" font-family="Inter, sans-serif" font-size="14" font-weight="600" fill="{white}" text-anchor="middle">{tag}</text>
  </g>

  <g transform="translate(70, 555)">
    <circle cx="14" cy="14" r="14" fill="{primary}"/>
    <text x="42" y="13" font-family="Montserrat, sans-serif" font-size="20" font-weight="700" fill="{dark}">Joy</text>
    <text x="80" y="13" font-family="Montserrat, sans-serif" font-size="20" font-weight="400" fill="{text}">of Care</text>
    <text x="42" y="32" font-family="Inter, sans-serif" font-size="13" fill="{muted}">joyofcare.net/blog/{cat_id}</text>
  </g>
</svg>'''

    elif variant == 2:
        # Benefit Scene - patient/family benefit focused
        title_line1 = escape_xml(f"Manfaat {data['name']}")
        title_line2 = escape_xml("di Rumah")
        # benefits already escaped above
        cta = escape_xml("Lihat Manfaat Lengkap →")
        tag = escape_xml("Pasien Senang & Sehat")
        sub_header = escape_xml("Kenapa ribuan keluarga percaya pada Joy of Care")
        card_footer = escape_xml("Direkomendasikan oleh tim medis")
        illustration_text = escape_xml("Hasil nyata dari 500+ pasien")

        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img" aria-label="Manfaat {name} - JoyofCare">
  <title>Manfaat {name} di Rumah - Joy of Care</title>
  <desc>Infografis manfaat layanan {name} JoyofCare untuk pasien dan keluarga.</desc>

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
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="6"/>
      <feOffset dx="0" dy="4"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.12"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="8"/>
      <feOffset dx="0" dy="6"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.18"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="1200" height="630" fill="url(#bgGrad)"/>

  <!-- Header -->
  <g transform="translate(80, 60)">
    <rect x="0" y="0" width="280" height="44" rx="22" fill="{primary}"/>
    <text x="140" y="29" font-family="Inter, Montserrat, sans-serif" font-size="14" font-weight="700" fill="{white}" text-anchor="middle" letter-spacing="2">KATEGORI BLOG</text>
    <text x="0" y="120" font-family="Montserrat, Inter, sans-serif" font-size="56" font-weight="800" fill="{text}">{title_line1}</text>
    <text x="0" y="185" font-family="Montserrat, Inter, sans-serif" font-size="48" font-weight="800" fill="{dark}">{title_line2}</text>
    <text x="0" y="235" font-family="Inter, sans-serif" font-size="18" font-weight="500" fill="{muted}">{sub_header}</text>
  </g>

  <!-- Benefit Cards Grid (2x2) -->
  <g transform="translate(80, 290)">
'''
        for i, b in enumerate(benefits):
            col = i % 2
            row = i // 2
            x = col * 300
            y = row * 140
            svg += f'''    <g transform="translate({x}, {y})" filter="url(#cardShadow)">
      <rect x="0" y="0" width="280" height="120" rx="16" fill="url(#cardGrad)"/>
      <circle cx="140" cy="30" r="28" fill="url(#primaryGrad)"/>
      <text x="140" y="36" font-family="Montserrat, sans-serif" font-size="28" font-weight="700" fill="{white}" text-anchor="middle">{i+1}</text>
      <text x="140" y="85" font-family="Montserrat, sans-serif" font-size="18" font-weight="700" fill="{text}" text-anchor="middle">{b}</text>
      <text x="140" y="108" font-family="Inter, sans-serif" font-size="13" fill="{muted}" text-anchor="middle">{card_footer}</text>
    </g>
'''
        svg += f'''  </g>

  <!-- Right side: Happy patient illustration -->
  <g transform="translate(850, 300)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="180" fill="{white}" opacity="0.95"/>
    <circle cx="0" cy="0" r="150" fill="url(#bgGrad)"/>
    <!-- Simple family/happy illustration -->
    <circle cx="-50" cy="-30" r="22" fill="{primary}" opacity="0.2"/>
    <circle cx="50" cy="-30" r="22" fill="{accent}" opacity="0.2"/>
    <ellipse cx="0" cy="30" rx="45" ry="35" fill="{primary}" opacity="0.15"/>
    <text x="0" y="85" font-family="Montserrat, sans-serif" font-size="16" font-weight="700" fill="{dark}" text-anchor="middle">{tag}</text>
    <text x="0" y="110" font-family="Inter, sans-serif" font-size="13" fill="{muted}" text-anchor="middle">Hasil nyata dari 500+ pasien</text>
  </g>

  <!-- CTA -->
  <g transform="translate(80, 550)">
    <rect x="0" y="0" width="320" height="48" rx="24" fill="url(#accentGrad)" filter="url(#shadow)"/>
    <text x="160" y="31" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="{white}" text-anchor="middle">{cta}</text>
  </g>

  <!-- Footer brand -->
  <g transform="translate(70, 555)">
    <circle cx="14" cy="14" r="14" fill="{primary}"/>
    <text x="42" y="13" font-family="Montserrat, sans-serif" font-size="20" font-weight="700" fill="{dark}">Joy</text>
    <text x="80" y="13" font-family="Montserrat, sans-serif" font-size="20" font-weight="400" fill="{text}">of Care</text>
    <text x="42" y="32" font-family="Inter, sans-serif" font-size="13" fill="{muted}">joyofcare.net/blog/{cat_id}</text>
  </g>
</svg>'''

    elif variant == 3:
        # Process Steps - step-by-step flow
        title_line1 = escape_xml(f"Proses {data['name']}")
        title_line2 = escape_xml("Mudah & Terstruktur")
        # steps already escaped above
        cta = escape_xml("Mulai Sekarang →")
        tag = escape_xml("4 Langkah Selesai")

        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img" aria-label="Proses {name} - JoyofCare">
  <title>Proses {name} di Rumah - Joy of Care</title>
  <desc>Alur langkah-langkah layanan {name} JoyofCare dari booking hingga selesai.</desc>

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
    <linearGradient id="stepGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{primary}"/>
      <stop offset="100%" stop-color="{teal}"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="8"/>
      <feOffset dx="0" dy="6"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.18"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="1200" height="630" fill="url(#bgGrad)"/>

  <!-- Header -->
  <g transform="translate(80, 60)">
    <rect x="0" y="0" width="280" height="44" rx="22" fill="{primary}"/>
    <text x="140" y="29" font-family="Inter, Montserrat, sans-serif" font-size="14" font-weight="700" fill="{white}" text-anchor="middle" letter-spacing="2">KATEGORI BLOG</text>
    <text x="0" y="120" font-family="Montserrat, Inter, sans-serif" font-size="56" font-weight="800" fill="{text}">{title_line1}</text>
    <text x="0" y="185" font-family="Montserrat, Inter, sans-serif" font-size="48" font-weight="800" fill="{dark}">{title_line2}</text>
    <text x="0" y="235" font-family="Inter, sans-serif" font-size="18" font-weight="500" fill="{muted}">Hanya 4 langkah menuju kesehatan optimal di rumah</text>
  </g>

  <!-- Step Flow (horizontal) -->
  <g transform="translate(80, 290)">
'''
        step_colors = [primary, teal, accent, dark]
        for i, step in enumerate(steps):
            x = i * 270
            color = step_colors[i]
            svg += f'''    <g transform="translate({x}, 0)">
      <!-- Step circle -->
      <circle cx="65" cy="65" r="55" fill="{white}" stroke="{color}" stroke-width="4"/>
      <circle cx="65" cy="65" r="42" fill="{color}"/>
      <text x="65" y="73" font-family="Montserrat, sans-serif" font-size="28" font-weight="800" fill="{white}" text-anchor="middle">{i+1}</text>

      <!-- Step label -->
      <text x="65" y="145" font-family="Montserrat, sans-serif" font-size="17" font-weight="700" fill="{text}" text-anchor="middle">{step}</text>

      <!-- Arrow to next (except last) -->
'''
            if i < len(steps) - 1:
                svg += f'''      <path d="M 130 65 Q 165 65 165 65" stroke="{color}" stroke-width="4" fill="none" stroke-linecap="round" marker-end="url(#arrowhead)"/>
      <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
          <polygon points="0 0, 10 3.5, 0 7" fill="{color}"/>
        </marker>
      </defs>
'''
            svg += f'''    </g>
'''
        svg += f'''  </g>

  <!-- Right side: Trust badges -->
  <g transform="translate(850, 300)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="180" fill="{white}" opacity="0.95"/>
    <circle cx="0" cy="0" r="150" fill="url(#bgGrad)"/>
    <text x="0" y="-30" font-family="Montserrat, sans-serif" font-size="18" font-weight="700" fill="{dark}" text-anchor="middle">Kenapa Joy of Care?</text>
    <g transform="translate(0, 10)">
'''
        for j, t in enumerate(data["trust"][:3]):
            svg += f'''      <g transform="translate(0, {j*38})">
        <circle cx="-85" cy="0" r="12" fill="{primary}" opacity="0.2"/>
        <circle cx="-85" cy="0" r="8" fill="{primary}"/>
        <text x="-60" y="5" font-family="Inter, sans-serif" font-size="14" font-weight="600" fill="{text}">{t}</text>
      </g>
'''
        svg += f'''    </g>
    <text x="0" y="115" font-family="Montserrat, sans-serif" font-size="16" font-weight="700" fill="{dark}" text-anchor="middle">{tag}</text>
  </g>

  <!-- CTA -->
  <g transform="translate(80, 550)">
    <rect x="0" y="0" width="280" height="48" rx="24" fill="url(#accentGrad)" filter="url(#shadow)"/>
    <text x="140" y="31" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="{white}" text-anchor="middle">{cta}</text>
  </g>

  <!-- Footer brand -->
  <g transform="translate(70, 555)">
    <circle cx="14" cy="14" r="14" fill="{primary}"/>
    <text x="42" y="13" font-family="Montserrat, sans-serif" font-size="20" font-weight="700" fill="{dark}">Joy</text>
    <text x="80" y="13" font-family="Montserrat, sans-serif" font-size="20" font-weight="400" fill="{text}">of Care</text>
    <text x="42" y="32" font-family="Inter, sans-serif" font-size="13" fill="{muted}">joyofcare.net/blog/{cat_id}</text>
  </g>
</svg>'''

    return svg


def main():
    out_dir = "/home/gobeam/Projects/joyofcare-web/assets/blog"
    os.makedirs(out_dir, exist_ok=True)

    for cat_id, data in CATEGORIES.items():
        for variant in [1, 2, 3]:
            fname = f"{cat_id}-v{variant}.svg"
            fpath = os.path.join(out_dir, fname)
            svg = make_svg(cat_id, variant, data)
            with open(fpath, "w") as f:
                f.write(svg)
            print(f"Created: {fname}")

    print("\nAll thumbnails generated!")
    print(f"Total files in {out_dir}: {len(os.listdir(out_dir))}")

if __name__ == "__main__":
    main()