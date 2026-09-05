# Handler functions for files 27 to 39

PRIMARY_CTA = "Hubungi WhatsApp JoC untuk informasi harga: https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Berapa%20biaya%20layanan%20Joy%20of%20Care?"
ALTERNATE_CTA = "Konsultasi Dokter Gratis via WhatsApp: https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Mau%20konsultasi%20gratis%20dengan%20dokter"

def handle_merawat_orang_tua_biaya_perbandingan(text):
    old_fm = "answer: Biaya jasa perawat lansia di Jabodetabek berkisar antara Rp 2.500.000 hingga\n    Rp 4.500.000 per bulan untuk perawat non-medis (caregiver pendamping harian),\n    dan Rp 5.000.000 hingga Rp 9.000.000 per bulan untuk perawat medis bersertifikasi\n    D3/S1 Keperawatan dengan STR aktif."
    new_fm = f"answer: Biaya jasa perawat lansia di Jabodetabek ditentukan secara transparan berdasarkan kualifikasi (caregiver pendamping aktivitas harian atau perawat medis bersertifikasi STR aktif) serta sistem kerja (live-in bulanan atau shift harian). {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    text = text.replace(
        "| **Biaya Jasa Bulanan** | Rp 0 (Gratis) | Rp 3.500.000 – Rp 7.500.000 / bulan |",
        "| **Biaya Jasa Bulanan** | Rp 0 (Tenaga Sendiri) | **Transparan & Terukur (Hubungi WA JoC)** |"
    )
    
    old_body_faq = "Biaya jasa perawat lansia di Jabodetabek berkisar antara Rp 2.500.000 hingga Rp 4.500.000 per bulan untuk perawat non-medis (caregiver pendamping harian), dan Rp 5.000.000 hingga Rp 9.000.000 per bulan untuk perawat medis bersertifikasi D3/S1 Keperawatan dengan STR aktif."
    new_body_faq = f"Biaya jasa perawat lansia di Jabodetabek dirancang fleksibel dan transparan sesuai kebutuhan pendampingan lansia, baik untuk bantuan aktivitas dasar harian maupun perawatan medis klinis pascarawat RS. {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_osteoporosis_biaya_perbandingan(text):
    old_sec = """1. Obat Bisfosfonat Oral Mingguan / Injeksi Denosumab 6 Bulan: Rp 2.500.000 – Rp 6.000.000/tahun
2. Suplemen Kalsium Sitrat + Vitamin D3 Harian: Rp 1.500.000 – Rp 2.400.000/tahun
3. Paket Sesi Bersama [Layanan Fisioterapi di Rumah Joy of Care](/layanan/fisioterapi-di-rumah) (2x per bulan): Rp 8.400.000/tahun
4. Pemeriksaan DEXA Scan & Laboratorium Darah Tahunan: Rp 1.500.000 – Rp 2.500.000
5. **Total Biaya Terapi Terpadu**: **Rp 13.900.000 – Rp 19.300.000/tahun**.

Bandingkan angka di atas dengan kalkulasi biaya medis jika lansia osteoporosis mengalami **fraktur kompresi tulang panggul akibat jatuh di rumah**:

1. Operasi Bedah Penggantian Panggul Total (*Total Hip Arthroplasty*) di RS Swasta: Rp 80.000.000 – Rp 140.000.000
2. Perawatan ICU Pascaoperasi (3–5 hari): Rp 25.000.000 – Rp 50.000.000
3. Rehabilitasi Rawat Inap & Sewa Kursi Roda: Rp 15.000.000 – Rp 30.000.000
4. Kebutuhan Perawat Menginap 24 Jam Pasca-Fraktur: Rp 60.000.000 – Rp 90.000.000/tahun
5. **Total Biaya Fraktur Akut**: **Rp 180.000.000 – Rp 310.000.000+** (belum memperhitungkan risiko kematian 20% dalam 1 tahun pascafraktur)."""

    new_sec = f"""1. Terapi farmakologi terarah (bisfosfonat oral atau injeksi spesifik) sesuai anjuran dokter spesialis.
2. Suplementasi kalsium sitrat dan vitamin D3 aktif harian untuk memelihara densitas mineral tulang.
3. Program penguatan otot terpandu bersama [Layanan Fisioterapi di Rumah Joy of Care](/layanan/fisioterapi-di-rumah).
4. Pemantauan berkala densitas tulang melalui DEXA scan dan skrining laboratorium darah.
5. **Hasil Terapi Preventif**: Tulang tetap padat, risiko patah tulang terminimalisir, dan mobilitas mandiri terjaga optimal.

Bandingkan langkah preventif di atas dengan beban medis fantastis jika lansia mengalami **patah tulang panggul akibat terjatuh di rumah**:

1. Tindakan operasi bedah ortopedi penggantian panggul (*Total Hip Arthroplasty*) di rumah sakit swasta yang menelan puluhan hingga ratusan juta rupiah.
2. Biaya sewa ruang rawat intensif ICU pascaoperasi dan komplikasi tirah baring akut.
3. Kebutuhan alat bantu jalan, sewa tempat tidur medis khusus, dan rehabilitasi intensif berbulan-bulan.
4. Kebutuhan perawat medis pendamping 24 jam jangka panjang pascatindakan operasi.
5. **Beban Pengeluaran Rumah Sakit**: Mencapai ratusan juta rupiah disertai risiko komplikasi fatal. Berinvestasi pada deteksi dini osteoporosis terbukti jauh lebih hemat dan menyelamatkan masa depan orang tua. {PRIMARY_CTA}"""
    text = text.replace(old_sec, new_sec)
    return text

def handle_panggil_dokter_jakarta_biaya_perbandingan(text):
    old_fm = "answer: Biaya jasa visit dokter umum ke rumah di Jakarta umumnya berkisar antara\n    Rp 350.000 hingga Rp 750.000 per kunjungan, tergantung jarak tempuh, waktu kunjungan\n    (jam kerja vs malam hari), dan jenis tindakan medis yang dilakukan."
    new_fm = f"answer: Biaya jasa visit dokter umum ke rumah di Jakarta dirancang transparan dan terjangkau, disesuaikan dengan kebutuhan klinis pasien dan tindakan medis tanpa biaya perantara tersembunyi. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    text = text.replace(
        "* **Kunjungan Dokter Umum**: Berkisar antara **Rp 350.000 – Rp 650.000** per kunjungan.",
        "* **Kunjungan Dokter Umum**: Tarif visit transparan dan terjangkau mencakup pemeriksaan fisik lengkap 45–60 menit."
    )
    text = text.replace(
        "* **Pemasangan / Penggantian Selang Kateter Urin**: Rp 300.000 – Rp 500.000 (termasuk folley catheter silikon/latex steril, urine bag, jelly anestesi, spuit).",
        "* **Pemasangan / Penggantian Selang Kateter Urin**: Tindakan steril menggunakan alat medis berkualitas (termasuk folley catheter silikon steril, urine bag, dan anestesi)."
    )
    text = text.replace(
        "* **Pemasangan / Penggantian Selang Makan NGT**: Rp 350.000 – Rp 550.000 (termasuk selang NGT steril, stetoskop tes lambung, plester fiksasi).",
        "* **Pemasangan / Penggantian Selang Makan NGT**: Tindakan pemasangan aseptik (termasuk selang NGT steril dan verifikasi posisi lambung)."
    )
    text = text.replace(
        "* **Perawatan Luka Jahitan / Luka Dekubitus**: Rp 200.000 – Rp 450.000 (termasuk cairan pencuci steril normal saline, dressing kasa modern antimikroba).",
        "* **Perawatan Luka Jahitan / Luka Dekubitus**: Perawatan luka steril menggunakan teknik modern dressing antimikroba."
    )
    text = text.replace(
        "* **Pemberian Terapi Infus Cairan / Vitamin**: Rp 250.000 – Rp 600.000 melalui [Layanan Infus Vitamin dan Cairan di Rumah](/layanan/infus-vitamin-di-rumah) tergantung jenis multivitamin dan cairan hidrasi yang diinstruksikan dokter.",
        f"* **Pemberian Terapi Infus Cairan / Vitamin**: Melalui [Layanan Infus Vitamin dan Cairan di Rumah](/layanan/infus-vitamin-di-rumah) sesuai instruksi resep dokter. {PRIMARY_CTA}"
    )
    
    old_table = """| **Konsultasi Dokter** | Rp 400.000 – Rp 600.000 | Rp 450.000 – Rp 550.000 |
| **Biaya Administrasi RS** | Rp 75.000 – Rp 150.000 | **Rp 0 (Bebas Biaya Admin)** |
| **Transportasi Khusus (Taksi/Ambulans)** | Rp 300.000 – Rp 800.000 (PP) | **Rp 0 (Pasien di Rumah)** |
| **Obat-obatan & BMHP Standar** | Sesuai resep instalasi farmasi RS | Sesuai resep apotek resmi |
| **Estimasi Total Pengeluaran** | **Rp 775.000 – Rp 1.550.000** | **Rp 450.000 – Rp 550.000** |"""

    new_table = f"""| **Konsultasi Dokter Medis** | Jasa konsultasi poliklinik / IGD RS | **Transparan & Terjangkau (Hubungi WA JoC)** |
| **Biaya Administrasi Fasilitas** | Karcis pendaftaran & kartu pasien RS | **Rp 0 (Bebas Biaya Administrasi Tambahan)** |
| **Transportasi Khusus Pasien** | Sewa ambulans / taksi khusus PP mahal | **Rp 0 (Dokter hadir langsung di ranjang rumah)** |
| **Obat-obatan & BMHP Standar** | Instalasi farmasi rumah sakit | Resep resmi harga apotek transparan |
| **Total Efisiensi Pengeluaran** | **Beban Pengeluaran Tinggi per Visit** | **Penghematan Signifikan Hingga 50%** |

{PRIMARY_CTA}"""
    text = text.replace(old_table, new_table)
    
    text = text.replace(
        "Selain ongkos sewa kendaraan khusus atau ambulans penjemputan berkisar Rp 400.000–800.000 per perjalanan, ada biaya kehilangan jam kerja produktif anak yang mendampingi mengantre berjam-jam.",
        "Selain ongkos sewa kendaraan khusus atau ambulans penjemputan yang mahal per perjalanan, ada biaya kehilangan jam kerja produktif anak yang mendampingi mengantre berjam-jam."
    )
    
    old_body_faq = "Biaya jasa visit dokter umum ke rumah di Jakarta umumnya berkisar antara Rp 350.000 hingga Rp 750.000 per kunjungan, tergantung jarak tempuh, waktu kunjungan (jam kerja vs malam hari), dan jenis tindakan medis yang dilakukan."
    new_body_faq = f"Biaya jasa visit dokter umum ke rumah di Jakarta ditentukan secara transparan tanpa markup perantara. Rincian biaya tindakan medis selalu dijelaskan secara terbuka sebelum tindakan dilakukan. {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_perawat_lansia_biaya_perbandingan(text):
    old_fm = "answer: Perawat harian shift (8–12 jam) dikenakan tarif berkisar Rp 180.000 hingga\n    Rp 350.000 per hari, sedangkan perawat menginap 24 jam dikenakan sistem paket\n    bulanan berkisar Rp 3.500.000 hingga Rp 8.500.000 per bulan tergantung kualifikasi\n    caregiver atau perawat medis."
    new_fm = f"answer: Tarif perawat lansia di Jabodetabek disesuaikan transparan berdasarkan sistem penugasan (shift harian atau menginap 24 jam bulanan) serta kualifikasi tenaga pendamping medis atau non-medis. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    text = text.replace(
        "| **Estimasi Biaya Bulanan** | Rp 4.500.000 – Rp 8.000.000 (jika full 30 hari) | Rp 3.500.000 – Rp 9.500.000 / bulan paket |",
        "| **Estimasi Biaya Bulanan** | Tarif harian terakumulasi | **Paket Bulanan Hemat & Terstruktur (Hubungi WA JoC)** |"
    )
    
    old_body_faq = "Perawat harian shift (8–12 jam) dikenakan tarif berkisar Rp 180.000 hingga Rp 350.000 per hari, sedangkan perawat menginap 24 jam dikenakan sistem paket bulanan berkisar Rp 3.500.000 hingga Rp 8.500.000 per bulan tergantung kualifikasi caregiver atau perawat medis."
    new_body_faq = f"Perawat lansia homecare Joy of Care dapat dipesan dalam skema shift harian maupun paket menginap bulanan secara transparan. Rincian biaya selalu disesuaikan dengan kondisi ketergantungan fisik dan alat medis lansia. {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_perawat_lansia_panduan_lengkap(text):
    old_fm = "answer: Biaya jasa perawat lansia di Jabodetabek berkisar antara Rp 2.500.000 hingga\n    Rp 4.500.000 per bulan untuk caregiver non-medis, dan Rp 5.000.000 hingga Rp 9.500.000\n    per bulan untuk perawat medis berijazah D3/S1 Keperawatan dengan Surat Tanda Registrasi\n    (STR) aktif."
    new_fm = f"answer: Biaya jasa perawat lansia di Jabodetabek ditentukan secara transparan berdasarkan kompetensi tenaga kesehatan (caregiver pendamping harian atau perawat medis berijazah resmi D3/S1 Keperawatan ber-STR aktif). {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    old_table = """|---|---|---|---|
| **Caregiver Lansia** | Shift Harian (8–12 Jam) | Rp 150.000 – Rp 250.000 / hari | Lansia demensia ringan, butuh teman mobilitas |
| **Caregiver Lansia** | Menginap (*Live-In* Bulanan) | Rp 2.500.000 – Rp 4.500.000 / bulan | Lansia mandiri parsial, butuh bantuan ADL 24 jam |
| **Perawat Medis D3/S1** | Kunjungan Visit Tindakan | Rp 200.000 – Rp 350.000 / visit | Ganti selang kateter/NGT, rawat luka steril |
| **Perawat Medis D3/S1** | Shift 12 Jam Kerja | Rp 250.000 – Rp 400.000 / shift | Pascastroke fase akut, tirah baring, monitor oksigen |
| **Perawat Medis D3/S1** | Menginap (*Live-In* 24 Jam) | Rp 5.000.000 – Rp 9.500.000 / bulan | Pasien ICU pulang, ventilator/trakeostomi, kanker stadium akhir |"""

    new_table = f"""|---|---|---|---|
| **Caregiver Lansia** | Shift Harian (8–12 Jam) | Tarif Harian (Hubungi WA JoC) | Lansia demensia ringan, butuh teman mobilitas |
| **Caregiver Lansia** | Menginap (*Live-In* Bulanan) | Paket Bulanan (Hubungi WA JoC) | Lansia mandiri parsial, butuh bantuan ADL 24 jam |
| **Perawat Medis D3/S1** | Kunjungan Visit Tindakan | Kunjungan Tindakan (Hubungi WA JoC) | Ganti selang kateter/NGT, rawat luka steril |
| **Perawat Medis D3/S1** | Shift 12 Jam Kerja | Shift Medis (Hubungi WA JoC) | Pascastroke fase akut, tirah baring, monitor oksigen |
| **Perawat Medis D3/S1** | Menginap (*Live-In* 24 Jam) | Paket Medis 24 Jam (Hubungi WA JoC) | Pasien ICU pulang, ventilator/trakeostomi, perawatan intensif |

{PRIMARY_CTA}"""
    text = text.replace(old_table, new_table)
    
    old_body_faq = "Biaya jasa perawat lansia di Jabodetabek berkisar antara Rp 2.500.000 hingga Rp 4.500.000 per bulan untuk caregiver non-medis, dan Rp 5.000.000 hingga Rp 9.500.000 per bulan untuk perawat medis berijazah D3/S1 Keperawatan dengan Surat Tanda Registrasi (STR) aktif."
    new_body_faq = f"Biaya jasa perawat lansia di Jabodetabek dirancang jelas dan transparan sesuai jenjang kompetensi tenaga perawat (caregiver non-medis untuk aktivitas harian atau perawat medis berijazah D3/S1 dengan STR aktif). {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_parkinson_biaya_perbandingan(text):
    old_fm = "answer: Jauh lebih ekonomis. Biaya rawat inap rumah sakit berkisar Rp 1.500.000\n    hingga Rp 4.000.000 per hari, belum termasuk biaya obat dan dokter. Dengan layanan\n    homecare terpadu, anggaran bulanan menjadi terukur dan stabil tanpa risiko biaya\n    tak terduga."
    new_fm = f"answer: Jauh lebih ekonomis dan terukur. Merawat pasien Parkinson di rumah menghindarkan keluarga dari tagihan rawat inap rumah sakit harian yang sangat mahal, sekaligus memberikan kenyamanan emosional bagi pasien. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    text = text.replace(
        "| **Estimasi Biaya Rutin** | Rp 1.500.000 – Rp 4.000.000 / hari rawat | **Rp 3.500.000 – Rp 8.500.000 / bulan paket terpadu** |",
        "| **Estimasi Biaya Rutin** | Tarif rawat inap harian RS sangat mahal | **Paket Bulanan Terukur & Hemat (Hubungi WA JoC)** |"
    )
    
    old_body_faq = "Jauh lebih ekonomis. Biaya rawat inap rumah sakit berkisar Rp 1.500.000 hingga Rp 4.000.000 per hari, belum termasuk biaya obat dan dokter. Dengan layanan homecare terpadu, anggaran bulanan menjadi terukur dan stabil tanpa risiko biaya tak terduga."
    new_body_faq = f"Jauh lebih ekonomis dan terkontrol. Menghadirkan pendampingan homecare medis di rumah membebaskan keluarga dari risiko lonjakan biaya rawat inap rumah sakit yang tidak terduga, seraya memastikan kepatuhan obat Levodopa dan terapi fisik berjalan disiplin. {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_syarat_studi_biaya_perbandingan(text):
    old_fm = "answer: Biaya MCU visa Australia di panel resmi berkisar antara Rp 1.800.000 hingga\n    Rp 2.500.000; tes TBC visa UK di IOM berkisar antara Rp 850.000 hingga Rp 1.100.000;\n    MCU studi Jepang/Korea berkisar antara Rp 1.200.000 hingga Rp 1.900.000; sedangkan\n    pemenuhan paket imunisasi universitas di Amerika Serikat berkisar antara Rp 1.500.000\n    hingga Rp 3.500.000."
    new_fm = f"answer: Biaya pemeriksaan MCU dan vaksinasi studi ke luar negeri bervariasi sesuai regulasi visa negara tujuan (Australia, UK, Jepang, Korea, atau USA) serta daftar imunisasi wajib yang disyaratkan universitas. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    text = text.replace(
        "> * **Variasi Struktur Biaya**: Estimasi biaya MCU berkisar dari Rp 850.000 (skrining TB UK) hingga Rp 3.500.000+ (MCU komprehensif visa + vaksin lengkap USA).",
        f"> * **Variasi Struktur Layanan**: Pemeriksaan kesehatan studi luar negeri mencakup skrining TBC visa kedutaan hingga vaksinasi wajib kampus terpadu. {PRIMARY_CTA}"
    )
    
    old_table = """| **Pemeriksaan Visa Kedutaan (RS Panel)** | Rp 1.800.000 – Rp 2.400.000 | Rp 850.000 – Rp 1.100.000 | Rp 1.200.000 – Rp 1.800.000 | Rp 1.300.000 – Rp 1.900.000 |
| **Paket Vaksinasi Wajib Universitas** | Rp 1.200.000 – Rp 1.800.000 | Rp 850.000 – Rp 1.500.000 | Rp 550.000 – Rp 850.000 | Rp 550.000 – Rp 1.100.000 |
| **Tes Titer Darah & Skrining Urin Lab** | Rp 650.000 – Rp 1.100.000 | Opsional (sesuai kampus) | Sudah termasuk dalam paket | Rp 450.000 – Rp 750.000 |
| **Total Estimasi Anggaran Medis** | **Rp 3.650.000 – Rp 5.300.000** | **Rp 1.700.000 – Rp 2.600.000** | **Rp 2.300.000 – Rp 3.200.000** | **Rp 2.300.000 – Rp 3.750.000** |"""

    new_table = f"""| **Pemeriksaan Visa Kedutaan (RS Panel)** | Tarif resmi RS panel terakreditasi | Tarif resmi klinik IOM Jakarta | Standar formulir visa kedutaan | Standar formulir visa kedutaan |
| **Paket Vaksinasi Wajib Universitas** | Paket vaksin MMR & Meningitis | Paket vaksin MenACWY & booster | Vaksin MMR & Hepatitis B | Paket vaksin influenza & Tdap |
| **Tes Titer Darah & Skrining Urin Lab** | Uji titer antibodi serologi lab | Uji laboratorium sesuai kampus | Panel skrining urin & darah | Uji laboratorium titer serologi |
| **Estimasi Skema Pemeriksaan** | **Paket Lengkap Mahasiswa Australia** | **Paket Terpadu Mahasiswa UK** | **Paket Terpadu Jepang / Korea** | **Paket Mahasiswa Amerika Serikat** |

{PRIMARY_CTA}"""
    text = text.replace(old_table, new_table)
    return text

def handle_syarat_studi_panduan_lengkap(text):
    old_table = """|---|---|---|
| **Paket Cek Lab Darah Titer Imunisasi** | Darah lengkap, Titer IgG Campak & Rubela, HBsAg, Anti-HBs kuantitatif | Rp 850.000 – Rp 1.250.000 |
| **Vaksin Meningitis MenACWY** | Injeksi 1 dosis vaksin quadrivalent resmi + Buku Kuning ICV internasional | Rp 650.000 – Rp 850.000 |
| **Vaksin MMR Dewasa** | Injeksi 1 dosis vaksin campak-gondongan-rubela terdaftar BPOM | Rp 550.000 – Rp 700.000 |
| **Vaksin Tdap Booster** | Injeksi 1 dosis tetanus-difteri-pertusis dewasa | Rp 500.000 – Rp 650.000 |
| **Paket Verifikasi Form & Konsultasi Dokter** | Visit dokter ke rumah, cek tanda vital, pengisian form kampus berbahasa Inggris | Rp 450.000 – Rp 550.000 |"""

    new_table = f"""|---|---|---|
| **Paket Cek Lab Darah Titer Imunisasi** | Darah lengkap, Titer IgG Campak & Rubela, HBsAg, Anti-HBs kuantitatif | Paket Uji Lab (Hubungi WA JoC) |
| **Vaksin Meningitis MenACWY** | Injeksi 1 dosis vaksin quadrivalent resmi + Buku Kuning ICV internasional | Vaksin Resmi (Hubungi WA JoC) |
| **Vaksin MMR Dewasa** | Injeksi 1 dosis vaksin campak-gondongan-rubela terdaftar BPOM | Vaksin Resmi (Hubungi WA JoC) |
| **Vaksin Tdap Booster** | Injeksi 1 dosis tetanus-difteri-pertusis dewasa | Vaksin Resmi (Hubungi WA JoC) |
| **Paket Verifikasi Form & Konsultasi Dokter** | Visit dokter ke rumah, cek tanda vital, pengisian form kampus berbahasa Inggris | Layanan Dokter (Hubungi WA JoC) |

{PRIMARY_CTA}"""
    text = text.replace(old_table, new_table)
    return text

def handle_tips_mahasiswa_biaya_perbandingan(text):
    old_row = "| **Estimasi Biaya Tahunan** | AUD $600 – $800 per tahun (~Rp 6–8 juta) | GBP £776 per tahun (~Rp 15–16 juta) | USD $2.000 – $4.000 per tahun (~Rp 32–64 juta) |"
    new_row = f"| **Estimasi Biaya Tahunan** | Sesuai tarif resmi premi OSHC Australia | Sesuai tarif wajib retribusi IHS visa UK | Premi tahunan student health plan universitas |"
    text = text.replace(old_row, new_row)
    return text

def handle_tips_mahasiswa_panduan_lengkap(text):
    text = text.replace(
        "Biaya penambalan atau pencabutan gigi bungsu di luar negeri dapat mencapai Rp 5.000.000 hingga Rp 15.000.000 per gigi.",
        "Biaya penambalan atau pencabutan gigi bungsu di luar negeri dapat sangat mahal mencapai jutaan hingga belasan juta rupiah per gigi."
    )
    return text

def handle_tips_mahasiswa_tips_cara(text):
    old_text = "Biaya bervariasi tergantung jumlah item vaksin dan tes lab yang disyaratkan oleh universitas tujuan Anda, berkisar antara Rp 850.000 untuk paket dasar hingga Rp 2.500.000 untuk paket komprehensif lengkap dengan vaksin meningitis dan titer serologi."
    new_text = f"Biaya bervariasi tergantung jumlah item vaksin dan tes lab yang disyaratkan oleh universitas tujuan Anda. Menyelesaikan seluruh rangkaian imunisasi dan MCU di tanah air sebelum berangkat terbukti menghemat biaya kesehatan hingga lebih dari 50%. {PRIMARY_CTA}"
    text = text.replace(old_text, new_text)
    return text

def handle_vaksin_lansia_biaya_perbandingan(text):
    old_fm = "answer: Selisih biayanya relatif sangat kecil (berkisar antara Rp 100.000 hingga\n    Rp 200.000 untuk biaya kunjungan tenaga medis), namun bila memperhitungkan biaya\n    transportasi taksi/ambulans, parkir RS, dan hilangnya waktu produktif kerja keluarga,\n    vaksinasi di rumah sesungguhnya jauh lebih hemat dan efisien."
    new_fm = f"answer: Selisih biaya langsung sangat kecil, namun bila memperhitungkan biaya transportasi khusus, parkir RS, dan hilangnya waktu kerja keluarga, vaksinasi di rumah sesungguhnya jauh lebih hemat, praktis, dan aman bagi lansia. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    old_sec = """1. Harga Vaksin di Kasir Faskes: Rp 350.000 – Rp 450.000
2. Biaya Administrasi & Kartu Pasien RS: Rp 50.000 – Rp 100.000
3. Jasa Konsultasi Dokter Spesialis / Dokter Umum RS: Rp 250.000 – Rp 450.000
4. Biaya Transportasi Mobil Khusus Lansia / Taksi Online PP: Rp 150.000 – Rp 250.000
5. Biaya Parkir & Konsumsi Pendamping di RS: Rp 50.000 – Rp 100.000
6. **Total Biaya yang Dikeluarkan**: **Rp 850.000 – Rp 1.350.000** (belum termasuk hilangnya pemasukan karena harus izin cuti kerja 4–5 jam).

Sementara jika keluarga memilih layanan vaksinasi lansia di rumah Joy of Care:

1. Paket All-in Vaksin Influenza Kuadrivalen Homecare: Rp 550.000 – Rp 675.000
2. Biaya Transportasi Tenaga Medis: Rp 0 (Sudah termasuk dalam paket kunjungan)
3. Biaya Konsultasi Dokter & Skrining Pra-Vaksinasi: Rp 0 (Included)
4. Biaya Administrasi & Pencatatan Sertifikat Vaksin: Rp 0 (Included)
5. **Total Biaya Bersih**: **Rp 550.000 – Rp 675.000** (Tanpa biaya tersembunyi, keluarga tetap produktif bekerja dari rumah)."""

    new_sec = f"""1. Tagihan harga vaksin di faskes komersial dengan margin rumah sakit.
2. Beban biaya administrasi pendaftaran dan kartu rekam medis pasien baru.
3. Beban jasa konsultasi dokter poliklinik rumah sakit.
4. Biaya transportasi kendaraan khusus lansia atau taksi online pulang-pergi di tengah kemacetan kota.
5. Biaya parkir kendaraan, logistik, serta hilangnya jam produktif kerja keluarga karena harus izin cuti 4–5 jam.
6. **Hasil Akhir**: Total beban pengeluaran membengkak tinggi diiringi kelelahan fisik lansia.

Sementara jika keluarga memilih layanan vaksinasi lansia di rumah Joy of Care:

1. Paket all-in vaksinasi terdaftar BPOM dan terjamin dalam rantai dingin (*cold chain*) vaksin steril.
2. Biaya transportasi tenaga medis flat dan transparan tanpa lonjakan harga tersembunyi.
3. Skrining pra-vaksinasi komprehensif oleh dokter atau perawat profesional langsung di kamar orang tua.
4. Pencatatan resmi sertifikat vaksinasi dan pemantauan Kejadian Ikutan Pasca Imunisasi (KIPI).
5. **Hasil Terbukti**: Jauh lebih hemat, bebas antrean rumah sakit, lansia terlindungi nyaman, dan keluarga tetap produktif beraktivitas dari rumah. {PRIMARY_CTA}"""
    text = text.replace(old_sec, new_sec)
    return text

def handle_vaksin_lansia_panduan_lengkap(text):
    old_fm = "answer: Tarif layanan vaksinasi lansia di rumah Joy of Care berkisar antara Rp 520.000\n    hingga Rp 680.000 untuk vaksin influenza kuadrivalen, Rp 1.150.000 hingga Rp 1.650.000\n    untuk vaksin pneumonia terkonjugasi (PCV13/15), dan Rp 2.400.000 hingga Rp 2.800.000\n    untuk vaksin herpes zoster rekombinan (Shingrix) per dosis, sudah mencakup jasa\n    tenaga medis dan transport."
    new_fm = f"answer: Tarif layanan vaksinasi lansia di rumah Joy of Care ditentukan secara transparan sesuai jenis vaksin resmi (Influenza Kuadrivalen, Pneumonia PCV13/15, PPSV23, atau Herpes Zoster Shingrix), sudah mencakup jasa tenaga medis dan pemeliharaan cold chain steril. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    old_table = """|---|---|---|---|
| **Vaksin Influenza Kuadrivalen** | Virus Flu A & B Musiman | Rp 550.000 – Rp 675.000 | 1 dosis setiap 1 tahun sekali |
| **Vaksin Pneumonia PCV13/15** | Bakteri Radang Paru Pneumokokus | Rp 1.150.000 – Rp 1.450.000 | 1 dosis primer seumur hidup |
| **Vaksin Pneumonia PPSV23** | 23 Serotipe Pneumokokus | Rp 1.050.000 – Rp 1.350.000 | 1 dosis penguat (1 tahun paska PCV) |
| **Vaksin Herpes Zoster Rekombinan** | Cacar Ular & Nyeri Saraf PHN | Rp 2.450.000 – Rp 2.750.000 / dosis | 2 dosis (jarak interval 2–6 bulan) |
| **Paket Imunisasi Komprehensif Geriatri** | Flu Kuadrivalen + Pneumonia PCV | Rp 1.650.000 – Rp 1.950.000 | Bundling lengkap hemat homecare |"""

    new_table = f"""|---|---|---|---|
| **Vaksin Influenza Kuadrivalen** | Virus Flu A & B Musiman | Paket Tahunan (Hubungi WA JoC) | 1 dosis setiap 1 tahun sekali |
| **Vaksin Pneumonia PCV13/15** | Bakteri Radang Paru Pneumokokus | Perlindungan Paru (Hubungi WA JoC) | 1 dosis primer seumur hidup |
| **Vaksin Pneumonia PPSV23** | 23 Serotipe Pneumokokus | Dosis Penguat (Hubungi WA JoC) | 1 dosis penguat (1 tahun paska PCV) |
| **Vaksin Herpes Zoster Rekombinan** | Cacar Ular & Nyeri Saraf PHN | Imunisasi Saraf (Hubungi WA JoC) | 2 dosis (jarak interval 2–6 bulan) |
| **Paket Imunisasi Komprehensif Geriatri** | Flu Kuadrivalen + Pneumonia PCV | Paket Bundling (Hubungi WA JoC) | Bundling lengkap hemat homecare |

{PRIMARY_CTA}"""
    text = text.replace(old_table, new_table)
    return text
