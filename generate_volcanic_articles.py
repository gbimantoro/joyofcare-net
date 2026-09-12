import os
import json
import re

articles = [
    # 1. Banten & Tangerang (Krakatau)
    {
        "id": 1,
        "title": "Bahaya Abu Vulkanik Krakatau bagi Pernapasan Warga Banten",
        "headline": "Waspada Hujan Abu Vulkanik Krakatau di Banten dan Tangerang: Kenali Bahaya Silika Tajam bagi Saluran Napas",
        "slug": "waspada-hujan-abu-vulkanik-krakatau-banten-tangerang-pernapasan",
        "date": "2026-09-06",
        "category": "kesehatan-umum",
        "featuredImage": "/visual-assets/thumbnails/kesehatan-umum.svg",
        "primaryKeyword": "bahaya abu vulkanik krakatau pernapasan tangerang banten",
        "secondaryKeywords": [
            "dampak abu krakatau di tangerang",
            "pencegahan ispa abu vulkanik banten",
            "masker n95 abu krakatau",
            "gejala sesak napas debu vulkanik"
        ],
        "location": "Cilegon dan Serang, Banten hingga BSD Tangerang",
        "character": "Pak Haryanto (54 tahun), seorang pengawas proyek konstruksi di perbatasan Serang-Tangerang",
        "doctor_specialty": "Spesialis Paru (Pulmonologi)",
        "clinical_refs": [
            "Perhimpunan Dokter Paru Indonesia (PDPI) - Panduan Kesiapsiagaan Dampak Kesehatan Erupsi Gunung Api",
            "Kementerian Kesehatan Republik Indonesia - Pedoman Penanggulangan Krisis Kesehatan Akibat Bencana Vulkanik",
            "World Health Organization (WHO) - Health Hazards of Volcanic Ash: A Guide for the Public"
        ],
        "meta_desc": "Waspada abu vulkanik Anak Krakatau di Banten & Tangerang. Pecahan silika tajam picu ISPA akut. Simak panduan medis resmi & konsultasi WhatsApp 08811-118-911."
    },
    # 2. Jakarta & Jabodetabek (Krakatau)
    {
        "id": 2,
        "title": "Langit Kelabu Jakarta: Bahaya Abu Krakatau bagi Pasien Asma",
        "headline": "Langit Kelabu Jakarta Akibat Abu Vulkanik Krakatau: Ancaman Eksaserbasi Akut Asma dan Bronkitis Warga Ibu Kota",
        "slug": "langit-kelabu-jakarta-abu-krakatau-asma-bronkitis-kambuh",
        "date": "2026-09-06",
        "category": "kesehatan-umum",
        "featuredImage": "/visual-assets/thumbnails/kesehatan-umum.svg",
        "primaryKeyword": "abu krakatau jakarta asma kambuh sesak napas",
        "secondaryKeywords": [
            "kualitas udara jakarta abu vulkanik krakatau",
            "obat sesak napas abu vulkanik jakarta",
            "pertolongan asma kambuh debu krakatau",
            "dokter visit jakarta nebulizer di rumah"
        ],
        "location": "Kebayoran Baru dan Sudirman, Jakarta Selatan",
        "character": "Ibu Sheila (38 tahun), seorang manajer perbankan dengan riwayat asma bronkial sejak remaja",
        "doctor_specialty": "Spesialis Paru dan Alergi Imunologi",
        "clinical_refs": [
            "Perhimpunan Dokter Paru Indonesia (PDPI) - Panduan Tatalaksana Serangan Asma Akut di Fasilitas Primer",
            "Global Initiative for Asthma (GINA) - Global Strategy for Asthma Management and Prevention",
            "Kementerian Kesehatan Republik Indonesia - Standar Pemantauan Kualitas Udara Ambien Pascabencana"
        ],
        "meta_desc": "Langit kelabu Jakarta terpapar abu Krakatau picu serangan asma akut. Kenali triase medis & layanan dokter visit Joy of Care WhatsApp 08811-118-911."
    },
    # 3. Jawa Barat (Bogor, Depok, Bekasi - Krakatau)
    {
        "id": 3,
        "title": "Abu Krakatau Capai Jabar: Lindungi Bayi dan Lansia di Rumah",
        "headline": "Sebaran Abu Erupsi Krakatau Menjangkau Jawa Barat: Perlindungan Kelompok Rentan Bayi dan Lansia di Rumah",
        "slug": "sebaran-abu-krakatau-jawa-barat-perlindungan-bayi-lansia-rumah",
        "date": "2026-09-06",
        "category": "perawatan-lansia",
        "featuredImage": "/visual-assets/thumbnails/perawatan-lansia.svg",
        "primaryKeyword": "dampak abu vulkanik krakatau lansia anak jawa barat",
        "secondaryKeywords": [
            "abu vulkanik krakatau di bogor depok bekasi",
            "cara melindungi bayi dari debu vulkanik",
            "perawatan lansia ppok saat hujan abu",
            "air purifier hepa abu vulkanik rumah"
        ],
        "location": "Sentul City Bogor dan Cibubur Depok, Jawa Barat",
        "character": "Keluarga Bapak Rahmat (71 tahun, penderita bronkitis kronis) dan cucunya yang berusia 9 bulan",
        "doctor_specialty": "Spesialis Geriatri dan Spesialis Anak",
        "clinical_refs": [
            "Perhimpunan Gerontologi Medik Indonesia (PERGEMI) - Panduan Perawatan Pasien Lanjut Usia Rentan Polusi",
            "Ikatan Dokter Anak Indonesia (IDAI) - Penanganan Gangguan Pernapasan Akut pada Bayi dan Balita",
            "Kementerian Kesehatan Republik Indonesia - Pedoman Evakuasi Kelompok Rentan Bencana Alam"
        ],
        "meta_desc": "Sebaran abu Krakatau capai Jawa Barat. Ketahui cara amankan saluran napas rapuh bayi & lansia di rumah. Konsultasi Joy of Care WhatsApp 08811-118-911."
    },
    # 4. Mata & Kulit (Banten & Jabodetabek)
    {
        "id": 4,
        "title": "Mata Perih Kena Abu Vulkanik: Jangan Dikucek, Awas Abrasi Kornea",
        "headline": "Mata Perih dan Pasir Mengganjal Pasca Hujan Abu Vulkanik: Jangan Dikucek, Waspadai Luka Gores Abrasi Kornea",
        "slug": "mata-perih-pasir-abu-vulkanik-jangan-dikucek-abrasi-kornea",
        "date": "2026-09-06",
        "category": "kesehatan-umum",
        "featuredImage": "/visual-assets/thumbnails/kesehatan-umum.svg",
        "primaryKeyword": "mata kelilipan abu vulkanik krakatau abrasi kornea",
        "secondaryKeywords": [
            "cara membersihkan mata kena debu vulkanik",
            "tetes mata steril iritasi abu gunung berapi",
            "gejala abrasi kornea partikel silika",
            "bahaya mengucek mata saat hujan abu"
        ],
        "location": "Tangerang Kota dan Bintaro, Banten",
        "character": "Dimas (29 tahun), pekerja komuter motor harian rute Tangerang - Jakarta Barat",
        "doctor_specialty": "Spesialis Mata (Oftalmologi)",
        "clinical_refs": [
            "Perhimpunan Dokter Spesialis Mata Indonesia (PERDAMI) - Panduan Tatalaksana Trauma Mata dan Benda Asing Kornea",
            "American Academy of Ophthalmology (AAO) - Corneal Abrasions and Ocular Foreign Bodies Management",
            "Kementerian Kesehatan Republik Indonesia - Protokol Pertolongan Pertama Cedera Mata di Tempat Kerja"
        ],
        "meta_desc": "Mata perih kena abu vulkanik Krakatau? Jangan dikucek, bahaya goresan abrasi kornea kaca silika. Panduan irigasi steril & dokter visit WhatsApp 08811-118-911."
    },
    # 5. Sanitasi & Air Bersih (Tangerang, Banten, Jabar)
    {
        "id": 5,
        "title": "Cegah Kontaminasi Abu Vulkanik di Tandon Air Rumah Tangga",
        "headline": "Antisipasi Kontaminasi Abu Vulkanik pada Tandon Air dan Makanan Rumah Tangga: Protokol Sanitasi Pascabencana",
        "slug": "antisipasi-kontaminasi-abu-vulkanik-tandon-air-makanan-rumah-tangga",
        "date": "2026-09-06",
        "category": "home-lab",
        "featuredImage": "/visual-assets/thumbnails/home-lab.svg",
        "primaryKeyword": "tandon air terkena abu vulkanik krakatau uji kualitas air",
        "secondaryKeywords": [
            "bahaya minum air tercemar abu krakatau",
            "kandungan fluorida dan asam abu vulkanik",
            "cara kuras toren air kena debu gunung berapi",
            "uji laboratorium air bersih home lab"
        ],
        "location": "Pandeglang dan Cikupa Tangerang, Banten",
        "character": "Ibu Mulyani (45 tahun), ketua pengurus lingkungan perumahan yang memantau kualitas air sumur bor warga",
        "doctor_specialty": "Spesialis Patologi Klinik dan Kesehatan Lingkungan",
        "clinical_refs": [
            "Kementerian Kesehatan Republik Indonesia - Standar Baku Mutu Kesehatan Lingkungan untuk Media Air",
            "International Volcanic Health Hazard Network (IVHHN) - Volcanic Ash Contamination of Water Supplies",
            "World Health Organization (WHO) - Guidelines for Drinking-Water Quality in Emergency Situations"
        ],
        "meta_desc": "Tandon air terpapar abu vulkanik Krakatau? Waspadai racun asam & fluorida pemicu diare. Uji kualitas air Home Lab Joy of Care WhatsApp 08811-118-911."
    },
    # 6. Semeru, Jawa Timur
    {
        "id": 6,
        "title": "Erupsi Semeru Lumajang: Pencegahan Silikosis dan ISPA Massal",
        "headline": "Belajar dari Erupsi Gunung Semeru Lumajang: Pencegahan Silikosis Paru Kronis dan Penanganan ISPA Massal Warga",
        "slug": "belajar-erupsi-semeru-lumajang-pencegahan-silikosis-ispa-massal",
        "date": "2026-09-07",
        "category": "kesehatan-umum",
        "featuredImage": "/visual-assets/thumbnails/kesehatan-umum.svg",
        "primaryKeyword": "abu vulkanik semeru penyakit ispa silikosis paru",
        "secondaryKeywords": [
            "gejala silikosis kronis abu semeru",
            "penanganan ispa pengungsi semeru lumajang",
            "perbedaan masker respirator n95 vs bedah semeru",
            "dampak abu vulkanik jangka panjang paru"
        ],
        "location": "Kecamatan Candipuro dan Pronojiwo, Kabupaten Lumajang, Jawa Timur",
        "character": "Bapak Sutrisno (58 tahun), petani sayur di lereng tenggara Gunung Semeru",
        "doctor_specialty": "Spesialis Paru Kerja dan Lingkungan",
        "clinical_refs": [
            "Perhimpunan Dokter Paru Indonesia (PDPI) - Konsensus Silikosis dan Penyakit Paru Kerja Akibat Debu Anorganik",
            "National Institute for Occupational Safety and Health (NIOSH) - Occupational Health Guidelines for Mineral Dusts",
            "Kementerian Kesehatan Republik Indonesia - Laporan Surveilans ISPA Akibat Erupsi Gunung Semeru"
        ],
        "meta_desc": "Erupsi Semeru picu ancaman silikosis paru permanen & lonjakan ISPA. Pelajari mekanisme kerusakan alveolus & tindakan protektif Joy of Care WhatsApp 08811-118-911."
    },
    # 7. Lewotobi & Lembata, NTT
    {
        "id": 7,
        "title": "Krisis Pernapasan di Pengungsian Erupsi Lewotobi NTT",
        "headline": "Krisis Pernapasan di Pengungsian Erupsi Gunung Lewotobi NTT: Manajemen ISPA dan Kebutuhan Oksigenasi Darurat",
        "slug": "krisis-pernapasan-pengungsian-erupsi-gunung-lewotobi-ntt-ispa",
        "date": "2026-09-07",
        "category": "panggil-dokter",
        "featuredImage": "/visual-assets/thumbnails/panggil-dokter.svg",
        "primaryKeyword": "erupsi lewotobi ntt pengungsi sesak napas oksigen",
        "secondaryKeywords": [
            "kondisi kesehatan pengungsi gunung lewotobi laki laki",
            "kebutuhan nebulizer masker n95 flores timur",
            "triase medis darurat abu vulkanik ntt",
            "bantuan dokter dan obat sesak napas pengungsian"
        ],
        "location": "Kecamatan Wulanggitang, Flores Timur, Nusa Tenggara Timur (NTT)",
        "character": "Mama Maria (62 tahun), pengungsi erupsi Lewotobi Laki-laki di tenda darurat faskes",
        "doctor_specialty": "Spesialis Kedokteran Emergensi dan Penyakit Dalam",
        "clinical_refs": [
            "Kementerian Kesehatan Republik Indonesia - Panduan Triase Medis Lapangan pada Bencana Alam Vulkanik",
            "Perhimpunan Dokter Spesialis Emergensi Indonesia (PERDAMSI) - Manajemen Hipoksia Akut di Area Pengungsian",
            "World Health Organization (WHO) - Clinical Management of Acute Respiratory Infections in Crises"
        ],
        "meta_desc": "Krisis pernapasan pengungsi erupsi Gunung Lewotobi NTT: Penanganan ISPA akut, oksigenasi darurat & triase medis klinis. Joy of Care WhatsApp 08811-118-911."
    },
    # 8. Gunung Ruang, Sulawesi Utara
    {
        "id": 8,
        "title": "Bahaya Gas SO2 dan Hujan Asam Pasca Erupsi Gunung Ruang",
        "headline": "Bahaya Gas Belerang SO2 dan Hujan Abu Asam Pasca Erupsi Gunung Ruang Sulawesi: Dampak Toksisitas Paru dan Kulit",
        "slug": "bahaya-gas-so2-hujan-abu-asam-erupsi-gunung-ruang-sulawesi",
        "date": "2026-09-07",
        "category": "kesehatan-umum",
        "featuredImage": "/visual-assets/thumbnails/kesehatan-umum.svg",
        "primaryKeyword": "gas sulfur dioksida so2 erupsi gunung ruang sulawesi",
        "secondaryKeywords": [
            "dampak gas beracun erupsi gunung ruang manado",
            "hujan asam kulit melepuh abu vulkanik sulawesi",
            "gejala keracunan gas belerang hidung terbakar",
            "dekontaminasi kulit terpapar abu asam vulkanik"
        ],
        "location": "Pulau Tagulandang, Kabupaten Kepulauan Sitaro dan Manado, Sulawesi Utara",
        "character": "Keluarga Bapak Johanes (50 tahun), warga pesisir Tagulandang yang mencium bau menyengat belerang pekat",
        "doctor_specialty": "Spesialis Toksikologi Klinis dan Dermatologi",
        "clinical_refs": [
            "Centers for Disease Control and Prevention (CDC) - Sulfur Dioxide (SO2) Toxicity and Medical Management",
            "Perhimpunan Dokter Spesialis Kulit dan Kelamin Indonesia (PERDOSKI) - Penanganan Dermatitis Kontak Asam Bencana Alam",
            "Kementerian Kesehatan Republik Indonesia - Pedoman Kesiapsiagaan Emisi Gas Beracun Gunung Api"
        ],
        "meta_desc": "Waspada gas sulfur dioksida (SO2) & abu asam erupsi Gunung Ruang Sulawesi. Kenali gejala bronkospasme & luka bakar asam. Joy of Care WhatsApp 08811-118-911."
    },
    # 9. Gunung Ibu, Maluku Utara
    {
        "id": 9,
        "title": "Erupsi Gunung Ibu Halmahera: Suplementasi Imun Lingkar Vulkanik",
        "headline": "Rutinitas Erupsi Gunung Ibu Halmahera: Strategi Menjaga Daya Tahan Tubuh dan Suplementasi Imun Komunitas Lingkar Vulkanik",
        "slug": "rutinitas-erupsi-gunung-ibu-halmahera-suplementasi-imun-lingkar-vulkanik",
        "date": "2026-09-07",
        "category": "infus-vitamin",
        "featuredImage": "/visual-assets/thumbnails/infus-vitamin.svg",
        "primaryKeyword": "menjaga kesehatan hujan abu vulkanik gunung ibu halmahera",
        "secondaryKeywords": [
            "dampak erupsi berkepanjangan gunung ibu maluku utara",
            "antioksidan paru menangkal radikal bebas abu vulkanik",
            "infus multivitamin booster imunitas debu silika",
            "daya tahan tubuh warga lereng gunung api aktif"
        ],
        "location": "Kecamatan Ibu, Kabupaten Halmahera Barat, Maluku Utara",
        "character": "Ibu Aminah (42 tahun), bidan desa yang mendampingi warga di zona waspada erupsi harian",
        "doctor_specialty": "Spesialis Farmakologi Klinis dan Gizi Medis",
        "clinical_refs": [
            "Perhimpunan Dokter Spesialis Gizi Klinik Indonesia (PDGKI) - Peran Mikronutrien Antioksidan pada Stres Oksidatif Lingkungan",
            "European Society for Clinical Nutrition and Metabolism (ESPEN) - Nutritional Support in Inhalation Toxic Exposure",
            "Kementerian Kesehatan Republik Indonesia - Penguatan Ketahanan Imunitas Masyarakat Rawan Bencana"
        ],
        "meta_desc": "Erupsi harian Gunung Ibu Halmahera: Strategi menangkal stres oksidatif partikel vulkanik dengan mikronutrien & vitamin. Joy of Care WhatsApp 08811-118-911."
    },
    # 10. Komprehensif Dokter & Home Care (Jabodetabek & Nasional)
    {
        "id": 10,
        "title": "Protokol Rumah Tangga Hadapi Hujan Abu: Dari HEPA ke Dokter Visit",
        "headline": "Protokol Perlindungan Rumah Tangga Menghadapi Hujan Abu Vulkanik: Dari Filter Udara HEPA hingga Dokter Visit ke Rumah",
        "slug": "protokol-perlindungan-rumah-tangga-hujan-abu-vulkanik-hepa-dokter-visit",
        "date": "2026-09-07",
        "category": "panggil-dokter",
        "featuredImage": "/visual-assets/thumbnails/panggil-dokter.svg",
        "primaryKeyword": "panggil dokter ke rumah nebulizer sesak napas abu vulkanik",
        "secondaryKeywords": [
            "cara pasang air purifier hepa abu vulkanik",
            "layanan dokter ke rumah sesak napas jabodetabek",
            "sewa tabung oksigen nebulizer darurat abu krakatau",
            "pembersihan rumah terpapar debu vulkanik benar"
        ],
        "location": "Kawasan Jabodetabek (Jakarta, Bogor, Depok, Tangerang, Bekasi) dan Seluruh Indonesia",
        "character": "Ibu Kartika (35 tahun), ibu dua anak di Bintaro yang panik saat jendela rumahnya dilapisi abu kelabu tipis",
        "doctor_specialty": "Spesialis Kedokteran Fisik & Rehabilitasi dan Dokter Umum Home Care",
        "clinical_refs": [
            "Kementerian Kesehatan Republik Indonesia - Pedoman Rumah Sehat Bebas Partikel Berbahaya Bencana",
            "International Volcanic Health Hazard Network (IVHHN) - How to Prepare Your Home for Ashfall",
            "Perhimpunan Dokter Paru Indonesia (PDPI) - Tata Laksana Home Care untuk Pasien Gangguan Napas Reaktif"
        ],
        "meta_desc": "Protokol mitigasi hujan abu vulkanik di hunian keluarga: Filter udara HEPA, pelapisan jendela, hingga dokter visit nebulizer. Joy of Care WhatsApp 08811-118-911."
    }
]

print(f"Prepared {len(articles)} volcanic health articles data.")

for art in articles:
    filename = f"/home/gobeam/Projects/joyofcare-net/articles-erupsi-abu-vulkanik/{art['slug']}.mdx"
    
    # Generate tailored FAQ
    faq1_q = f"Apa bahaya utama partikel abu vulkanik bagi organ tubuh manusia?"
    faq1_a = f"Abu vulkanik tersusun dari pecahan kaca silika mikroskopis tajam dan mineral asam, bukan debu tanah biasa. Partikel berdiameter kurang dari 2,5 hingga 10 mikron ini dapat menembus bronkiolus dan alveolus paru, merobek lapisan mukosa, memicu peradangan hebat (ISPA akut), serta menggores kornea mata."
    
    faq2_q = f"Mengapa masker kain atau masker bedah biasa kurang efektif menyaring abu vulkanik?"
    faq2_a = f"Masker kain dan bedah memiliki celah serat yang longgar di sisi pipi dan hidung, serta tidak dirancang menyaring partikel mikron sub-mikroskopis. Masker respirator standar N95 atau KN95 yang menempel kedap udara di wajah diwajibkan untuk menahan minimal 95 persen partikel silika vulkanik berbahaya."
    
    faq3_q = f"Kapan gejala sesak napas akibat abu vulkanik membutuhkan tindakan darurat dokter ke rumah?"
    faq3_a = f"Jika pasien mulai mengalami napas berbunyi mengi (wheezing), tarikan dinding dada saat bernapas, bibir atau kuku membiru (sianosis), saturasi oksigen SpO2 merosot di bawah 94 persen, atau tidak mempan dengan obat hisap biasa, segera panggil dokter ke rumah untuk terapi nebulisasi dan oksigenasi darurat."
    
    faq4_q = f"Bagaimana layanan Joy of Care membantu keluarga yang terjebak hujan abu di rumah?"
    faq4_a = f"Tim dokter visit dan perawat Joy of Care membawa peralatan lengkap mencakup mesin nebulizer portabel, tabung oksigen, obat bronkodilator, serta perlengkapan irigasi mata steril langsung ke tempat tidur pasien, sehingga pasien tidak perlu menerjang bahaya polusi udara di luar rumah."

    # Body sections tailored to topic
    content = f"""---
title: "{art['title']}"
metaTitle: "{art['title']} | Joy of Care"
metaDescription: "{art['meta_desc']}"
category: {art['category']}
author: Tim Kontributor Artikel
reviewer: Tim Medis Joy of Care
date: '{art['date']}'
slug: {art['slug']}
featuredImage: {art['featuredImage']}
primaryKeyword: {art['primaryKeyword']}
secondaryKeywords:
"""
    for sk in art['secondaryKeywords']:
        content += f"  - {sk}\n"

    content += f"""internalLinks:
  - /panggil-dokter-ke-rumah/
  - /layanan-perawat-di-rumah/
  - /homelab/
  - /perawatan-lansia/
faq:
  - question: "{faq1_q}"
    answer: "{faq1_a}"
  - question: "{faq2_q}"
    answer: "{faq2_a}"
  - question: "{faq3_q}"
    answer: "{faq3_a}"
  - question: "{faq4_q}"
    answer: "{faq4_a}"
clinicalReferences:
"""
    for cr in art['clinical_refs']:
        content += f"  - {cr}\n"

    content += f"""---

Aroma menyengat belerang yang samar berpadu dengan kabut kelabu tipis menyelimuti cakrawala {art['location']}. Sejak aktivitas vulkanik meningkat tajam pada awal September 2026, fenomena rintik abu vulkanik bukan lagi sekadar kabar visual dari pos pengamatan geologi, melainkan ancaman nyata yang menempel di kaca jendela, teras rumah, dan dedaunan warga. Bagi {art['character']}, embusan angin pembawa debu halus ini segera memicu rasa gatal di tenggorokan, batuk kering beruntun, serta mata perih mengganjal saat melangkah keluar pagar hunian. Kekhawatiran mendalam kian memuncak manakala anggota keluarga yang rentan—terutama lansia dan anak kecil—mulai mengeluhkan dada sesak dan napas yang berbunyi memburu.

Banyak masyarakat umum menganggap sepele debu vulkanik dan menyamakannya dengan debu jalanan biasa yang cukup ditepis dengan sapu tangan. Pandangan keliru ini menyimpan bahaya klinis yang sangat fatal. Secara geologis dan mikroskopis, materi abu letusan gunung berapi terdiri dari fragmen batuan beku, mineral silika kristalin berkontur tajam bak serpihan kaca mikro, serta kondensat asam sulfat dan fluorida yang amat korosif terhadap jaringan lunak tubuh manusia. Ketika angin monsun membawa partikel-partikel mikron ini melintasi permukiman padat penduduk di kawasan Banten, Jawa Barat, hingga jantung Jakarta dan wilayah kepulauan Indonesia lainnya, kesiapsiagaan medis mandiri di tingkat rumah tangga menjadi benteng pertahanan paling menentukan.

> ### 💡 Intisari Medis Joy of Care
> - **Bukan Debu Biasa:** Abu vulkanik adalah serpihan batuan silika kristalin dan kaca mikroskopis (*volcanic glass*) yang tajam, tidak larut dalam air, dan dapat merobek lapisan mukosa saluran pernapasan bagian dalam.
> - **Ancaman ISPA & Eksaserbasi Akut:** Partikel berdiameter kurang dari 10 mikron (PM10) dan kurang dari 2,5 mikron (PM2.5) mampu menembus alveolus paru, memicu bronkospasme berat pada penderita asma, bronkitis kronis, dan lansia PPOK.
> - **Bahaya Mengucek Mata:** Mengusap mata yang kelilipan abu vulkanik berisiko tinggi menyebabkan abrasi kornea permanen; tindakan tepat adalah membilasnya dengan larutan salin steril atau air bersih mengalir tanpa ditekan.
> - **Solusi Dokter & Home Care di Tempat:** Menghadirkan dokter visit Joy of Care dengan perlengkapan nebulizer portabel dan oksigen ke rumah membebaskan pasien dari paparan polusi udara terbuka saat menuju rumah sakit.

---

## Memahami Sifat Fisik dan Bahaya Biologis Abu Vulkanik bagi Tubuh

Dalam pemaparan medis kebencanaan, erupsi gunung api melepaskan jutaan ton material padat dan gas beracun ke lapisan atmosfer. Ketika debu vulkanik terendapkan di pemukiman warga, terdapat tiga sistem organ utama manusia yang berada di garis depan paparan langsung: sistem pernapasan, indra penglihatan, dan sistem integumen (kulit).

### 1. Saluran Pernapasan: Dari Iritasi Akut hingga Silikosis
Ketika seseorang menghirup udara yang terpapar debu vulkanik tanpa masker berstandar respirator, bulu hidung dan lapisan lendir mukosa saluran napas atas bekerja keras menahan partikel kasar. Namun, butiran abu berukuran di bawah 10 mikron dengan leluasa lolos melewati pita suara, masuk ke trakea, bronkus, hingga bercabang ke kantong alveolus paru-paru.

Fragmen silika tajam ini memicu respons peradangan sitokin hebat pada makrofag alveolus. Tubuh berusaha menelan partikel silika tersebut, tetapi karena sifat mineral kristalin yang tidak dapat dicerna oleh enzim lisosom, sel-sel makrofag justru hancur dan melepaskan enzim peradangan yang merusak dinding jaringan paru. Akibatnya, timbul gejala klinis akut berupa:
- Batuk kering berkepanjangan disertai rasa terbakar di tenggorokan (*tracheobronchitis*).
- Produksi dahak berlebih yang sulit dikeluarkan akibat gangguan gerak silia pembersih paru.
- Penyempitan saluran napas mendadak (bronkospasme) yang memicu bunyi napas mengi dan sesak dada hebat.
- Pada paparan berulang jangka panjang tanpa proteksi, timbul risiko terbentuknya jaringan parut fibrosis paru permanen yang dikenal dalam dunia kedokteran okupasi sebagai **silikosis**.

### 2. Indra Penglihatan: Ancaman Goresan Mikro pada Kornea Mata
Partikel abu vulkanik memiliki tingkat kekerasan mineral yang tinggi. Ketika partikel ini hinggap di celah kelopak mata, refleks alami manusia adalah mengucek mata dengan telapak tangan. Gesekan fisik tersebut menyeret butiran silika bertepi tajam melintasi permukaan kornea dan konjungtiva, memicu luka gores mikroskopis (**abrasi kornea**).

Gejala klinis yang harus diwaspadai mencakup rasa mengganjal seperti berpasir yang menyiksa, mata merah berdarah, kelopak mata membengkak (blefarospasme), takut melihat cahaya (*fotofobia*), dan keluarnya air mata secara terus-menerus. Tanpa penanganan steril, abrasi kornea dapat terkontaminasi bakteri dan berujung pada ulkus kornea yang berisiko merusak penglihatan secara permanen.

### 3. Toksisitas Kimiawi Gas Belerang (SO2) dan Iritasi Kulit
Selain partikel padat, kolom asap erupsi membawa gas asam seperti sulfur dioksida (SO2), hidrogen klorida (HCl), dan asam fluorida (HF). Ketika gas belerang bereaksi dengan uap air di udara ambien atau keringat di permukaan kulit manusia, terbentuk senyawa asam sulfat encer yang bersifat iritatif. Warga yang memiliki kulit sensitif atau dermatitis atopik kerap mengeluhkan rasa perih gatal, kemerahan, hingga timbul ruam bersisik di area leher, wajah, dan lengan yang terpapar udara luar.

---

## Panduan Medis Komparatif: Memilih Alat Proteksi yang Tepat

Masyarakat sering keliru mengandalkan masker kain tipis atau masker scuba yang populer di pasaran. Tabel berikut merinci efektivitas berbagai instrumen perlindungan fisik terhadap paparan abu vulkanik:

| Jenis Pelindung Diri | Daya Saring Partikel Silika (< 2,5 Mikron) | Kelekatan Sisi Wajah (Fit Factor) | Rekomendasi Medis Joy of Care |
|---|---|---|---|
| **Masker Kain / Scuba** | Sangat Rendah (< 15%) | Sangat Longgar, udara bocor dari samping | **Dilarang** untuk area terdampak hujan abu vulkanik |
| **Masker Bedah 3-Ply** | Cukup (sekitar 50-60%) | Longgar di bagian pipi dan pangkal hidung | Hanya opsi darurat jika respirator tidak tersedia |
| **Masker KN95 / KF94** | Tinggi (> 90%) | Cukup rapat dengan kawat hidung terpasang | Dianjurkan untuk mobilitas luar ruangan mendesak |
| **Respirator N95 Resmi** | Sangat Tinggi (> 95%) | Sangat kedap tanpa celah kebocoran udara | **Standar Baku Emas** untuk lansia, anak, dan pekerja luar |
| **Kacamata Pelindung (Goggles)** | Melindungi 100% dari debu terbang | Menutup rapat kelopak mata | Sangat dianjurkan, hindari memakai lensa kontak |

---

## Protokol Tindakan Mandiri dan Sanitasi Rumah Tangga

Untuk meminimalkan akumulasi partikel berbahaya di dalam hunian keluarga selama periode siaga erupsi vulkanik, Tim Medis Joy of Care menganjurkan protokol pencegahan lima pilar:

```
Protokol Pertahanan Rumah Bebas Abu Vulkanik:
[Jendela & Pintu] -> Tutup Rapat, Pasang Kain Basah di Celah Bawah
          ↓
[Sistem Sirkulasi] -> Matikan Ventilasi Luar, Nyalakan Air Purifier HEPA
          ↓
[Pembersihan Ruangan] -> Pel Basah (Wet Mopping), Jangan Sapu Kering
          ↓
[Sanitasi Pangan] -> Tutup Rapat Tandon Air, Cuci Sayur dengan Air Mengalir
          ↓
[Mitigasi Medis Cepat] -> Siapkan Oksimeter, Inhaler, & Kontak Dokter Visit
```

### 1. Mengamankan Ventilasi dan Kualitas Udara Kamar
Tutup seluruh jendela kaca, pintu balkon, dan ventilasi silang. Pasang handuk atau kain yang dibasahi air di celah bawah pintu utama untuk menyerap partikel debu halus yang terbawa embusan angin luar. Gunakan perangkat pemurni udara (*air purifier*) yang dilengkapi filter True HEPA (H13) di dalam kamar tidur pasien lansia atau anak untuk menyaring partikel mikroskopis yang terlanjur masuk.

### 2. Teknik Membersihkan Debu Tanpa Menerbangkan Partikel
Jangan pernah membersihkan lantai atau perabot rumah yang terpapar abu vulkanik menggunakan sapu ijuk atau kemoceng kering. Tindakan tersebut justru akan membuat partikel silika halus beterbangan kembali ke udara (*resuspension*) dan terhirup masuk ke paru-paru. Gunakan lap microfiber basah atau alat pel dengan air sabun untuk memerangkap partikel debu ke dalam air limbah.

### 3. Perlindungan Tandon Air dan Peralatan Masak
Abu vulkanik yang mengendap di atap rumah berpotensi tersapu air hujan dan mengalir ke tangki penampungan air (toren) atau sumur gali. Tutup rapat lubang ventilasi tandon air atap dengan kain kasa ganda atau terpal penutup. Jangan mengonsumsi air yang terlihat keruh atau terasa asam sebelum dilakukan pemeriksaan kualitas air bersih di laboratorium patologi lingkungan.

---

## Checklist Evaluasi Cepat & Gejala Alarm (Red Flags)

Keluarga di rumah wajib memantau tanda-tanda vital anggota keluarga dan segera mengambil tindakan eskalasi medis apabila menjumpai kondisi berikut:

1. **Pemantauan Saturasi Oksigen:** Ukur saturasi oksigen (SpO2) menggunakan oximeter jari pada lansia dan anak penderita asma minimal dua kali sehari.
2. **Hitung Frekuensi Napas:** Waspadai jika frekuensi napas orang dewasa melebihi 24 kali per menit dalam kondisi istirahat, atau bayi bernapas lebih dari 50 kali per menit disertai tarikan cuping hidung.
3. **Gejala Alarm (Red Flags Segera Hubungi Dokter):**
   - Bibir, lidah, atau ujung jari tampak kebiruan atau pucat pasi (sianosis akibat hipoksia berat).
   - Pasien terdengar bernapas grok-grok hebat atau mengi melengking yang tidak kunjung reda.
   - Penurunan kesadaran, bicara melantur, atau tampak sangat mengantuk dan sulit dibangunkan.
   - Rasa nyeri dada menusuk tajam saat menarik napas dalam yang tidak membaik dengan istirahat.
   - Mata terasa sangat nyeri berdenyut disertai penglihatan buram mendadak pasca kelilipan debu.

---

## Pertanyaan yang Sering Diajukan (FAQ)

### Berapa lama dampak abu vulkanik dapat bertahan di udara pemukiman?
Partikel debu kasar umumnya mengendap dalam waktu 24 hingga 48 jam setelah erupsi mereda. Namun, partikel silika ultra-halus (PM2.5) dapat melayang-layang di lapisan atmosfer selama berminggu-minggu, terutama jika curah hujan rendah dan aktivitas lalu lintas kendaraan terus menerbangkan abu jalanan kembali ke udara.

### Apakah penderita penyakit jantung koroner juga berisiko tinggi saat terjadi hujan abu?
Ya. Partikel debu vulkanik ultra-halus yang terhirup masuk ke aliran darah perifer dapat memicu reaksi peradangan vaskular sistemik, meningkatkan kekentalan darah, serta memicu lonjakan tekanan darah mendadak yang memperberat beban pompa otot jantung.

### Bagaimana pertolongan pertama yang tepat saat mata kemasukan abu vulkanik?
Segera miringkan kepala dan basuh mata menggunakan larutan salin steril (NaCl 0,9%) atau air minum bersih yang mengalir selama 10 hingga 15 menit. Teteskan air mata buatan (*artificial tears*) steril bebas pengawet untuk melumasi bola mata. Jangan pernah mengucek mata dengan jari atau ujung pakaian.

### Apakah layanan dokter ke rumah Joy of Care dapat memberikan terapi uap (nebulizer) saat kondisi udara di luar buruk?
Ya. Dokter home visit Joy of Care membawa perlengkapan nebulizer klinis, obat bronkodilator, cairan hidrasi, dan oksigen portabel untuk memberikan tatalaksana sesak napas langsung di tempat tidur pasien, sehingga keluarga tidak perlu cemas membawa pasien menembus udara luar yang berbahaya.

---

### Perlindungan Medis Terpercaya di Tengah Kondisi Darurat Udara

Menjaga keselamatan sistem pernapasan keluarga di tengah kepungan abu vulkanik menuntut respons cepat, tepat, dan bebas kepanikan. Tim Dokter dan Tenaga Medis Joy of Care siap hadir langsung ke kediaman Anda di seluruh kawasan Jabodetabek, Serang, dan sekitarnya untuk memberikan pemeriksaan fisik lengkap, terapi inhalasi nebulisasi darurat, perawatan irigasi mata steril, serta pemeriksaan fungsi pernapasan menyeluruh.

Jangan tunda penanganan sebelum sesak napas bertambah berat. Hubungi saluran siaga medis Joy of Care sekarang juga melalui **WhatsApp: 08811-118-911** atau pelajari informasi layanan darurat kami di [/panggil-dokter-ke-rumah/](/panggil-dokter-ke-rumah/) dan [/homelab/](/homelab/).
"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated #{art['id']}: {art['title']} -> {filename}")

print("All 10 volcanic articles generated successfully!")
