import re

PRIMARY_CTA = "Hubungi WhatsApp JoC untuk informasi harga: https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Berapa%20biaya%20layanan%20Joy%20of%20Care?"
ALTERNATE_CTA = "Konsultasi Dokter Gratis via WhatsApp: https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Mau%20konsultasi%20gratis%20dengan%20dokter"

def h_persyaratan_kesehatan_perjalanan_9(text):
    return text.replace("USD 50,000–100,000.", "perlindungan repatriasi medis penuh dan komprehensif. " + PRIMARY_CTA)

def h_persyaratan_medis_australia_14(text):
    text = re.sub(
        r'Biaya pemeriksaan bervariasi antara Rp 1\.200\.000 hingga Rp 2\.500\.000 tergantung[^\n]*',
        'Biaya pemeriksaan visa pelajar ditentukan oleh panel physician resmi sesuai regulasi kedutaan dan kebutuhan tes tambahan. ' + PRIMARY_CTA,
        text
    )
    return text

def h_akupuntur_biaya_perbandingan(text):
    text = text.replace("seharga Rp 20.000 per strip adalah opsi yang sangat murah", "secara bebas tanpa resep adalah opsi yang murah")
    old_sec = """### Skenario A: Perawatan Akibat Komplikasi Konsumsi Obat Nyeri Rutin (1 Tahun)
1. Pembelian obat NSAID + obat pelindung lambung harian: Rp 3.600.000/tahun
2. Biaya Rawat Inap RS Akibat Tukak Lambung Berdarah (Kamar + Transfusi Darah): Rp 25.000.000 – Rp 45.000.000
3. Biaya Perawatan Gagal Ginjal Stadium Awal (Nefrolog + Obat Ginjal): Rp 15.000.000 – Rp 35.000.000
4. **Total Risiko Biaya Medis**: **Rp 43.600.000 – Rp 83.600.000+**

### Skenario B: Program Terapi Akupuntur Medis Berkala Joy of Care (1 Tahun)
1. Siklus Awal Akupuntur Medis Intensif (8 sesi di rumah): Rp 3.200.000
2. Sesi Pemeliharaan Rutin (1x per bulan untuk menjaga sendi lentur): Rp 4.500.000/tahun
3. Suplemen Pelumas Sendi Alami (Glukosamin / Kolagen Tipe 2): Rp 2.400.000/tahun
4. **Total Investasi Kesehatan**: **Rp 10.100.000/tahun** (Nol komplikasi organ, ginjal dan lambung lansia 100% sehat terlindungi)."""

    new_sec = f"""### Skenario A: Risiko Komplikasi Konsumsi Obat Nyeri Kimiawi Jangka Panjang (1 Tahun)
1. Pembelian obat antinyeri NSAID dan pelindung lambung terus-menerus tanpa pengawasan dokter.
2. Beban rawat inap rumah sakit akibat tukak lambung akut atau perdarahan saluran cerna yang menuntut transfusi.
3. Beban perawatan gagal ginjal atau penurunan laju filtrasi glomerulus yang membutuhkan pemantauan nefrolog.
4. **Total Beban Medis**: Membengkak sangat besar hingga puluhan bahkan ratusan juta rupiah serta memicu penurunan kualitas hidup lansia.

### Skenario B: Program Terapi Akupuntur Medis Terpadu Joy of Care (1 Tahun)
1. Siklus awal akupuntur medis intensif di rumah oleh dokter/terapis berlisensi Kemenkes.
2. Sesi pemeliharaan berkala untuk menjaga kelenturan sendi dan meredakan kekakuan otot pagi hari.
3. Suplemen nutrisi pelindung sendi tanpa risiko toksisitas pada lambung maupun ginjal.
4. **Investasi Kesehatan Terencana**: Nol risiko komplikasi organ internal, kenyamanan dan mobilitas lansia terlindungi optimal. {PRIMARY_CTA}"""
    return text.replace(old_sec, new_sec)

def h_akupuntur_panduan_lengkap(text):
    text = re.sub(
        r'answer: Biaya resmi layanan akupuntur medis home visit Joy of Care berkisar antara\s+Rp 375\.000 hingga Rp 550\.000 per sesi[^\n]*',
        f'answer: Biaya layanan akupuntur medis home visit Joy of Care ditentukan secara transparan berdasarkan kebutuhan klinis pasien, sudah mencakup jasa tindakan dokter/terapis berlisensi, jarum steril sekali pakai, dan modalitas elektroakupunktur. {PRIMARY_CTA}',
        text
    )
    old_table = """|---|---|---|---|
| **Sesi Tunggal Akupuntur Manual** | Anamnesis, desinfeksi aseptik, tusuk 12–16 jarum mikro, retensi 25 menit | Rp 375.000 – Rp 450.000 | Nyeri sendi ringan, pegal linu, pemeliharaan |
| **Akupuntur Medik + Elektroakupunktur** | Akupuntur manual + stimulasi arus listrik mikro TENS frekuensi rendah | Rp 475.000 – Rp 550.000 | Osteoartritis derajat sedang-berat, kaku sendi pagi |
| **Paket Pemulihan Sendi (5 Sesi)** | 5 sesi elektroakupunktur + evaluasi mobilitas berkala (hemat 10%) | Rp 2.150.000 / paket | Pasien dengan kesulitan jalan mandiri |
| **Paket Intensif Kuratif (10 Sesi)** | 10 sesi komprehensif + konsultasi dokter (hemat 15%) | Rp 3.950.000 / paket | Nyeri sendi kronis menahun, pasca-jatuh |"""

    new_table = f"""|---|---|---|---|
| **Sesi Tunggal Akupuntur Manual** | Anamnesis, desinfeksi aseptik, tusuk 12–16 jarum mikro, retensi 25 menit | Transparan (Hubungi WA JoC) | Nyeri sendi ringan, pegal linu, pemeliharaan |
| **Akupuntur Medik + Elektroakupunktur** | Akupuntur manual + stimulasi arus listrik mikro TENS frekuensi rendah | Sesi Lengkap (Hubungi WA JoC) | Osteoartritis derajat sedang-berat, kaku sendi pagi |
| **Paket Pemulihan Sendi (5 Sesi)** | 5 sesi elektroakupunktur + evaluasi mobilitas berkala | Paket Hemat (Hubungi WA JoC) | Pasien dengan kesulitan jalan mandiri |
| **Paket Intensif Kuratif (10 Sesi)** | 10 sesi komprehensif + konsultasi dokter terpadu | Paket Intensif (Hubungi WA JoC) | Nyeri sendi kronis menahun, pasca-jatuh |

{PRIMARY_CTA}"""
    return text.replace(old_table, new_table)

def h_antar_jemput_biaya_perbandingan(text):
    text = text.replace(
        "| **Struktur Biaya** | Paket PP Rp 750.000 – Rp 950.000 (termasuk tunggu perawat 2–3 jam). | Ongkos argo per km (sering melonjak *surge price* saat jam sibuk/hujan). | Tarif panggilan darurat RS (Rp 1.200.000 – Rp 2.500.000 per trip). |",
        "| **Struktur Biaya** | Paket transparan all-in termasuk perawat pendamping & waktu tunggu RS. | Ongkos argo berfluktuasi tajam saat jam sibuk atau cuaca hujan. | Tarif panggilan darurat ambulans RS yang relatif sangat mahal. |"
    )
    old_sim = """* **Simulasi Opsi A (Taksi Online + Mandiri)**:
  * Taksi Online Berangkat (Jam Sibuk Pagi): Rp 180.000
  * Sewa Kursi Roda Lipat Portabel: Rp 150.000 / hari
  * Taksi Online Pulang (Hujan Sore / Surge Pricing): Rp 240.000
  * Biaya Tip Pengemudi Membantu Angkat Pasien: Rp 50.000
  * Biaya Izin Cuti Kerja 1 Hari Penuh: Tidak ternilai
  * **Total Biaya**: **Rp 620.000** (ditambah rasa cemas di jalan dan kelelahan fisik keluarga luar biasa).

* **Simulasi Opsi B (Joy of Care NEMT Transport Medis)**:
  * Paket Antar Jemput PP All-in: Rp 850.000
  * Armada Mobil Medis Khusus Brankar / Kursi Roda: Included
  * Tenaga Perawat Pendamping Medis Standby Poliklinik: Included
  * Fasilitas Oksigen Medis Standby: Included
  * **Total Biaya**: **Rp 850.000** (Pasien aman nyaman di ranjang mobil, urusan rumah sakit selesai tuntas, keluarga tenang)."""

    new_sim = f"""* **Simulasi Opsi A (Transportasi Konvensional & Mandiri)**:
  * Biaya taksi online pulang-pergi yang berfluktuasi tajam akibat kemacetan dan cuaca hujan.
  * Biaya sewa kursi roda portabel harian dan risiko pengemudi menolak membawa pasien berisiko tinggi.
  * Kelelahan fisik anggota keluarga yang harus membopong pasien masuk-keluar mobil pribadi.
  * Kehilangan produktivitas kerja seharian penuh karena harus mengantre dan mengurus administrasi RS sendirian.
  * **Hasil**: Biaya tak terduga membengkak, pasien rentan mengalami cedera sendi, dan keluarga dilanda stres berat.

* **Simulasi Opsi B (Joy of Care NEMT Transport Medis Khusus)**:
  * Paket antar jemput pulang-pergi all-in transparan tanpa lonjakan tarif tersembunyi.
  * Armada mobil medis berfasilitas ramp kursi roda hidrolik, brankar ambulans, dan suspensi lembut anti-guncangan.
  * Tenaga perawat medis pendamping yang mengawal tanda vital, membantu transfer pasien, dan mengurus antrean obat di faskes.
  * Fasilitas tabung oksigen medis dan peralatan darurat siaga penuh di dalam kendaraan.
  * **Hasil**: Pasien aman dan nyaman di ranjang ambulans, urusan faskes tuntas teratur, keluarga tenang tanpa perlu izin cuti kerja. {PRIMARY_CTA}"""
    return text.replace(old_sim, new_sim)

def h_antar_jemput_panduan_lengkap(text):
    text = re.sub(
        r'answer: Tarif layanan antar-jemput medis non-darurat \(NEMT\) Joy of Care di Jakarta\s+berkisar antara Rp 450\.000[^\n]*\n\s+Rp 750\.000 hingga Rp 1\.100\.000[^\n]*',
        f'answer: Tarif layanan antar-jemput medis non-darurat Joy of Care di Jakarta ditentukan secara transparan berdasarkan paket satu arah maupun pulang-pergi, sudah mencakup armada khusus berfasilitas medis serta pendampingan perawat profesional. {PRIMARY_CTA}',
        text
    )
    text = re.sub(
        r'> \* \*\*Transparansi Tarif Jakarta 2026\*\*: Paket pulang-pergi \(PP\) mulai Rp 750\.000 mencakup biaya tunggu perawat di rumah sakit tanpa argo tersembunyi\.',
        f'> * **Transparansi Layanan Medis Jakarta**: Layanan antar-jemput medis terpadu Joy of Care menyediakan paket transparan dengan perawat pendamping poliklinik tanpa biaya argo tersembunyi. {PRIMARY_CTA}',
        text
    )
    old_table = """|---|---|---|---|
| **Paket Satu Arah (One-Way)** | Mobil NEMT + Driver + Perawat Pendamping + Kursi Roda / Brankar | Rp 450.000 – Rp 650.000 | Cocok untuk pasien pulang rawat inap RS ke rumah |
| **Paket Pulang-Pergi Standar (PP)** | Antar + Tunggu Poliklinik + Jemput Pulang + Pendampingan Perawat | Rp 750.000 – Rp 950.000 | Termasuk waktu tunggu di RS hingga 2 jam |
| **Paket Khusus Hemodialisis / Kemo** | Antar-jemput terjadwal mingguan + tabung oksigen standby + perawat | Rp 850.000 – Rp 1.100.000 | Termasuk waktu tunggu prosedur medis hingga 4 jam |
| **Paket Lintas Kota (Jabodetabek)** | Perjalanan antar kota (misal: Tangerang ke RS di Jakarta Pusat) | Rp 950.000 – Rp 1.450.000 | Menyesuaikan jarak kilometer dan tarif jalan tol |"""

    new_table = f"""|---|---|---|---|
| **Paket Satu Arah (One-Way)** | Mobil NEMT + Driver + Perawat Pendamping + Kursi Roda / Brankar | Paket All-in (Hubungi WA JoC) | Cocok untuk pasien pulang rawat inap RS ke rumah |
| **Paket Pulang-Pergi Standar (PP)** | Antar + Tunggu Poliklinik + Jemput Pulang + Pendampingan Perawat | Paket Terjadwal (Hubungi WA JoC) | Termasuk waktu tunggu di RS hingga 2 jam |
| **Paket Khusus Hemodialisis / Kemo** | Antar-jemput terjadwal mingguan + tabung oksigen standby + perawat | Paket Berkala (Hubungi WA JoC) | Termasuk waktu tunggu prosedur medis hingga 4 jam |
| **Paket Lintas Kota (Jabodetabek)** | Perjalanan antar kota (misal: Tangerang ke RS di Jakarta Pusat) | Paket Lintas Wilayah (Hubungi WA JoC) | Menyesuaikan jarak kilometer dan tarif jalan tol |

{PRIMARY_CTA}"""
    return text.replace(old_table, new_table)

def h_biaya_dokter_biaya_perbandingan(text):
    text = re.sub(
        r'answer: Tarif visit dokter umum Joy of Care berkisar antara Rp 275\.000 hingga Rp\s+450\.000[^\n]*\n\s+antara Rp 450\.000 hingga Rp 850\.000[^\n]*',
        f'answer: Tarif visit dokter umum Joy of Care dirancang transparan, terjangkau, dan langsung ditangani tim medis tanpa biaya perantara aplikasi atau markup tersembunyi. {PRIMARY_CTA}',
        text
    )
    text = re.sub(
        r'tarif visit dokter dasar umumnya berada pada rentang lebih tinggi \(Rp 450\.000 – Rp 750\.000 per kunjungan\)\.',
        'tarif visit dokter dasar umumnya berada pada rentang lebih tinggi akibat potongan komisi dan beban admin platform.',
        text
    )
    text = text.replace(
        "tarif visit dokter Joy of Care jauh lebih ramah dan transparan (mulai dari **Rp 275.000 – Rp 400.000** per visit).",
        "tarif visit dokter Joy of Care jauh lebih ramah, transparan, dan terukur tanpa biaya perantara tersembunyi."
    )
    text = text.replace(
        "| **Estimasi Tarif Visit Dokter Umum** | **Rp 275.000 – Rp 400.000** | Rp 450.000 – Rp 700.000 | Rp 500.000 – Rp 850.000 |",
        "| **Estimasi Tarif Visit Dokter Umum** | **Tarif Transparan (Hubungi WA JoC)** | Tarif Tinggi Platform + Admin | Tarif RS Swasta Tinggi |"
    )
    text = text.replace(
        "Tarif visit dokter umum Joy of Care berkisar antara Rp 275.000 hingga Rp 450.000, sementara penyedia korporat atau platform lain mematok tarif berkisar antara Rp 450.000 hingga Rp 850.000 per kunjungan di luar biaya tindakan dan obat.",
        f"Tarif visit dokter umum Joy of Care dirancang sangat transparan dan kompetitif tanpa biaya perantara aplikasi atau beban administrasi rumah sakit. Rincian biaya tindakan medis dan obat selalu dikomunikasikan secara terbuka kepada keluarga. {PRIMARY_CTA}"
    )
    return text

def h_biaya_dokter_kapan_harus(text):
    text = re.sub(
        r'answer: Keluarga berhasil menghemat lebih dari Rp 4\.500\.000[^\n]*\n\s+demam dan dehidrasi lansia[^\n]*',
        f'answer: Keluarga berhasil menghemat lebih dari 60% biaya medis dalam satu episode penanganan demam dan dehidrasi lansia dibanding rawat inap RS swasta. {ALTERNATE_CTA}',
        text
    )
    text = text.replace(
        "sering kali menghasilkan tagihan Rp 3 juta hingga Rp 7 juta dalam hitungan 48 jam.",
        "sering kali menghasilkan tagihan jutaan rupiah dalam hitungan 48 jam akibat biaya kamar, karcis observasi, dan farmasi RS."
    )
    text = text.replace(
        "> * **Penghematan Finansial Riil Rp 4,5 Juta**: Total pengeluaran hanya Rp 1,2 juta untuk dokter dan infus homecare, dibanding estimasi biaya rawat inap RS sebesar Rp 5,8 juta.",
        f"> * **Efisiensi Finansial Signifikan**: Perawatan dokter dan infus homecare di rumah memberikan penghematan biaya lebih dari 60% dibanding estimasi rawat inap RS swasta. {ALTERNATE_CTA}"
    )
    text = text.replace(
        "menghabiskan total tagihan biaya rumah sakit mencapai **Rp 8.200.000**.",
        "menghabiskan total tagihan biaya rumah sakit mencapai belasan juta rupiah."
    )
    old_table = """| **Sewa Ambulans / Transportasi Khusus PP** | Rp 450.000 (Ambulans antar-jemput) | **Rp 50.000 (Transport flat dokter)** |
| **Karcis Pendaftaran & Biaya Ruang IGD** | Rp 650.000 | **Rp 0 (Pemeriksaan di kamar sendiri)** |
| **Jasa Dokter Pemeriksa** | Rp 600.000 (Dokter IGD + Visite dr Spesialis) | **Rp 350.000 (Dokter visit 75 menit)** |
| **Biaya Kamar Rawat Inap (2 Malam)** | Rp 2.400.000 (Kamar Standar Kelas 1) | **Rp 0 (Gratis di ranjang pribadi)** |
| **Pemasangan Infus & Cairan Medis** | Rp 750.000 (Jasa pasang + kantong infus RS) | **Rp 350.000 (Paket infus hidrasi Joy of Care)** |
| **Perawat Pendamping Harian** | Rp 600.000 (Biaya administrasi keperawatan RS) | **Rp 300.000 (Perawat homecare shift)** |
| **Biaya Obat-obatan & BMHP** | Rp 950.000 (Margin farmasi rumah sakit) | **Rp 200.000 (Obat generik resmi apotek)** |
| **Total Biaya Pengeluaran** | **Rp 6.400.000** | **Rp 1.250.000** |"""

    new_table = f"""| **Sewa Ambulans / Transportasi Medis PP** | Biaya sewa ambulans swasta mahal | **Transportasi flat terjangkau & transparan** |
| **Karcis Pendaftaran & Fasilitas IGD** | Beban karcis dan biaya ruangan RS tinggi | **Bebas Biaya (Pemeriksaan langsung di ranjang rumah)** |
| **Jasa Dokter Pemeriksa** | Jasa ganda dokter jaga IGD & visite spesialis | **Jasa dokter visit terjangkau & berdedikasi 60+ menit** |
| **Biaya Kamar Rawat Inap (2 Malam)** | Tarif kamar opname RS kelas standar/VIP | **Bebas Biaya (Kenyamanan penuh di kamar sendiri)** |
| **Pemasangan Infus & Cairan Medis** | Biaya tindakan infus dan BMHP rumah sakit tinggi | **Paket infus hidrasi homecare transparan** |
| **Perawat Pendamping Harian** | Beban administrasi keperawatan bangsal RS | **Perawat homecare terakreditasi dan berfokus penuh** |
| **Biaya Obat-obatan & BMHP** | Margin harga farmasi instalasi rawat inap RS | **Resep obat apotek resmi transparan & terjangkau** |
| **Total Beban Pengeluaran** | **Total Biaya RS Sangat Tinggi** | **Penghematan Signifikan Lebih dari 60%** |

{ALTERNATE_CTA}"""
    text = text.replace(old_table, new_table)
    text = text.replace(
        "Keluarga berhasil menghemat lebih dari Rp 4.500.000 dalam satu episode penanganan demam dan dehidrasi lansia, dibandingkan jika pasien harus dibawa ke IGD rumah sakit swasta dan menjalani rawat inap selama 2 malam.",
        f"Keluarga berhasil menghemat lebih dari 60% dari total estimasi biaya rawat inap rumah sakit swasta dalam satu episode penanganan demam dan dehidrasi lansia. Selain efisiensi biaya, kenyamanan psikologis pasien dan keluarga terjaga maksimal. {ALTERNATE_CTA}"
    )
    return text

def h_biaya_dokter_panduan_lengkap(text):
    text = re.sub(
        r'answer: Tarif dasar kunjungan dokter umum Joy of Care di wilayah Jakarta pada tahun\s+2026 berkisar antara Rp 275\.000 hingga Rp 450\.000 per sesi visit[^\n]*',
        f'answer: Tarif dasar kunjungan dokter umum Joy of Care di wilayah Jakarta dirancang transparan dan terjangkau, sudah mencakup konsultasi klinis mendalam, pemeriksaan fisik lengkap (tensi, saturasi oksigen, auskultasi), dan peresepan obat resmi. {PRIMARY_CTA}',
        text
    )
    text = text.replace(
        "> * **Tarif Visit Dasar Transparan**: Biaya kunjungan dokter umum Joy of Care berkisar antara Rp 275.000 hingga Rp 450.000 per sesi, mencakup pemeriksaan fisik komprehensif tanpa biaya transportasi liar.",
        f"> * **Tarif Visit Dasar Transparan**: Biaya kunjungan dokter umum Joy of Care dirancang jelas dan transparan di awal, mencakup pemeriksaan fisik komprehensif tanpa biaya transportasi liar. {PRIMARY_CTA}"
    )
    old_procs = """* **Pemasangan atau Penggantian Selang NGT**: Rp 250.000 – Rp 400.000 (termasuk selang silikon steril dan spuit irigasi).
* **Pemasangan atau Penggantian Kateter Urine Foley**: Rp 250.000 – Rp 450.000 (termasuk urine bag steril dan pelumas anestesi).
* **Terapi Uap Nebulizer**: Rp 150.000 – Rp 250.000 per sesi (termasuk obat bronkodilator pelega napas).
* **Perawatan Luka Steril / Jahit Luka Robek**: Rp 200.000 – Rp 500.000 tergantung luas dan kedalaman luka."""

    new_procs = f"""* **Pemasangan atau Penggantian Selang NGT**: Tindakan steril oleh dokter berpengalaman (termasuk selang silikon steril dan spuit irigasi). Biaya transparan dikonfirmasi sebelum tindakan.
* **Pemasangan atau Penggantian Kateter Urine Foley**: Tindakan aseptik (termasuk urine bag steril dan pelumas anestesi). Bebas biaya tersembunyi.
* **Terapi Uap Nebulizer**: Terapi uap pernapasan per sesi (termasuk obat bronkodilator pelega napas).
* **Perawatan Luka Steril / Jahit Luka Robek**: Debridement dan penjahitan luka steril disesuaikan dengan luas dan kedalaman luka. {PRIMARY_CTA}"""
    text = text.replace(old_procs, new_procs)

    old_table = """|---|---|---|---|
| **Dokter Umum Kunjungan Rumah (Reguler)** | Anamnesis, tanda vital, peresepan obat, surat sakit | Rp 275.000 – Rp 350.000 | 45 – 60 Menit |
| **Dokter Umum Same-Day (Mendesak)** | Kunjungan darurat non-kritis (< 90 menit tiba) | Rp 350.000 – Rp 500.000 | 45 – 60 Menit |
| **Paket Kunjungan Dokter + Cek Darah Rutin** | Visit dokter + Darah Lengkap (CBC) + Gula Darah | Rp 550.000 – Rp 750.000 | 60 Menit |
| **Paket Dokter + Ganti Selang NGT / Kateter** | Visit dokter + tindakan ganti selang steril lengkap | Rp 500.000 – Rp 750.000 | 60 Menit |
| **Paket Visit Dokter + Terapi Infus Vitamin** | Pemeriksaan dokter + Infus multivitamin booster | Rp 650.000 – Rp 950.000 | 60 – 75 Menit |"""

    new_table = f"""|---|---|---|---|
| **Dokter Umum Kunjungan Rumah (Reguler)** | Anamnesis, tanda vital, peresepan obat, surat sakit | Tarif Transparan (Hubungi WA JoC) | 45 – 60 Menit |
| **Dokter Umum Same-Day (Mendesak)** | Kunjungan darurat non-kritis (< 90 menit tiba) | Layanan Prioritas (Hubungi WA JoC) | 45 – 60 Menit |
| **Paket Kunjungan Dokter + Cek Darah Rutin** | Visit dokter + Darah Lengkap (CBC) + Gula Darah | Paket Pemeriksaan (Hubungi WA JoC) | 60 Menit |
| **Paket Dokter + Ganti Selang NGT / Kateter** | Visit dokter + tindakan ganti selang steril lengkap | Tindakan Prosedural (Hubungi WA JoC) | 60 Menit |
| **Paket Visit Dokter + Terapi Infus Vitamin** | Pemeriksaan dokter + Infus multivitamin booster | Paket Sehat Terpadu (Hubungi WA JoC) | 60 – 75 Menit |"""
    text = text.replace(old_table, new_table)

    old_sim = """* **Skenario Berobat ke IGD Rumah Sakit Swasta**:
  * Biaya sewa mobil ambulans swasta / taksi khusus kursi roda PP: **Rp 350.000 – Rp 600.000**.
  * Biaya administrasi pendaftaran & karcis IGD: **Rp 150.000 – Rp 250.000**.
  * Jasa konsultasi dokter jaga IGD: **Rp 250.000 – Rp 400.000**.
  * Biaya tindakan dasar IGD & pemakaian ruangan observasi: **Rp 400.000 – Rp 800.000**.
  * Biaya parkir kendaraan keluarga & makan di kantin RS: **Rp 100.000**.
  * **Total Biaya di Rumah Sakit**: **Rp 1.250.000 – Rp 2.150.000** (ditambah 4 jam antrean melelahkan).

* **Skenario Kunjungan Dokter ke Rumah Bersama Joy of Care**:
  * Jasa visit dokter umum ke rumah: **Rp 300.000**.
  * Biaya transportasi flat: **Rp 50.000**.
  * Biaya resep obat standar: **Rp 150.000 – Rp 250.000**.
  * Waktu antrean: **0 menit** (pasien santai di tempat tidur).
  * **Total Biaya Bersama Joy of Care**: **Rp 500.000 – Rp 600.000**!"""

    new_sim = f"""* **Skenario Berobat ke IGD Rumah Sakit Swasta**:
  * Biaya sewa ambulans swasta atau transportasi khusus kursi roda pulang-pergi yang mahal.
  * Beban administrasi pendaftaran dan karcis ruang observasi IGD rumah sakit.
  * Jasa konsultasi dokter jaga IGD dan biaya pemakaian fasilitas tindakan.
  * Biaya tambahan parkir kendaraan keluarga, bensin, dan logistik di rumah sakit.
  * **Total Biaya di Rumah Sakit**: Relatif sangat tinggi disertai antrean panjang berjam-jam yang menguras energi lansia.

* **Skenario Kunjungan Dokter ke Rumah Bersama Joy of Care**:
  * Jasa visit dokter umum langsung di ranjang pasien dengan tarif terjangkau dan transparan.
  * Biaya transportasi flat zonasi yang jelas tanpa lonjakan harga tersembunyi.
  * Peresepan obat standar resmi dengan harga apotek jujur tanpa margin berlebih.
  * Waktu antrean 0 menit: pasien beristirahat nyaman di rumah didampingi keluarga tercinta.
  * **Total Biaya Bersama Joy of Care**: Jauh lebih hemat hingga 50% dibanding berobat ke IGD! {PRIMARY_CTA}"""
    text = text.replace(old_sim, new_sim)

    text = text.replace(
        "Tarif dasar kunjungan dokter umum Joy of Care di wilayah Jakarta pada tahun 2026 berkisar antara Rp 275.000 hingga Rp 450.000 per sesi visit. Tarif ini sudah mencakup konsultasi klinis mendalam, pemeriksaan fisik lengkap (tensi, saturasi oksigen, auskultasi paru/jantung), dan peresepan obat resmi.",
        f"Tarif dasar kunjungan dokter umum Joy of Care di wilayah Jakarta dirancang transparan dan terjangkau, mencakup konsultasi klinis mendalam, pemeriksaan fisik lengkap (tensi, saturasi oksigen, auskultasi), dan peresepan obat resmi. {PRIMARY_CTA}"
    )
    return text

def h_biaya_dokter_tips_cara(text):
    text = text.replace(
        "Pada kategori ini, Anda hanya perlu membayar **Tarif Visit Dasar (Rp 275.000 – Rp 350.000)** ditambah obat oral standar.",
        "Pada kategori ini, Anda hanya perlu membayar tarif visit dokter dasar yang transparan ditambah obat oral standar."
    )
    text = text.replace(
        "Pada kategori ini, tambahkan biaya tindakan alat medis steril sekitar **Rp 200.000 – Rp 400.000**.",
        "Pada kategori ini, tindakan medis menggunakan alat steril dikenakan biaya transparan yang diinformasikan sebelum tindakan."
    )
    text = text.replace(
        "Biaya transportasi dokter telah diformulasikan dalam sistem tarif flat zonasi yang transparan, umumnya berkisar antara **Rp 0 hingga Rp 75.000** tergantung jarak kecamatan di wilayah Jabodetabek.",
        "Biaya transportasi dokter telah diformulasikan dalam sistem tarif flat zonasi yang transparan dan bersahabat di seluruh wilayah Jabodetabek."
    )
    text = text.replace(
        "Joy of Care hanya mengenakan tambahan biaya konsultasi ringan (Rp 150.000 – Rp 200.000 per orang tambahan), sementara biaya transportasi dokter tetap gratis/dihitung satu kali. Hal ini menghemat pengeluaran hingga 40% dibanding memesan secara terpisah.",
        f"Joy of Care memberikan paket add-on keluarga dengan biaya konsultasi tambahan yang sangat terjangkau, sementara biaya transportasi dokter tetap dihitung satu kali. {PRIMARY_CTA}"
    )
    old_table = """| **Jasa Visit Dokter Umum** | Rp 300.000 | Rp 300.000 | Rp 300.000 |
| **Biaya Anggota Keluarga ke-2** | Rp 0 (1 pasien) | Rp 0 (1 pasien) | Rp 175.000 (Add-on istri) |
| **Biaya Tindakan Medis NGT** | Rp 0 | Rp 300.000 (selang + pasang) | Rp 0 |
| **Biaya Transportasi Zonasi** | Rp 50.000 | Rp 50.000 | Rp 50.000 |
| **Estimasi Resep Obat Standar** | Rp 150.000 | Rp 100.000 | Rp 200.000 |
| **Total Estimasi Biaya** | **Rp 500.000** | **Rp 750.000** | **Rp 725.000 (untuk 2 orang)** |"""

    new_table = f"""| **Jasa Visit Dokter Umum** | Tarif Standar Transparan | Tarif Standar Transparan | Tarif Standar Transparan |
| **Biaya Anggota Keluarga ke-2** | Bebas Biaya (1 Pasien) | Bebas Biaya (1 Pasien) | Paket Hemat Add-on Keluarga |
| **Biaya Tindakan Medis NGT** | Bebas Tindakan Medis | Tindakan Steril Alat Medis | Bebas Tindakan Medis |
| **Biaya Transportasi Zonasi** | Tarif Flat Terjangkau | Tarif Flat Terjangkau | Tarif Flat Terjangkau |
| **Estimasi Resep Obat Standar** | Resep Apotek Transparan | Resep Apotek Transparan | Resep Apotek Transparan |
| **Skema Total Biaya** | **Transparan & Terukur** | **Transparan & Terukur** | **Paket Hemat Keluarga (2 Orang)** |

{PRIMARY_CTA}"""
    return text.replace(old_table, new_table)

def h_biaya_dokter_yang_perlu_anda_ketahui(text):
    text = text.replace(
        "Tarif visit dasar dokter Joy of Care (Rp 275.000 – Rp 400.000) bersifat komprehensif, mencakup:",
        "Tarif visit dasar dokter Joy of Care bersifat transparan dan komprehensif, mencakup:"
    )
    text = text.replace(
        "Biaya tindakan medis tambahan berkisar antara Rp 200.000 hingga Rp 400.000, sudah mencakup bahan medis habis pakai (BMHP) berkualitas steril seperti selang silikon, pelumas antiseptik, spuit irigasi, dan kantong penampung urin steril.",
        f"Biaya tindakan medis tambahan bersifat transparan dan sudah mencakup bahan medis habis pakai (BMHP) berkualitas steril. {PRIMARY_CTA}"
    )
    text = text.replace(
        "| **Tindakan Ganti Selang NGT/Kateter** | Tambahan Tindakan Medis | Rp 200.000 – Rp 400.000 (Konfirmasi awal) |",
        "| **Tindakan Ganti Selang NGT/Kateter** | Tambahan Tindakan Medis | Transparan (Konfirmasi Awal via WA) |"
    )
    text = text.replace(
        "| **Terapi Uap Nebulizer di Rumah** | Tambahan Tindakan Medis | Rp 150.000 – Rp 250.000 (Konfirmasi awal) |",
        "| **Terapi Uap Nebulizer di Rumah** | Tambahan Tindakan Medis | Transparan (Konfirmasi Awal via WA) |"
    )
    return text

def h_cegah_jatuh_kapan_harus(text):
    text = re.sub(
        r'answer: Biaya tindakan bedah ortopedi \(operasi pemasangan pen atau penggantian sendi\s+panggul bipolar/THR\) berkisar antara Rp 70\.000\.000 hingga Rp 150\.000\.000[^\n]*',
        f'answer: Biaya tindakan bedah ortopedi panggul di rumah sakit menelan anggaran puluhan hingga ratusan juta rupiah di luar biaya ICU dan rehabilitasi pascabedah. {ALTERNATE_CTA}',
        text
    )
    text = text.replace(
        "rata-rata Rp 70 juta hingga Rp 150 juta.",
        "biaya sangat besar hingga puluhan bahkan ratusan juta rupiah."
    )
    text = text.replace(
        "operasi fraktur panggul yang diperkirakan bisa mencapai lebih dari Rp 90 juta.",
        "operasi fraktur panggul di rumah sakit swasta yang menelan biaya sangat tinggi."
    )
    old_table = """| **Biaya Operasi & Implan Pen Panggul** | Rp 70.000.000 – Rp 120.000.000 (RS Swasta) | **Rp 0 (Fraktur dicegah total)** |
| **Kamar Rawat Inap & ICU (7 Hari)** | Rp 25.000.000 – Rp 45.000.000 | **Rp 0 (Tetap sehat di rumah)** |
| **Biaya Modifikasi Rumah Anti-Jatuh** | Rp 0 (Tidak dilakukan) | **Rp 800.000 – Rp 1.500.000 (Sekali pasang)** |
| **Paket Fisioterapi Keseimbangan (3 Bulan)**| Rp 0 | **Rp 5.500.000 (Program 24 sesi)** |
| **Kunjungan Dokter Review Obat** | Rp 0 | **Rp 600.000 (2 kali visit dokter)** |
| **TOTAL BIAYA KELUARGA** | **Rp 95.000.000 – Rp 165.000.000** | **Rp 6.900.000 – Rp 7.600.000** |"""

    new_table = f"""| **Biaya Operasi & Implan Bedah Panggul** | Tagihan operasi fraktur RS swasta sangat tinggi | **Bebas Biaya (Fraktur dicegah total)** |
| **Kamar Rawat Inap & Ruang ICU (7 Hari)** | Beban sewa kamar rawat inap dan ICU tinggi | **Bebas Biaya (Lansia tetap sehat di rumah)** |
| **Biaya Modifikasi Rumah Anti-Jatuh** | Bebas Biaya (Tidak dilakukan, risiko fatal) | **Investasi terjangkau (Sekali pasang)** |
| **Paket Fisioterapi Keseimbangan (3 Bulan)**| Bebas Biaya (Tanpa latihan penguatan otot) | **Program rehabilitasi terukur & transparan** |
| **Kunjungan Dokter Review Polifarmasi** | Bebas Biaya | **Visit dokter evaluasi obat di rumah** |
| **TOTAL BEBAN KEUANGAN KELUARGA** | **Beban Rumah Sakit Ratusan Juta Rupiah** | **Investasi Preventif Sangat Hemat & Aman** |

{ALTERNATE_CTA}"""
    text = text.replace(old_table, new_table)
    text = text.replace(
        "Biaya tindakan bedah ortopedi (operasi pemasangan pen atau penggantian sendi panggul bipolar/THR) berkisar antara Rp 70.000.000 hingga Rp 150.000.000, belum termasuk biaya perawatan ruang ICU jika timbul komplikasi sistemik pascabedah.",
        f"Biaya tindakan bedah ortopedi panggul di rumah sakit swasta dapat menelan biaya hingga puluhan bahkan ratusan juta rupiah di luar biaya ruang ICU. Melakukan langkah preventif modifikasi rumah dan fisioterapi keseimbangan terbukti menghemat finansial keluarga secara luar biasa. {ALTERNATE_CTA}"
    )
    return text

def h_cegah_jatuh_tips_cara(text):
    old_table = """|---|---|---|---|
| **Grab Bar Kamar Mandi** | Stainless steel 304, diameter 32–38 mm, baut dinabolt | Rp 150.000 – Rp 250.000 / unit | Menurunkan jatuh kamar mandi hingga 55% |
| **Keset Karet Anti-Slip** | Bahan PVC berlubang drainase dengan suction cup bawah | Rp 80.000 – Rp 150.000 / lembar | Mencegah terpeleset di lantai ubin basah |
| **Lampu Sensor Gerak LED** | Baterai isi ulang / colokan listrik, sensor jangkauan 3m | Rp 45.000 – Rp 90.000 / unit | Menghilangkan risiko jatuh dalam gelap |
| **Peninggi Kloset (Raised Seat)**| Bahan plastik medis antibakteri dengan pengunci samping | Rp 300.000 – Rp 550.000 / unit | Mempermudah berdiri tanpa nyeri sendi |
| **Strip Tangga Anti-Slip** | Pita perekat berpasir silika kasar berpendar dalam gelap | Rp 50.000 – Rp 100.000 / roll | Mencegah kaki meluncur di anak tangga |"""

    new_table = f"""|---|---|---|---|
| **Grab Bar Kamar Mandi** | Stainless steel 304, diameter 32–38 mm, baut dinabolt | Sangat Terjangkau / Mudah Dipasang | Menurunkan jatuh kamar mandi hingga 55% |
| **Keset Karet Anti-Slip** | Bahan PVC berlubang drainase dengan suction cup bawah | Terjangkau (Tersedia Toko Medis) | Mencegah terpeleset di lantai ubin basah |
| **Lampu Sensor Gerak LED** | Baterai isi ulang / colokan listrik, sensor jangkauan 3m | Ekonomis & Praktis Mandiri | Menghilangkan risiko jatuh dalam gelap |
| **Peninggi Kloset (Raised Seat)**| Bahan plastik medis antibakteri dengan pengunci samping | Investasi Standar Medis Geriatri | Mempermudah berdiri tanpa nyeri sendi |
| **Strip Tangga Anti-Slip** | Pita perekat berpasir silika kasar berpendar dalam gelap | Ekonomis & Pemasangan Mudah | Mencegah kaki meluncur di anak tangga |

{PRIMARY_CTA}"""
    return text.replace(old_table, new_table)

def h_cek_darah_biaya_perbandingan(text):
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
    return text.replace(old_sim, new_sim)

def h_cek_darah_panduan_lengkap(text):
    text = re.sub(
        r'answer: Biaya cek darah di rumah \(home lab\) berkisar antara Rp 150\.000 hingga Rp\s+350\.000[^\n]*\n\s+atau asam urat\)[^\n]*\n\s+panel fungsi hati[^\n]*\n\s+jasa pengambilan darah[^\n]*',
        f'answer: Biaya cek darah di rumah Joy of Care ditentukan secara transparan sesuai parameter atau paket panel komprehensif yang dipilih, sudah mencakup jasa pengambilan darah steril oleh flebotomis berlisensi dan pengantaran sampel ke laboratorium rekanan resmi. {PRIMARY_CTA}',
        text
    )
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
    text = text.replace(
        "Biaya cek darah di rumah (home lab) berkisar antara Rp 150.000 hingga Rp 350.000 untuk parameter tunggal (seperti gula darah puasa, kolesterol lengkap, atau asam urat), dan Rp 650.000 hingga Rp 2.500.000 untuk paket komprehensif (seperti panel fungsi hati, fungsi ginjal, profil lipid, dan darah lengkap), sudah termasuk jasa pengambilan darah steril oleh flebotomis.",
        f"Biaya cek darah di rumah Joy of Care ditentukan secara transparan sesuai parameter atau paket komprehensif yang dibutuhkan, sudah mencakup jasa pengambilan darah steril oleh flebotomis berlisensi dan pengantaran sampel ke laboratorium rekanan resmi. {PRIMARY_CTA}"
    )
    return text

def h_dokter_tangerang_biaya_perbandingan(text):
    text = text.replace(
        "> * **Kepastian Tarif Tanpa Biaya Tersembunyi**: Tarif resmi transparan mulai Rp 450.000 all-in tanpa lonjakan harga tak terduga (*no surge pricing*) saat jam sibuk.",
        f"> * **Kepastian Layanan Tanpa Biaya Tersembunyi**: Tarif visit resmi transparan all-in tanpa lonjakan harga tak terduga (*no surge pricing*) saat jam sibuk. {PRIMARY_CTA}"
    )
    text = text.replace(
        "| **Struktur Biaya** | **Transparan All-in** (Rp 450.000 – Rp 550.000), tanpa biaya tersembunyi. | Sering ada tambahan biaya admin aplikasi, biaya transport per km, dan *surge pricing*. | Tarif bervariasi luas tanpa standar baku, sering kali belum termasuk biaya transportasi. |",
        "| **Struktur Biaya** | **Transparan All-in** tanpa biaya tersembunyi (Hubungi WA JoC). | Tambahan biaya admin aplikasi, tarif per km, dan *surge pricing*. | Tarif bervariasi luas tanpa standar baku dan belum termasuk transport. |"
    )
    old_sim = """  * Paket Dokter Umum Visit: Rp 475.000
  * Transportasi Medis: Rp 0 (Included)
  * Resep Obat Oral Standar: Tebus di apotek terdekat atau via apotek online
  * **Total Biaya**: **Rp 475.000** (Pasien istirahat tenang di rumah, waktu keluarga terhemat 100%).

* **Skenario Berobat ke IGD Rumah Sakit Swasta di BSD/Karawaci**:
  * Jasa Dokter IGD: Rp 250.000 – Rp 350.000
  * Biaya Administrasi & Kartu Pasien RS: Rp 75.000 – Rp 150.000
  * Biaya Penggunaan Ruang Tindakan IGD: Rp 200.000 – Rp 400.000
  * Biaya Taksi Online PP / Bensin & Parkir: Rp 100.000 – Rp 150.000
  * **Total Biaya**: **Rp 625.000 – Rp 1.050.000** (ditambah kelelahan fisik antre 2–3 jam di IGD dan risiko terpapar virus pasien lain)."""

    new_sim = f"""  * Paket Dokter Umum Visit transparan mencakup anamnesis mendalam dan pemeriksaan fisik 45–60 menit.
  * Transportasi Medis flat zonasi terjangkau tanpa biaya perantara aplikasi.
  * Resep obat resmi yang dapat ditebus langsung di apotek pilihan keluarga tanpa markup instalasi RS.
  * **Hasil**: Pasien beristirahat tenang di rumah sendiri, bebas antrean, dan waktu keluarga terhemat 100%. {PRIMARY_CTA}

* **Skenario Berobat ke IGD Rumah Sakit Swasta di BSD/Karawaci**:
  * Tagihan ganda jasa dokter IGD dan biaya administrasi faskes.
  * Biaya pemakaian ruang observasi dan tindakan medis rumah sakit.
  * Biaya sewa transportasi khusus atau taksi online dan parkir RS.
  * **Hasil**: Total pengeluaran membengkak tinggi ditambah kelelahan fisik antre berjam-jam di IGD."""
    return text.replace(old_sim, new_sim)

def h_dokter_tangerang_panduan_lengkap(text):
    text = re.sub(
        r'answer: Biaya jasa panggil dokter umum ke rumah Joy of Care untuk wilayah Kota\s+Tangerang dan Tangsel berkisar antara Rp 450\.000[^\n]*',
        f'answer: Biaya panggil dokter umum ke rumah Joy of Care untuk wilayah Kota Tangerang dan Tangsel dirancang transparan, terjangkau, dan disesuaikan dengan kebutuhan tindakan klinis pasien tanpa biaya tersembunyi. {PRIMARY_CTA}',
        text
    )
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
    return text.replace(old_table, new_table)

def h_fisioterapi_lansia_biaya_perbandingan(text):
    text = re.sub(
        r'answer: Biaya sesi terapi per visit adalah setara \(Rp 250\.000 – Rp 350\.000\)\.\s+Namun\s+pergi ke klinik menambah beban biaya transportasi taksi khusus/kursi roda \(Rp\s+150\.000 – Rp 300\.000 PP\)[^\n]*',
        f'answer: Biaya sesi fisioterapi per visit sangat kompetitif dan transparan. Melakukan terapi di rumah menghapus total biaya sewa taksi kursi roda dan menghemat waktu produktif keluarga hingga berjam-jam. {PRIMARY_CTA}',
        text
    )
    old_table = """| **Tarif Jasa Terapis Dasar** | Rp 250.000 – Rp 400.000 / sesi | **Rp 275.000 – Rp 350.000 / sesi (Setara)** |
| **Biaya Tambahan Transportasi** | Rp 150.000 – Rp 300.000 (Taksi/Ambulans PP) | **Rp 0 – Rp 50.000 (Biaya transport terapis flat)** |"""

    new_table = """| **Tarif Jasa Fisioterapis Dasar** | Tarif standar klinik atau rumah sakit | **Kompetitif & Transparan (Hubungi WA JoC)** |
| **Biaya Tambahan Transportasi** | Biaya tinggi sewa taksi khusus kursi roda PP | **Bebas Biaya Transportasi (Terapis datang ke rumah)** |"""
    text = text.replace(old_table, new_table)
    text = text.replace(
        "Biaya sesi terapi per visit adalah setara (Rp 250.000 – Rp 350.000). Namun pergi ke klinik menambah beban biaya transportasi taksi khusus/kursi roda (Rp 150.000 – Rp 300.000 PP) serta waktu kerja keluarga yang hilang hingga 3 jam per kedatangan.",
        f"Biaya sesi terapi per visit Joy of Care sangat terjangkau dan transparan. Keunggulan terbesar homecare adalah menghapus seluruh biaya sewa transportasi khusus, bebas macet, dan tidak menyita jam kerja anggota keluarga. {PRIMARY_CTA}"
    )
    return text

def h_fisioterapi_lansia_panduan_lengkap(text):
    text = re.sub(
        r'answer: Biaya fisioterapi lansia kunjungan ke rumah di Jakarta berkisar antara Rp\s+250\.000 hingga Rp 400\.000 per sesi[^\n]*',
        f'answer: Biaya fisioterapi lansia kunjungan ke rumah di Jakarta dirancang terjangkau dan transparan per sesi berdurasi 45–60 menit. Tersedia pula paket rehabilitasi berkala bulanan yang lebih hemat untuk pemulihan jangka panjang. {PRIMARY_CTA}',
        text
    )
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
    text = text.replace(
        "Biaya fisioterapi lansia kunjungan ke rumah di Jakarta berkisar antara Rp 250.000 hingga Rp 400.000 per sesi latihan berdurasi 45–60 menit. Tersedia pula paket terapi berkala (8 hingga 12 sesi per bulan) dengan potongan harga khusus untuk program rehabilitasi jangka panjang.",
        f"Biaya fisioterapi lansia kunjungan ke rumah di Jakarta dirancang terjangkau dan transparan per sesi berdurasi 45–60 menit. Tersedia pula paket program pemulihan intensif bulanan yang sangat terukur untuk memastikan lansia kembali mandiri. {PRIMARY_CTA}"
    )
    return text

def h_fisioterapi_stroke_biaya_perbandingan(text):
    text = re.sub(
        r'answer: Biaya satu sesi kunjungan fisioterapi pasca stroke ke rumah di Jakarta umumnya\s+berkisar antara Rp 250\.000[^\n]*',
        f'answer: Biaya fisioterapi pasca stroke ke rumah di Jakarta dirancang terjangkau dan transparan per sesi, disesuaikan dengan fase rehabilitasi dan modalitas stimulasi neuromuskular yang diperlukan pasien. {ALTERNATE_CTA}',
        text
    )
    old_table = """| **Biaya Jasa Terapi** | Rp 200.000 – Rp 400.000 / sesi | **Rp 275.000 – Rp 400.000 / sesi** |
| **Biaya Transport Khusus PP** | Rp 300.000 – Rp 700.000 / hari | **Rp 0 (Bebas Biaya Kendaraan Sewa)** |
| **Estimasi Total Pengeluaran** | **Rp 500.000 – Rp 1.100.000 / visit** | **Rp 275.000 – Rp 400.000 / visit** |"""

    new_table = f"""| **Biaya Jasa Terapi Sesi** | Tarif standar fisioterapi klinik | **Transparan & Terjangkau (Hubungi WA JoC)** |
| **Biaya Transport Khusus PP** | Sewa ambulans / taksi kursi roda PP mahal | **Bebas Biaya Sewa (Terapis datang ke rumah)** |
| **Efisiensi Total Biaya** | **Beban Pengeluaran Tinggi per Sesi** | **Hemat Signifikan Tanpa Biaya Tersembunyi** |

{ALTERNATE_CTA}"""
    text = text.replace(old_table, new_table)
    text = text.replace(
        "Biaya satu sesi kunjungan fisioterapi pasca stroke ke rumah di Jakarta umumnya berkisar antara Rp 250.000 hingga Rp 450.000 per sesi, tergantung paket kunjungan dan modalitas stimulasi yang digunakan.",
        f"Biaya satu sesi kunjungan fisioterapi pasca stroke ke rumah di Jakarta dirancang kompetitif dan transparan, disesuaikan dengan kebutuhan modalitas pemulihan gerak fungsional dan paket pendampingan yang dipilih. {ALTERNATE_CTA}"
    )
    return text

def h_infus_vitamin_biaya_perbandingan(text):
    text = re.sub(
        r'answer: Tidak selalu\. Tarif paket infus vitamin Joy of Care \(Rp 635\.000 – Rp 850\.000\)[^\n]*',
        f'answer: Tidak selalu. Tarif paket infus vitamin Joy of Care bersifat transparan dan all-in sudah mencakup multivitamin berstandar BPOM, jasa perawat ber-STR, dan transport flat tanpa biaya registrasi tambahan. {PRIMARY_CTA}',
        text
    )
    old_table = """| **Estimasi Biaya Paket Multivitamin** | Rp 750.000 – Rp 1.500.000 / sesi | **Rp 636.500 – Rp 850.000 / sesi (Transparan)** |
| **Biaya Tambahan Tersembunyi** | Biaya konsultasi dokter, parkir, admin | **Rp 0 (Semua komponen sudah all-in)** |"""

    new_table = """| **Paket Multivitamin Berkualitas** | Tarif klinik dengan margin komersial tinggi | **Transparan & Terjangkau (Hubungi WA JoC)** |
| **Biaya Tambahan Tersembunyi** | Beban karcis registrasi, parkir mall, admin | **Bebas Biaya Tambahan (Semua tindakan all-in)** |"""
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
    text = text.replace(
        "Tidak selalu. Tarif paket infus vitamin Joy of Care (Rp 635.000 – Rp 850.000) bersifat transparan dan all-in sudah termasuk jasa perawat dan transport flat, setara atau bahkan lebih hemat dibanding klinik kecantikan yang sering membebankan biaya konsultasi dokter klinik dan biaya registrasi tambahan.",
        f"Tidak selalu. Tarif paket infus vitamin Joy of Care bersifat transparan dan all-in sudah termasuk jasa perawat profesional dan transport flat, jauh lebih hemat dibanding klinik komersial yang membebankan biaya konsultasi dan registrasi terpisah. {PRIMARY_CTA}"
    )
    return text

def h_infus_vitamin_panduan_lengkap(text):
    text = re.sub(
        r'answer: Harga terapi infus vitamin di rumah Joy of Care berkisar antara Rp 475\.000[^\n]*\n\s+untuk suntik vitamin C murni[^\n]*\n\s+untuk paket infus drip[^\n]*\n\s+hingga Rp 1\.800\.000[^\n]*',
        f'answer: Tarif terapi infus vitamin di rumah Joy of Care ditentukan transparan berdasarkan formulasi multivitamin yang dibutuhkan (Vitamin C murni, Neurotropik B Kompleks, hingga Immune Booster Cocktail), sudah all-in dengan jasa perawat profesional. {PRIMARY_CTA}',
        text
    )
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
    text = text.replace(
        "Harga terapi infus vitamin di rumah Joy of Care berkisar antara Rp 475.000 untuk suntik vitamin C murni (injeksi IV langsung), Rp 635.000 hingga Rp 850.000 untuk paket infus drip multivitamin B Kompleks + Vitamin C 1.000 mg, dan Rp 1.200.000 hingga Rp 1.800.000 untuk paket premium Immune Booster / Anti-Fatigue Cocktail.",
        f"Harga terapi infus vitamin di rumah Joy of Care disesuaikan dengan formulasi nutrisi yang dipilih, mulai dari injeksi vitamin C murni, multivitamin neurotropik B-kompleks, hingga formula immune booster lengkap dengan jaminan all-in bebas biaya tersembunyi. {PRIMARY_CTA}"
    )
    return text

def h_perawat_terpercaya_biaya_perbandingan(text):
    return text.replace(
        "Banyak agensi konvensional mengenakan biaya administrasi penempatan awal yang sangat mahal (berkisar Rp 1.500.000 hingga Rp 3.000.000). Jika dalam waktu 1 bulan perawat berhenti bekerja, uang administrasi tersebut sering kali hangus atau keluarga dikenakan biaya denda baru untuk mendatangkan pengganti.",
        f"Banyak agensi konvensional mengenakan biaya administrasi penempatan awal yang sangat mahal tanpa jaminan pasti. Jika perawat berhenti bekerja, uang administrasi sering kali hangus. Sebaliknya, Joy of Care menerapkan sistem transparan dengan jaminan penggantian perawat tanpa biaya tersembunyi. {PRIMARY_CTA}"
    )

def h_perawat_terpercaya_panduan_lengkap(text):
    text = re.sub(
        r'answer: Biaya jasa perawat homecare medis berijazah D3/S1 Keperawatan berkisar antara\s+Rp 5\.000\.000 hingga Rp 9\.500\.000 per bulan[^\n]*\n\s+250\.000 hingga Rp 400\.000[^\n]*',
        f'answer: Biaya jasa perawat homecare medis berijazah resmi ditentukan secara transparan berdasarkan sistem penugasan (live-in 24 jam, shift harian, atau per visit tindakan medis) serta kompleksitas alat kesehatan pasien. {PRIMARY_CTA}',
        text
    )
    old_list = """* **Perawat Medis Live-In 24 Jam (Menginap Bulanan)**: Rp 5.500.000 – Rp 9.500.000 per bulan. Khusus untuk pasien pascastroke, tirah baring (*bedridden*), terpasang selang makan NGT, kateter urin, atau trakeostomi.
* **Caregiver Lansia Live-In 24 Jam (Menginap Bulanan)**: Rp 2.800.000 – Rp 4.500.000 per bulan. Untuk pendampingan lansia mandiri sebagian (*partial dependent*), bantuan aktivitas mandi, makan, dan jalan santai.
* **Perawat Medis Shift Harian (12 Jam)**: Rp 250.000 – Rp 400.000 per shift. Cocok untuk keluarga yang membutuhkan pengawasan medis saat jam kerja kantor siang hari.
* **Kunjungan Tindakan Medis Khusus (Per Visit)**: Rp 200.000 – Rp 350.000 per kunjungan. Untuk penggantian selang NGT steril, pemasangan kateter urine baru, atau perawatan luka diabetes gangren."""

    new_list = f"""* **Perawat Medis Live-In 24 Jam (Menginap Bulanan)**: Layanan komprehensif bagi pasien pascastroke, tirah baring, terpasang selang makan NGT, kateter urin, atau trakeostomi dengan sistem kontrak transparan.
* **Caregiver Lansia Live-In 24 Jam (Menginap Bulanan)**: Pendampingan lansia mandiri sebagian, pemenuhan kebutuhan aktivitas harian (ADL), pendampingan mobilisasi, dan stimulasi kognitif.
* **Perawat Medis Shift Harian (12 Jam)**: Pendampingan medis profesional saat jam kerja keluarga siang hari atau pemantauan malam hari.
* **Kunjungan Tindakan Medis Khusus (Per Visit)**: Kunjungan steril untuk penggantian selang NGT, pemasangan kateter urine Foley, atau perawatan luka diabetes modern dressing. {PRIMARY_CTA}"""
    text = text.replace(old_list, new_list)
    text = text.replace(
        "Biaya jasa perawat homecare medis berijazah D3/S1 Keperawatan berkisar antara Rp 5.000.000 hingga Rp 9.500.000 per bulan untuk sistem live-in 24 jam, atau Rp 250.000 hingga Rp 400.000 per shift harian 12 jam, tergantung kompleksitas alat medis pasien.",
        f"Biaya jasa perawat homecare medis berijazah resmi dirancang transparan berdasarkan sistem kerja yang dibutuhkan (live-in, shift harian, atau per visit tindakan khusus) serta kualifikasi klinis tenaga kesehatan. {PRIMARY_CTA}"
    )
    return text

def h_kesehatan_lansia_rutinitas_biaya_perbandingan(text):
    text = re.sub(
        r'answer: Lansia pasif yang mengalami komplikasi penyakit degeneratif rata-rata\s+membutuhkan biaya 4 hingga 7 kali lipat lebih tinggi \(berkisar antara Rp 80\.000\.000\s+hingga Rp 180\.000\.000 per tahun\)[^\n]*\n\s+kemih berulang[^\n]*\n\s+lansia aktif yang hanya memerlukan biaya perawatan preventif sekitar Rp 15\.000\.000\s+hingga Rp 25\.000\.000 per tahun\.',
        f'answer: Lansia pasif yang mengalami komplikasi penyakit rata-rata membutuhkan biaya medis 4 hingga 7 kali lipat lebih tinggi untuk rawat inap ICU dan penanganan dekubitus, dibanding lansia aktif yang mengutamakan rutinitas fisik preventif. {PRIMARY_CTA}',
        text
    )
    # replace the simulation
    text = re.sub(
        r'1\. \*\*Rawat Inap RS Akibat Pneumonia Aspirasi / Sepsis Dekubitus\*\*:.*?\n2\. \*\*Perawatan Luka Dekubitus Khusus oleh Tenaga Medis\*\*:.*?\n3\. \*\*Kebutuhan Logistik Pasien Bedridden\*\*:.*?\n4\. \*\*Total Estimasi Biaya Per Tahun\*\*:.*?\n',
        """1. **Rawat Inap RS Akibat Pneumonia Aspirasi / Sepsis Dekubitus**: Komplikasi infeksi berat membutuhkan perawatan ICU/HCU dengan beban biaya fantastis.
2. **Perawatan Luka Dekubitus Khusus oleh Tenaga Medis**: Penggantian balutan kassa modern dressing rutin yang membutuhkan alokasi biaya berkelanjutan.
3. **Kebutuhan Logistik Pasien Bedridden**: Pengeluaran rutin popok dewasa, kateter urin, selang NGT, dan alat suction lendir.
4. **Total Beban Medis Per Tahun**: Membengkak sangat besar hingga ratusan juta rupiah serta memicu kelelahan fisik dan emosional keluarga.
""",
        text, flags=re.DOTALL
    )
    text = re.sub(
        r'1\. \*\*Pemeriksaan Dokter dan Skrining Laboratorium Berkala\*\*:.*?\n2\. \*\*Paket Sesi Latihan Bersama Fisioterapis Homecare\*\*:.*?\n3\. \*\*Suplemen Nutrisi & Vitamin Esensial\*\*:.*?\n4\. \*\*Total Estimasi Biaya Per Tahun\*\*:.*?\n',
        f"""1. **Pemeriksaan Dokter dan Skrining Laboratorium Berkala**: Kunjungan teratur [Layanan Panggil Dokter ke Rumah Jakarta](/layanan/panggil-dokter) dan [Layanan Cek Lab Darah di Rumah](/layanan/cek-lab-di-rumah) secara berkala.
2. **Paket Sesi Latihan Bersama Fisioterapis Homecare**: Mempertahankan mobilitas fungsional dan kekuatan otot lansia.
3. **Suplemen Nutrisi & Vitamin Esensial**: Asupan kalsium, vitamin D3, dan gizi seimbang.
4. **Total Investasi Kesehatan**: Sangat hemat, terukur, dan mencegah pengeluaran darurat rumah sakit. {PRIMARY_CTA}
""",
        text, flags=re.DOTALL
    )
    text = re.sub(
        r'Investasi preventif pada pola hidup aktif menghasilkan penghematan biaya medis riil lebih dari Rp 100\.000\.000 per tahun,',
        'Investasi preventif pada pola hidup aktif menghasilkan penghematan biaya medis riil sangat besar hingga ratusan juta rupiah per tahun,',
        text
    )
    return text

def h_latihan_fisioterapi_biaya_perbandingan(text):
    text = re.sub(
        r'answer: Latihan mandiri berbiaya Rp 0, namun memiliki risiko biaya pengobatan ratusan\s+juta jika terjadi insiden jatuh patah tulang\.\s+Paket fisioterapis homecare \(sekitar\s+Rp 2\.000\.000 – Rp 2\.400\.000 per bulan untuk 8 sesi\)[^\n]*',
        f'answer: Latihan fisik tanpa pengawasan terapis berisiko memicu cedera jatuh fatal yang menelan biaya medis hingga ratusan juta rupiah. Paket fisioterapi homecare merupakan investasi preventif yang terukur dan aman. {PRIMARY_CTA}',
        text
    )
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
    text = text.replace(
        "Latihan mandiri berbiaya Rp 0, namun memiliki risiko biaya pengobatan ratusan juta jika terjadi insiden jatuh patah tulang. Paket fisioterapis homecare (sekitar Rp 2.000.000 – Rp 2.400.000 per bulan untuk 8 sesi) merupakan investasi preventif yang sangat hemat dan terukur.",
        f"Latihan mandiri tanpa pengawasan ahli rentan memicu cedera jatuh yang membutuhkan biaya penanganan rumah sakit sangat besar. Paket fisioterapis homecare terbukti menjadi langkah preventif yang aman, terencana, dan melindungi masa depan keluarga. {PRIMARY_CTA}"
    )
    return text

def h_merawat_orang_tua_biaya_perbandingan(text):
    text = re.sub(
        r'answer: Biaya jasa perawat lansia di Jabodetabek berkisar antara Rp 2\.500\.000 hingga\s+Rp 4\.500\.000 per bulan untuk perawat non-medis[^\n]*\n\s+dan Rp 5\.000\.000 hingga Rp 9\.000\.000 per bulan[^\n]*',
        f'answer: Biaya jasa perawat lansia di Jabodetabek ditentukan secara transparan berdasarkan kualifikasi (caregiver pendamping harian atau perawat medis bersertifikasi STR aktif) serta sistem kerja bulanan atau shift. {PRIMARY_CTA}',
        text
    )
    text = text.replace(
        "| **Biaya Jasa Bulanan** | Rp 0 (Gratis) | Rp 3.500.000 – Rp 7.500.000 / bulan |",
        "| **Biaya Jasa Bulanan** | Bebas Biaya (Tenaga Sendiri) | **Transparan & Terukur (Hubungi WA JoC)** |"
    )
    text = text.replace(
        "Biaya jasa perawat lansia di Jabodetabek berkisar antara Rp 2.500.000 hingga Rp 4.500.000 per bulan untuk perawat non-medis (caregiver pendamping harian), dan Rp 5.000.000 hingga Rp 9.000.000 per bulan untuk perawat medis bersertifikasi D3/S1 Keperawatan dengan STR aktif.",
        f"Biaya jasa perawat lansia di Jabodetabek dirancang fleksibel dan transparan sesuai kebutuhan pendampingan lansia, baik untuk bantuan aktivitas dasar harian maupun perawatan medis klinis pascarawat RS. {PRIMARY_CTA}"
    )
    return text

def h_osteoporosis_biaya_perbandingan(text):
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
    return text.replace(old_sec, new_sec)

def h_panggil_dokter_jakarta_biaya_perbandingan(text):
    text = re.sub(
        r'answer: Biaya jasa visit dokter umum ke rumah di Jakarta umumnya berkisar antara\s+Rp 350\.000 hingga Rp 750\.000 per kunjungan[^\n]*',
        f'answer: Biaya jasa visit dokter umum ke rumah di Jakarta dirancang transparan dan terjangkau, disesuaikan dengan kebutuhan klinis pasien dan tindakan medis tanpa biaya perantara tersembunyi. {PRIMARY_CTA}',
        text
    )
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
| **Biaya Administrasi Fasilitas** | Karcis pendaftaran & kartu pasien RS | **Bebas Biaya (Bebas Biaya Administrasi Tambahan)** |
| **Transportasi Khusus Pasien** | Sewa ambulans / taksi khusus PP mahal | **Bebas Biaya (Dokter hadir langsung di ranjang rumah)** |
| **Obat-obatan & BMHP Standar** | Instalasi farmasi rumah sakit | Resep resmi harga apotek transparan |
| **Total Efisiensi Pengeluaran** | **Beban Pengeluaran Tinggi per Visit** | **Penghematan Signifikan Hingga 50%** |

{PRIMARY_CTA}"""
    text = text.replace(old_table, new_table)
    text = text.replace(
        "Selain ongkos sewa kendaraan khusus atau ambulans penjemputan berkisar Rp 400.000–800.000 per perjalanan, ada biaya kehilangan jam kerja produktif anak yang mendampingi mengantre berjam-jam.",
        "Selain ongkos sewa kendaraan khusus atau ambulans penjemputan yang mahal per perjalanan, ada biaya kehilangan jam kerja produktif anak yang mendampingi mengantre berjam-jam."
    )
    text = text.replace(
        "Biaya jasa visit dokter umum ke rumah di Jakarta umumnya berkisar antara Rp 350.000 hingga Rp 750.000 per kunjungan, tergantung jarak tempuh, waktu kunjungan (jam kerja vs malam hari), dan jenis tindakan medis yang dilakukan.",
        f"Biaya jasa visit dokter umum ke rumah di Jakarta ditentukan secara transparan tanpa markup perantara. Rincian biaya tindakan medis selalu dijelaskan secara terbuka sebelum tindakan dilakukan. {PRIMARY_CTA}"
    )
    return text

def h_perawat_lansia_biaya_perbandingan(text):
    text = re.sub(
        r'answer: Perawat harian shift \(8–12 jam\) dikenakan tarif berkisar Rp 180\.000 hingga\s+Rp 350\.000 per hari[^\n]*\n\s+bulanan berkisar Rp 3\.500\.000 hingga Rp 8\.500\.000 per bulan[^\n]*',
        f'answer: Tarif perawat lansia di Jabodetabek disesuaikan transparan berdasarkan sistem penugasan (shift harian atau menginap 24 jam bulanan) serta kualifikasi tenaga pendamping medis atau non-medis. {PRIMARY_CTA}',
        text
    )
    text = text.replace(
        "| **Estimasi Biaya Bulanan** | Rp 4.500.000 – Rp 8.000.000 (jika full 30 hari) | Rp 3.500.000 – Rp 9.500.000 / bulan paket |",
        "| **Estimasi Biaya Bulanan** | Tarif harian terakumulasi | **Paket Bulanan Hemat & Terstruktur (Hubungi WA JoC)** |"
    )
    text = text.replace(
        "Perawat harian shift (8–12 jam) dikenakan tarif berkisar Rp 180.000 hingga Rp 350.000 per hari, sedangkan perawat menginap 24 jam dikenakan sistem paket bulanan berkisar Rp 3.500.000 hingga Rp 8.500.000 per bulan tergantung kualifikasi caregiver atau perawat medis.",
        f"Perawat lansia homecare Joy of Care dapat dipesan dalam skema shift harian maupun paket menginap bulanan secara transparan. Rincian biaya selalu disesuaikan dengan kondisi ketergantungan fisik dan alat medis lansia. {PRIMARY_CTA}"
    )
    return text

def h_perawat_lansia_panduan_lengkap(text):
    text = re.sub(
        r'answer: Biaya jasa perawat lansia di Jabodetabek berkisar antara Rp 2\.500\.000 hingga\s+Rp 4\.500\.000 per bulan[^\n]*\n\s+\(STR\) aktif\.',
        f'answer: Biaya jasa perawat lansia di Jabodetabek ditentukan secara transparan berdasarkan kompetensi tenaga kesehatan (caregiver pendamping harian atau perawat medis berijazah resmi D3/S1 Keperawatan ber-STR aktif). {PRIMARY_CTA}',
        text
    )
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
    text = text.replace(
        "Biaya jasa perawat lansia di Jabodetabek berkisar antara Rp 2.500.000 hingga Rp 4.500.000 per bulan untuk caregiver non-medis, dan Rp 5.000.000 hingga Rp 9.500.000 per bulan untuk perawat medis berijazah D3/S1 Keperawatan dengan Surat Tanda Registrasi (STR) aktif.",
        f"Biaya jasa perawat lansia di Jabodetabek dirancang jelas dan transparan sesuai jenjang kompetensi tenaga perawat (caregiver non-medis untuk aktivitas harian atau perawat medis berijazah D3/S1 dengan STR aktif). {PRIMARY_CTA}"
    )
    return text

def h_parkinson_biaya_perbandingan(text):
    text = re.sub(
        r'answer: Jauh lebih ekonomis\. Biaya rawat inap rumah sakit berkisar Rp 1\.500\.000\s+hingga Rp 4\.000\.000 per hari[^\n]*\n\s+homecare terpadu[^\n]*',
        f'answer: Jauh lebih ekonomis dan terukur. Merawat pasien Parkinson di rumah menghindarkan keluarga dari tagihan rawat inap rumah sakit harian yang sangat mahal, sekaligus memberikan kenyamanan emosional bagi pasien. {PRIMARY_CTA}',
        text
    )
    text = text.replace(
        "| **Estimasi Biaya Rutin** | Rp 1.500.000 – Rp 4.000.000 / hari rawat | **Rp 3.500.000 – Rp 8.500.000 / bulan paket terpadu** |",
        "| **Estimasi Biaya Rutin** | Tarif rawat inap harian RS sangat mahal | **Paket Bulanan Terukur & Hemat (Hubungi WA JoC)** |"
    )
    text = text.replace(
        "Jauh lebih ekonomis. Biaya rawat inap rumah sakit berkisar Rp 1.500.000 hingga Rp 4.000.000 per hari, belum termasuk biaya obat dan dokter. Dengan layanan homecare terpadu, anggaran bulanan menjadi terukur dan stabil tanpa risiko biaya tak terduga.",
        f"Jauh lebih ekonomis dan terkontrol. Menghadirkan pendampingan homecare medis di rumah membebaskan keluarga dari risiko lonjakan biaya rawat inap rumah sakit yang tidak terduga, seraya memastikan kepatuhan obat Levodopa dan terapi fisik berjalan disiplin. {PRIMARY_CTA}"
    )
    return text

def h_syarat_studi_biaya_perbandingan(text):
    text = re.sub(
        r'answer: Biaya MCU visa Australia di panel resmi berkisar antara Rp 1\.800\.000 hingga\s+Rp 2\.500\.000; tes TBC visa UK di IOM berkisar antara Rp 850\.000 hingga Rp 1\.100\.000;\s+MCU studi Jepang/Korea berkisar antara Rp 1\.200\.000 hingga Rp 1\.900\.000; sedangkan\s+pemenuhan paket imunisasi universitas di Amerika Serikat berkisar antara Rp 1\.500\.000\s+hingga Rp 3\.500\.000\.',
        f'answer: Biaya pemeriksaan MCU dan vaksinasi studi ke luar negeri bervariasi sesuai regulasi visa negara tujuan (Australia, UK, Jepang, Korea, atau USA) serta daftar imunisasi wajib yang disyaratkan universitas. {PRIMARY_CTA}',
        text
    )
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
    return text.replace(old_table, new_table)

def h_syarat_studi_panduan_lengkap(text):
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
    return text.replace(old_table, new_table)

def h_tips_mahasiswa_biaya_perbandingan(text):
    old_row = "| **Estimasi Biaya Tahunan** | AUD $600 – $800 per tahun (~Rp 6–8 juta) | GBP £776 per tahun (~Rp 15–16 juta) | USD $2.000 – $4.000 per tahun (~Rp 32–64 juta) |"
    new_row = f"| **Estimasi Biaya Tahunan** | Sesuai tarif resmi premi OSHC Australia | Sesuai tarif wajib retribusi IHS visa UK | Premi tahunan student health plan universitas |"
    text = text.replace(old_row, new_row)
    text = text.replace("Pembayaran *copayment* (USD $20–50)", "Pembayaran *copayment* nominal terjangkau")
    return text

def h_tips_mahasiswa_panduan_lengkap(text):
    return text.replace(
        "Biaya penambalan atau pencabutan gigi bungsu di luar negeri dapat mencapai Rp 5.000.000 hingga Rp 15.000.000 per gigi.",
        "Biaya penambalan atau pencabutan gigi bungsu di luar negeri dapat sangat mahal mencapai jutaan hingga belasan juta rupiah per gigi."
    )

def h_tips_mahasiswa_tips_cara(text):
    old_text = "Biaya bervariasi tergantung jumlah item vaksin dan tes lab yang disyaratkan oleh universitas tujuan Anda, berkisar antara Rp 850.000 untuk paket dasar hingga Rp 2.500.000 untuk paket komprehensif lengkap dengan vaksin meningitis dan titer serologi."
    new_text = f"Biaya bervariasi tergantung jumlah item vaksin dan tes lab yang disyaratkan oleh universitas tujuan Anda. Menyelesaikan seluruh rangkaian imunisasi dan MCU di tanah air sebelum berangkat terbukti menghemat biaya kesehatan hingga lebih dari 50%. {PRIMARY_CTA}"
    return text.replace(old_text, new_text)

def h_vaksin_lansia_biaya_perbandingan(text):
    text = re.sub(
        r'answer: Selisih biayanya relatif sangat kecil \(berkisar antara Rp 100\.000 hingga\s+Rp 200\.000 untuk biaya kunjungan tenaga medis\)[^\n]*\n\s+biaya\s+transportasi taksi/ambulans[^\n]*\n\s+vaksinasi di rumah[^\n]*',
        f'answer: Selisih biaya langsung sangat kecil, namun bila memperhitungkan biaya transportasi khusus, parkir RS, dan hilangnya waktu kerja keluarga, vaksinasi di rumah sesungguhnya jauh lebih hemat, praktis, dan aman bagi lansia. {PRIMARY_CTA}',
        text
    )
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
    return text.replace(old_sec, new_sec)

def h_vaksin_lansia_panduan_lengkap(text):
    text = re.sub(
        r'answer: Tarif layanan vaksinasi lansia di rumah Joy of Care berkisar antara Rp 520\.000\s+hingga Rp 680\.000 untuk vaksin influenza kuadrivalen, Rp 1\.150\.000 hingga Rp 1\.650\.000\s+untuk vaksin pneumonia terkonjugasi \(PCV13/15\), dan Rp 2\.400\.000 hingga Rp 2\.800\.000\s+untuk vaksin herpes zoster rekombinan \(Shingrix\) per dosis, sudah mencakup jasa\s+tenaga medis dan transport\.',
        f'answer: Tarif layanan vaksinasi lansia di rumah Joy of Care ditentukan secara transparan sesuai jenis vaksin resmi (Influenza Kuadrivalen, Pneumonia PCV13/15, PPSV23, atau Herpes Zoster Shingrix), sudah mencakup jasa tenaga medis dan pemeliharaan cold chain steril. {PRIMARY_CTA}',
        text
    )
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
    return text.replace(old_table, new_table)

HANDLERS = {
    'persyaratan-kesehatan-untuk-perjalanan-internasional-dan-pendidikan-9.txt': (h_persyaratan_kesehatan_perjalanan_9, 'articles-overhauled'),
    'persyaratan-medis-untuk-melanjutkan-studi-di-australia-14.txt': (h_persyaratan_medis_australia_14, 'articles-overhauled'),
    'akupuntur-untuk-nyeri-sendi-lansia-biaya-dan-perbandingan.txt': (h_akupuntur_biaya_perbandingan, 'articles-new'),
    'akupuntur-untuk-nyeri-sendi-lansia-panduan-lengkap.txt': (h_akupuntur_panduan_lengkap, 'articles-new'),
    'antar-jemput-rumah-sakit-jakarta-harga-biaya-dan-perbandingan.txt': (h_antar_jemput_biaya_perbandingan, 'articles-new'),
    'antar-jemput-rumah-sakit-jakarta-harga-panduan-lengkap.txt': (h_antar_jemput_panduan_lengkap, 'articles-new'),
    'biaya-panggil-dokter-ke-rumah-2026-biaya-dan-perbandingan.txt': (h_biaya_dokter_biaya_perbandingan, 'articles-new'),
    'biaya-panggil-dokter-ke-rumah-2026-kapan-harus.txt': (h_biaya_dokter_kapan_harus, 'articles-new'),
    'biaya-panggil-dokter-ke-rumah-2026-panduan-lengkap.txt': (h_biaya_dokter_panduan_lengkap, 'articles-new'),
    'biaya-panggil-dokter-ke-rumah-2026-tips-dan-cara.txt': (h_biaya_dokter_tips_cara, 'articles-new'),
    'biaya-panggil-dokter-ke-rumah-2026-yang-perlu-anda-ketahui.txt': (h_biaya_dokter_yang_perlu_anda_ketahui, 'articles-new'),
    'cegah-jatuh-pada-lansia-tips-rumah-kapan-harus.txt': (h_cegah_jatuh_kapan_harus, 'articles-new'),
    'cegah-jatuh-pada-lansia-tips-rumah-tips-dan-cara.txt': (h_cegah_jatuh_tips_cara, 'articles-new'),
    'cek-darah-di-rumah-jakarta-biaya-biaya-dan-perbandingan.txt': (h_cek_darah_biaya_perbandingan, 'articles-new'),
    'cek-darah-di-rumah-jakarta-biaya-panduan-lengkap.txt': (h_cek_darah_panduan_lengkap, 'articles-new'),
    'dokter-umum-ke-rumah-tangerang-biaya-dan-perbandingan.txt': (h_dokter_tangerang_biaya_perbandingan, 'articles-new'),
    'dokter-umum-ke-rumah-tangerang-panduan-lengkap.txt': (h_dokter_tangerang_panduan_lengkap, 'articles-new'),
    'fisioterapi-lansia-di-rumah-jakarta-biaya-dan-perbandingan.txt': (h_fisioterapi_lansia_biaya_perbandingan, 'articles-new'),
    'fisioterapi-lansia-di-rumah-jakarta-panduan-lengkap.txt': (h_fisioterapi_lansia_panduan_lengkap, 'articles-new'),
    'fisioterapi-pasca-stroke-di-rumah-biaya-dan-perbandingan.txt': (h_fisioterapi_stroke_biaya_perbandingan, 'articles-new'),
    'infus-vitamin-di-rumah-jakarta-harga-biaya-dan-perbandingan.txt': (h_infus_vitamin_biaya_perbandingan, 'articles-new'),
    'infus-vitamin-di-rumah-jakarta-harga-panduan-lengkap.txt': (h_infus_vitamin_panduan_lengkap, 'articles-new'),
    'jasa-perawat-homecare-terpercaya-biaya-dan-perbandingan.txt': (h_perawat_terpercaya_biaya_perbandingan, 'articles-new'),
    'jasa-perawat-homecare-terpercaya-panduan-lengkap.txt': (h_perawat_terpercaya_panduan_lengkap, 'articles-new'),
    'kesehatan-lansia-sehat-rutinitas-harian-biaya-dan-perbandingan.txt': (h_kesehatan_lansia_rutinitas_biaya_perbandingan, 'articles-new'),
    'latihan-fisioterapi-untuk-lansia-di-rumah-biaya-dan-perbandingan.txt': (h_latihan_fisioterapi_biaya_perbandingan, 'articles-new'),
    'merawat-orang-tua-di-rumah-biaya-dan-perbandingan.txt': (h_merawat_orang_tua_biaya_perbandingan, 'articles-new'),
    'osteoporosis-pada-lansia-pencegahan-dan-perawatan-biaya-dan-perbandingan.txt': (h_osteoporosis_biaya_perbandingan, 'articles-new'),
    'panggil-dokter-ke-rumah-jakarta-biaya-dan-perbandingan.txt': (h_panggil_dokter_jakarta_biaya_perbandingan, 'articles-new'),
    'perawat-lansia-di-rumah-jabodetabek-biaya-dan-perbandingan.txt': (h_perawat_lansia_biaya_perbandingan, 'articles-new'),
    'perawat-lansia-di-rumah-jabodetabek-panduan-lengkap.txt': (h_perawat_lansia_panduan_lengkap, 'articles-new'),
    'perawatan-pasien-parkinson-di-rumah-biaya-dan-perbandingan.txt': (h_parkinson_biaya_perbandingan, 'articles-new'),
    'syarat-kesehatan-studi-luar-negeri-vaksin-mcu-biaya-dan-perbandingan.txt': (h_syarat_studi_biaya_perbandingan, 'articles-new'),
    'syarat-kesehatan-studi-luar-negeri-vaksin-mcu-panduan-lengkap.txt': (h_syarat_studi_panduan_lengkap, 'articles-new'),
    'tips-kesehatan-untuk-mahasiswa-kuliah-di-luar-negeri-biaya-dan-perbandingan.txt': (h_tips_mahasiswa_biaya_perbandingan, 'articles-new'),
    'tips-kesehatan-untuk-mahasiswa-kuliah-di-luar-negeri-panduan-lengkap.txt': (h_tips_mahasiswa_panduan_lengkap, 'articles-new'),
    'tips-kesehatan-untuk-mahasiswa-kuliah-di-luar-negeri-tips-dan-cara.txt': (h_tips_mahasiswa_tips_cara, 'articles-new'),
    'vaksin-di-rumah-jakarta-lansia-biaya-dan-perbandingan.txt': (h_vaksin_lansia_biaya_perbandingan, 'articles-new'),
    'vaksin-di-rumah-jakarta-lansia-panduan-lengkap.txt': (h_vaksin_lansia_panduan_lengkap, 'articles-new'),
}
