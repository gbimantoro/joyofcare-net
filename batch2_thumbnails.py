#!/usr/bin/env python3
"""Batch 2 — Premium category thumbnail SVGs (12 categories x 3 variants = 36 SVGs).
Production-quality: multi-element compositions, refined typography, subtle texture,
8px grid, generous whitespace. 1200x630. Brand palette: #00bf63 / #007A3D / #FC9000 / #0E7490.
"""
import os, html

BLOG_DIR = "/home/gobeam/Projects/joyofcare-web/assets/blog"
os.makedirs(BLOG_DIR, exist_ok=True)

# Palette
P = "#00bf63"
PD = "#007A3D"
A = "#FC9000"
AL = "#FFA940"
T = "#0E7490"
L = "#7ED957"
BG = "#EFFBF4"
BG2 = "#F4FAF6"
INK = "#0F172A"
SLATE = "#475569"
SOFT = "#E2E8F0"
W = "#FFFFFF"

CATS = {
    "perawatan-lansia": {
        "name": "Perawatan Lansia", "slug": "lansia", "sub": "Geriatri & Pendampingan",
        "hero_label": "LANGSUNG KE RUMAH ANDA", "hero_desc": "Tim geriatri bersertifikat, pendampingan penuh kasih untuk Opa & Oma di rumah.",
        "stats": [("500+", "Keluarga"), ("24/7", "Siaga"), ("Dinkes", "Resmi")],
        "keypoints": ["Assessment geriatri", "Perawat bersertifikat", "Pantau keluarga"],
        "process": ["Hubungi WA", "Assessment", "Penugasan", "Pantau"],
    },
    "fisioterapi-rumah": {
        "name": "Fisioterapi Rumah", "slug": "fisio", "sub": "Pemulihan Mobilitas",
        "hero_label": "FISIOTERAPI PROFESIONAL", "hero_desc": "Hemat waktu, privasi terjaga, latihan dirancang klinisi untuk stroke, sendi, pasca operasi.",
        "stats": [("98%", "Pasien Puas"), ("SIPP", "Terverifikasi"), ("Mandiri", "Recovery")],
        "keypoints": ["Konsultasi pertama", "Latihan terstruktur", "Evaluasi mingguan"],
        "process": ["Booking", "Assessment", "Latihan", "Evaluasi"],
    },
    "panggil-dokter": {
        "name": "Panggil Dokter", "slug": "dokter", "sub": "Dokter ke Rumah",
        "hero_label": "DOKTER DATANG KE RUMAH", "hero_desc": "Tidak perlu antri, tidak perlu keluar rumah. Dokter umum & spesialis siap melayani.",
        "stats": [("30 min", "Respon"), ("SIP", "Aktif"), ("Cipta", "Tenang")],
        "keypoints": ["Diagnosis di rumah", "Resep digital", "Rujukan spesialis"],
        "process": ["Chat WA", "Penugasan", "Kunjungan", "Tindak lanjut"],
    },
    "parkinson": {
        "name": "Parkinson", "slug": "parkinson", "sub": "Neuromotor & Dukungan",
        "hero_label": "DUKUNGAN NEUROMOTOR", "hero_desc": "Fisioterapi, terapi wicara, dan pendampingan keluarga untuk kualitas hidup optimal.",
        "stats": [("ESAS", "Skor Laporan"), ("EPDA", "Standar"), ("Rumah", "Aman")],
        "keypoints": ["Latihan mobilitas", "Manajemen obat", "Konsultan saraf"],
        "process": ["Assessment", "Terapi", "Obat", "Kontrol"],
    },
    "studi-luar-negeri": {
        "name": "Studi Luar Negeri", "slug": "study", "sub": "Kesehatan & Imigrasi",
        "hero_label": "PERSYARATAN KESEHATAN", "hero_desc": "Medical check up, vaksinasi, surat keterangan sehat berstandar universitas & imigrasi.",
        "stats": [("WHO", "Standar"), ("10+", "Negara"), ("Resmi", "Materai")],
        "keypoints": ["Cek lab lengkap", "Vaksin internasional", "Surat dokter"],
        "process": ["Cek syarat", "Medical", "Vaksin", "Surat"],
    },
    "osteoporosis": {
        "name": "Osteoporosis", "slug": "tulang", "sub": "Kesehatan Tulang",
        "hero_label": "PENCEGAHAN & TERAPI", "hero_desc": "Penanganan holistik untuk tulang kuat: obat, nutrisi, latihan, dan infus tulang.",
        "stats": [("BMD", "Scan"), ("IOF", "Guideline"), ("Rumah", "Praktis")],
        "keypoints": ["Tes kepadatan", "Terapi infus", "Latihan beban"],
        "process": ["Skrining", "Diagnosis", "Terapi", "Kontrol"],
    },
    "antar-jemput-rs": {
        "name": "Antar Jemput RS", "slug": "transit", "sub": "Transportasi Medis",
        "hero_label": "TRANSCARE AMBULANCE", "hero_desc": "Antar jemput rumah sakit dengan ambulans berstandar, perawat pendamping, GPS tracking.",
        "stats": [("GPS", "Tracking"), ("ICU", "Peralatan"), ("24/7", "Siap")],
        "keypoints": ["Ambulans lengkap", "Perawat jaga", "Antar jemput"],
        "process": ["Pesan", "Jemput", "Perjalanan", "Tujuan"],
    },
    "perawat-homecare": {
        "name": "Perawat Homecare", "slug": "nurse", "sub": "Perawatan Profesional",
        "hero_label": "PERAWAT BERSERTIFIKAT", "hero_desc": "STR terverifikasi, pengalaman RS rujukan, pendampingan personal dengan empati.",
        "stats": [("STR", "Aktif"), ("RS", "Pengalaman"), ("24h", "Siaga")],
        "keypoints": ["Perawat terampil", "Pendampingan 24h", "Laporan harian"],
        "process": ["Cek kebutuhan", "Cocok perawat", "Mulai jaga", "Evaluasi"],
    },
    "home-lab": {
        "name": "Home Lab", "slug": "lab", "sub": "Cek Darah di Rumah",
        "hero_label": "LABORATORIUM MOBILE", "hero_desc": "Cek darah, profil lipid, gula, fungsi organ — hasil digital dalam 24 jam.",
        "stats": [("Akredit", "Lab"), ("24h", "Hasil"), ("Paket", "Lengkap")],
        "keypoints": ["Cek lab lengkap", "Hasil digital", "Konsultasi dokter"],
        "process": ["Pesan", "Sampling", "Analisa", "Hasil"],
    },
    "vaksinasi-rumah": {
        "name": "Vaksinasi Rumah", "slug": "vaksin", "sub": "Imunisasi Terjadwal",
        "hero_label": "VAKSINASI AMAN", "hero_desc": "Vaksin anak, dewasa, lansia, perjalanan — semua berstandar Kemenkes dan cold chain.",
        "stats": [("BPOM", "Resmi"), ("Cold", "Chain"), ("Lansia", "Lengkap")],
        "keypoints": ["Vaksin terjadwal", "Penyimpanan aman", "Bidan/dokter"],
        "process": ["Konsul", "Pilih jenis", "Suntik", "Sertifikat"],
    },
    "infus-vitamin": {
        "name": "Infus Vitamin", "slug": "infus", "sub": "Stamina & Imunitas",
        "hero_label": "IV THERAPY", "hero_desc": "Vitamin C, B complex, NAD+, glutathione untuk stamina, imun, dan kecantikan kulit.",
        "stats": [("IV", "Bersertifikat"), ("Dokter", "Resep"), ("Steril", "Alkes")],
        "keypoints": ["Cek kebutuhan", "Formula custom", "Monitor langsung"],
        "process": ["Cek darah", "Konsultasi", "Formula", "Infus"],
    },
    "kesehatan-umum": {
        "name": "Kesehatan Umum", "slug": "umum", "sub": "Cek & Rawat",
        "hero_label": "LAYANAN UMUM", "hero_desc": "Cek rutin, keluhan harian, rujukan spesialis, dan tindak lanjut terkoordinasi.",
        "stats": [("7 hari", "Layanan"), ("10+", "Spesialisasi"), ("Rumah", "Aman")],
        "keypoints": ["Cek kesehatan", "Diagnosis tepat", "Rujukan lancar"],
        "process": ["Keluhan", "Assessment", "Diagnosis", "Tindak"],
    },
}


def esc(s):
    return html.escape(str(s), quote=True)


def icon_for(slug):
    """Geometric icon per category — multi-element composition."""
    if slug == "lansia":
        return ('  <circle cx="0" cy="0" r="32" fill="' + P + '" opacity="0.18"/>\n'
                '  <circle cx="0" cy="-8" r="14" fill="none" stroke="' + PD + '" stroke-width="3"/>\n'
                '  <path d="M -16 8 Q -16 -2 0 -2 Q 16 -2 16 8 L 16 24 L -16 24 Z" fill="none" stroke="' + PD + '" stroke-width="3" stroke-linejoin="round"/>\n'
                '  <path d="M -8 24 L -10 30 M 8 24 L 10 30" stroke="' + PD + '" stroke-width="3" stroke-linecap="round"/>\n'
                '  <circle cx="0" cy="-8" r="3" fill="' + A + '"/>')
    if slug == "fisio":
        return ('  <circle cx="0" cy="0" r="34" fill="' + P + '" opacity="0.15"/>\n'
                '  <path d="M -24 -8 L -12 -8 L -8 -24 L 8 -24 L 12 -8 L 24 -8 L 24 8 L 12 8 L 8 24 L -8 24 L -12 8 L -24 8 Z" fill="' + PD + '"/>\n'
                '  <path d="M -10 0 L 10 0 M 0 -10 L 0 10" stroke="' + W + '" stroke-width="3" stroke-linecap="round"/>\n'
                '  <circle cx="0" cy="0" r="4" fill="' + A + '"/>')
    if slug == "dokter":
        return ('  <rect x="-30" y="-30" width="60" height="60" rx="14" fill="' + P + '" opacity="0.15"/>\n'
                '  <rect x="-22" y="-22" width="44" height="44" rx="10" fill="' + W + '" stroke="' + PD + '" stroke-width="3"/>\n'
                '  <path d="M 0 -10 L 0 10 M -10 0 L 10 0" stroke="' + PD + '" stroke-width="4" stroke-linecap="round"/>\n'
                '  <circle cx="0" cy="0" r="3" fill="' + A + '"/>')
    if slug == "parkinson":
        return ('  <circle cx="0" cy="0" r="32" fill="' + P + '" opacity="0.12"/>\n'
                '  <circle cx="0" cy="0" r="28" fill="none" stroke="' + PD + '" stroke-width="2"/>\n'
                '  <circle cx="0" cy="-18" r="5" fill="' + P + '"/>\n'
                '  <circle cx="18" cy="0" r="5" fill="' + A + '"/>\n'
                '  <circle cx="0" cy="18" r="5" fill="' + T + '"/>\n'
                '  <circle cx="-18" cy="0" r="5" fill="' + PD + '"/>\n'
                '  <line x1="0" y1="-18" x2="18" y2="0" stroke="' + PD + '" stroke-width="1.5" opacity="0.5"/>\n'
                '  <line x1="18" y1="0" x2="0" y2="18" stroke="' + PD + '" stroke-width="1.5" opacity="0.5"/>\n'
                '  <line x1="0" y1="18" x2="-18" y2="0" stroke="' + PD + '" stroke-width="1.5" opacity="0.5"/>\n'
                '  <line x1="-18" y1="0" x2="0" y2="-18" stroke="' + PD + '" stroke-width="1.5" opacity="0.5"/>\n'
                '  <circle cx="0" cy="0" r="4" fill="' + PD + '"/>')
    if slug == "study":
        return ('  <circle cx="0" cy="0" r="30" fill="' + P + '" opacity="0.15"/>\n'
                '  <path d="M -24 4 L 0 -10 L 24 4 L 24 16 Q 0 26 -24 16 Z" fill="' + W + '" stroke="' + PD + '" stroke-width="2.5" stroke-linejoin="round"/>\n'
                '  <path d="M 0 -10 L 0 26" stroke="' + PD + '" stroke-width="2"/>\n'
                '  <circle cx="0" cy="-10" r="4" fill="' + A + '"/>\n'
                '  <path d="M -10 -2 L 10 -2" stroke="' + T + '" stroke-width="1.5" opacity="0.5"/>\n'
                '  <path d="M -10 4 L 10 4" stroke="' + T + '" stroke-width="1.5" opacity="0.5"/>')
    if slug == "tulang":
        return ('  <circle cx="0" cy="0" r="32" fill="' + P + '" opacity="0.12"/>\n'
                '  <path d="M -22 14 Q -30 -6 -16 -18 Q -2 -26 6 -16 Q 16 -8 10 4 L 18 12 L 26 6 L 28 18 L 20 24 L 14 16 L 8 20 L 4 24 L -8 26 Q -24 24 -22 14 Z" fill="' + W + '" stroke="' + PD + '" stroke-width="2.5" stroke-linejoin="round"/>\n'
                '  <circle cx="-12" cy="-8" r="3" fill="' + P + '"/>\n'
                '  <circle cx="8" cy="10" r="3" fill="' + A + '"/>\n'
                '  <circle cx="18" cy="6" r="2" fill="' + T + '"/>')
    if slug == "transit":
        return ('  <rect x="-30" y="-18" width="60" height="36" rx="8" fill="' + P + '" opacity="0.12"/>\n'
                '  <rect x="-26" y="-14" width="52" height="28" rx="6" fill="' + W + '" stroke="' + PD + '" stroke-width="2.5"/>\n'
                '  <rect x="-20" y="-8" width="18" height="14" rx="2" fill="' + P + '" opacity="0.4"/>\n'
                '  <rect x="2" y="-8" width="18" height="14" rx="2" fill="' + P + '" opacity="0.4"/>\n'
                '  <circle cx="-16" cy="18" r="7" fill="' + W + '" stroke="' + PD + '" stroke-width="2.5"/>\n'
                '  <circle cx="16" cy="18" r="7" fill="' + W + '" stroke="' + PD + '" stroke-width="2.5"/>\n'
                '  <circle cx="-16" cy="18" r="2.5" fill="' + A + '"/>\n'
                '  <circle cx="16" cy="18" r="2.5" fill="' + A + '"/>\n'
                '  <path d="M -8 -18 L -8 -26 L 8 -26 L 8 -18" fill="none" stroke="' + A + '" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
    if slug == "nurse":
        return ('  <circle cx="0" cy="0" r="32" fill="' + P + '" opacity="0.15"/>\n'
                '  <circle cx="0" cy="-2" r="14" fill="' + W + '" stroke="' + PD + '" stroke-width="2.5"/>\n'
                '  <path d="M -8 -2 a 8 8 0 0 1 16 0" fill="none" stroke="' + A + '" stroke-width="2.5" stroke-linecap="round"/>\n'
                '  <path d="M -4 4 L 4 4 M 0 6 L 0 10" stroke="' + PD + '" stroke-width="2.5" stroke-linecap="round"/>\n'
                '  <path d="M -12 12 Q 0 18 12 12 L 12 24 L -12 24 Z" fill="' + PD + '" opacity="0.2" stroke="' + PD + '" stroke-width="2"/>\n'
                '  <path d="M 0 -16 L 0 8 M -10 0 L 10 0" stroke="' + P + '" stroke-width="2.5" stroke-linecap="round" opacity="0.5"/>')
    if slug == "lab":
        return ('  <circle cx="0" cy="0" r="32" fill="' + P + '" opacity="0.12"/>\n'
                '  <path d="M -8 -22 L -8 -4 L -22 22 Q -24 30 -16 30 L 16 30 Q 24 30 22 22 L 8 -4 L 8 -22 Z" fill="' + W + '" stroke="' + PD + '" stroke-width="2.5" stroke-linejoin="round"/>\n'
                '  <line x1="-14" y1="-22" x2="14" y2="-22" stroke="' + A + '" stroke-width="3" stroke-linecap="round"/>\n'
                '  <path d="M 0 4 L 0 26" stroke="' + PD + '" stroke-width="1" stroke-dasharray="2 2" opacity="0.4"/>\n'
                '  <circle cx="-4" cy="14" r="2.5" fill="' + P + '"/>\n'
                '  <circle cx="6" cy="10" r="2.5" fill="' + A + '"/>\n'
                '  <circle cx="-2" cy="22" r="2.5" fill="' + T + '"/>')
    if slug == "vaksin":
        return ('  <circle cx="0" cy="0" r="32" fill="' + P + '" opacity="0.12"/>\n'
                '  <path d="M 0 -24 L 0 18" stroke="' + PD + '" stroke-width="3" stroke-linecap="round"/>\n'
                '  <path d="M -6 24 L 6 24 L 0 30 Z" fill="' + P + '"/>\n'
                '  <path d="M 0 -12 L 0 -4" stroke="' + A + '" stroke-width="3" stroke-linecap="round"/>\n'
                '  <path d="M 0 -12 L 8 -12" stroke="' + A + '" stroke-width="3" stroke-linecap="round"/>\n'
                '  <path d="M 0 -24 L 0 -20 M -3 -22 L 3 -22" stroke="' + PD + '" stroke-width="2" stroke-linecap="round"/>\n'
                '  <circle cx="0" cy="-24" r="3" fill="' + A + '"/>')
    if slug == "infus":
        return ('  <circle cx="0" cy="0" r="32" fill="' + P + '" opacity="0.12"/>\n'
                '  <rect x="-10" y="-26" width="20" height="22" rx="3" fill="' + W + '" stroke="' + PD + '" stroke-width="2.5"/>\n'
                '  <rect x="-7" y="-23" width="14" height="16" rx="2" fill="' + P + '" opacity="0.4"/>\n'
                '  <path d="M 0 -4 L 0 16 L -8 26 L 8 26 L 0 16" fill="none" stroke="' + PD + '" stroke-width="2.5" stroke-linejoin="round"/>\n'
                '  <path d="M -4 -18 L 4 -18" stroke="' + A + '" stroke-width="2.5" stroke-linecap="round"/>\n'
                '  <circle cx="0" cy="6" r="2.5" fill="' + P + '"/>\n'
                '  <circle cx="0" cy="14" r="2.5" fill="' + A + '"/>\n'
                '  <circle cx="0" cy="22" r="2.5" fill="' + T + '"/>')
    # umum
    return ('  <circle cx="0" cy="0" r="32" fill="' + P + '" opacity="0.12"/>\n'
            '  <path d="M 0 -24 L 6 -6 L 24 -6 L 10 4 L 14 22 L 0 10 L -14 22 L -10 4 L -24 -6 L -6 -6 Z" fill="' + W + '" stroke="' + PD + '" stroke-width="2.5" stroke-linejoin="round"/>\n'
            '  <circle cx="0" cy="2" r="3" fill="' + A + '"/>')


def build_v1(cat_id, c):
    """Editorial hero with refined composition."""
    pdir = f"/home/gobeam/Projects/joyofcare-web/content-source/articles/{cat_id}"
    article_count = len([f for f in os.listdir(pdir) if f.endswith('.txt')]) if os.path.isdir(pdir) else 0

    stats_lines = []
    for i, (val, lbl) in enumerate(c["stats"]):
        x = 24 + i * 176
        if i > 0:
            sep_x = i * 176
            stats_lines.append(f'    <line x1="{sep_x}" y1="14" x2="{sep_x}" y2="62" stroke="{SOFT}" stroke-width="1"/>')
        stats_lines.append(f'    <text x="{x}" y="40" font-family="Montserrat, sans-serif" font-size="24" font-weight="800" fill="{PD}">{esc(val)}</text>')
        stats_lines.append(f'    <text x="{x}" y="60" font-family="Inter, sans-serif" font-size="12" font-weight="500" fill="{SLATE}" letter-spacing="0.5">{esc(lbl)}</text>')
    stats_html = "\n".join(stats_lines)

    icon = icon_for(c["slug"])

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img" aria-label="Kategori {esc(c["name"])} - JoyofCare">
<title>{esc(c["name"])} - Joy of Care</title>
<desc>Editorial thumbnail kategori {esc(c["name"])} — JoyofCare.</desc>
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BG}"/><stop offset="1" stop-color="{BG2}"/></linearGradient>
<radialGradient id="orb" cx="0.3" cy="0.3"><stop offset="0" stop-color="{L}"/><stop offset="0.6" stop-color="{P}"/><stop offset="1" stop-color="{PD}"/></radialGradient>
<linearGradient id="pri" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{P}"/><stop offset="1" stop-color="{PD}"/></linearGradient>
<pattern id="grid" x="0" y="0" width="48" height="48" patternUnits="userSpaceOnUse"><path d="M 48 0 L 0 0 0 48" fill="none" stroke="{P}" stroke-width="0.5" opacity="0.08"/></pattern>
<filter id="card" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur in="SourceAlpha" stdDeviation="6"/><feOffset dx="0" dy="4"/><feComponentTransfer><feFuncA type="linear" slope="0.1"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur in="SourceAlpha" stdDeviation="10"/><feOffset dx="0" dy="6"/><feComponentTransfer><feFuncA type="linear" slope="0.18"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="1200" height="630" fill="url(#bg)"/>
<rect width="1200" height="630" fill="url(#grid)"/>
<circle cx="1080" cy="120" r="200" fill="{P}" opacity="0.05"/>
<circle cx="1140" cy="220" r="100" fill="{A}" opacity="0.08"/>
<circle cx="980" cy="500" r="80" fill="{T}" opacity="0.06"/>
<g transform="translate(72, 80)">
<rect x="0" y="0" width="56" height="4" rx="2" fill="{A}"/>
<text x="68" y="8" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="{PD}" letter-spacing="2.5">{esc(c["hero_label"])}</text>
<text x="0" y="86" font-family="Montserrat, sans-serif" font-size="68" font-weight="800" fill="{INK}" letter-spacing="-2">{esc(c["name"])}</text>
<text x="0" y="156" font-family="Montserrat, sans-serif" font-size="32" font-weight="500" fill="{PD}">{esc(c["sub"])}</text>
<text x="0" y="204" font-family="Inter, sans-serif" font-size="17" fill="{SLATE}">{esc(c["hero_desc"])}</text>
<g transform="translate(0, 252)" filter="url(#card)">
<rect x="0" y="0" width="528" height="80" rx="16" fill="{W}"/>
{stats_html}
</g>
<g transform="translate(0, 360)">
<rect x="0" y="0" width="220" height="52" rx="26" fill="url(#pri)" filter="url(#soft)"/>
<text x="110" y="32" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="{W}" text-anchor="middle">Konsultasi Gratis →</text>
<text x="240" y="32" font-family="Inter, sans-serif" font-size="14" fill="{SLATE}">📲 08811-118-911</text>
</g>
</g>
<g transform="translate(820, 200)">
<circle cx="180" cy="120" r="180" fill="url(#orb)" filter="url(#soft)"/>
<circle cx="180" cy="120" r="180" fill="{W}" opacity="0.92"/>
<circle cx="180" cy="120" r="140" fill="url(#bg)"/>
<circle cx="180" cy="120" r="160" fill="none" stroke="{P}" stroke-width="1" opacity="0.3" stroke-dasharray="2 6"/>
<circle cx="180" cy="120" r="100" fill="none" stroke="{A}" stroke-width="1" opacity="0.3"/>
<g transform="translate(180, 120)">
{icon}
</g>
<text x="180" y="320" font-family="Montserrat, sans-serif" font-size="13" font-weight="700" fill="{PD}" text-anchor="middle" letter-spacing="1.5">{esc(article_count)} ARTIKEL TERSEDIA</text>
</g>
<g transform="translate(72, 552)">
<circle cx="10" cy="10" r="10" fill="{P}"/>
<path d="M 6 10 a 4 4 0 0 1 8 0" fill="none" stroke="{W}" stroke-width="1.5" stroke-linecap="round"/>
<text x="30" y="9" font-family="Montserrat, sans-serif" font-size="14" font-weight="700" fill="{PD}">Joy</text>
<text x="58" y="9" font-family="Montserrat, sans-serif" font-size="14" font-weight="500" fill="{INK}">of Care</text>
<text x="30" y="24" font-family="Inter, sans-serif" font-size="11" fill="{SLATE}">joyofcare.net/blog/{esc(cat_id)}</text>
</g>
</svg>'''


def build_v2(cat_id, c):
    """3-card benefit grid."""
    cards = []
    gradients = [f"url(#c2pri)", f"url(#c2acc)", f"url(#c2teal)"]
    accents = [A, P, T]
    for i, kp in enumerate(c["keypoints"]):
        cards.append(f'''<g transform="translate({i*360}, 0)" filter="url(#c2)">
<rect x="0" y="0" width="340" height="280" rx="20" fill="{W}"/>
<rect x="0" y="0" width="340" height="6" rx="3" fill="{gradients[i]}"/>
<circle cx="56" cy="60" r="32" fill="{gradients[i]}"/>
<text x="56" y="68" font-family="Montserrat, sans-serif" font-size="28" font-weight="800" fill="{W}" text-anchor="middle">{i+1:02d}</text>
<text x="24" y="138" font-family="Montserrat, sans-serif" font-size="20" font-weight="700" fill="{INK}">{esc(kp)}</text>
<text x="24" y="180" font-family="Inter, sans-serif" font-size="14" fill="{SLATE}">Pelayanan prima oleh tim</text>
<text x="24" y="200" font-family="Inter, sans-serif" font-size="14" fill="{SLATE}">bersertifikat Dinkes</text>
<line x1="24" y1="232" x2="48" y2="232" stroke="{accents[i]}" stroke-width="3" stroke-linecap="round"/>
</g>''')
    cards_html = "\n".join(cards)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img" aria-label="Manfaat {esc(c["name"])} - JoyofCare">
<title>Manfaat {esc(c["name"])} - Joy of Care</title>
<desc>Infografis 3 manfaat utama layanan {esc(c["name"])}.</desc>
<defs>
<linearGradient id="c2bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG}"/><stop offset="1" stop-color="{BG2}"/></linearGradient>
<linearGradient id="c2pri" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{P}"/><stop offset="1" stop-color="{PD}"/></linearGradient>
<linearGradient id="c2acc" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{A}"/><stop offset="1" stop-color="{AL}"/></linearGradient>
<linearGradient id="c2teal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{T}"/><stop offset="1" stop-color="#155E75"/></linearGradient>
<pattern id="c2dot" x="0" y="0" width="32" height="32" patternUnits="userSpaceOnUse"><circle cx="16" cy="16" r="1" fill="{P}" opacity="0.15"/></pattern>
<filter id="c2" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur in="SourceAlpha" stdDeviation="8"/><feOffset dx="0" dy="4"/><feComponentTransfer><feFuncA type="linear" slope="0.1"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="1200" height="630" fill="url(#c2bg)"/>
<rect width="1200" height="630" fill="url(#c2dot)"/>
<g transform="translate(72, 64)">
<rect x="0" y="0" width="48" height="3" rx="1.5" fill="{A}"/>
<text x="60" y="6" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="{PD}" letter-spacing="2.5">3 MANFAAT UTAMA</text>
<text x="0" y="68" font-family="Montserrat, sans-serif" font-size="48" font-weight="800" fill="{INK}">Mengapa pilih</text>
<text x="0" y="124" font-family="Montserrat, sans-serif" font-size="48" font-weight="800" fill="url(#c2pri)">{esc(c["name"])}</text>
<text x="0" y="168" font-family="Inter, sans-serif" font-size="16" fill="{SLATE}">Komitmen kami untuk setiap keluarga di Jabodetabek.</text>
</g>
<g transform="translate(72, 280)">
{cards_html}
</g>
<g transform="translate(1100, 600)" text-anchor="end">
<text x="0" y="-12" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="{PD}">joyofcare.net/blog/{esc(cat_id)}</text>
<text x="0" y="4" font-family="Montserrat, sans-serif" font-size="14" font-weight="800" fill="{PD}">Joy</text>
<text x="-26" y="4" font-family="Montserrat, sans-serif" font-size="14" font-weight="500" fill="{INK}">of Care</text>
</g>
</svg>'''


def build_v3(cat_id, c):
    """4-step process flow."""
    steps = c["process"]
    step_g = []
    for i, step in enumerate(steps):
        x = i * 270
        is_last = i == len(steps) - 1
        fill = "url(#c3acc)" if is_last else "url(#c3pri)"
        accent_line = A if is_last else P
        step_g.append(f'''<g transform="translate({x}, 0)">
<circle cx="60" cy="50" r="44" fill="{W}" filter="url(#c3)"/>
<circle cx="60" cy="50" r="36" fill="{fill}"/>
<text x="60" y="60" font-family="Montserrat, sans-serif" font-size="22" font-weight="800" fill="{W}" text-anchor="middle">{i+1:02d}</text>
<text x="60" y="124" font-family="Montserrat, sans-serif" font-size="15" font-weight="700" fill="{INK}" text-anchor="middle">{esc(step)}</text>
<line x1="42" y1="140" x2="78" y2="140" stroke="{accent_line}" stroke-width="2" stroke-linecap="round"/>
</g>''')
    steps_html = "\n".join(step_g)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img" aria-label="Proses {esc(c["name"])} - JoyofCare">
<title>Proses {esc(c["name"])} - Joy of Care</title>
<desc>Alur {len(steps)} langkah mudah layanan {esc(c["name"])}.</desc>
<defs>
<linearGradient id="c3bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BG}"/><stop offset="1" stop-color="{BG2}"/></linearGradient>
<linearGradient id="c3pri" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{P}"/><stop offset="1" stop-color="{T}"/></linearGradient>
<linearGradient id="c3acc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{A}"/><stop offset="1" stop-color="{AL}"/></linearGradient>
<pattern id="c3diag" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="20" stroke="{P}" stroke-width="0.5" opacity="0.1"/></pattern>
<filter id="c3" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur in="SourceAlpha" stdDeviation="6"/><feOffset dx="0" dy="4"/><feComponentTransfer><feFuncA type="linear" slope="0.1"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="1200" height="630" fill="url(#c3bg)"/>
<rect width="1200" height="630" fill="url(#c3diag)"/>
<g transform="translate(72, 64)">
<rect x="0" y="0" width="48" height="3" rx="1.5" fill="{A}"/>
<text x="60" y="6" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="{PD}" letter-spacing="2.5">ALUR LAYANAN</text>
<text x="0" y="68" font-family="Montserrat, sans-serif" font-size="48" font-weight="800" fill="{INK}">{len(steps)} langkah mudah</text>
<text x="0" y="124" font-family="Montserrat, sans-serif" font-size="48" font-weight="800" fill="url(#c3pri)">{esc(c["name"])}</text>
<text x="0" y="168" font-family="Inter, sans-serif" font-size="16" fill="{SLATE}">Dari konsultasi pertama hingga tindak lanjut berkualitas.</text>
</g>
<g transform="translate(72, 320)">
<line x1="60" y1="50" x2="{60 + (len(steps)-1)*270}" y2="50" stroke="{SOFT}" stroke-width="2" stroke-dasharray="6 6"/>
{steps_html}
</g>
<g transform="translate(72, 540)">
<rect x="0" y="0" width="320" height="56" rx="28" fill="url(#c3acc)" filter="url(#c3)"/>
<text x="160" y="34" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="{W}" text-anchor="middle">Mulai dari WhatsApp →</text>
</g>
<g transform="translate(420, 540)">
<text x="0" y="22" font-family="Inter, sans-serif" font-size="13" font-weight="600" fill="{PD}">📲 Hubungi:</text>
<text x="0" y="42" font-family="Montserrat, sans-serif" font-size="18" font-weight="700" fill="{PD}">08811-118-911</text>
</g>
<g transform="translate(1100, 600)" text-anchor="end">
<text x="0" y="-12" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="{PD}">joyofcare.net/blog/{esc(cat_id)}</text>
<text x="0" y="4" font-family="Montserrat, sans-serif" font-size="14" font-weight="800" fill="{PD}">Joy</text>
<text x="-26" y="4" font-family="Montserrat, sans-serif" font-size="14" font-weight="500" fill="{INK}">of Care</text>
</g>
</svg>'''


def main():
    for cat_id, c in CATS.items():
        for v, builder in [(1, build_v1), (2, build_v2), (3, build_v3)]:
            fname = f"{cat_id}.svg" if v == 1 else f"{cat_id}-v{v}.svg"
            svg = builder(cat_id, c)
            with open(os.path.join(BLOG_DIR, fname), "w") as f:
                f.write(svg)
            print(f"Created: {fname}")
    print(f"\nTotal: {len(CATS)*3} SVGs in {BLOG_DIR}")

if __name__ == "__main__":
    main()