#!/usr/bin/env python3
"""
Generate upgraded visual assets for Joy of Care:
1. Human-Centric Category Thumbnails (3 variants per category x 12 categories = 36 SVGs + primary banners + legacy assets).
2. Clean top badge (no star rating x/y bullet, accurate compliant claims).
3. Relevant, high-impact 4:5 infographics for 1 out of 3 articles across all 12 categories (48 article infographics).
4. Fully integrated with official joc_icon.png and joc_long.png logo assets.
5. Synced to both joyofcare-web/assets and joyofcare-net/visual-assets.
"""
import os
import io
import re
import html
import json
import glob
import base64
import textwrap
import yaml
from PIL import Image

BASE_NET = "/home/gobeam/Projects/joyofcare-net"
BASE_WEB = "/home/gobeam/Projects/joyofcare-web"

WEB_THUMBS = os.path.join(BASE_WEB, "assets", "thumbnails")
WEB_BLOG = os.path.join(BASE_WEB, "assets", "blog")
WEB_INFOS = os.path.join(BASE_WEB, "assets", "infographics")

NET_THUMBS = os.path.join(BASE_NET, "visual-assets", "thumbnails")
NET_INFOS = os.path.join(BASE_NET, "visual-assets", "infographics")

for d in [WEB_THUMBS, WEB_BLOG, WEB_INFOS, NET_THUMBS, NET_INFOS]:
    os.makedirs(d, exist_ok=True)

# Image map for the 12 categories
IMAGE_FILES = {
    "fisioterapi-rumah": os.path.join(BASE_WEB, "public/images/layanan-fisioterapi-ke-rumah/1.jpg"),
    "perawatan-lansia": os.path.join(BASE_WEB, "public/images/layanan-perawat-di-rumah/1.jpg"),
    "panggil-dokter": os.path.join(BASE_WEB, "public/images/panggil-dokter-ke-rumah/1.jpg"),
    "parkinson": os.path.join(BASE_WEB, "public/images/parkinson-care.jpg"),
    "studi-luar-negeri": os.path.join(BASE_WEB, "public/images/studi-luar-negeri.jpg"),
    "osteoporosis": os.path.join(BASE_WEB, "public/images/osteoporosis-care.jpg"),
    "antar-jemput-rs": os.path.join(BASE_WEB, "public/images/transcare-antar-jemput-ke-rs-jakarta-tangerang/1.jpg"),
    "perawat-homecare": os.path.join(BASE_WEB, "public/images/layanan-perawat-di-rumah/2.jpg"),
    "home-lab": os.path.join(BASE_WEB, "public/images/homelab/1.jpg"),
    "vaksinasi-rumah": os.path.join(BASE_WEB, "public/images/panggil-dokter-ke-rumah/3.jpg"),
    "infus-vitamin": os.path.join(BASE_WEB, "public/images/infus-suntik-vitamin-di-rumah/1.jpg"),
    "kesehatan-umum": os.path.join(BASE_WEB, "public/images/layanan-akupuntur-di-rumah/1.png"),
}

def get_base64_image(filepath, max_dim=800, quality=84):
    """Load, square-crop / resize, and base64-encode image as JPEG."""
    img = Image.open(filepath)
    if img.mode != "RGB":
        img = img.convert("RGB")
    w, h = img.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    img_cropped = img.crop((left, top, left + min_dim, top + min_dim))
    img_cropped.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    img_cropped.save(buf, format="JPEG", quality=quality, optimize=True)
    return base64.b64encode(buf.getvalue()).decode("utf-8")

def get_png_b64(path, max_dim=None):
    """Load and base64-encode PNG with transparency."""
    im = Image.open(path)
    if max_dim:
        im.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode("utf-8")

# Official JoC Brand Logos
B64_JOC_ICON = get_png_b64(os.path.join(BASE_WEB, "public/images/joc_icon.png"), 160)
B64_JOC_LONG = get_png_b64(os.path.join(BASE_WEB, "public/images/joc_long.png"))

# Cache category base64 images
IMAGE_B64 = {}
for cat_id, fpath in IMAGE_FILES.items():
    if os.path.exists(fpath):
        IMAGE_B64[cat_id] = get_base64_image(fpath)
    else:
        print(f"Warning: file not found: {fpath}")

# Category metadata with compliant claims and no star x/y bullets
CATEGORIES_METADATA = {
    "perawatan-lansia": {
        "name": "Perawatan Lansia",
        "short": "Lansia",
        "punchy_hero": ("Rawat Lansia", "Penuh Kasih di Rumah"),
        "subtitle": "Pendampingan geriatri terpercaya dan penuh perhatian untuk kenyamanan Opa & Oma di rumah.",
        "badge": "PERAWATAN LANSIA GERIATRI",
        "trust": [
            "Perawat Berizin & Berpengalaman RS",
            "Pendampingan Pasien Mandiri & Empatik",
            "Laporan Medis Berkala untuk Keluarga"
        ],
        "pill1": "Dipercaya keluarga",
        "pill2": "● Siaga Homecare 24 Jam",
        "cta": "Konsultasi Lansia Gratis →",
        "steps": [
            ("Skrining Kebutuhan", "Evaluasi kondisi fisik & psikologis lansia di rumah", "Profil geriatri"),
            ("Pencocokan Perawat", "Pemilihan tenaga medis sesuai kebiasaan Opa/Oma", "Perawat terverifikasi"),
            ("Pendampingan Rutin", "Perawatan harian, nutrisi, mobilitas & jadwal obat", "Aktivitas teratur"),
            ("Monitoring Berkala", "Laporan vital sign & koordinasi dokter penanggung", "Keluarga tenang")
        ],
        "benefit_title": ("Kenyamanan Lansia,", "Ketenangan Keluarga"),
        "benefit_sub": "Menghindari risiko kelelahan dan infeksi silang rumah sakit dengan perawatan homecare terbaik.",
    },
    "fisioterapi-rumah": {
        "name": "Fisioterapi Rumah",
        "short": "Fisioterapi",
        "punchy_hero": ("Pemulihan Stroke", "di Rumah Anda"),
        "subtitle": "Kembalikan mobilitas fisik mandiri dengan bimbingan fisioterapis profesional langsung di kenyamanan rumah.",
        "badge": "FISIOTERAPI PROFESIONAL DI RUMAH",
        "trust": [
            "Fisioterapis Berizin Resmi (STR)",
            "Latihan Terukur & Evaluasi Berkala",
            "Privasi Terjaga Tanpa Antre di RS"
        ],
        "pill1": "100+ Pasien terlayani",
        "pill2": "● Home Visit Jabodetabek",
        "cta": "Konsultasi Fisio Gratis →",
        "steps": [
            ("Evaluasi Awal", "Pemeriksaan rentang gerak sendi (ROM) & kekuatan otot", "Baseline motorik"),
            ("Rencana Latihan", "Modul latihan spesifik disesuaikan target mandiri pasien", "Jadwal terukur"),
            ("Sesi Terapi", "Bimbingan intensif 1-on-1 dengan stimulasi modern", "Latihan aman"),
            ("Evaluasi Progres", "Pengukuran capaian gerak mingguan secara objektif", "Laporan kemajuan")
        ],
        "benefit_title": ("Pulih Lebih Cepat,", "Bebas dari Ketergantungan"),
        "benefit_sub": "Latihan personal di lingkungan rumah yang familiar terbukti mempercepat pemulihan fungsi neuromuskular.",
    },
    "panggil-dokter": {
        "name": "Panggil Dokter",
        "short": "Dokter Rumah",
        "punchy_hero": ("Dokter Profesional", "Datang ke Rumah"),
        "subtitle": "Pemeriksaan medis menyeluruh, diagnosis tepat, dan resep obat langsung tanpa repot keluar rumah.",
        "badge": "PANGGIL DOKTER KE RUMAH",
        "trust": [
            "Dokter Berizin Resmi (SIP Aktif)",
            "Kunjungan Dokter Umum & Spesialis",
            "Resep Digital & Tindakan Medis Lengkap"
        ],
        "pill1": "Respon Non Emergency",
        "pill2": "● Dokter Umum & Spesialis",
        "cta": "Panggil Dokter Sekarang →",
        "steps": [
            ("Booking Kunjungan", "Konsultasi awal keluhan via WhatsApp resmi", "Jadwal fleksibel"),
            ("Dokter Tiba", "Kunjungan dokter ber-SIP dengan peralatan lengkap", "Tepat waktu"),
            ("Pemeriksaan Fisik", "Diagnosis menyeluruh di tempat & resep digital", "Penanganan akurat"),
            ("Tindak Lanjut", "Pantau kondisi berkala dan konsultasi lanjutan", "Pemulihan terjaga")
        ],
        "benefit_title": ("Kesehatan Prioritas,", "Bebas Antrean Rumah Sakit"),
        "benefit_sub": "Dapatkan perhatian klinis privat tanpa stres menunggu lama di ruang tunggu faskes umum.",
    },
    "parkinson": {
        "name": "Penyakit Parkinson",
        "short": "Parkinson",
        "punchy_hero": ("Dukungan Parkinson", "Terpadu di Rumah"),
        "subtitle": "Fisioterapi neuromotorik, latihan keseimbangan, dan panduan obat untuk menjaga kemandirian gerak pasien.",
        "badge": "TERAPI PARKINSON & NEUROMOTOR",
        "trust": [
            "Latihan Motorik & Koordinasi Ritmik",
            "Latihan Keseimbangan Cegah Risiko Jatuh",
            "Edukasi & Pendampingan Holistik Keluarga"
        ],
        "pill1": "Perawat terdaftar",
        "pill2": "● Pendampingan Khusus Saraf",
        "cta": "Konsultasi Parkinson →",
        "steps": [
            ("Asesmen Neuromotor", "Pemeriksaan kekakuan, tremor & pola jalan", "Skoring mobilitas"),
            ("Program Terapi Gerak", "Latihan langkah besar & koordinasi ritmik", "Modul khusus"),
            ("Manajemen Obat", "Sinkronisasi waktu obat dan sesi latihan gerak", "Efek optimal"),
            ("Evaluasi Stabilitas", "Pemantauan kemandirian aktivitas harian (ADL)", "Cegah jatuh")
        ],
        "benefit_title": ("Stabilitas Gerak,", "Kualitas Hidup Optimal"),
        "benefit_sub": "Latihan konsisten membantu mempertahankan kelenturan otot dan mencegah komplikasi penurunan gerak.",
    },
    "studi-luar-negeri": {
        "name": "Studi Luar Negeri",
        "short": "Medical Visa",
        "punchy_hero": ("Medical Check-Up", "Studi Luar Negeri"),
        "subtitle": "Pemeriksaan kesehatan, vaksinasi internasional, dan surat keterangan medis resmi berstandar global.",
        "badge": "LAYANAN KESEHATAN STUDI GLOBAL",
        "trust": [
            "Format Resmi Universitas & Imigrasi",
            "Vaksinasi Internasional & Buku Kuning",
            "Hasil Cepat dengan Tanda Tangan Dokter"
        ],
        "pill1": "Beragam Negara Tujuan",
        "pill2": "● Dokumen Resmi Bermaterai",
        "cta": "Cek Syarat Medis Visa →",
        "steps": [
            ("Verifikasi Formulir", "Pengecekan syarat universitas (UK, US, Aus, dll)", "Checklist valid"),
            ("Pemeriksaan Lab & MCU", "Tes darah, rontgen, dan skrining infeksi", "Lab akreditasi"),
            ("Vaksinasi Wajib", "Pemberian vaksin sesuai regulasi negara tujuan", "Sertifikat resmi"),
            ("Penerbitan Berkas", "Dokumen medis bertanda tangan dokter & cap resmi", "Siap apply visa")
        ],
        "benefit_title": ("Proses Cepat,", "100% Lolos Verifikasi Medis"),
        "benefit_sub": "Didampingi tim medis berpengalaman agar seluruh form kesehatan kampus dan visa terpenuhi tanpa kendala.",
    },
    "osteoporosis": {
        "name": "Osteoporosis",
        "short": "Kepadatan Tulang",
        "punchy_hero": ("Tulang Kuat Lansia", "Bebas Patah Tulang"),
        "subtitle": "Skrining kepadatan tulang, terapi nutrisi & infus kalsium, serta latihan beban terarah di rumah.",
        "badge": "PENCEGAHAN & TERAPI OSTEOPOROSIS",
        "trust": [
            "Fisioterapis Berizin & Terdaftar Resmi",
            "Layanan Terapi Infus Kalsium di Rumah",
            "Latihan Penguatan Otot Penopang Rangka"
        ],
        "pill1": "Fisioterapi terdaftar",
        "pill2": "● Proteksi Fraktur Lansia",
        "cta": "Konsultasi Tulang Sehat →",
        "steps": [
            ("Skrining Risiko", "Kuesioner FRAX & evaluasi riwayat fraktur", "Tingkat risiko"),
            ("Tes Kepadatan Tulang", "Pemeriksaan biomarker kalsium & vitamin D", "Hasil akurat"),
            ("Pemberian Terapi", "Injeksi/infus penguat tulang & suplemen", "Dosis presisi"),
            ("Latihan Penopang", "Fisioterapi weight-bearing aman untuk sendi", "Mobilitas tegak")
        ],
        "benefit_title": ("Masa Tua Aktif,", "Rangka Kokoh Terlindungi"),
        "benefit_sub": "Mencegah kerapuhan tulang secara dini menjaga lansia tetap produktif dan percaya diri bergerak bebas.",
    },
    "antar-jemput-rs": {
        "name": "Antar Jemput RS",
        "short": "TransCare Medis",
        "punchy_hero": ("TransCare Medis", "Aman ke Rumah Sakit"),
        "subtitle": "Ambulans berstandar rumah sakit dengan pendampingan perawat, tandu medis, dan monitoring tanda vital.",
        "badge": "TRANSCARE AMBULANS JABODETABEK",
        "trust": [
            "Armada Ambulans Lengkap & Higienis",
            "Perawat Pendamping Berlisensi Selama Jalan",
            "GPS Tracking Real-Time & Tepat Waktu"
        ],
        "pill1": "Tepat Waktu & Nyaman",
        "pill2": "● Siaga Medis 24/7",
        "cta": "Pesan Antar Jemput RS →",
        "steps": [
            ("Pemesanan Jadwal", "Koordinasi jam kontrol dokter & kondisi pasien", "Slot konfirmasi"),
            ("Penjemputan Tepat", "Ambulans tiba di rumah dengan perawat jaga", "Transfer aman"),
            ("Perjalanan Terpantau", "Monitoring oksigen, infus & tanda vital di ambulans", "Kenyamanan prima"),
            ("Tiba di Faskes", "Pendampingan hingga poli/ruang rawat rumah sakit", "Layanan tuntas")
        ],
        "benefit_title": ("Perjalanan Tenang,", "Pasien Nyaman Tanpa Lelah"),
        "benefit_sub": "Hindari risiko cedera transfer mobil pribadi dengan perlengkapan tandu dan perawat standby.",
    },
    "perawat-homecare": {
        "name": "Perawat Homecare",
        "short": "Perawat Medis",
        "punchy_hero": ("Perawat Medis STR", "Siaga di Rumah"),
        "subtitle": "Perawatan luka diabetes, pasca operasi, pemasangan NGT/kateter, serta pendampingan 24 jam penuh empati.",
        "badge": "PERAWAT HOMECARE BERSERTIFIKAT",
        "trust": [
            "STR Aktif & Lolos Uji Kompetensi Klinis",
            "Pengalaman Ruang Rawat Inap Rumah Sakit",
            "Laporan Asuhan Keperawatan Harian"
        ],
        "pill1": "Perawat terdaftar",
        "pill2": "● Shift 12 Jam / 24 Jam",
        "cta": "Pilih Perawat Homecare →",
        "steps": [
            ("Asesmen Tindakan", "Identifikasi kebutuhan perawatan medis di rumah", "Rencana tindakan"),
            ("Penugasan Perawat", "Pencocokan perawat berkeahlian spesifik", "Profil perawat"),
            ("Pelaksanaan Asuhan", "Perawatan luka, obat, nutrisi, & tanda vital", "Steril & teliti"),
            ("Laporan Digital", "Pencatatan perkembangan pasien untuk keluarga", "Transparan")
        ],
        "benefit_title": ("Tindakan Klinis Steril,", "Perhatian Penuh Kasih"),
        "benefit_sub": "Mengurangi beban fisik keluarga dengan dukungan perawat profesional yang telaten dan terlatih.",
    },
    "home-lab": {
        "name": "Home Lab",
        "short": "Cek Darah Lab",
        "punchy_hero": ("Cek Darah Lengkap", "di Rumah Anda"),
        "subtitle": "Pengambilan sampel darah & urin nyaman oleh analis lab resmi, hasil digital keluar cepat dalam 24 jam.",
        "badge": "LABORATORIUM KLINIS MOBILE",
        "trust": [
            "Kerjasama Laboratorium Terakreditasi Nasional",
            "Petugas Flebotomi Bersertifikat & Jarum Steril",
            "Hasil Digital PDF Cepat & Konsultasi Dokter"
        ],
        "pill1": "Hasil 24 jam digital",
        "pill2": "● Tanpa Antre di Faskes",
        "cta": "Pesan Cek Darah di Rumah →",
        "steps": [
            ("Pilih Paket Tes", "Pilih cek darah rutin, diabetes, kolesterol, organ", "Harga transparan"),
            ("Sampling di Rumah", "Petugas lab datang dengan alat sekali pakai steril", "Proses cepat"),
            ("Analisis Lab", "Sampel diuji di mesin laboratorium akreditasi", "Presisi tinggi"),
            ("Hasil Digital", "Laporan hasil dikirim via WhatsApp & email", "Konsul dokter")
        ],
        "benefit_title": ("Deteksi Dini Praktis,", "Tanpa Hambatan Transport"),
        "benefit_sub": "Sangat ideal bagi lansia, pasien bedridden, atau keluarga sibuk yang memerlukan pemantauan rutin.",
    },
    "vaksinasi-rumah": {
        "name": "Vaksinasi Rumah",
        "short": "Vaksinasi",
        "punchy_hero": ("Vaksinasi Aman", "Langsung ke Rumah"),
        "subtitle": "Vaksin influenza, pneumonia, herpes zoster, dan hepatitis berstandar cold-chain resmi disuntikkan dokter/perawat.",
        "badge": "VAKSINASI KELUARGA & LANSIA",
        "trust": [
            "Cold-Chain Terjaga (Suhu 2-8°C Aman)",
            "Vaksin Original Resmi Distributor Berizin",
            "Dilakukan oleh Dokter / Tenaga Medis Terlatih"
        ],
        "pill1": "Vaksinasi Aman Terjamin",
        "pill2": "● Dewasa, Anak & Lansia",
        "cta": "Pesan Jadwal Vaksinasi →",
        "steps": [
            ("Konsultasi Riwayat", "Pengecekan riwayat alergi & jadwal vaksinasi", "Skrining aman"),
            ("Penyimpanan Vaksin", "Vaksin dibawa dalam coolbox ber-termometer resmi", "Kualitas terjaga"),
            ("Injeksi Medis", "Penyuntikan steril dengan observasi KIPI 15 menit", "Nyaman & aman"),
            ("Pencatatan Vaksin", "Pemberian buku/kartu vaksinasi resmi", "Jadwal booster")
        ],
        "benefit_title": ("Proteksi Maksimal,", "Keluarga Terlindungi Sehat"),
        "benefit_sub": "Cegah pneumonia dan influenza berat pada lansia dengan imunisasi tepat waktu tanpa risiko tertular di RS.",
    },
    "infus-vitamin": {
        "name": "Infus Vitamin",
        "short": "IV Vitamin",
        "punchy_hero": ("Infus Vitamin Medis", "Kembalikan Stamina"),
        "subtitle": "Injeksi & infus Vitamin C, B-Complex, Neurobion, dan Glutathione untuk imun optimal dan pemulihan cepat.",
        "badge": "IV THERAPY & IMMUNE BOOSTER",
        "trust": [
            "Formula Medis Terdaftar BPOM Resmi",
            "Tindakan Steril oleh Perawat / Dokter Ber-STR",
            "Monitoring Keamanan Reaksi Selama Prosedur"
        ],
        "pill1": "Formula Medis Teruji",
        "pill2": "● Penyerapan 100% Seluler",
        "cta": "Pesan Infus Vitamin →",
        "steps": [
            ("Konsultasi Kondisi", "Pemeriksaan keluhan kelelahan & tanda vital", "Formula tepat"),
            ("Pemasangan Infus", "Akses vena lembut oleh perawat berpengalaman", "Minim nyeri"),
            ("Pemberian Nutrisi", "Aliran vitamin bertahap dalam cairan elektrolit", "Monitoring ketat"),
            ("Selesai & Segar", "Pelepasan canula steril dan edukasi hidrasi", "Tubuh berenergi")
        ],
        "benefit_title": ("Pulih Cepat,", "Imunitas Tubuh Terjaga Kuat"),
        "benefit_sub": "Penyerapan langsung ke aliran darah memberi efek pemulihan lebih cepat dibanding suplemen oral biasa.",
    },
    "kesehatan-umum": {
        "name": "Kesehatan Umum",
        "short": "Akupuntur Medis",
        "punchy_hero": ("Akupuntur Medis", "Redakan Nyeri di Rumah"),
        "subtitle": "Terapi jarum steril medis untuk atasi migrain, saraf kejepit (HNP), insomnia, dan pemulihan stroke.",
        "badge": "AKUPUNTUR MEDIS & KESEHATAN UMUM",
        "trust": [
            "Akupunkturis Medis Berlisensi Resmi Kemenkes",
            "Jarum Sekali Pakai Steril Bebas Risiko",
            "Redakan Ketegangan Otot & Nyeri Kronis Alami"
        ],
        "pill1": "Jarum Steril Sekali Pakai",
        "pill2": "● Terapi Terintegrasi",
        "cta": "Konsultasi Akupuntur →",
        "steps": [
            ("Pemeriksaan Titik", "Identifikasi titik meridian & trigger point nyeri", "Peta klinis"),
            ("Pemasangan Jarum", "Insersi jarum mikro steril dengan teknik presisi", "Rasa nyaman"),
            ("Elektrostimulasi", "Stimulasi denyut lembut untuk merelaksasi saraf", "Redakan nyeri"),
            ("Evaluasi Sensasi", "Pelepasan jarum dan evaluasi rentang gerak", "Otot rileks")
        ],
        "benefit_title": ("Nyeri Berkurang,", "Tubuh Kembali Rileks Seimbang"),
        "benefit_sub": "Mengombinasikan ilmu anatomi medis modern dengan stimulasi titik akupuntur tanpa efek samping obat kimia.",
    }
}

def generate_thumbnail_svg(cat_id, meta, variant=1):
    """
    Generate 1200x630 SVG for a category variant.
    Clean top pill without any star x/y bullet, centered text.
    """
    b64_photo = IMAGE_B64.get(cat_id, "")
    name = html.escape(meta["name"])
    badge = html.escape(meta["badge"])
    
    if variant == 1:
        line1, line2 = meta["punchy_hero"]
        sub_raw = meta["subtitle"]
    elif variant == 2:
        line1, line2 = meta["benefit_title"]
        sub_raw = meta["benefit_sub"]
    else: # variant 3
        line1, line2 = ("4 Langkah Praktis", f"Layanan {meta['short']}")
        sub_raw = "Protokol terstandar klinis Joy of Care untuk hasil terapi aman dan terukur di rumah."
    
    line1 = html.escape(line1)
    line2 = html.escape(line2)
    wrapped_sub = textwrap.wrap(sub_raw, width=58)
    sub_l1 = html.escape(wrapped_sub[0]) if len(wrapped_sub) > 0 else ""
    sub_l2 = html.escape(wrapped_sub[1]) if len(wrapped_sub) > 1 else ""

    cta = html.escape(meta["cta"])
    pill1 = html.escape(meta["pill1"])
    pill2 = html.escape(meta["pill2"])

    # Calculate width for pill 1 (clean centered pill, no star x/y bullet)
    pill1_w = max(160, int(len(meta["pill1"]) * 8.2) + 40)
    # Calculate width for category badge pill
    badge_w = max(260, int(len(meta["badge"]) * 8.4) + 54)

    # Left content based on variant
    if variant in [1, 2]:
        items_svg = ""
        trust_list = meta["trust"] if variant == 1 else [
            "Terapi Nyaman di Rumah Tanpa Repot Antre",
            "Jadwal Fleksibel Menyesuaikan Kebutuhan Keluarga",
            "Tenaga Medis Berizin Resmi Kemenkes (SIP / STR)"
        ]
        for idx, item in enumerate(trust_list):
            y_off = idx * 48
            items_svg += f"""
      <g transform="translate(0, {y_off})">
        <circle cx="16" cy="16" r="16" fill="#00bf63" fill-opacity="0.15"/>
        <path d="M10 16 L14 20 L22 12" fill="none" stroke="#007A3D" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="44" y="22" font-family="Inter, sans-serif" font-size="15" font-weight="600" fill="#0F172A">{html.escape(item)}</text>
      </g>"""
    else: # variant 3: timeline steps
        items_svg = ""
        for idx, (stitle, sdesc, sbadge) in enumerate(meta["steps"]):
            y_off = idx * 46
            num = f"0{idx+1}"
            col = "#007A3D" if idx == 0 else ("#00bf63" if idx == 1 else ("#FC9000" if idx == 2 else "#0E7490"))
            items_svg += f"""
      <g transform="translate(0, {y_off})">
        <circle cx="14" cy="14" r="14" fill="{col}"/>
        <text x="14" y="19" font-family="Montserrat, sans-serif" font-size="11" font-weight="800" fill="#FFFFFF" text-anchor="middle">{num}</text>
        <text x="36" y="19" font-family="Montserrat, sans-serif" font-size="14" font-weight="700" fill="#0F172A">{html.escape(stitle)}: <tspan font-family="Inter" font-weight="500" fill="#475569" font-size="13">{html.escape(sdesc[:42])}...</tspan></text>
      </g>"""

    # SVG markup
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
  <defs>
    <linearGradient id="bgGrad_{cat_id}_{variant}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EFFBF4"/>
      <stop offset="50%" stop-color="#F8FCF9"/>
      <stop offset="100%" stop-color="#E6F7ED"/>
    </linearGradient>
    <linearGradient id="accentGrad_{cat_id}_{variant}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FC9000"/>
      <stop offset="100%" stop-color="#FFA940"/>
    </linearGradient>
    <filter id="softShadow_{cat_id}_{variant}" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#007A3D" flood-opacity="0.12"/>
    </filter>
    <filter id="badgeShadow_{cat_id}_{variant}" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
    <pattern id="gridDots_{cat_id}_{variant}" x="0" y="0" width="32" height="32" patternUnits="userSpaceOnUse">
      <circle cx="16" cy="16" r="1.5" fill="#00bf63" opacity="0.18"/>
    </pattern>
    <clipPath id="photoClip_{cat_id}_{variant}">
      <rect x="650" y="65" width="480" height="500" rx="28"/>
    </clipPath>
  </defs>

  <!-- Background -->
  <rect width="1200" height="630" fill="url(#bgGrad_{cat_id}_{variant})"/>
  <rect width="1200" height="630" fill="url(#gridDots_{cat_id}_{variant})"/>

  <circle cx="1100" cy="100" r="220" fill="#00bf63" opacity="0.08"/>
  <circle cx="150" cy="550" r="180" fill="#FC9000" opacity="0.05"/>

  <!-- Left Content Column -->
  <g transform="translate(80, 68)">
    <!-- Category Pill Badge with joc_icon -->
    <g>
      <rect x="0" y="0" width="{badge_w}" height="38" rx="19" fill="#00bf63" fill-opacity="0.12"/>
      <rect x="0" y="0" width="{badge_w}" height="38" rx="19" fill="none" stroke="#00bf63" stroke-width="1.5"/>
      <image href="data:image/png;base64,{B64_JOC_ICON}" x="8" y="7" width="24" height="24"/>
      <text x="38" y="24" font-family="Inter, -apple-system, sans-serif" font-size="12" font-weight="800" fill="#007A3D" letter-spacing="1.1">{badge}</text>
    </g>

    <!-- Punchy Titles (3C Rule) -->
    <text x="0" y="102" font-family="Montserrat, Inter, sans-serif" font-size="50" font-weight="800" fill="#0F172A" letter-spacing="-1">{line1}</text>
    <text x="0" y="160" font-family="Montserrat, Inter, sans-serif" font-size="50" font-weight="800" fill="#007A3D" letter-spacing="-1">{line2}</text>

    <!-- Subtitle -->
    <text x="0" y="214" font-family="Inter, -apple-system, sans-serif" font-size="17" font-weight="500" fill="#475569">
      <tspan x="0" dy="0">{sub_l1}</tspan>
      <tspan x="0" dy="26">{sub_l2}</tspan>
    </text>

    <!-- Features / Steps -->
    <g transform="translate(0, 280)">
      {items_svg}
    </g>

    <!-- CTA Button -->
    <g transform="translate(0, 440)">
      <rect x="0" y="0" width="260" height="48" rx="24" fill="url(#accentGrad_{cat_id}_{variant})" filter="url(#badgeShadow_{cat_id}_{variant})"/>
      <text x="130" y="30" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#FFFFFF" text-anchor="middle">{cta}</text>
    </g>
  </g>

  <!-- Right Human-Centric UI Card -->
  <g filter="url(#softShadow_{cat_id}_{variant})">
    <rect x="648" y="63" width="484" height="504" rx="30" fill="#FFFFFF" stroke="#00bf63" stroke-opacity="0.15" stroke-width="2"/>
    <image href="data:image/jpeg;base64,{b64_photo}" x="650" y="65" width="480" height="500" preserveAspectRatio="xMidYMid slice" clip-path="url(#photoClip_{cat_id}_{variant})"/>

    <!-- Floating Glassmorphic Pill 1 (Top Status, clean centered text, NO star x/y bullet) -->
    <g transform="translate(674, 90)" filter="url(#badgeShadow_{cat_id}_{variant})">
      <rect x="0" y="0" width="{pill1_w}" height="42" rx="21" fill="#FFFFFF" fill-opacity="0.95"/>
      <text x="{pill1_w // 2}" y="26" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">{pill1}</text>
    </g>

    <!-- Floating Glassmorphic Pill 2 with joc_icon -->
    <g transform="translate(674, 500)" filter="url(#badgeShadow_{cat_id}_{variant})">
      <rect x="0" y="0" width="245" height="42" rx="21" fill="#FFFFFF" fill-opacity="0.95"/>
      <image href="data:image/png;base64,{B64_JOC_ICON}" x="12" y="8" width="26" height="26"/>
      <text x="46" y="26" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#007A3D">{pill2}</text>
    </g>
  </g>

  <!-- Brand Signature Footer with joc_long -->
  <g transform="translate(80, 565)">
    <image href="data:image/png;base64,{B64_JOC_LONG}" x="0" y="0" width="130" height="42" preserveAspectRatio="xMidYMid meet"/>
    <text x="145" y="26" font-family="Inter, sans-serif" font-size="13" fill="#475569" opacity="0.85">|  Layanan Kesehatan Resmi ke Rumah · Jabodetabek</text>
  </g>
</svg>"""
    return svg

def build_article_infographic(art):
    """
    Generate 1080x1350 vertical infographic SVG for an article with official joc_long and joc_icon logos.
    """
    raw_title = art["title"]
    title = html.escape(raw_title)
    cat = art["category"]
    cat_meta = CATEGORIES_METADATA.get(cat, CATEGORIES_METADATA["perawatan-lansia"])
    slug = art["slug"]

    # Extract steps or key takeaways
    steps = cat_meta["steps"]
    
    # Check if article has specific content to customize
    fm = art.get("fm", {})
    pk = html.escape(fm.get("primaryKeyword", cat_meta["short"]))

    # Clean multi-line title
    title_words = raw_title.split()
    if len(title_words) <= 5:
        t_line1 = raw_title
        t_line2 = ""
    else:
        mid = len(title_words) // 2
        t_line1 = " ".join(title_words[:mid])
        t_line2 = " ".join(title_words[mid:])

    t_line1 = html.escape(t_line1)
    t_line2 = html.escape(t_line2)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1350" width="1080" height="1350">
  <defs>
    <linearGradient id="bgGrad_{slug}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EFFBF4"/>
      <stop offset="40%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#EFFBF4"/>
    </linearGradient>
    <linearGradient id="hdrGrad_{slug}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#007A3D"/>
      <stop offset="100%" stop-color="#00bf63"/>
    </linearGradient>
    <linearGradient id="accentGrad_{slug}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FC9000"/>
      <stop offset="100%" stop-color="#FFA940"/>
    </linearGradient>
    <filter id="cardShadow_{slug}" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
    <filter id="pillShadow_{slug}" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#007A3D" flood-opacity="0.12"/>
    </filter>
    <pattern id="gridDots_{slug}" x="0" y="0" width="36" height="36" patternUnits="userSpaceOnUse">
      <circle cx="18" cy="18" r="1.5" fill="#00bf63" opacity="0.16"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="1080" height="1350" fill="url(#bgGrad_{slug})"/>
  <rect width="1080" height="1350" fill="url(#gridDots_{slug})"/>

  <!-- Top Header Banner with joc_long -->
  <rect width="1080" height="130" fill="url(#hdrGrad_{slug})"/>
  <g transform="translate(60, 36)">
    <rect x="0" y="0" width="190" height="58" rx="14" fill="#FFFFFF" filter="url(#cardShadow_{slug})"/>
    <image href="data:image/png;base64,{B64_JOC_LONG}" x="12" y="8" width="166" height="42" preserveAspectRatio="xMidYMid meet"/>
    <text x="210" y="36" font-family="Inter, sans-serif" font-size="14" font-weight="600" fill="#EFFBF4">Layanan Kesehatan Homecare &amp; Geriatri Resmi</text>
  </g>
  <g transform="translate(760, 44)">
    <rect x="0" y="0" width="260" height="44" rx="22" fill="#FFFFFF" fill-opacity="0.18"/>
    <text x="130" y="27" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#FFFFFF" text-anchor="middle">📲 WA: 08811-118-911</text>
  </g>

  <!-- Infographic Badge & Title with joc_icon -->
  <g transform="translate(60, 165)">
    <rect x="0" y="0" width="250" height="34" rx="17" fill="#00bf63" fill-opacity="0.15"/>
    <image href="data:image/png;base64,{B64_JOC_ICON}" x="8" y="5" width="24" height="24"/>
    <text x="38" y="22" font-family="Inter, sans-serif" font-size="12" font-weight="800" fill="#007A3D" letter-spacing="1.2">INFOGRAFIS · {cat.upper()}</text>
    
    <text x="0" y="76" font-family="Montserrat, sans-serif" font-size="38" font-weight="800" fill="#0F172A" letter-spacing="-0.5">
      <tspan x="0" dy="0">{t_line1}</tspan>
      <tspan x="0" dy="48">{t_line2}</tspan>
    </text>
    
    <text x="0" y="174" font-family="Inter, sans-serif" font-size="17" font-weight="500" fill="#475569">
      Panduan terstandar klinis Joy of Care untuk topik: <tspan font-weight="700" fill="#007A3D">{pk}</tspan>
    </text>
  </g>

  <!-- Hero Stat Banner -->
  <g transform="translate(60, 365)" filter="url(#cardShadow_{slug})">
    <rect x="0" y="0" width="960" height="96" rx="20" fill="#FFFFFF" stroke="#00bf63" stroke-width="1.5"/>
    <g transform="translate(30, 20)">
      <circle cx="28" cy="28" r="28" fill="#00bf63" fill-opacity="0.12"/>
      <text x="28" y="37" font-family="Inter, sans-serif" font-size="26" text-anchor="middle">🩺</text>
      <text x="76" y="28" font-family="Montserrat, sans-serif" font-size="22" font-weight="800" fill="#007A3D">Layanan Profesional Langsung di Rumah</text>
      <text x="76" y="52" font-family="Inter, sans-serif" font-size="15" fill="#475569">Pasien merasakan penanganan lebih tenang, aman, dan nyaman bersama tim medis terverifikasi.</text>
    </g>
  </g>

  <!-- Connecting Timeline Line -->
  <line x1="120" y1="520" x2="120" y2="1020" stroke="#00bf63" stroke-width="4" stroke-dasharray="6 6" opacity="0.4"/>

  <!-- STEP 1 -->
  <g transform="translate(60, 485)" filter="url(#cardShadow_{slug})">
    <rect x="90" y="0" width="870" height="116" rx="18" fill="#FFFFFF"/>
    <circle cx="60" cy="58" r="32" fill="#007A3D" filter="url(#pillShadow_{slug})"/>
    <text x="60" y="66" font-family="Montserrat, sans-serif" font-size="20" font-weight="800" fill="#FFFFFF" text-anchor="middle">01</text>
    <g transform="translate(120, 26)">
      <text x="0" y="22" font-family="Montserrat, sans-serif" font-size="20" font-weight="800" fill="#0F172A">{html.escape(steps[0][0])}</text>
      <text x="0" y="50" font-family="Inter, sans-serif" font-size="15" fill="#475569">{html.escape(steps[0][1])}</text>
      <text x="0" y="72" font-family="Inter, sans-serif" font-size="13" font-weight="600" fill="#007A3D">✓ Hasil: {html.escape(steps[0][2])}</text>
    </g>
  </g>

  <!-- STEP 2 -->
  <g transform="translate(60, 625)" filter="url(#cardShadow_{slug})">
    <rect x="90" y="0" width="870" height="116" rx="18" fill="#FFFFFF"/>
    <circle cx="60" cy="58" r="32" fill="#00bf63" filter="url(#pillShadow_{slug})"/>
    <text x="60" y="66" font-family="Montserrat, sans-serif" font-size="20" font-weight="800" fill="#FFFFFF" text-anchor="middle">02</text>
    <g transform="translate(120, 26)">
      <text x="0" y="22" font-family="Montserrat, sans-serif" font-size="20" font-weight="800" fill="#0F172A">{html.escape(steps[1][0])}</text>
      <text x="0" y="50" font-family="Inter, sans-serif" font-size="15" fill="#475569">{html.escape(steps[1][1])}</text>
      <text x="0" y="72" font-family="Inter, sans-serif" font-size="13" font-weight="600" fill="#00bf63">✓ Hasil: {html.escape(steps[1][2])}</text>
    </g>
  </g>

  <!-- STEP 3 -->
  <g transform="translate(60, 765)" filter="url(#cardShadow_{slug})">
    <rect x="90" y="0" width="870" height="116" rx="18" fill="#FFFFFF"/>
    <circle cx="60" cy="58" r="32" fill="#FC9000" filter="url(#pillShadow_{slug})"/>
    <text x="60" y="66" font-family="Montserrat, sans-serif" font-size="20" font-weight="800" fill="#FFFFFF" text-anchor="middle">03</text>
    <g transform="translate(120, 26)">
      <text x="0" y="22" font-family="Montserrat, sans-serif" font-size="20" font-weight="800" fill="#0F172A">{html.escape(steps[2][0])}</text>
      <text x="0" y="50" font-family="Inter, sans-serif" font-size="15" fill="#475569">{html.escape(steps[2][1])}</text>
      <text x="0" y="72" font-family="Inter, sans-serif" font-size="13" font-weight="600" fill="#FC9000">✓ Hasil: {html.escape(steps[2][2])}</text>
    </g>
  </g>

  <!-- STEP 4 -->
  <g transform="translate(60, 905)" filter="url(#cardShadow_{slug})">
    <rect x="90" y="0" width="870" height="116" rx="18" fill="#FFFFFF"/>
    <circle cx="60" cy="58" r="32" fill="#0E7490" filter="url(#pillShadow_{slug})"/>
    <text x="60" y="66" font-family="Montserrat, sans-serif" font-size="20" font-weight="800" fill="#FFFFFF" text-anchor="middle">04</text>
    <g transform="translate(120, 26)">
      <text x="0" y="22" font-family="Montserrat, sans-serif" font-size="20" font-weight="800" fill="#0F172A">{html.escape(steps[3][0])}</text>
      <text x="0" y="50" font-family="Inter, sans-serif" font-size="15" fill="#475569">{html.escape(steps[3][1])}</text>
      <text x="0" y="72" font-family="Inter, sans-serif" font-size="13" font-weight="600" fill="#0E7490">✓ Hasil: {html.escape(steps[3][2])}</text>
    </g>
  </g>

  <!-- Medical Advice & Tips Box -->
  <g transform="translate(60, 1050)" filter="url(#cardShadow_{slug})">
    <rect x="0" y="0" width="960" height="120" rx="18" fill="#FFFFFF" stroke="#FC9000" stroke-width="1.5"/>
    <g transform="translate(30, 24)">
      <circle cx="20" cy="20" r="20" fill="#FC9000" fill-opacity="0.15"/>
      <text x="20" y="27" font-family="Inter, sans-serif" font-size="18" text-anchor="middle">💡</text>
      <text x="56" y="22" font-family="Montserrat, sans-serif" font-size="17" font-weight="800" fill="#0F172A">Rekomendasi Tim Medis Joy of Care</text>
      <text x="56" y="48" font-family="Inter, sans-serif" font-size="14" fill="#475569">Setiap tindakan medis di rumah wajib didampingi tenaga kesehatan berizin (SIP / STR aktif).</text>
      <text x="56" y="70" font-family="Inter, sans-serif" font-size="14" fill="#475569">Konsultasikan segera kondisi pasien Anda untuk rencana perawatan yang paling tepat dan aman.</text>
    </g>
  </g>

  <!-- Footer Banner / CTA with joc_icon -->
  <g transform="translate(60, 1195)" filter="url(#pillShadow_{slug})">
    <rect x="0" y="0" width="960" height="95" rx="20" fill="url(#hdrGrad_{slug})"/>
    <g transform="translate(40, 24)">
      <image href="data:image/png;base64,{B64_JOC_ICON}" x="0" y="2" width="44" height="44"/>
      <text x="56" y="22" font-family="Montserrat, sans-serif" font-size="20" font-weight="800" fill="#FFFFFF">Konsultasi Gratis dengan Tim Medis Joy of Care</text>
      <text x="56" y="44" font-family="Inter, sans-serif" font-size="14" fill="#EFFBF4" opacity="0.9">Layanan terpercaya, nyaman, dan siaga ke seluruh wilayah Jabodetabek.</text>
    </g>
    <g transform="translate(690, 24)">
      <rect x="0" y="0" width="230" height="48" rx="24" fill="url(#accentGrad_{slug})"/>
      <text x="115" y="30" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#FFFFFF" text-anchor="middle">Chat WhatsApp →</text>
    </g>
  </g>
</svg>"""
    return svg

def main():
    print("🚀 Starting Joy of Care Visual Asset Generation (Clean Badges, No Star x/y)...")
    
    # 1. Generate Thumbnails (12 categories x 3 variants = 36 SVGs)
    print("\n📸 Generating Category Thumbnails (36 variants + category banners)...")
    thumb_count = 0
    
    for cat_id, meta in CATEGORIES_METADATA.items():
        for variant in [1, 2, 3]:
            svg = generate_thumbnail_svg(cat_id, meta, variant)
            v_name = f"{cat_id}-v{variant}-{'hero' if variant==1 else ('benefit' if variant==2 else 'process')}.svg"
            
            # Save to web thumbnails
            with open(os.path.join(WEB_THUMBS, v_name), "w", encoding="utf-8") as f:
                f.write(svg)
            # Save to net thumbnails
            with open(os.path.join(NET_THUMBS, v_name), "w", encoding="utf-8") as f:
                f.write(svg)
            thumb_count += 1
        
        # Primary category banner (Variant 1 Hero)
        primary_svg = generate_thumbnail_svg(cat_id, meta, variant=1)
        for dest in [
            os.path.join(WEB_THUMBS, f"{cat_id}.svg"),
            os.path.join(WEB_BLOG, f"{cat_id}.svg"),
            os.path.join(NET_THUMBS, f"{cat_id}.svg")
        ]:
            with open(dest, "w", encoding="utf-8") as f:
                f.write(primary_svg)
        print(f"  ✓ {cat_id}: 3 variants + primary banner generated (Pill: {meta['pill1']})")

    # 2. Legacy names previously in /joyofcare-net/visual-assets
    legacy_map = {
        "healthy-aging.svg": ("perawatan-lansia", 1),
        "pengalaman-pasien.svg": ("perawatan-lansia", 2),
        "osteoporosis.svg": ("osteoporosis", 1),
        "parkinson.svg": ("parkinson", 1),
        "studi-luar-negeri.svg": ("studi-luar-negeri", 1),
        "vaksinasi.svg": ("vaksinasi-rumah", 1),
    }
    for leg_name, (cid, v) in legacy_map.items():
        svg = generate_thumbnail_svg(cid, CATEGORIES_METADATA[cid], variant=v)
        for dest in [
            os.path.join(WEB_THUMBS, leg_name),
            os.path.join(WEB_BLOG, leg_name),
            os.path.join(NET_THUMBS, leg_name),
        ]:
            with open(dest, "w", encoding="utf-8") as f:
                f.write(svg)
        print(f"  ✓ Legacy asset upgraded: {leg_name}")

    # 3. Generate Infographics for 1 out of 3 articles across all 12 categories
    print("\n📊 Generating Article Infographics (1 out of 3 articles)...")
    articles_by_cat = {}
    mdx_files = sorted(glob.glob(os.path.join(BASE_WEB, "src/content/articles/*.mdx")))
    
    for fpath in mdx_files:
        content = open(fpath, encoding="utf-8").read()
        if content.startswith("---"):
            parts = content.split("---")
            fm = yaml.safe_load(parts[1])
            slug = fm.get("slug", os.path.splitext(os.path.basename(fpath))[0])
            title = fm.get("title", "")
            cat = fm.get("category", "perawatan-lansia")
            articles_by_cat.setdefault(cat, []).append({
                "slug": slug,
                "title": title,
                "category": cat,
                "fm": fm,
                "file": fpath
            })

    info_count = 0
    infographics_manifest = []

    for cat, arts in sorted(articles_by_cat.items()):
        selected = [art for idx, art in enumerate(arts) if idx % 3 == 0]
        print(f"  -> Category {cat}: {len(arts)} articles -> {len(selected)} infographics")
        
        for art in selected:
            slug = art["slug"]
            info_svg = build_article_infographic(art)
            
            # Save as {slug}.svg and {slug}-infografis.svg
            for sname in [f"{slug}.svg", f"{slug}-infografis.svg"]:
                with open(os.path.join(WEB_INFOS, sname), "w", encoding="utf-8") as f:
                    f.write(info_svg)
                with open(os.path.join(NET_INFOS, sname), "w", encoding="utf-8") as f:
                    f.write(info_svg)
            
            infographics_manifest.append({
                "slug": slug,
                "title": art["title"],
                "category": cat,
                "path": f"/assets/infographics/{slug}.svg",
                "width": 1080,
                "height": 1350,
                "type": "Process Timeline & Clinical Guide"
            })
            info_count += 1

    # Also generate the category-level infographics
    cat_level_infographics = {
        "fisioterapi-lansia.svg": ("fisioterapi-rumah", "4 Langkah Pemulihan Fisioterapi di Rumah"),
        "panduan-merawat-orang-tua.svg": ("perawatan-lansia", "Panduan Emas Merawat Orang Tua di Rumah"),
        "biaya-panggil-dokter.svg": ("panggil-dokter", "Panduan Layanan Dokter ke Rumah"),
        "persyaratan-kesehatan-studi-luar-negeri.svg": ("studi-luar-negeri", "Checklist Medis Studi Luar Negeri"),
        "vaksinasi-untuk-lansia.svg": ("vaksinasi-rumah", "Panduan Jadwal Vaksinasi Lansia di Rumah")
    }

    for fname, (cat_id, ititle) in cat_level_infographics.items():
        mock_art = {
            "title": ititle,
            "category": cat_id,
            "slug": os.path.splitext(fname)[0],
            "fm": {"primaryKeyword": ititle}
        }
        info_svg = build_article_infographic(mock_art)
        with open(os.path.join(WEB_INFOS, fname), "w", encoding="utf-8") as f:
            f.write(info_svg)
        with open(os.path.join(NET_INFOS, fname), "w", encoding="utf-8") as f:
            f.write(info_svg)
        print(f"  ✓ Category Infographic: {fname}")

    # 4. Generate JSON Manifest
    manifest = {
        "title": "Joy of Care Visual Assets Catalog",
        "updatedAt": "2026-09-06",
        "totalThumbnails": thumb_count + len(CATEGORIES_METADATA) + len(legacy_map),
        "totalInfographics": info_count + len(cat_level_infographics),
        "branding": {
            "icon": "joc_icon.png embedded as base64 in SVG",
            "logoLong": "joc_long.png embedded as base64 in SVG",
            "colors": {
                "primary": "#00bf63",
                "primaryDark": "#007A3D",
                "accent": "#FC9000",
                "teal": "#0E7490",
                "bgLight": "#EFFBF4"
            }
        },
        "categories": list(CATEGORIES_METADATA.keys()),
        "infographics": infographics_manifest,
    }
    
    with open(os.path.join(WEB_THUMBS, "..", "index.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    with open(os.path.join(BASE_NET, "visual-assets", "index.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\n🎉 Finished successfully!")
    print(f"  • Total Thumbnails generated: {manifest['totalThumbnails']}")
    print(f"  • Total Infographics generated: {manifest['totalInfographics']}")
    print(f"  • Star ratings x/y bullets removed, compliant claims updated!")
    print(f"  • Synced to {WEB_THUMBS}, {WEB_BLOG}, {WEB_INFOS} and {BASE_NET}/visual-assets")

if __name__ == "__main__":
    main()
