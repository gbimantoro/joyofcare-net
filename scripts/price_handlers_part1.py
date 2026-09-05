# Handler functions for files 1 to 13

PRIMARY_CTA = "Hubungi WhatsApp JoC untuk informasi harga: https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Berapa%20biaya%20layanan%20Joy%20of%20Care?"
ALTERNATE_CTA = "Konsultasi Dokter Gratis via WhatsApp: https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Mau%20konsultasi%20gratis%20dengan%20dokter"

def handle_persyaratan_kesehatan_perjalanan_9(text):
    text = text.replace(
        "USD 50,000–100,000.",
        "perlindungan repatriasi medis penuh dan komprehensif. " + PRIMARY_CTA
    )
    return text

def handle_persyaratan_medis_australia_14(text):
    old_fm = "answer: Biaya pemeriksaan bervariasi antara Rp 1.200.000 hingga Rp 2.500.000 tergantung\n    usia pemohon dan jenis tes tambahan yang diwajibkan dalam Referral Letter HAP\n    ID Anda."
    new_fm = "answer: Biaya pemeriksaan visa pelajar Australia ditentukan oleh panel physician resmi berdasarkan usia pemohon dan jenis tes tambahan yang diwajibkan dalam Referral Letter HAP ID Anda. " + PRIMARY_CTA
    text = text.replace(old_fm, new_fm)
    
    old_body = "Biaya pemeriksaan bervariasi antara Rp 1.200.000 hingga Rp 2.500.000 tergantung usia pemohon dan jenis tes tambahan yang diwajibkan dalam Referral Letter HAP ID Anda."
    new_body = "Biaya pemeriksaan bervariasi tergantung usia pemohon dan jenis tes tambahan yang diwajibkan dalam Referral Letter HAP ID Anda. Layanan persiapan dokumen dan konsultasi kesehatan Joy of Care siap membantu kelancaran proses studi Anda. " + PRIMARY_CTA
    text = text.replace(old_body, new_body)
    return text

def handle_akupuntur_biaya_perbandingan(text):
    old_sec = """Banyak orang mengira membeli obat pereda nyeri generik seharga Rp 20.000 per strip adalah opsi yang sangat murah. Namun, mari kita cermati kalkulasi biaya medis riil jika komplikasi terjadi:

### Skenario A: Perawatan Akibat Komplikasi Konsumsi Obat Nyeri Rutin (1 Tahun)
1. Pembelian obat NSAID + obat pelindung lambung harian: Rp 3.600.000/tahun
2. Biaya Rawat Inap RS Akibat Tukak Lambung Berdarah (Kamar + Transfusi Darah): Rp 25.000.000 – Rp 45.000.000
3. Biaya Perawatan Gagal Ginjal Stadium Awal (Nefrolog + Obat Ginjal): Rp 15.000.000 – Rp 35.000.000
4. **Total Risiko Biaya Medis**: **Rp 43.600.000 – Rp 83.600.000+**

### Skenario B: Program Terapi Akupuntur Medis Berkala Joy of Care (1 Tahun)
1. Siklus Awal Akupuntur Medis Intensif (8 sesi di rumah): Rp 3.200.000
2. Sesi Pemeliharaan Rutin (1x per bulan untuk menjaga sendi lentur): Rp 4.500.000/tahun
3. Suplemen Pelumas Sendi Alami (Glukosamin / Kolagen Tipe 2): Rp 2.400.000/tahun
4. **Total Investasi Kesehatan**: **Rp 10.100.000/tahun** (Nol komplikasi organ, ginjal dan lambung lansia 100% sehat terlindungi)."""

    new_sec = f"""Banyak orang mengira membeli obat pereda nyeri generik secara bebas tanpa resep adalah opsi murah. Namun, mari kita cermati risiko kesehatan dan beban biaya medis jangka panjang jika komplikasi organ terjadi:

### Skenario A: Risiko Komplikasi Konsumsi Obat Pereda Nyeri Kimiawi Jangka Panjang (1 Tahun)
1. Pembelian obat antinyeri NSAID dan obat pelindung lambung harian secara terus-menerus tanpa pengawasan dokter.
2. Risiko rawat inap rumah sakit darurat akibat tukak lambung berdarah yang membutuhkan transfusi darah dan endoskopi darurat.
3. Beban perawatan gagal ginjal atau penurunan fungsi ginjal kronis yang menuntut konsultasi dokter spesialis nefrologi rutin.
4. **Total Risiko Beban Finansial**: Membengkak sangat besar hingga puluhan bahkan ratusan juta rupiah, disertai penurunan drastis kualitas hidup lansia.

### Skenario B: Program Terapi Akupuntur Medis Terpadu Joy of Care di Rumah (1 Tahun)
1. Siklus awal akupuntur medis intensif di rumah oleh dokter dan akupunkturis medis berlisensi resmi Kemenkes.
2. Sesi pemeliharaan berkala untuk menjaga kelenturan sendi, melancarkan aliran mikrosirkulasi darah, dan mencegah kekakuan sendi pagi hari.
3. Penggunaan jarum mikro steril sekali pakai (*single-use*) yang bebas risiko penularan infeksi silang dan aman untuk ginjal lansia.
4. **Investasi Kesehatan Terencana**: Nol risiko komplikasi lambung dan ginjal, mobilitas harian orang tua tetap mandiri dan bahagia. {PRIMARY_CTA}"""

    text = text.replace(old_sec, new_sec)
    return text

def handle_akupuntur_panduan_lengkap(text):
    old_fm = "answer: Biaya resmi layanan akupuntur medis home visit Joy of Care berkisar antara\n    Rp 375.000 hingga Rp 550.000 per sesi, sudah mencakup jasa tindakan medis oleh\n    dokter/terapis berlisensi, jarum steril sekali pakai, modalitas elektroakupunktur"
    new_fm = f"answer: Biaya layanan akupuntur medis home visit Joy of Care ditentukan secara transparan berdasarkan kondisi klinis pasien, sudah mencakup jasa tindakan dokter/terapis berlisensi, jarum steril sekali pakai, dan modalitas elektroakupunktur. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
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
    text = text.replace(old_table, new_table)
    return text

def handle_antar_jemput_biaya_perbandingan(text):
    old_row = "| **Struktur Biaya** | Paket PP Rp 750.000 – Rp 950.000 (termasuk tunggu perawat 2–3 jam). | Ongkos argo per km (sering melonjak *surge price* saat jam sibuk/hujan). | Tarif panggilan darurat RS (Rp 1.200.000 – Rp 2.500.000 per trip). |"
    new_row = f"| **Struktur Biaya** | Paket transparan all-in termasuk perawat pendamping & waktu tunggu RS. | Ongkos argo berfluktuasi tajam saat jam sibuk atau cuaca hujan. | Tarif panggilan darurat ambulans RS yang relatif sangat mahal. |"
    text = text.replace(old_row, new_row)
    
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

    text = text.replace(old_sim, new_sim)
    return text

def handle_antar_jemput_panduan_lengkap(text):
    old_fm = "answer: Tarif layanan antar-jemput medis non-darurat (NEMT) Joy of Care di Jakarta\n    berkisar antara Rp 450.000 hingga Rp 650.000 untuk perjalanan satu arah, dan\n    Rp 750.000 hingga Rp 1.100.000 untuk paket pulang-pergi (PP) termasuk waktu tunggu\n    perawat di poliklinik rumah sakit selama 2–3 jam."
    new_fm = f"answer: Tarif layanan antar-jemput medis non-darurat Joy of Care di Jakarta ditentukan secara transparan berdasarkan paket satu arah maupun pulang-pergi, sudah mencakup armada khusus berfasilitas medis serta pendampingan perawat profesional. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    old_callout = "> * **Transparansi Tarif Jakarta 2026**: Paket pulang-pergi (PP) mulai Rp 750.000 mencakup biaya tunggu perawat di poliklinik 2-3 jam tanpa biaya argo tersembunyi."
    new_callout = f"> * **Transparansi Layanan Medis Jakarta**: Layanan antar-jemput medis terpadu Joy of Care menyediakan paket transparan dengan perawat pendamping poliklinik tanpa biaya argo tersembunyi. {PRIMARY_CTA}"
    text = text.replace(old_callout, new_callout)
    
    old_table = """|---|---|---|
| **Paket Satu Arah (One-Way)** | Mobil NEMT + Driver + Perawat Pendamping + Kursi Roda / Brankar | Rp 450.000 – Rp 650.000 |
| **Paket Pulang-Pergi Standar (PP)** | Antar + Tunggu Poliklinik + Jemput Pulang + Pendampingan Perawat | Rp 750.000 – Rp 1.000.000 |
| **Paket Khusus Hemodialisis / Kemo** | Antar-jemput terjadwal mingguan + tabung oksigen standby + perawat | Rp 2.800.000 – Rp 3.600.000 (Paket 4x PP) |
| **Paket Lintas Kota (Jabodetabek)** | Perjalanan antar kota (misal: Tangerang ke RS di Jakarta Pusat) | Rp 950.000 – Rp 1.400.000 (PP) |"""

    new_table = f"""|---|---|---|
| **Paket Satu Arah (One-Way)** | Mobil NEMT + Driver + Perawat Pendamping + Kursi Roda / Brankar | Paket All-in (Hubungi WA JoC) |
| **Paket Pulang-Pergi Standar (PP)** | Antar + Tunggu Poliklinik + Jemput Pulang + Pendampingan Perawat | Paket Terjadwal (Hubungi WA JoC) |
| **Paket Khusus Hemodialisis / Kemo** | Antar-jemput terjadwal mingguan + tabung oksigen standby + perawat | Paket Berkala (Hubungi WA JoC) |
| **Paket Lintas Kota (Jabodetabek)** | Perjalanan antar kota (misal: Tangerang ke RS di Jakarta Pusat) | Paket Lintas Wilayah (Hubungi WA JoC) |

{PRIMARY_CTA}"""
    text = text.replace(old_table, new_table)
    return text

def handle_biaya_dokter_biaya_perbandingan(text):
    old_fm = "answer: Tarif visit dokter umum Joy of Care berkisar antara Rp 275.000 hingga Rp\n    450.000, sementara penyedia korporat atau platform lain mematok tarif berkisar\n    antara Rp 450.000 hingga Rp 850.000 per kunjungan di luar biaya tindakan dan obat."
    new_fm = f"answer: Tarif visit dokter umum Joy of Care dirancang transparan, terjangkau, dan langsung ditangani tim medis tanpa biaya perantara aplikasi atau markup tersembunyi. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
    text = text.replace(
        "tarif visit dokter Joy of Care jauh lebih ramah dan transparan (mulai dari **Rp 275.000 – Rp 400.000** per visit).",
        "tarif visit dokter Joy of Care jauh lebih ramah, transparan, dan terukur tanpa biaya perantara tersembunyi."
    )
    text = text.replace(
        "tarif visit dokter umum sering kali dipatok mulai dari Rp 450.000 hingga Rp 700.000 per visit hanya untuk jasa perantara saja.",
        "tarif visit dokter umum sering kali dipatok tinggi akibat biaya perantara dan komisi aplikasi digital."
    )
    
    old_row = "| **Estimasi Tarif Visit Dokter Umum** | **Rp 275.000 – Rp 400.000** | Rp 450.000 – Rp 700.000 | Rp 500.000 – Rp 850.000 |"
    new_row = "| **Estimasi Tarif Visit Dokter Umum** | **Tarif Transparan (Hubungi WA JoC)** | Tarif Tinggi Platform + Admin | Tarif RS Swasta Tinggi |"
    text = text.replace(old_row, new_row)
    
    old_body_faq = "Tarif visit dokter umum Joy of Care berkisar antara Rp 275.000 hingga Rp 450.000, sementara penyedia korporat atau platform lain mematok tarif berkisar antara Rp 450.000 hingga Rp 850.000 per kunjungan di luar biaya tindakan dan obat."
    new_body_faq = f"Tarif visit dokter umum Joy of Care dirancang sangat transparan dan kompetitif tanpa biaya perantara aplikasi atau beban administrasi rumah sakit. Rincian biaya tindakan medis dan obat selalu dikomunikasikan secara terbuka kepada keluarga. {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_biaya_dokter_kapan_harus(text):
    old_fm = "answer: Keluarga berhasil menghemat lebih dari Rp 4.500.000 dalam satu episode penanganan\n    demam dan dehidrasi lansia, dibandingkan jika pasien harus dibawa ke IGD rumah\n    sakit swasta dan menjalani rawat inap selama 2 malam."
    new_fm = f"answer: Keluarga berhasil menghemat lebih dari 60% biaya medis dalam satu episode penanganan demam dan dehidrasi lansia, dibandingkan jika pasien harus dibawa ke IGD dan dirawat inap di RS swasta. {ALTERNATE_CTA}"
    text = text.replace(old_fm, new_fm)
    
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
| **Karcis Pendaftaran & Fasilitas IGD** | Beban karcis dan biaya ruangan RS tinggi | **Rp 0 (Pemeriksaan langsung di ranjang rumah)** |
| **Jasa Dokter Pemeriksa** | Jasa ganda dokter jaga IGD & visite spesialis | **Jasa dokter visit terjangkau & berdedikasi 60+ menit** |
| **Biaya Kamar Rawat Inap (2 Malam)** | Tarif kamar opname RS kelas standar/VIP | **Rp 0 (Kenyamanan penuh di kamar sendiri)** |
| **Pemasangan Infus & Cairan Medis** | Biaya tindakan infus dan BMHP rumah sakit tinggi | **Paket infus hidrasi homecare transparan** |
| **Perawat Pendamping Harian** | Beban administrasi keperawatan bangsal RS | **Perawat homecare terakreditasi dan berfokus penuh** |
| **Biaya Obat-obatan & BMHP** | Margin harga farmasi instalasi rawat inap RS | **Resep obat apotek resmi transparan & terjangkau** |
| **Total Beban Pengeluaran** | **Total Biaya RS Sangat Tinggi** | **Penghematan Signifikan Lebih dari 60%** |

{ALTERNATE_CTA}"""
    text = text.replace(old_table, new_table)
    
    old_body_faq = "Keluarga berhasil menghemat lebih dari Rp 4.500.000 dalam satu episode penanganan demam dan dehidrasi lansia, dibandingkan jika pasien harus dibawa ke IGD rumah sakit swasta dan menjalani rawat inap selama 2 malam."
    new_body_faq = f"Keluarga berhasil menghemat lebih dari 60% dari total estimasi biaya rawat inap rumah sakit swasta dalam satu episode penanganan demam dan dehidrasi lansia. Selain efisiensi biaya, kenyamanan psikologis pasien dan keluarga terjaga maksimal. {ALTERNATE_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_biaya_dokter_panduan_lengkap(text):
    old_fm = "answer: Tarif dasar kunjungan dokter umum Joy of Care di wilayah Jakarta pada tahun\n    2026 berkisar antara Rp 275.000 hingga Rp 450.000 per sesi visit. Tarif ini sudah\n    mencakup konsultasi klinis mendalam, pemeriksaan fisik lengkap (tensi, saturasi\n    oksigen, auskultasi paru/jantung), dan peresepan obat resmi."
    new_fm = f"answer: Tarif dasar kunjungan dokter umum Joy of Care di wilayah Jakarta dirancang transparan dan terjangkau, sudah mencakup konsultasi klinis mendalam, pemeriksaan fisik lengkap (tensi, saturasi oksigen, auskultasi), dan peresepan obat resmi. {PRIMARY_CTA}"
    text = text.replace(old_fm, new_fm)
    
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
    
    old_body_faq = "Tarif dasar kunjungan dokter umum Joy of Care di wilayah Jakarta pada tahun 2026 berkisar antara Rp 275.000 hingga Rp 450.000 per sesi visit. Tarif ini sudah mencakup konsultasi klinis mendalam, pemeriksaan fisik lengkap (tensi, saturasi oksigen, auskultasi paru/jantung), dan peresepan obat resmi."
    new_body_faq = f"Tarif dasar kunjungan dokter umum Joy of Care di wilayah Jakarta dirancang transparan dan terjangkau, mencakup konsultasi klinis mendalam, pemeriksaan fisik lengkap (tensi, saturasi oksigen, auskultasi), dan peresepan obat resmi. {PRIMARY_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_biaya_dokter_tips_cara(text):
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
| **Biaya Anggota Keluarga ke-2** | Rp 0 (1 Pasien) | Rp 0 (1 Pasien) | Paket Hemat Add-on Keluarga |
| **Biaya Tindakan Medis NGT** | Rp 0 | Tindakan Steril Alat Medis | Rp 0 |
| **Biaya Transportasi Zonasi** | Tarif Flat Terjangkau | Tarif Flat Terjangkau | Tarif Flat Terjangkau |
| **Estimasi Resep Obat Standar** | Resep Apotek Transparan | Resep Apotek Transparan | Resep Apotek Transparan |
| **Skema Total Biaya** | **Transparan & Terukur** | **Transparan & Terukur** | **Paket Hemat Keluarga (2 Orang)** |

{PRIMARY_CTA}"""
    text = text.replace(old_table, new_table)
    return text

def handle_biaya_dokter_yang_perlu_anda_ketahui(text):
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

def handle_cegah_jatuh_kapan_harus(text):
    old_fm = "answer: Biaya tindakan bedah ortopedi (operasi pemasangan pen atau penggantian sendi\n    panggul bipolar/THR) berkisar antara Rp 70.000.000 hingga Rp 150.000.000, belum\n    termasuk biaya perawatan ruang ICU jika timbul komplikasi sistemik pascabedah."
    new_fm = f"answer: Biaya tindakan bedah ortopedi panggul di rumah sakit menelan anggaran puluhan hingga ratusan juta rupiah di luar biaya ICU dan rehabilitasi pascabedah. {ALTERNATE_CTA}"
    text = text.replace(old_fm, new_fm)
    
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

    new_table = f"""| **Biaya Operasi & Implan Bedah Panggul** | Tagihan operasi fraktur RS swasta sangat tinggi | **Rp 0 (Fraktur dicegah total)** |
| **Kamar Rawat Inap & Ruang ICU (7 Hari)** | Beban sewa kamar rawat inap dan ICU tinggi | **Rp 0 (Lansia tetap sehat di rumah)** |
| **Biaya Modifikasi Rumah Anti-Jatuh** | Rp 0 (Tidak dilakukan, risiko fatal) | **Investasi terjangkau (Sekali pasang)** |
| **Paket Fisioterapi Keseimbangan (3 Bulan)**| Rp 0 (Tanpa latihan penguatan otot) | **Program rehabilitasi terukur & transparan** |
| **Kunjungan Dokter Review Polifarmasi** | Rp 0 | **Visit dokter evaluasi obat di rumah** |
| **TOTAL BEBAN KEUANGAN KELUARGA** | **Beban Rumah Sakit Ratusan Juta Rupiah** | **Investasi Preventif Sangat Hemat & Aman** |

{ALTERNATE_CTA}"""
    text = text.replace(old_table, new_table)
    
    old_body_faq = "Biaya tindakan bedah ortopedi (operasi pemasangan pen atau penggantian sendi panggul bipolar/THR) berkisar antara Rp 70.000.000 hingga Rp 150.000.000, belum termasuk biaya perawatan ruang ICU jika timbul komplikasi sistemik pascabedah."
    new_body_faq = f"Biaya tindakan bedah ortopedi panggul di rumah sakit swasta dapat menelan biaya hingga puluhan bahkan ratusan juta rupiah di luar biaya ruang ICU. Melakukan langkah preventif modifikasi rumah dan fisioterapi keseimbangan terbukti menghemat finansial keluarga secara luar biasa. {ALTERNATE_CTA}"
    text = text.replace(old_body_faq, new_body_faq)
    return text

def handle_cegah_jatuh_tips_cara(text):
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
    text = text.replace(old_table, new_table)
    return text
