#!/usr/bin/env python3
"""
scripts/update_to_kesehatan_lingkungan_and_16_9.py
1. Combines/merges siaga-vulkanik into kesehatan-lingkungan.
2. Updates all 352 image prompts to strictly use --ar 16:9 and authentic journalistic photography style (Kompas documentary photojournalism).
3. Updates frontmatter of all 352 articles in joyofcare-web.
4. Generates updated 1200x630 SVGs with updated category themes and motifs.
5. Updates image-prompts-nanobanana.json.
"""

import os
import glob
import json
import re
import xml.sax.saxutils as saxutils

NET_DIR = "/home/gobeam/Projects/joyofcare-net"
WEB_DIR = "/home/gobeam/Projects/joyofcare-web"
ARTICLES_DIR = os.path.join(WEB_DIR, "src/content/articles")
IMAGES_DIR = os.path.join(WEB_DIR, "assets/images/articles")

os.makedirs(IMAGES_DIR, exist_ok=True)

# 12 Category Themes (Color Palettes & Vector Motifs)
CATEGORY_THEMES = {
    "panggil-dokter": {
        "label": "Panggil Dokter ke Rumah",
        "bg_start": "#ECFDF5",
        "bg_mid": "#F0FDF4",
        "bg_end": "#D1FAE5",
        "accent": "#059669",
        "accent_dark": "#047857",
        "badge_bg": "#D1FAE5",
        "badge_text": "#065F46",
        "motif": "stethoscope",
        "icon_label": "DOKTER VISIT",
    },
    "perawat-homecare": {
        "label": "Perawat Medis Homecare",
        "bg_start": "#F0FDFA",
        "bg_mid": "#F4FDF9",
        "bg_end": "#CCFBF1",
        "accent": "#0D9488",
        "accent_dark": "#0F766E",
        "badge_bg": "#CCFBF1",
        "badge_text": "#115E59",
        "motif": "nurse_care",
        "icon_label": "PERAWAT HOMECARE",
    },
    "fisioterapi-rumah": {
        "label": "Fisioterapi ke Rumah",
        "bg_start": "#EEF2FF",
        "bg_mid": "#F5F7FF",
        "bg_end": "#E0E7FF",
        "accent": "#4F46E5",
        "accent_dark": "#4338CA",
        "badge_bg": "#E0E7FF",
        "badge_text": "#3730A3",
        "motif": "physio_joint",
        "icon_label": "FISIOTERAPI MEDIS",
    },
    "home-lab": {
        "label": "Home Lab & Cek Darah",
        "bg_start": "#F0F9FF",
        "bg_mid": "#F8FAFC",
        "bg_end": "#E0F2FE",
        "accent": "#0284C7",
        "accent_dark": "#0369A1",
        "badge_bg": "#E0F2FE",
        "badge_text": "#075985",
        "motif": "lab_microscope",
        "icon_label": "LABORATORIUM RUMAH",
    },
    "perawatan-lansia": {
        "label": "Perawatan Lansia & Geriatri",
        "bg_start": "#FFFBEB",
        "bg_mid": "#FFFDF5",
        "bg_end": "#FEF3C7",
        "accent": "#D97706",
        "accent_dark": "#B45309",
        "badge_bg": "#FEF3C7",
        "badge_text": "#92400E",
        "motif": "elderly_care",
        "icon_label": "CARE GERIATRI",
    },
    "infus-vitamin": {
        "label": "Infus & Suntik Vitamin",
        "bg_start": "#FFF7ED",
        "bg_mid": "#FFFAF0",
        "bg_end": "#FFEDD5",
        "accent": "#EA580C",
        "accent_dark": "#C2410C",
        "badge_bg": "#FFEDD5",
        "badge_text": "#9A3412",
        "motif": "vitamin_drop",
        "icon_label": "IMMUNE BOOSTER",
    },
    "osteoporosis": {
        "label": "Osteoporosis & Tulang",
        "bg_start": "#F1F5F9",
        "bg_mid": "#F8FAFC",
        "bg_end": "#E2E8F0",
        "accent": "#475569",
        "accent_dark": "#334155",
        "badge_bg": "#E2E8F0",
        "badge_text": "#1E293B",
        "motif": "bone_spine",
        "icon_label": "KESEHATAN TULANG",
    },
    "parkinson": {
        "label": "Parkinson & Saraf Motorik",
        "bg_start": "#F5F3FF",
        "bg_mid": "#FAF5FF",
        "bg_end": "#EDE9FE",
        "accent": "#7C3AED",
        "accent_dark": "#6D28D9",
        "badge_bg": "#EDE9FE",
        "badge_text": "#5B21B6",
        "motif": "brain_neuro",
        "icon_label": "NEUROLOGI & SARAF",
    },
    "antar-jemput-rs": {
        "label": "Antar Jemput RS (TransCare)",
        "bg_start": "#FFF1F2",
        "bg_mid": "#FFF7ED",
        "bg_end": "#FFE4E6",
        "accent": "#E11D48",
        "accent_dark": "#BE123C",
        "badge_bg": "#FFE4E6",
        "badge_text": "#9F1239",
        "motif": "transport_escort",
        "icon_label": "TRANSPORT MEDIS",
    },
    "studi-luar-negeri": {
        "label": "Studi Luar Negeri & Vaksin",
        "bg_start": "#EFF6FF",
        "bg_mid": "#F8FAFC",
        "bg_end": "#DBEAFE",
        "accent": "#2563EB",
        "accent_dark": "#1D4ED8",
        "badge_bg": "#DBEAFE",
        "badge_text": "#1E40AF",
        "motif": "study_globe",
        "icon_label": "MCU & VAKSINASI",
    },
    "vaksinasi-rumah": {
        "label": "Vaksinasi Dewasa di Rumah",
        "bg_start": "#ECFDF5",
        "bg_mid": "#F0FDF4",
        "bg_end": "#D1FAE5",
        "accent": "#059669",
        "accent_dark": "#047857",
        "badge_bg": "#D1FAE5",
        "badge_text": "#065F46",
        "motif": "vaccine_shield",
        "icon_label": "VAKSINASI RESMI",
    },
    "kesehatan-umum": {
        "label": "Kesehatan Umum & Terapi",
        "bg_start": "#ECFDF5",
        "bg_mid": "#F8FCF9",
        "bg_end": "#E6F7ED",
        "accent": "#00bf63",
        "accent_dark": "#007A3D",
        "badge_bg": "#E6F7ED",
        "badge_text": "#007A3D",
        "motif": "wellness_shield",
        "icon_label": "KESEHATAN KELUARGA",
    },
    "kesehatan-lingkungan": {
        "label": "Kesehatan Lingkungan",
        "bg_start": "#F0FDF4",
        "bg_mid": "#F8FCF9",
        "bg_end": "#ECFDF5",
        "accent": "#00bf63",
        "accent_dark": "#007A3D",
        "badge_bg": "#DCFCE7",
        "badge_text": "#166534",
        "motif": "environmental_mitigation",
        "icon_label": "KESEHATAN LINGKUNGAN",
    },
}

def get_theme(category):
    if category == "siaga-vulkanik":
        category = "kesehatan-lingkungan"
    return CATEGORY_THEMES.get(category, CATEGORY_THEMES["kesehatan-umum"])

def wrap_title_to_lines(title, max_chars=34):
    words = title.split()
    lines = []
    current_line = []
    current_len = 0
    
    for word in words:
        if current_len + len(word) + (1 if current_line else 0) <= max_chars:
            current_line.append(word)
            current_len += len(word) + (1 if len(current_line) > 1 else 0)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
            current_len = len(word)
            
    if current_line:
        lines.append(" ".join(current_line))
        
    if len(lines) > 3:
        lines = lines[:2] + [" ".join(lines[2:])]
        if len(lines[2]) > max_chars + 10:
            lines[2] = lines[2][:max_chars + 7] + "..."
            
    return lines

def generate_svg_motif(motif, accent, accent_dark):
    if motif == "environmental_mitigation":
        return f"""
        <g transform="translate(770, 180)">
          <circle cx="120" cy="120" r="105" fill="#FFFFFF" stroke="{accent}" stroke-width="4" filter="url(#shadow)"/>
          <!-- Eco Shield & Clean Air Waves -->
          <path d="M120 40 L180 65 L180 130 C180 180 120 205 120 205 C120 205 60 180 60 130 L60 65 Z" fill="{accent}" opacity="0.15"/>
          <!-- Leaf & Clean Air Swirl -->
          <path d="M120 70 C150 70 165 95 165 125 C165 165 120 185 120 185 C120 185 75 165 75 125 C75 95 90 70 120 70 Z" fill="{accent}" opacity="0.4"/>
          <path d="M120 85 Q145 110 120 165" fill="none" stroke="#FFFFFF" stroke-width="3"/>
          <!-- Respirator Mask Accent -->
          <path d="M85 145 Q120 125 155 145 Q145 180 120 180 Q95 180 85 145 Z" fill="{accent_dark}" stroke="#FFFFFF" stroke-width="2.5"/>
          <circle cx="120" cy="155" r="7" fill="#FFFFFF"/>
        </g>
        """
    elif motif == "stethoscope":
        return f"""
        <g transform="translate(770, 180)">
          <circle cx="120" cy="120" r="105" fill="#FFFFFF" stroke="{accent}" stroke-width="4" filter="url(#shadow)"/>
          <path d="M40 120 L85 120 L100 80 L115 160 L130 100 L145 140 L160 120 L200 120" fill="none" stroke="{accent}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="120" cy="250" r="28" fill="{accent}" stroke="#FFFFFF" stroke-width="4"/>
          <circle cx="120" cy="250" r="14" fill="#FFFFFF"/>
          <path d="M120 222 C120 180 70 190 70 150 L70 100" fill="none" stroke="{accent_dark}" stroke-width="8" stroke-linecap="round"/>
          <path d="M120 222 C120 180 170 190 170 150 L170 100" fill="none" stroke="{accent_dark}" stroke-width="8" stroke-linecap="round"/>
        </g>
        """
    elif motif == "nurse_care":
        return f"""
        <g transform="translate(770, 180)">
          <circle cx="120" cy="120" r="105" fill="#FFFFFF" stroke="{accent}" stroke-width="4" filter="url(#shadow)"/>
          <path d="M120 40 L180 65 L180 130 C180 180 120 205 120 205 C120 205 60 180 60 130 L60 65 Z" fill="{accent}" opacity="0.15"/>
          <rect x="105" y="70" width="30" height="85" rx="6" fill="{accent}"/>
          <rect x="77" y="97" width="85" height="30" rx="6" fill="{accent}"/>
          <path d="M50 190 Q120 230 190 190" fill="none" stroke="{accent_dark}" stroke-width="6" stroke-linecap="round"/>
        </g>
        """
    elif motif == "physio_joint":
        return f"""
        <g transform="translate(770, 180)">
          <circle cx="120" cy="120" r="105" fill="#FFFFFF" stroke="{accent}" stroke-width="4" filter="url(#shadow)"/>
          <circle cx="120" cy="120" r="32" fill="{accent}"/>
          <circle cx="120" cy="120" r="16" fill="#FFFFFF"/>
          <path d="M120 50 L120 88" stroke="{accent_dark}" stroke-width="12" stroke-linecap="round"/>
          <path d="M120 152 L170 200" stroke="{accent_dark}" stroke-width="12" stroke-linecap="round"/>
          <path d="M55 120 A65 65 0 0 1 185 120" fill="none" stroke="{accent}" stroke-width="4" stroke-dasharray="6,6"/>
          <polygon points="185,115 195,120 185,125" fill="{accent}"/>
        </g>
        """
    elif motif == "lab_microscope":
        return f"""
        <g transform="translate(770, 180)">
          <circle cx="120" cy="120" r="105" fill="#FFFFFF" stroke="{accent}" stroke-width="4" filter="url(#shadow)"/>
          <rect x="90" y="60" width="22" height="90" rx="11" fill="{accent}" opacity="0.25" stroke="{accent}" stroke-width="3"/>
          <rect x="125" y="75" width="22" height="75" rx="11" fill="{accent_dark}" opacity="0.4" stroke="{accent_dark}" stroke-width="3"/>
          <circle cx="101" cy="130" r="6" fill="{accent}"/>
          <circle cx="136" cy="130" r="6" fill="{accent_dark}"/>
          <path d="M70 185 Q120 165 170 185 Q120 205 70 185" fill="none" stroke="{accent}" stroke-width="4"/>
          <line x1="95" y1="178" x2="95" y2="192" stroke="{accent_dark}" stroke-width="3"/>
          <line x1="120" y1="175" x2="120" y2="195" stroke="{accent_dark}" stroke-width="3"/>
          <line x1="145" y1="178" x2="145" y2="192" stroke="{accent_dark}" stroke-width="3"/>
        </g>
        """
    elif motif == "elderly_care":
        return f"""
        <g transform="translate(770, 180)">
          <circle cx="120" cy="120" r="105" fill="#FFFFFF" stroke="{accent}" stroke-width="4" filter="url(#shadow)"/>
          <path d="M120 70 C100 40 60 55 60 90 C60 130 120 170 120 170 C120 170 180 130 180 90 C180 55 140 40 120 70 Z" fill="{accent}" opacity="0.2"/>
          <path d="M120 85 C105 60 75 72 75 98 C75 128 120 155 120 155 C120 155 165 128 165 98 C165 72 135 60 120 85 Z" fill="{accent}"/>
          <path d="M50 165 C80 205 160 205 190 165" fill="none" stroke="{accent_dark}" stroke-width="6" stroke-linecap="round"/>
        </g>
        """
    elif motif == "vitamin_drop":
        return f"""
        <g transform="translate(770, 180)">
          <circle cx="120" cy="120" r="105" fill="#FFFFFF" stroke="{accent}" stroke-width="4" filter="url(#shadow)"/>
          <path d="M120 45 C120 45 65 120 65 150 C65 185 90 205 120 205 C150 205 175 185 175 150 C175 120 120 45 120 45 Z" fill="{accent}" opacity="0.25"/>
          <path d="M120 65 C120 65 78 125 78 148 C78 175 97 190 120 190 C143 190 162 175 162 148 C162 125 120 65 120 65 Z" fill="{accent}"/>
          <rect x="113" y="125" width="14" height="42" rx="3" fill="#FFFFFF"/>
          <rect x="99" y="139" width="42" height="14" rx="3" fill="#FFFFFF"/>
        </g>
        """
    elif motif == "bone_spine":
        return f"""
        <g transform="translate(770, 180)">
          <circle cx="120" cy="120" r="105" fill="#FFFFFF" stroke="{accent}" stroke-width="4" filter="url(#shadow)"/>
          <rect x="90" y="60" width="60" height="24" rx="10" fill="{accent}"/>
          <rect x="85" y="92" width="70" height="24" rx="10" fill="{accent_dark}"/>
          <rect x="90" y="124" width="60" height="24" rx="10" fill="{accent}"/>
          <rect x="80" y="156" width="80" height="24" rx="10" fill="{accent_dark}"/>
          <line x1="120" y1="50" x2="120" y2="190" stroke="#FFFFFF" stroke-width="4" stroke-dasharray="4,4"/>
        </g>
        """
    elif motif == "brain_neuro":
        return f"""
        <g transform="translate(770, 180)">
          <circle cx="120" cy="120" r="105" fill="#FFFFFF" stroke="{accent}" stroke-width="4" filter="url(#shadow)"/>
          <circle cx="120" cy="90" r="18" fill="{accent}"/>
          <circle cx="75" cy="140" r="14" fill="{accent_dark}"/>
          <circle cx="165" cy="140" r="14" fill="{accent_dark}"/>
          <circle cx="120" cy="175" r="12" fill="{accent}"/>
          <line x1="120" y1="90" x2="75" y2="140" stroke="{accent}" stroke-width="5"/>
          <line x1="120" y1="90" x2="165" y2="140" stroke="{accent}" stroke-width="5"/>
          <line x1="75" y1="140" x2="120" y2="175" stroke="{accent_dark}" stroke-width="4"/>
          <line x1="165" y1="140" x2="120" y2="175" stroke="{accent_dark}" stroke-width="4"/>
        </g>
        """
    elif motif == "transport_escort":
        return f"""
        <g transform="translate(770, 180)">
          <circle cx="120" cy="120" r="105" fill="#FFFFFF" stroke="{accent}" stroke-width="4" filter="url(#shadow)"/>
          <path d="M60 140 L80 90 L150 90 L180 120 L180 160 L60 160 Z" fill="{accent}" opacity="0.2"/>
          <rect x="70" y="105" width="90" height="45" rx="8" fill="{accent}"/>
          <rect x="110" y="115" width="10" height="25" fill="#FFFFFF"/>
          <rect x="102" y="122" width="26" height="10" fill="#FFFFFF"/>
          <circle cx="95" cy="155" r="14" fill="{accent_dark}"/>
          <circle cx="150" cy="155" r="14" fill="{accent_dark}"/>
        </g>
        """
    else:
        return f"""
        <g transform="translate(770, 180)">
          <circle cx="120" cy="120" r="105" fill="#FFFFFF" stroke="{accent}" stroke-width="4" filter="url(#shadow)"/>
          <path d="M120 40 L180 65 L180 130 C180 180 120 205 120 205 C120 205 60 180 60 130 L60 65 Z" fill="{accent}" opacity="0.2"/>
          <rect x="107" y="75" width="26" height="75" rx="6" fill="{accent}"/>
          <rect x="82" y="100" width="76" height="26" rx="6" fill="{accent}"/>
          <circle cx="120" cy="120" r="75" fill="none" stroke="{accent_dark}" stroke-width="3" stroke-dasharray="4,4"/>
        </g>
        """

def generate_svg_header(slug, title, category, primary_keyword=""):
    theme = get_theme(category)
    lines = wrap_title_to_lines(title, max_chars=33)
    
    if len(lines) == 1:
        font_size = 44
        line_height = 56
        start_y = 160
    elif len(lines) == 2:
        font_size = 38
        line_height = 48
        start_y = 145
    else:
        font_size = 31
        line_height = 40
        start_y = 135

    escaped_lines = [saxutils.escape(l) for l in lines]
    escaped_category = saxutils.escape(theme["label"].upper())
    escaped_kw = saxutils.escape(primary_keyword[:45] if primary_keyword else theme["label"])
    
    motif_svg = generate_svg_motif(theme["motif"], theme["accent"], theme["accent_dark"])
    
    title_text_elements = "\n".join([
        f'<text x="0" y="{start_y + i * line_height}" font-family="Montserrat, Inter, -apple-system, sans-serif" font-size="{font_size}" font-weight="800" fill="#0F172A" letter-spacing="-0.8">{line}</text>'
        for i, line in enumerate(escaped_lines)
    ])
    
    bottom_keyword_y = start_y + len(lines) * line_height + 25

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{theme['bg_start']}"/>
      <stop offset="50%" stop-color="{theme['bg_mid']}"/>
      <stop offset="100%" stop-color="{theme['bg_end']}"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{theme['accent']}"/>
      <stop offset="100%" stop-color="{theme['accent_dark']}"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
    <filter id="cardShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="{theme['accent']}" flood-opacity="0.14"/>
    </filter>
    <pattern id="dotPattern" x="0" y="0" width="28" height="28" patternUnits="userSpaceOnUse">
      <circle cx="14" cy="14" r="1.5" fill="{theme['accent']}" opacity="0.16"/>
    </pattern>
  </defs>

  <!-- Background Canvas -->
  <rect width="1200" height="630" fill="url(#bgGrad)"/>
  <rect width="1200" height="630" fill="url(#dotPattern)"/>

  <!-- Ambient Glowing Orbs -->
  <circle cx="1100" cy="90" r="240" fill="{theme['accent']}" opacity="0.06"/>
  <circle cx="120" cy="560" r="200" fill="{theme['accent_dark']}" opacity="0.04"/>

  <!-- Left Content Column -->
  <g transform="translate(80, 75)">
    <!-- Top Pill: Category + Verification Badges -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="310" height="36" rx="18" fill="{theme['badge_bg']}"/>
      <circle cx="18" cy="18" r="6" fill="{theme['accent']}"/>
      <text x="34" y="23" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="800" fill="{theme['badge_text']}" letter-spacing="1">{escaped_category}</text>
    </g>

    <!-- Medical Review Trust Badge -->
    <g transform="translate(325, 0)">
      <rect x="0" y="0" width="230" height="36" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
      <path d="M14 18 L19 23 L28 13" fill="none" stroke="{theme['accent']}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="36" y="23" font-family="Inter, -apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#334155">Review Tim Medis JOC</text>
    </g>

    <!-- Dynamic Multi-line Title -->
    {title_text_elements}

    <!-- Keyword Highlight Pill -->
    <g transform="translate(0, {bottom_keyword_y})">
      <rect x="0" y="0" width="540" height="42" rx="10" fill="#FFFFFF" stroke="{theme['accent']}" stroke-opacity="0.3" stroke-width="1.5" filter="url(#shadow)"/>
      <rect x="0" y="0" width="6" height="42" rx="3" fill="{theme['accent']}"/>
      <text x="20" y="26" font-family="Inter, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#475569">
        Fokus Klinis: <tspan font-weight="700" fill="{theme['accent_dark']}">{escaped_kw}</tspan>
      </text>
    </g>

    <!-- Checklist / Value Points -->
    <g transform="translate(0, {bottom_keyword_y + 65})">
      <g transform="translate(0, 0)">
        <circle cx="10" cy="10" r="10" fill="{theme['accent']}" fill-opacity="0.15"/>
        <path d="M6 10 L9 13 L14 7" fill="none" stroke="{theme['accent']}" stroke-width="2" stroke-linecap="round"/>
        <text x="28" y="14" font-family="Inter, sans-serif" font-size="13.5" font-weight="600" fill="#334155">Standar Komprehensif Dokter &amp; Perawat Berlisensi STR/SIP</text>
      </g>
      <g transform="translate(0, 30)">
        <circle cx="10" cy="10" r="10" fill="{theme['accent']}" fill-opacity="0.15"/>
        <path d="M6 10 L9 13 L14 7" fill="none" stroke="{theme['accent']}" stroke-width="2" stroke-linecap="round"/>
        <text x="28" y="14" font-family="Inter, sans-serif" font-size="13.5" font-weight="600" fill="#334155">Layanan Home Visit Jabodetabek • Siaga Hotline 08811-118-911</text>
      </g>
    </g>
  </g>

  <!-- Right Visual Focus Card -->
  <g filter="url(#cardShadow)">
    <rect x="710" y="65" width="410" height="500" rx="32" fill="#FFFFFF" stroke="{theme['accent']}" stroke-opacity="0.25" stroke-width="2"/>
    <rect x="725" y="80" width="380" height="470" rx="24" fill="{theme['bg_start']}"/>
    
    <!-- Vector Motif Graphic -->
    {motif_svg}

    <!-- Bottom Stamp in Card -->
    <g transform="translate(745, 480)">
      <rect x="0" y="0" width="340" height="46" rx="23" fill="#0F172A"/>
      <text x="170" y="28" font-family="Inter, sans-serif" font-size="12.5" font-weight="800" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">JOY OF CARE • PROTOKOL RESMI</text>
    </g>
  </g>
</svg>"""
    return svg

def generate_journalistic_prompt(title, category, primary_keyword, slug):
    scenarios = {
        "panggil-dokter": "an authentic Indonesian doctor in white medical coat and stethoscope visiting an elderly patient and family inside an upscale contemporary living room with marble flooring and large floor-to-ceiling windows of an elite urban landed house or luxury apartment in Jakarta, candid documentary moment of measuring blood pressure and talking attentively with patient",
        "perawat-homecare": "a licensed Indonesian nurse in clinical scrubs performing sterile wound care with hydrogel dressing on a resting patient in a spacious, modern air-conditioned master bedroom of an elite urban residence or luxury apartment in Jabodetabek, genuine focus, unposed documentary setting with modern hospital-grade homecare bed and clean architectural interior",
        "fisioterapi-rumah": "a professional Indonesian physiotherapist gently assisting a patient through knee mobility and gait rehabilitation exercises on an exercise mat in a bright, modern living room with polished marble flooring and contemporary minimalist furniture in an elite urban landed house in Jabodetabek",
        "home-lab": "a professional Indonesian phlebotomist in medical gloves preparing vacuum blood collection tubes beside an insulated sample cooler bag at an elegant contemporary dining table in a luxury high-rise apartment or elite landed home in Jabodetabek",
        "perawatan-lansia": "a compassionate Indonesian homecare nurse holding hands and comforting an elderly Indonesian grandmother sitting in an ergonomic modern armchair in a sunlit contemporary living room with large garden-view windows in an elite urban landed house in Jabodetabek",
        "infus-vitamin": "an experienced Indonesian nurse monitoring an intravenous vitamin drip line on a stainless IV pole while patient rests comfortably on an elegant contemporary designer sofa in an upscale modern apartment or luxury landed house in Jabodetabek",
        "osteoporosis": "an Indonesian healthcare professional explaining bone density results and postural exercises to an active Indonesian elderly couple in their spacious, modern upscale urban living room in Jabodetabek",
        "parkinson": "an Indonesian neuro-rehabilitation therapist practicing rhythmic walking exercises with a Parkinson patient holding an ergonomic walking frame along a spacious modern corridor of an elite urban residence or high-rise penthouse, with attentive family watching",
        "antar-jemput-rs": "a Joy of Care medical escort nurse carefully assisting a wheelchair patient at the grand driveway of an elite gated residential estate or luxury high-rise condominium lobby in Jakarta, boarding a well-equipped medical ambulance, candid documentary capture",
        "studi-luar-negeri": "a licensed Indonesian doctor reviewing international immunization certificates and administering travel vaccines to an Indonesian university student in a sleek, modern private study room of an upscale urban apartment in Jakarta",
        "vaksinasi-rumah": "a friendly Indonesian doctor preparing a sterile pre-filled vaccine syringe for an elderly couple at an elegant marble dining table in an elite urban landed residence in Jabodetabek",
        "kesehatan-umum": "an Indonesian health doctor in discussion with an affluent Indonesian family about proactive health management in a bright, contemporary open-concept living room of an elite urban landed home or luxury apartment in Jabodetabek",
        "kesehatan-lingkungan": "an Indonesian doctor and nurse wearing certified N95 particulate respirator masks, conducting respiratory lung checkups with a stethoscope during volcanic haze inside an elite modern urban home in Jabodetabek with closed double-glazed panoramic windows and a premium sleek HEPA air purifier running quietly",
    }
    
    scenario = scenarios.get(category, scenarios["kesehatan-umum"])
    
    prompt = (
        f"Nanobanana Pro 2 prompt: Editorial documentary photojournalism in Kompas and National Geographic news photography style, "
        f"authentic unposed Indonesian healthcare scene set in elite urban housing in Jabodetabek (modern luxury landed house or upscale high-rise apartment): "
        f"Indonesian, healthcare, professionals, taking care of patient in an affluent urban residence, {scenario}. "
        f"Focusing on topic '{title}'. Primary keyword: {primary_keyword}. "
        f"Candid photojournalistic capture, natural daylight from large panoramic windows, authentic Indonesian family and medical workers, "
        f"honest expressions of empathy and clinical attentiveness, elite urban housing setting (modern landed house or luxury apartment in Jabodetabek), "
        f"pristine clean contemporary interior, polished stone floors, elegant modern furniture, "
        f"Leica M11 with Summilux 35mm f/1.4 lens, natural skin tones, true-to-life documentary color grading, "
        f"high realism, Pulitzer-prize photojournalistic storytelling --ar 16:9 --style raw"
    )
    return prompt


def main():
    print("=== UPDATING TO KESEHATAN LINGKUNGAN & 16:9 JOURNALISTIC PROMPTS ===")
    
    all_files = glob.glob(os.path.join(ARTICLES_DIR, "*.mdx"))
    print(f"Total articles to process in web: {len(all_files)}")
    
    all_prompts_catalog = {}
    updated_category_count = 0
    
    for file_path in all_files:
        basename = os.path.basename(file_path)
        slug = basename.replace(".mdx", "")
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        parts = content.split("---", 2)
        if len(parts) < 3:
            continue
            
        fm_raw = parts[1]
        body = parts[2]
        
        title_m = re.search(r'^title:\s*["\']?(.*?)["\']?$', fm_raw, re.MULTILINE)
        title = title_m.group(1).strip() if title_m else slug.replace("-", " ").title()
        
        cat_m = re.search(r'^category:\s*["\']?(.*?)["\']?$', fm_raw, re.MULTILINE)
        category = cat_m.group(1).strip() if cat_m else "kesehatan-umum"
        
        # 1. Check if category is siaga-vulkanik or related volcanic -> update to kesehatan-lingkungan
        if category == "siaga-vulkanik" or "vulkanik" in slug or "krakatau" in slug or "erupsi" in slug:
            category = "kesehatan-lingkungan"
            fm_raw = re.sub(r'^category:.*$', 'category: kesehatan-lingkungan', fm_raw, flags=re.MULTILINE)
            updated_category_count += 1
            
        kw_m = re.search(r'^primaryKeyword:\s*["\']?(.*?)["\']?$', fm_raw, re.MULTILINE)
        primary_kw = kw_m.group(1).strip() if kw_m else ""
        
        # 2. Formulate authentic 16:9 journalistic photography prompt
        journalistic_prompt = generate_journalistic_prompt(title, category, primary_kw, slug)
        
        # 3. Generate updated SVG header
        svg_content = generate_svg_header(slug, title, category, primary_kw)
        svg_path = os.path.join(IMAGES_DIR, f"{slug}.svg")
        with open(svg_path, "w", encoding="utf-8") as f_svg:
            f_svg.write(svg_content)
            
        image_url = f"/assets/images/articles/{slug}.svg"
        
        all_prompts_catalog[slug] = {
            "title": title,
            "category": category,
            "primaryKeyword": primary_kw,
            "aspectRatio": "16:9",
            "style": "journalistic photography",
            "imagePrompt": journalistic_prompt,
            "featuredImage": image_url,
        }
        
        # 4. Update imagePrompt in frontmatter
        escaped_prompt = journalistic_prompt.replace('"', '\\"')
        if re.search(r'^imagePrompt:', fm_raw, re.MULTILINE):
            fm_raw = re.sub(r'^imagePrompt:.*$', f'imagePrompt: "{escaped_prompt}"', fm_raw, flags=re.MULTILINE)
        else:
            fm_raw += f'\nimagePrompt: "{escaped_prompt}"'
            
        # Ensure featuredImage is set
        if re.search(r'^featuredImage:', fm_raw, re.MULTILINE):
            fm_raw = re.sub(r'^featuredImage:.*$', f'featuredImage: {image_url}', fm_raw, flags=re.MULTILINE)
        else:
            fm_raw += f'\nfeaturedImage: {image_url}'
            
        # Ensure author and reviewer are standard
        if re.search(r'^author:', fm_raw, re.MULTILINE):
            fm_raw = re.sub(r'^author:.*$', 'author: Tim Kontributor Artikel', fm_raw, flags=re.MULTILINE)
        if re.search(r'^reviewer:', fm_raw, re.MULTILINE):
            fm_raw = re.sub(r'^reviewer:.*$', 'reviewer: Tim Medis Joy of Care', fm_raw, flags=re.MULTILINE)
            
        # Ensure trailing newline on fm_raw
        if not fm_raw.endswith("\n"):
            fm_raw += "\n"
            
        with open(file_path, "w", encoding="utf-8") as f_out:
            f_out.write(f"---{fm_raw}---{body}")
            
    print(f"Updated {updated_category_count} articles to category 'kesehatan-lingkungan'.")
    print(f"Updated all {len(all_prompts_catalog)} articles with 16:9 journalistic prompts.")
    
    # Save prompts catalog
    json_path = os.path.join(IMAGES_DIR, "image-prompts-nanobanana.json")
    with open(json_path, "w", encoding="utf-8") as f_json:
        json.dump(all_prompts_catalog, f_json, indent=2, ensure_ascii=False)
        
    print(f"Saved {len(all_prompts_catalog)} prompts to {json_path}")
    print("=== SCRIPT FINISHED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
