# Handler functions for files 14 to 26

PRIMARY_CTA = "Hubungi WhatsApp JoC untuk informasi harga: https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Berapa%20biaya%20layanan%20Joy%20of%20Care?"
ALTERNATE_CTA = "Konsultasi Dokter Gratis via WhatsApp: https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Mau%20konsultasi%20gratis%20dengan%20dokter"

def handle_cek_darah_biaya_perbandingan(text):
    text = text.replace(
        "| **Tarif Dasar Uji Parameter Lab** | Standar klinik resmi (Rp 300rb – Rp 1,5jt) | **Sama dengan standar resmi klinik terakreditasi** |",
        "| **Tarif Dasar Uji Parameter Lab** | Standar laboratorium klinik resmi | **Sama dengan standar resmi laboratorium terakreditasi** |"
    )
    text = text.replace(
        "| **Biaya Transportasi & Tol** | Rp 80.000 – Rp 200.000 (Taksi/Bensin/Tol) | **Rp 0 – Rp 75.000 (Biaya transport flebotomis minimal)** |",
        "| **Biaya Transportasi & Tol** | Ongkos taksi, bensin, dan tol pulang-pergi | **Bebas Macet (Transport flebotomis flat & terjangkau)** |"
    )
    
    old_sim = """* Biaya taksi online pulang-pergi (atau bensin + tol kendaraan pribadi): rata-rata **Rp 120.000**.
* Biaya parkir rumah sakit/klinik selama 2–3 jam: **Rp 20.000**.
* Biaya makan sarapan darurat di kantin rumah sakit: **Rp 75.000**.
* Nilai waktu produktif kerja Anda yang hilang (setengah hari cuti kerja): minimal setara **Rp 200.000 – Rp 400.000**.
* Total biaya tersembunyi (*hidden costs*) pergi ke klinik: **Rp 415.000 – Rp 615.000**!

Pada layanan home lab Joy of Care, biaya transport flebotomis hanya berkisar antara Rp 50.000 hingga Rp 100.000 (bahkan gratis pada paket-paket pemeriksaan geriatri berkala). Dengan demikian, memilih layanan cek darah di rumah sejatinya **menghemat uang keluarga hingga ratusan ribu rupiah**, sekaligus menyelamatkan kondisi emosional orang tua dari keletihan yang sia-sia."""

    new_sim = f"""* Biaya taksi online atau bensin kendaraan pribadi ditambah karcis tol pulang-pergi.
* Biaya karcis parkir rumah sakit/laboratorium dan biaya logistik pendamping.
* Kehilangan waktu produktif kerja berharga karena harus mengambil cuti setengah hari.
* Risiko kelelahan fisik lansia akibat harus berpuasa dalam perjalanan macet.
* **Hasil**: Total pengeluaran tersembunyi (*hidden costs*) berobat ke klinik membengkak tinggi tanpa disadari!

Pada layanan home lab Joy of Care, flebotomis tersertifikasi datang langsung ke rumah dengan peralatan tabung vakum steril dan rantai dingin terstandar. Biaya layanan transparan tanpa biaya tersembunyi. Memilih cek darah di rumah terbukti jauh lebih efisien, nyaman, dan melindungi lansia dari risiko kelelahan. {PRIMARY_CTA}"""
    text = text.replace(old_sim, new_sim)
    return text

def handle_cek_darah_panduan_lengkap(text):
    old_fm = "answer: Biaya cek darah di rumah (home lab) berkisar antara Rp 150.000 hingga Rp\n    350.000 untuk parameter tunggal (seperti gula darah puasa, kolesterol lengkap,\n    atau asam urat), dan Rp 650.000 hingga Rp 2.500.000 untuk paket komprehensif (seperti\n    panel fungsi hati, fungsi ginjal, profil lipid, dan darah lengkap), sudah termasuk\n    jasa pengambilan darah steril oleh flebotomis."
    new_fm = f"answer: Biaya cek darah di rumah Joy of Care ditentukan secara transparan sesuai parameter atau paket panel komprehensif yang dipilih, sudah mencakup jasa pengambilan darah steril oleh flebotomis berlisensi dan pengantaran sampel ke laboratorium rekanan resmi. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    text = text.replace(
        "> * **Transparansi Biaya 2026**: Paket pemeriksaan darah rutin mulai dari Rp 300.000-an hingga paket panel lengkap komorbid geriatri sekitar Rp 1.500.000 hingga Rp 2.500.000 tanpa biaya terselubung.",
        f"> * **Transparansi Layanan Home Lab**: Paket pemeriksaan darah rutin hingga paket panel lengkap komorbid geriatri dirancang transparan tanpa biaya terselubung. {PRIMARY_CTA}"
    )
    
    old_table = """|---|---|---|---|
| **Paket Skrining Diabetes** | Gula Darah Puasa (GDP), HbA1c, Glukosa 2 Jam PP | Rp 280.000 – Rp 450.000 | Penderita diabetes & riwayat gula tinggi |
| **Paket Profil Lipid (Lemak)** | Kolesterol Total, HDL, LDL, Trigliserida | Rp 250.000 – Rp 400.000 | Evaluasi risiko jantung, stroke, hipertensi |
| **Paket Fungsi Organ Vital** | SGOT, SGPT (Hati), Ureum, Kreatinin (Ginjal), Asam Urat | Rp 450.000 – Rp 750.000 | Pasien konsumsi obat rutin jangka panjang |
| **Paket Darah Rutin & Imun** | Darah Lengkap (CBC 18 parameter), LED, CRP Kuantitatif | Rp 300.000 – Rp 550.000 | Pasien demam, tanda infeksi paru/saluran kemih |
| **Paket Geriatri Komprehensif** | CBC, Profil Lipid, Fungsi Hati, Fungsi Ginjal, HbA1c, Elektrolit | Rp 1.250.000 – Rp 1.950.000 | Lansia > 60 tahun untuk Medical Check Up berkala |
| **Paket Khusus Tirah Baring** | Panel Geriatri + Albumin Serum, Analisis Urin Lengkap | Rp 1.500.000 – Rp 2.400.000 | Pasien stroke, tirah baring, risiko malnutrisi |"""

    new_table = f"""|---|---|---|---|
| **Paket Skrining Diabetes** | Gula Darah Puasa (GDP), HbA1c, Glukosa 2 Jam PP | Panel Terstandar (Hubungi WA JoC) | Penderita diabetes & riwayat gula tinggi |
| **Paket Profil Lipid (Lemak)** | Kolesterol Total, HDL, LDL, Trigliserida | Panel Terstandar (Hubungi WA JoC) | Evaluasi risiko jantung, stroke, hipertensi |
| **Paket Fungsi Organ Vital** | SGOT, SGPT (Hati), Ureum, Kreatinin (Ginjal), Asam Urat | Panel Terstandar (Hubungi WA JoC) | Pasien konsumsi obat rutin jangka panjang |
| **Paket Darah Rutin & Imun** | Darah Lengkap (CBC 18 parameter), LED, CRP Kuantitatif | Panel Terstandar (Hubungi WA JoC) | Pasien demam, tanda infeksi paru/saluran kemih |
| **Paket Geriatri Komprehensif** | CBC, Profil Lipid, Fungsi Hati, Fungsi Ginjal, HbA1c, Elektrolit | Panel Lengkap (Hubungi WA JoC) | Lansia > 60 tahun untuk Medical Check Up berkala |
| **Paket Khusus Tirah Baring** | Panel Geriatri + Albumin Serum, Analisis Urin Lengkap | Panel Lengkap (Hubungi WA JoC) | Pasien stroke, tirah baring, risiko malnutrisi |

{PRIMARY_CTA}"""
    text = text.replace(old_table, new_table)
    
    old_body_faq = "Biaya cek darah di rumah (home lab) berkisar antara Rp 150.000 hingga Rp 350.000 untuk parameter tunggal (seperti gula darah puasa, kolesterol lengkap, atau asam urat), dan Rp 650.000 hingga Rp 2.500.000 untuk paket komprehensif (seperti panel fungsi hati, fungsi ginjal, profil lipid, dan darah lengkap), sudah termasuk jasa pengambilan darah steril oleh flebotomis."
    new_body_faq = f"Biaya cek darah di rumah Joy of Care ditentukan secara transparan sesuai parameter atau paket komprehensif yang dibutuhkan, sudah mencakup jasa pengambilan darah steril oleh flebotomis berlisensi dan pengantaran sampel ke laboratorium rekanan resmi. {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_dokter_tangerang_biaya_perbandingan(text):
    text = text.replace(
        "> * **Kepastian Tarif Tanpa Biaya Tersembunyi**: Tarif resmi transparan mulai Rp 450.000 all-in tanpa lonjakan harga tak terduga (*no surge pricing*) saat jam sibuk.",
        f"> * **Kepastian Layanan Tanpa Biaya Tersembunyi**: Tarif visit resmi transparan all-in tanpa lonjakan harga tak terduga (*no surge pricing*) saat jam sibuk. {PRIMARY_CTA}"
    )
    text = text.replace(
        "| **Struktur Biaya** | **Transparan All-in** (Rp 450.000 – Rp 550.000), tanpa biaya tersembunyi. | Sering ada tambahan biaya admin aplikasi, biaya transport per km, dan *surge pricing*. | Tarif bervariasi luas tanpa standar baku, sering kali belum termasuk biaya transportasi. |",
        "| **Struktur Biaya** | **Transparan All-in** tanpa biaya tersembunyi (Hubungi WA JoC). | Tambahan biaya admin aplikasi, tarif per km, dan *surge pricing*. | Tarif bervariasi luas tanpa standar baku dan belum termasuk transport. |"
    )
    
    old_sim = """* **Skenario Kunjungan Dokter Joy of Care ke Rumah (Wilayah Tangerang)**:
  * Paket Dokter Umum Visit: Rp 475.000
  * Transportasi Medis: Rp 0 (Included)
  * Resep Obat Oral Standar: Tebus di apotek terdekat atau via apotek online
  * **Total Biaya**: **Rp 475.000** (Pasien istirahat tenang di rumah, waktu keluarga terhemat 100%).

* **Skenario Berobat ke IGD Rumah Sakit Swasta di BSD/Karawaci**:
  * Jasa Dokter IGD: Rp 250.000 – Rp 350.000
  * Biaya Administrasi & Kartu Pasien RS: Rp 75.000 – Rp 150.000
  * Biaya Penggunaan Ruang Tindakan IGD: Rp 200.000 – Rp 400.000
  * Biaya Taksi Online PP / Bensin & Parkir: Rp 100.000 – Rp 150.000
  * **Total Biaya**: **Rp 625.000 – Rp 1.050.000** (ditambah kelelahan fisik antre 2–3 jam di IGD dan risiko terpapar virus pasien lain)."""

    new_sim = f"""* **Skenario Kunjungan Dokter Joy of Care ke Rumah (Wilayah Tangerang)**:
  * Paket Dokter Umum Visit transparan mencakup anamnesis mendalam dan pemeriksaan fisik 45–60 menit.
  * Transportasi Medis flat zonasi terjangkau tanpa biaya perantara aplikasi.
  * Resep obat resmi yang dapat ditebus langsung di apotek pilihan keluarga tanpa markup instalasi RS.
  * **Hasil**: Pasien beristirahat tenang di rumah sendiri, bebas antrean, dan waktu keluarga terhemat 100%. {PRIMARY_CTA}

* **Skenario Berobat ke IGD Rumah Sakit Swasta di BSD/Karawaci**:
  * Tagihan ganda jasa dokter IGD dan biaya administrasi faskes.
  * Biaya pemakaian ruang observasi dan tindakan medis rumah sakit.
  * Biaya sewa transportasi khusus atau taksi online dan parkir RS.
  * **Hasil**: Total pengeluaran membengkak tinggi ditambah kelelahan fisik antre berjam-jam di IGD."""
    text = text.replace(old_sim, new_sim)
    return text

def handle_dokter_tangerang_panduan_lengkap(text):
    old_fm = "answer: Biaya jasa panggil dokter umum ke rumah Joy of Care untuk wilayah Kota\n    Tangerang dan Tangsel berkisar antara Rp 450.000 hingga Rp 650.000 per kunjungan,\n    tergantung jarak zonasi tempuh dan jenis tindakan medis tambahan yang diperlukan."
    new_fm = f"answer: Biaya panggil dokter umum ke rumah Joy of Care untuk wilayah Kota Tangerang dan Tangsel dirancang transparan, terjangkau, dan disesuaikan dengan kebutuhan tindakan klinis pasien tanpa biaya tersembunyi. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    text = text.replace(
        "> * **Transparansi Tarif 2026**: Biaya kunjungan terjangkau mulai Rp 450.000 all-in tanpa biaya tersembunyi yang memberatkan keluarga.",
        f"> * **Transparansi Layanan Dokter**: Biaya kunjungan dokter ke rumah dirancang terjangkau dan transparan all-in tanpa biaya tersembunyi yang memberatkan keluarga. {PRIMARY_CTA}"
    )
    
    old_table = """|---|---|---|
| **Kunjungan Dokter Umum Standar** | Anamnesis, TTV lengkap, pemeriksaan fisik, diagnosis, resep obat | Rp 450.000 – Rp 550.000 |
| **Kunjungan Dokter + Cek Darah Instan** | Visit dokter + tes glukosa sewaktu, asam urat, atau kolesterol strip | Rp 550.000 – Rp 680.000 |
| **Kunjungan Dokter + Tindakan Khusus** | Visit dokter + perawatan luka jahitan / debridement luka ringan | Rp 650.000 – Rp 850.000 |
| **Paket Evaluasi Geriatri Komprehensif** | Visit dokter + skrining kognitif geriatri + evaluasi polifarmasi obat | Rp 600.000 – Rp 750.000 |"""

    new_table = f"""|---|---|---|
| **Kunjungan Dokter Umum Standar** | Anamnesis, TTV lengkap, pemeriksaan fisik, diagnosis, resep obat | Tarif Transparan (Hubungi WA JoC) |
| **Kunjungan Dokter + Cek Darah Instan** | Visit dokter + tes glukosa sewaktu, asam urat, atau kolesterol strip | Layanan Terpadu (Hubungi WA JoC) |
| **Kunjungan Dokter + Tindakan Khusus** | Visit dokter + perawatan luka jahitan / debridement luka ringan | Tindakan Steril (Hubungi WA JoC) |
| **Paket Evaluasi Geriatri Komprehensif** | Visit dokter + skrining kognitif geriatri + evaluasi polifarmasi obat | Paket Spesial (Hubungi WA JoC) |

{PRIMARY_CTA}"""
    text = text.replace(old_table, new_table)
    return text

def handle_fisioterapi_lansia_biaya_perbandingan(text):
    old_fm = "answer: Biaya sesi terapi per visit adalah setara (Rp 250.000 – Rp 350.000). Namun\n    pergi ke klinik menambah beban biaya transportasi taksi khusus/kursi roda (Rp\n    150.000 – Rp 300.000 PP) serta waktu kerja keluarga yang hilang hingga 3 jam per\n    kedatangan."
    new_fm = f"answer: Biaya sesi fisioterapi per visit sangat kompetitif dan transparan. Melakukan terapi di rumah menghapus total biaya sewa taksi kursi roda dan menghemat waktu produktif keluarga hingga berjam-jam. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    old_table = """| **Tarif Jasa Terapis Dasar** | Rp 250.000 – Rp 400.000 / sesi | **Rp 275.000 – Rp 350.000 / sesi (Setara)** |
| **Biaya Tambahan Transportasi** | Rp 150.000 – Rp 300.000 (Taksi/Ambulans PP) | **Rp 0 – Rp 50.000 (Biaya transport terapis flat)** |"""

    new_table = """| **Tarif Jasa Fisioterapis Dasar** | Tarif standar klinik atau rumah sakit | **Kompetitif & Transparan (Hubungi WA JoC)** |
| **Biaya Tambahan Transportasi** | Biaya tinggi sewa taksi khusus kursi roda PP | **Rp 0 (Terapis datang langsung ke rumah)** |"""
    text = text.replace(old_table, new_table)
    
    old_body_faq = "Biaya sesi terapi per visit adalah setara (Rp 250.000 – Rp 350.000). Namun pergi ke klinik menambah beban biaya transportasi taksi khusus/kursi roda (Rp 150.000 – Rp 300.000 PP) serta waktu kerja keluarga yang hilang hingga 3 jam per kedatangan."
    new_body_faq = f"Biaya sesi terapi per visit Joy of Care sangat terjangkau dan transparan. Keunggulan terbesar homecare adalah menghapus seluruh biaya sewa transportasi khusus, bebas macet, dan tidak menyita jam kerja anggota keluarga. {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_fisioterapi_lansia_panduan_lengkap(text):
    old_fm = "answer: Biaya fisioterapi lansia kunjungan ke rumah di Jakarta berkisar antara Rp\n    250.000 hingga Rp 400.000 per sesi latihan berdurasi 45–60 menit. Tersedia pula\n    paket terapi berkala (8 hingga 12 sesi per bulan) dengan potongan harga khusus\n    untuk program rehabilitasi jangka panjang."
    new_fm = f"answer: Biaya fisioterapi lansia kunjungan ke rumah di Jakarta dirancang terjangkau dan transparan per sesi berdurasi 45–60 menit. Tersedia pula paket rehabilitasi berkala bulanan yang lebih hemat untuk pemulihan jangka panjang. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    old_table = """|---|---|---|---|
| **Fisioterapi Kunjungan Tunggal (Per Visit)** | Asesmen fisik, latihan motorik, edukasi keluarga | Rp 275.000 – Rp 350.000 | 45 – 60 Menit |
| **Paket Pemulihan Aktif (8 Sesi / Bulan)** | Asesmen berkala, latihan kekuatan, modalitas TENS | Rp 2.000.000 – Rp 2.400.000 | 60 Menit per sesi |
| **Paket Rehabilitasi Intensif (12 Sesi / Bulan)** | Program pascastroke / pascaoperasi panggul | Rp 2.850.000 – Rp 3.450.000 | 60 Menit per sesi |
| **Paket Khusus Tirah Baring (Passive ROM)** | Mobilisasi sendi kaku, alih baring, latihan napas | Rp 2.200.000 – Rp 2.600.000 | 45 – 60 Menit (8 sesi) |"""

    new_table = f"""|---|---|---|---|
| **Fisioterapi Kunjungan Tunggal (Per Visit)** | Asesmen fisik, latihan motorik, edukasi keluarga | Tarif Transparan (Hubungi WA JoC) | 45 – 60 Menit |
| **Paket Pemulihan Aktif (8 Sesi / Bulan)** | Asesmen berkala, latihan kekuatan, modalitas TENS | Paket Berkala (Hubungi WA JoC) | 60 Menit per sesi |
| **Paket Rehabilitasi Intensif (12 Sesi / Bulan)** | Program pascastroke / pascaoperasi panggul | Paket Intensif (Hubungi WA JoC) | 60 Menit per sesi |
| **Paket Khusus Tirah Baring (Passive ROM)** | Mobilisasi sendi kaku, alih baring, latihan napas | Paket Pasien Tirah Baring (Hubungi WA JoC) | 45 – 60 Menit (8 sesi) |

{PRIMARY_CTA}"""
    text = text.replace(old_table, new_table)
    
    old_body_faq = "Biaya fisioterapi lansia kunjungan ke rumah di Jakarta berkisar antara Rp 250.000 hingga Rp 400.000 per sesi latihan berdurasi 45–60 menit. Tersedia pula paket terapi berkala (8 hingga 12 sesi per bulan) dengan potongan harga khusus untuk program rehabilitasi jangka panjang."
    new_body_faq = f"Biaya fisioterapi lansia kunjungan ke rumah di Jakarta dirancang terjangkau dan transparan per sesi berdurasi 45–60 menit. Tersedia pula paket program pemulihan intensif bulanan yang sangat terukur untuk memastikan lansia kembali mandiri. {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_fisioterapi_stroke_biaya_perbandingan(text):
    old_fm = "answer: Biaya satu sesi kunjungan fisioterapi pasca stroke ke rumah di Jakarta umumnya\n    berkisar antara Rp 250.000 hingga Rp 450.000 per sesi, tergantung paket kunjungan\n    dan modalitas stimulasi yang digunakan."
    new_fm = f"answer: Biaya fisioterapi pasca stroke ke rumah di Jakarta dirancang terjangkau dan transparan per sesi, disesuaikan dengan fase rehabilitasi dan modalitas stimulasi neuromuskular yang diperlukan pasien. {ALTERNATE_CTA}"
    text = text.replace(old_fm, new_fm)
    
    old_table = """| **Biaya Jasa Terapi** | Rp 200.000 – Rp 400.000 / sesi | **Rp 275.000 – Rp 400.000 / sesi** |
| **Biaya Transport Khusus PP** | Rp 300.000 – Rp 700.000 / hari | **Rp 0 (Bebas Biaya Kendaraan Sewa)** |
| **Estimasi Total Pengeluaran** | **Rp 500.000 – Rp 1.100.000 / visit** | **Rp 275.000 – Rp 400.000 / visit** |"""

    new_table = f"""| **Biaya Jasa Terapi Sesi** | Tarif standar fisioterapi klinik | **Transparan & Terjangkau (Hubungi WA JoC)** |
| **Biaya Transport Khusus PP** | Sewa ambulans / taksi kursi roda PP mahal | **Rp 0 (Terapis datang langsung ke rumah)** |
| **Efisiensi Total Biaya** | **Beban Pengeluaran Tinggi per Sesi** | **Hemat Signifikan Tanpa Biaya Tersembunyi** |

{ALTERNATE_CTA}"""
    text = text.replace(old_table, new_table)
    
    old_body_faq = "Biaya satu sesi kunjungan fisioterapi pasca stroke ke rumah di Jakarta umumnya berkisar antara Rp 250.000 hingga Rp 450.000 per sesi, tergantung paket kunjungan dan modalitas stimulasi yang digunakan."
    new_body_faq = f"Biaya satu sesi kunjungan fisioterapi pasca stroke ke rumah di Jakarta dirancang kompetitif dan transparan, disesuaikan dengan kebutuhan modalitas pemulihan gerak fungsional dan paket pendampingan yang dipilih. {ALTERNATE_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_infus_vitamin_biaya_perbandingan(text):
    old_fm = "answer: Tidak selalu. Tarif paket infus vitamin Joy of Care (Rp 635.000 – Rp 850.000)\n    bersifat transparan dan all-in sudah termasuk jasa perawat dan transport flat,\n    setara atau bahkan lebih hemat dibanding klinik kecantikan yang sering membebankan\n    biaya konsultasi dokter klinik dan biaya registrasi tambahan."
    new_fm = f"answer: Tidak selalu. Tarif paket infus vitamin Joy of Care bersifat transparan dan all-in sudah mencakup multivitamin berstandar BPOM, jasa perawat ber-STR, dan transport flat tanpa biaya registrasi tambahan. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    old_table = """| **Estimasi Biaya Paket Multivitamin** | Rp 750.000 – Rp 1.500.000 / sesi | **Rp 636.500 – Rp 850.000 / sesi (Transparan)** |
| **Biaya Tambahan Tersembunyi** | Biaya konsultasi dokter, parkir, admin | **Rp 0 (Semua komponen sudah all-in)** |"""

    new_table = """| **Paket Multivitamin Berkualitas** | Tarif klinik dengan margin komersial tinggi | **Transparan & Terjangkau (Hubungi WA JoC)** |
| **Biaya Tambahan Tersembunyi** | Beban karcis registrasi, parkir mall, admin | **Rp 0 (Semua komponen tindakan sudah all-in)** |"""
    text = text.replace(old_table, new_table)
    
    old_sim = """* Biaya transportasi taksi online pulang-pergi (atau bensin + tol): **Rp 100.000 – Rp 180.000**.
* Biaya parkir gedung atau valet mall klinik: **Rp 20.000 – Rp 50.000**.
* Biaya registrasi pasien baru klinik estetika: **Rp 50.000 – Rp 100.000**.
* Biaya konsultasi dokter klinik: **Rp 150.000 – Rp 250.000**.
* **Total Biaya Tersembunyi di Klinik**: **Rp 320.000 – Rp 580.000** di luar harga paket vitamin itu sendiri!"""

    new_sim = f"""* Beban transportasi kendaraan pribadi atau taksi online pulang-pergi di jalan macet.
* Karcis parkir gedung komersial atau biaya valet klinik kecantikan di mall.
* Biaya administrasi kartu pasien baru dan karcis konsultasi dokter klinik.
* **Hasil**: Tambahan biaya terselubung di klinik membuat pengeluaran membengkak jauh di atas harga paket vitamin itu sendiri! Pada layanan Joy of Care, seluruh tindakan dilakukan steril di rumah dengan tarif transparan. {PRIMARY_CTA}"""
    text = text.replace(old_sim, new_sim)
    
    old_body_faq = "Tidak selalu. Tarif paket infus vitamin Joy of Care (Rp 635.000 – Rp 850.000) bersifat transparan dan all-in sudah termasuk jasa perawat dan transport flat, setara atau bahkan lebih hemat dibanding klinik kecantikan yang sering membebankan biaya konsultasi dokter klinik dan biaya registrasi tambahan."
    new_body_faq = f"Tidak selalu. Tarif paket infus vitamin Joy of Care bersifat transparan dan all-in sudah termasuk jasa perawat profesional dan transport flat, jauh lebih hemat dibanding klinik komersial yang membebankan biaya konsultasi dan registrasi terpisah. {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_infus_vitamin_panduan_lengkap(text):
    old_fm = "answer: Harga terapi infus vitamin di rumah Joy of Care berkisar antara Rp 475.000\n    untuk suntik vitamin C murni (injeksi IV langsung), Rp 635.000 hingga Rp 850.000\n    untuk paket infus drip multivitamin B Kompleks + Vitamin C 1.000 mg, dan Rp 1.200.000\n    hingga Rp 1.800.000 untuk paket premium Immune Booster / Anti-Fatigue Cocktail."
    new_fm = f"answer: Tarif terapi infus vitamin di rumah Joy of Care ditentukan transparan berdasarkan formulasi multivitamin yang dibutuhkan (Vitamin C murni, Neurotropik B Kompleks, hingga Immune Booster Cocktail), sudah all-in dengan jasa perawat profesional. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    text = text.replace(
        "> * **Transparansi Tarif Resmi 2026**: Paket suntik vitamin C mulai Rp 475.000-an, paket infus drip B+C Rp 635.000-an, hingga formula immune booster lengkap tanpa biaya tersembunyi.",
        f"> * **Transparansi Tarif Resmi**: Paket suntik vitamin C, infus drip multivitamin B+C, hingga formula immune booster lengkap disajikan dengan sistem tarif all-in tanpa biaya tersembunyi. {PRIMARY_CTA}"
    )
    
    old_table = """|---|---|---|---|
| **Suntik Vitamin C Murni (IV Push)** | Pure Vitamin C 1.000 mg steril | Rp 475.000 / sesi | Imunitas harian, pencerah kulit, antioksidan |
| **Infus Multivitamin B + C Drip** | Vit C 1.000 mg + B1, B6, B12 Neurotropik | Rp 636.500 / sesi | Atasi badan pegal, lemas, kelelahan kerja |
| **Paket Immune Booster Platinum** | Vit C Dosis Tinggi + B Kompleks + Zinc + Elektrolit | Rp 850.000 – Rp 1.100.000 | Masa pemulihan pasca-DBD, tifus, atau flu berat |
| **Paket Anti-Fatigue & Vitalitas** | Formula Myers Cocktail (Magnesium, B-Kompleks, C) | Rp 1.150.000 – Rp 1.450.000 | Mengatasi migrain, insomnia, jet lag, burnout |
| **Paket Geriatri Wellness Lansia** | Multivitamin B-Kompleks + Hidrasi Cairan Elektrolit | Rp 750.000 – Rp 950.000 | Lansia sulit makan, dehidrasi ringan, lemas |"""

    new_table = f"""|---|---|---|---|
| **Suntik Vitamin C Murni (IV Push)** | Pure Vitamin C 1.000 mg steril | Paket Standar (Hubungi WA JoC) | Imunitas harian, pencerah kulit, antioksidan |
| **Infus Multivitamin B + C Drip** | Vit C 1.000 mg + B1, B6, B12 Neurotropik | Paket Neurotropik (Hubungi WA JoC) | Atasi badan pegal, lemas, kelelahan kerja |
| **Paket Immune Booster Platinum** | Vit C Dosis Tinggi + B Kompleks + Zinc + Elektrolit | Paket Pemulihan (Hubungi WA JoC) | Masa pemulihan pasca-DBD, tifus, atau flu berat |
| **Paket Anti-Fatigue & Vitalitas** | Formula Myers Cocktail (Magnesium, B-Kompleks, C) | Paket Vitalitas (Hubungi WA JoC) | Mengatasi migrain, insomnia, jet lag, burnout |
| **Paket Geriatri Wellness Lansia** | Multivitamin B-Kompleks + Hidrasi Cairan Elektrolit | Paket Lansia (Hubungi WA JoC) | Lansia sulit makan, dehidrasi ringan, lemas |

{PRIMARY_CTA}"""
    text = text.replace(old_table, new_table)
    
    old_body_faq = "Harga terapi infus vitamin di rumah Joy of Care berkisar antara Rp 475.000 untuk suntik vitamin C murni (injeksi IV langsung), Rp 635.000 hingga Rp 850.000 untuk paket infus drip multivitamin B Kompleks + Vitamin C 1.000 mg, dan Rp 1.200.000 hingga Rp 1.800.000 untuk paket premium Immune Booster / Anti-Fatigue Cocktail."
    new_body_faq = f"Harga terapi infus vitamin di rumah Joy of Care disesuaikan dengan formulasi nutrisi yang dipilih, mulai dari injeksi vitamin C murni, multivitamin neurotropik B-kompleks, hingga formula immune booster lengkap dengan jaminan all-in bebas biaya tersembunyi. {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_perawat_terpercaya_biaya_perbandingan(text):
    text = text.replace(
        "Banyak agensi konvensional mengenakan biaya administrasi penempatan awal yang sangat mahal (berkisar Rp 1.500.000 hingga Rp 3.000.000). Jika dalam waktu 1 bulan perawat berhenti bekerja, uang administrasi tersebut sering kali hangus atau keluarga dikenakan biaya denda baru untuk mendatangkan pengganti.",
        f"Banyak agensi konvensional mengenakan biaya administrasi penempatan awal yang sangat mahal tanpa jaminan pasti. Jika perawat berhenti bekerja, uang administrasi sering kali hangus. Sebaliknya, Joy of Care menerapkan sistem transparan dengan jaminan penggantian perawat tanpa biaya tersembunyi. {PRIMARY_CTA}"
    )
    return text

def handle_perawat_terpercaya_panduan_lengkap(text):
    old_fm = "answer: Biaya jasa perawat homecare medis berijazah D3/S1 Keperawatan berkisar antara\n    Rp 5.000.000 hingga Rp 9.500.000 per bulan untuk sistem live-in 24 jam, atau Rp\n    250.000 hingga Rp 400.000 per shift harian 12 jam, tergantung kompleksitas alat\n    medis pasien."
    new_fm = f"answer: Biaya jasa perawat homecare medis berijazah resmi ditentukan secara transparan berdasarkan sistem penugasan (live-in 24 jam, shift harian, atau per visit tindakan medis) serta kompleksitas alat kesehatan pasien. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    old_list = """* **Perawat Medis Live-In 24 Jam (Menginap Bulanan)**: Rp 5.500.000 – Rp 9.500.000 per bulan. Khusus untuk pasien pascastroke, tirah baring (*bedridden*), terpasang selang makan NGT, kateter urin, atau trakeostomi.
* **Caregiver Lansia Live-In 24 Jam (Menginap Bulanan)**: Rp 2.800.000 – Rp 4.500.000 per bulan. Untuk pendampingan lansia mandiri sebagian (*partial dependent*), bantuan aktivitas mandi, makan, dan jalan santai.
* **Perawat Medis Shift Harian (12 Jam)**: Rp 250.000 – Rp 400.000 per shift. Cocok untuk keluarga yang membutuhkan pengawasan medis saat jam kerja kantor siang hari.
* **Kunjungan Tindakan Medis Khusus (Per Visit)**: Rp 200.000 – Rp 350.000 per kunjungan. Untuk penggantian selang NGT steril, pemasangan kateter urine baru, atau perawatan luka diabetes gangren."""

    new_list = f"""* **Perawat Medis Live-In 24 Jam (Menginap Bulanan)**: Layanan komprehensif bagi pasien pascastroke, tirah baring, terpasang selang makan NGT, kateter urin, atau trakeostomi dengan sistem kontrak transparan.
* **Caregiver Lansia Live-In 24 Jam (Menginap Bulanan)**: Pendampingan lansia mandiri sebagian, pemenuhan kebutuhan aktivitas harian (ADL), pendampingan mobilisasi, dan stimulasi kognitif.
* **Perawat Medis Shift Harian (12 Jam)**: Pendampingan medis profesional saat jam kerja keluarga siang hari atau pemantauan malam hari.
* **Kunjungan Tindakan Medis Khusus (Per Visit)**: Kunjungan steril untuk penggantian selang NGT, pemasangan kateter urine Foley, atau perawatan luka diabetes modern dressing. {PRIMARY_CTA}"""
    text = text.replace(old_list, new_list)
    
    old_body_faq = "Biaya jasa perawat homecare medis berijazah D3/S1 Keperawatan berkisar antara Rp 5.000.000 hingga Rp 9.500.000 per bulan untuk sistem live-in 24 jam, atau Rp 250.000 hingga Rp 400.000 per shift harian 12 jam, tergantung kompleksitas alat medis pasien."
    new_body_faq = f"Biaya jasa perawat homecare medis berijazah resmi dirancang transparan berdasarkan sistem kerja yang dibutuhkan (live-in, shift harian, atau per visit tindakan khusus) serta kualifikasi klinis tenaga kesehatan. {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_kesehatan_lansia_rutinitas_biaya_perbandingan(text):
    old_fm = "answer: Lansia pasif yang mengalami komplikasi penyakit degeneratif rata-rata\n    membutuhkan biaya 4 hingga 7 kali lipat lebih tinggi (berkisar antara Rp 80.000.000\n    hingga Rp 180.000.000 per tahun) untuk penanganan luka dekubitus, infeksi saluran\n    kemih berulang, pneumonia aspirasi, dan rawat inap ICU, dibandingkan dengan\n    lansia aktif yang hanya memerlukan biaya perawatan preventif sekitar Rp 15.000.000\n    hingga Rp 25.000.000 per tahun."
    new_fm = f"answer: Lansia pasif yang mengalami komplikasi penyakit rata-rata membutuhkan biaya medis 4 hingga 7 kali lipat lebih tinggi untuk rawat inap ICU dan penanganan dekubitus, dibanding lansia aktif yang mengutamakan rutinitas fisik preventif. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    old_sec = """1. **Rawat Inap RS Akibat Pneumonia Aspirasi / Sepsis Dekubitus**: Rata-rata 1–2 kali perawatan ICU/HCU per tahun = Rp 50.000.000 – Rp 90.000.000.
2. **Perawatan Luka Dekubitus Khusus oleh Tenaga Medis**: Penggantian kassa modern dressing 3x seminggu = Rp 1.200.000/minggu atau sekitar Rp 62.000.000/tahun.
3. **Kebutuhan Logistik Pasien Bedridden**: Popok dewasa (*diapers*), perlak medis, kateter urin, selang NGT, dan suction lendir = Rp 18.000.000 – Rp 25.000.000/tahun.
4. **Total Estimasi Biaya Per Tahun**: **Rp 130.000.000 – Rp 177.000.000+** (serta beban mental dan emosional keluarga yang sangat berat).

Sementara itu, mari kita bandingkan dengan estimasi biaya pemeliharaan kesehatan lansia aktif yang konsisten menjalankan rutinitas harian terstruktur:

1. **Pemeriksaan Dokter dan Skrining Laboratorium Berkala**: Kunjungan [Layanan Panggil Dokter ke Rumah Jakarta](/layanan/panggil-dokter) dan [Layanan Cek Lab Darah di Rumah](/layanan/cek-lab-di-rumah) setiap 3 bulan = Rp 4.500.000/tahun.
2. **Paket Sesi Latihan Bersama Fisioterapis Homecare**: Mempertahankan mobilitas dan keseimbangan fisik 2x sebulan = Rp 8.400.000/tahun.
3. **Suplemen Nutrisi & Vitamin Esensial**: Kalsium, vitamin D3, dan susu protein geriatri = Rp 6.000.000/tahun.
4. **Total Estimasi Biaya Per Tahun**: **Rp 18.900.000 – Rp 24.500.000/tahun**.

Investasi preventif pada pola hidup aktif menghasilkan penghematan biaya medis riil lebih dari Rp 100.000.000 per tahun, sekaligus memberikan kebahagiaan batin yang tak ternilai bagi orang tua tercinta."""

    new_sec = f"""1. **Rawat Inap Rumah Sakit Akibat Infeksi Berat**: Komplikasi pneumonia aspirasi atau sepsis luka tirah baring membutuhkan perawatan ruang intensif (ICU/HCU) dengan tagihan puluhan hingga ratusan juta rupiah.
2. **Perawatan Luka Khusus oleh Tenaga Medis**: Penggantian balutan luka modern secara berkelanjutan yang menguras biaya rutin keluarga.
3. **Kebutuhan Logistik Pasien Pasif**: Konsumsi harian popok dewasa, kateter urin, selang NGT, dan alat suction lendir berkepanjangan.
4. **Total Beban Medis Tahunan**: Mencapai ratusan juta rupiah diiringi penurunan drastis kualitas hidup dan kelelahan mental keluarga (*caregiver burnout*).

Sebaliknya, mari kita cermati pendekatan preventif pada lansia aktif yang konsisten menjalankan rutinitas harian terstruktur:

1. **Pemeriksaan Dokter dan Skrining Laboratorium Berkala**: Evaluasi kesehatan teratur di rumah melalui [Layanan Panggil Dokter ke Rumah Jakarta](/layanan/panggil-dokter) dan [Layanan Cek Lab Darah di Rumah](/layanan/cek-lab-di-rumah).
2. **Sesi Latihan Terarah Bersama Fisioterapis Homecare**: Menjaga fleksibilitas sendi, massa otot rangka, dan keseimbangan tubuh.
3. **Pemenuhan Nutrisi & Suplemen Esensial**: Asupan protein bergizi, kalsium, vitamin D3, dan hidrasi seimbang.
4. **Hasil Terbukti**: Menghemat biaya pengobatan darurat rumah sakit hingga lebih dari 70%, sekaligus menghadirkan masa tua yang mandiri, bahagia, dan bermartabat. {PRIMARY_CTA}"""
    text = text.replace(old_sec, new_sec)
    return text

def handle_latihan_fisioterapi_biaya_perbandingan(text):
    old_fm = "answer: Latihan mandiri berbiaya Rp 0, namun memiliki risiko biaya pengobatan ratusan\n    juta jika terjadi insiden jatuh patah tulang. Paket fisioterapis homecare (sekitar\n    Rp 2.000.000 – Rp 2.400.000 per bulan untuk 8 sesi) merupakan investasi preventif\n    yang sangat hemat dan terukur."
    new_fm = f"answer: Latihan fisik tanpa pengawasan terapis berisiko memicu cedera jatuh fatal yang menelan biaya medis hingga ratusan juta rupiah. Paket fisioterapi homecare merupakan investasi preventif yang terukur dan aman. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    text = text.replace(
        "| **Biaya Jasa Langsung** | **Rp 0 (Gratis)** | Rp 250.000 – Rp 350.000 / sesi paket |",
        "| **Biaya Jasa Langsung** | Bebas Biaya Langsung | **Transparan & Terukur (Hubungi WA JoC)** |"
    )
    
    old_sim = """* Biaya ambulans darurat: **Rp 500.000**.
* Operasi pemasangan pen patah panggul di rumah sakit swasta: **Rp 60.000.000 – Rp 120.000.000**.
* Rawat inap ruang intensif (ICU/HDU) selama 5 hari: **Rp 25.000.000**.
* Jasa perawat pendamping medis pascabedah selama 3 bulan: **Rp 18.000.000**.
* Pembelian tempat tidur medis hidrolik (*hospital bed*) dan kursi roda: **Rp 12.000.000**.
* **Total Tagihan Medis Darurat**: **Rp 115.500.000 – Rp 175.500.000+**!

Sebaliknya, berinvestasi pada paket fisioterapi lansia Joy of Care (berkisar antara **Rp 2.000.000 – Rp 2.400.000 per bulan** untuk 8 sesi komprehensif) memberikan perlindungan keselamatan fisik tingkat tinggi, memastikan otot lansia terbangun secara aman, serta membebaskan anak dari ketakutan konstan akan kecelakaan rumah tangga."""

    new_sim = f"""* Beban biaya evakuasi ambulans gawat darurat rumah sakit.
* Biaya tindakan operasi bedah ortopedi dan implan pen panggul yang menelan puluhan hingga ratusan juta rupiah.
* Biaya sewa ruang rawat intensif (ICU/HDU) dan kamar rawat inap rumah sakit swasta.
* Beban biaya keperawatan pascabedah dan pengadaan peralatan medis darurat di rumah.
* **Hasil**: Tagihan medis membengkak fantastis hingga ratusan juta rupiah, belum terhitung trauma fisik lansia.

Sebaliknya, berinvestasi pada paket fisioterapi terpadu Joy of Care di rumah memberikan perlindungan maksimal, menjaga koordinasi motorik lansia secara terukur, dan membebaskan keluarga dari kecemasan insiden jatuh. {PRIMARY_CTA}"""
    text = text.replace(old_sim, new_sim)
    
    old_body_faq = "Latihan mandiri berbiaya Rp 0, namun memiliki risiko biaya pengobatan ratusan juta jika terjadi insiden jatuh patah tulang. Paket fisioterapis homecare (sekitar Rp 2.000.000 – Rp 2.400.000 per bulan untuk 8 sesi) merupakan investasi preventif yang sangat hemat dan terukur."
    new_body_faq = f"Latihan mandiri tanpa pengawasan ahli rentan memicu cedera jatuh yang membutuhkan biaya penanganan rumah sakit sangat besar. Paket fisioterapis homecare terbukti menjadi langkah preventif yang aman, terencana, dan melindungi masa depan keluarga. {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text
