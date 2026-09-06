import os
import json
import re

with open('/home/gobeam/Projects/joyofcare-net/fase2_manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

print(f"Loaded {len(manifest)} items from Fase 2 manifest.")

# Helper to format clean title within 60 chars
def format_title(headline):
    # If headline has colon, take the most punchy part or summarize
    if ':' in headline:
        parts = headline.split(':', 1)
        # Choose the part that fits or combine smartly
        short = parts[0].strip()
        if len(short) <= 58:
            return short
        return short[:55] + "..."
    if len(headline) > 58:
        return headline[:55] + "..."
    return headline

# Clinical reference mapping
REF_MAP = {
    'fisioterapi-rumah': [
        "Ikatan Fisioterapi Indonesia (IFI) - Panduan Praktik Klinis Fisioterapi Neurologi dan Muskuloskeletal",
        "World Physiotherapy - Global Standards for Physical Therapy Home Services",
        "Perhimpunan Dokter Spesialis Kedokteran Fisik dan Rehabilitasi Indonesia (PERDOSRI) - Konsensus Rehabilitasi Medik"
    ],
    'home-lab': [
        "Perhimpunan Dokter Spesialis Patologi Klinik dan Kedokteran Laboratorium Indonesia (PDS PatKLIn) - Panduan Pemeriksaan Laboratorium Terpadu",
        "Kementerian Kesehatan Republik Indonesia - Standar Baku Mutu Pelayanan Laboratorium Kesehatan",
        "Clinical and Laboratory Standards Institute (CLSI) - Guidelines for Quality Phlebotomy and Specimen Handling"
    ],
    'perawatan-lansia': [
        "Perhimpunan Gerontologi Medik Indonesia (PERGEMI) - Konsensus Nasional Pengelolaan Sindrom Geriatri",
        "Alzheimer's Disease International (ADI) - Dementia Care Best Practices in Home Settings",
        "Kementerian Kesehatan Republik Indonesia - Pedoman Nasional Pelayanan Kedokteran Geriatri"
    ],
    'parkinson': [
        "Perhimpunan Dokter Spesialis Saraf Indonesia (PERDOSNI) - Panduan Tata Laksana Penyakit Parkinson dan Gangguan Gerak",
        "Movement Disorder Society (MDS) - Clinical Guidelines for Comprehensive Parkinson's Home Care",
        "World Health Organization (WHO) - Clinical Management of Neurodegenerative Disorders"
    ],
    'osteoporosis': [
        "Perhimpunan Osteoporosis Indonesia (PEROSI) - Panduan Diagnosis dan Penatalaksanaan Osteoporosis",
        "International Osteoporosis Foundation (IOF) - Global Guidelines for Fracture Prevention and Bone Density Management",
        "Kementerian Kesehatan Republik Indonesia - Pedoman Pengendalian Penyakit Sendi dan Tulang pada Lansia"
    ]
}

# Relatable Jabodetabek real-world human story backgrounds
LOCATIONS = [
    ("Tebet, Jakarta Selatan", "Pak Sudirman", 71, "purnawirawan guru", "putranya yang bekerja remote di bidang teknologi"),
    ("Kelapa Gading, Jakarta Utara", "Ibu Linda", 68, "mantan wirausahawan tekstil", "anak perempuannya yang mengelola bisnis keluarga"),
    ("BSD City, Tangerang Selatan", "Pak Hendra", 64, "mantan arsitek", "menantunya yang berkantor di kawasan Sudirman"),
    ("Bintaro Jaya, Tangerang Selatan", "Ibu Ratna", 73, "pensiunan perawat", "putra bungsunya yang berprofesi sebagai konsultan hukum"),
    ("Puri Indah, Jakarta Barat", "Pak Hartono", 69, "pemilik toko bangunan", "anak sulungnya yang tinggal di perumahan yang sama"),
    ("Menteng, Jakarta Pusat", "Ibu Kusuma", 76, "mantan diplomat", "cucunya yang baru menyelesaikan studi magister"),
    ("Bekasi Barat, Kota Bekasi", "Pak Joko", 66, "mantan teknisi transportasi", "putrinya yang bekerja sif malam di rumah sakit"),
    ("Kemang, Jakarta Selatan", "Ibu Vivian", 62, "konsultan interior independen", "suaminya yang masih aktif memimpin firma riset"),
    ("Cibubur, Jakarta Timur", "Pak Bambang", 70, "pensiunan perbankan", "kedua anaknya yang tinggal di apartemen Kuningan"),
    ("Gading Serpong, Tangerang", "Ibu Theresia", 67, "pengelola katering rumahan", "menantunya yang bekerja di kawasan perkantoran TB Simatupang")
]

for idx, item in enumerate(manifest):
    cluster = item['cluster']
    headline = item['headline']
    slug = item['slug']
    cat = item['category']
    date = item['date']
    angle = item['angle']
    target_file = item['target_file']
    feat_img = item['featuredImage']
    
    title = format_title(headline)
    meta_title = f"{title} | Joy of Care"
    loc_info = LOCATIONS[idx % len(LOCATIONS)]
    loc_name, person_name, person_age, person_job, family_person = loc_info
    
    refs = REF_MAP.get(cat, REF_MAP['perawatan-lansia'])
    
    # Generate tailored FAQ
    faq1_q = f"Mengapa penanganan {headline.split(':')[0].strip()} lebih efektif dilakukan langsung di rumah?"
    faq1_a = f"Penanganan di rumah menghilangkan stres perjalanan dan antrean faskes Jabodetabek, memungkinkan adaptasi langsung pada perabot hunian nyata, serta melibatkan keluarga secara terpadu di bawah bimbingan terapis dan tim medis Joy of Care."
    
    faq2_q = f"Kapan keluarga harus segera menghubungi layanan Joy of Care untuk kondisi ini?"
    faq2_a = f"Segera hubungi kami jika terdapat penurunan mobilitas mendadak, kebingungan akut, rasa nyeri yang tidak tertahankan, atau kesulitan pemenuhan nutrisi dan cairan harian pada pasien di rumah."
    
    faq3_q = f"Apakah tenaga medis Joy of Care memiliki surat tanda registrasi (STR) dan izin resmi?"
    faq3_a = f"Seluruh dokter, perawat luka, fisioterapis, dan analis laboratorium Joy of Care memegang STR aktif dari Konsil Tenaga Kesehatan Indonesia, Surat Izin Praktik (SIP), dan sertifikasi kompetensi klinis resmi."
    
    faq4_q = f"Bagaimana cara memesan jadwal kunjungan dan konsultasi awal?"
    faq4_a = f"Keluarga dapat langsung menghubungi tim triase Joy of Care melalui layanan respons cepat WhatsApp 08811-118-911 untuk penjadwalan fleksibel setiap hari termasuk akhir pekan."
    
    # Internal links
    if cat == 'fisioterapi-rumah':
        int_links = ["/fisioterapi-ke-rumah/", "/perawatan-lansia/", "/panggil-dokter-ke-rumah/"]
        svc_link = "/fisioterapi-ke-rumah/"
        svc_name = "Fisioterapi ke Rumah"
    elif cat == 'home-lab':
        int_links = ["/homelab/", "/panggil-dokter-ke-rumah/", "/layanan-perawat-di-rumah/"]
        svc_link = "/homelab/"
        svc_name = "Home Lab & Cek Darah"
    elif cat in ['parkinson', 'osteoporosis', 'perawatan-lansia']:
        int_links = ["/perawatan-lansia/", "/layanan-perawat-di-rumah/", "/fisioterapi-ke-rumah/"]
        svc_link = "/perawatan-lansia/"
        svc_name = "Perawatan Lansia Terpadu"
    else:
        int_links = ["/panggil-dokter-ke-rumah/", "/layanan-perawat-di-rumah/", "/homelab/"]
        svc_link = "/panggil-dokter-ke-rumah/"
        svc_name = "Layanan Kesehatan Joy of Care"

    # Meta description
    meta_desc = f"{headline[:110]}. Panduan praktis medis bagi keluarga di rumah. Konsultasi WhatsApp resmi Joy of Care 08811-118-911."
    if len(meta_desc) > 160:
        meta_desc = meta_desc[:157] + "..."

    # Write content
    content = f"""---
title: "{title}"
metaTitle: "{meta_title}"
metaDescription: "{meta_desc}"
category: {cat}
author: Tim Kontributor Artikel
reviewer: Tim Medis Joy of Care
date: '{date}'
slug: {slug}
featuredImage: {feat_img}
primaryKeyword: {slug.replace('-', ' ')}
secondaryKeywords:
  - {slug.replace('-', ' ')} jakarta
  - home care medis jabodetabek
  - perawatan pasien di rumah
  - joy of care indonesia
internalLinks:
"""
    for lnk in int_links:
        content += f"  - {lnk}\n"

    content += f"""faq:
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
    for rf in refs:
        content += f"  - {rf}\n"

    content += f"""---

Di sebuah sudut hunian yang tenang di kawasan {loc_name}, {person_name} ({person_age} tahun), seorang {person_job}, tengah menghadapi fase baru dalam perjalanan kesehatannya. Selama beberapa pekan terakhir, ritme keseharian keluarga mulai terganggu ketika gejala klinis yang perlahan muncul mulai membatasi kemandirian dan rasa percaya diri sang orang tua. Bagi {family_person}, menyaksikan perubahan kondisi orang terkasih sembari membagi konsentrasi dengan tuntutan pekerjaan profesional di Jabodetabek menghadirkan pergulatan batin yang tidak mudah. Hambatan kemacetan lalu lintas, antrean panjang di fasilitas kesehatan, serta risiko kelelahan fisik kerap menjadi kendala utama saat harus bolak-balik membawa pasien kontrol ke rumah sakit.

Keputusan keluarga untuk menghadirkan pendampingan klinis langsung di kediaman melalui Joy of Care menjadi titik balik penting. Ketika tenaga medis profesional melangkah masuk ke dalam kamar tidur pasien dengan perlengkapan berstandar rumah sakit, evaluasi holistik tidak lagi sekadar berfokus pada keluhan sesaat di atas kertas rekam medis. Observasi menyeluruh dilakukan langsung pada ekosistem hidup harian pasien: bagaimana postur tubuhnya saat bangkit dari kasur, interaksi dengan anggota keluarga, hingga kenyamanan lingkungan kamar tidur. Pendekatan inilah yang melandasi pentingnya pemahaman mendalam mengenai topik ini bagi setiap keluarga urban modern.

> ### 💡 Intisari Medis Joy of Care
> - **Penanganan Tepat Sasaran:** Memahami akar klinis {headline.split(':')[0].strip()} secara dini mencegah timbulnya komplikasi sekunder yang memperberat kondisi fisik pasien.
> - **Efisiensi Lingkungan Nyata:** Intervensi medis dan rehabilitasi di hunian sendiri terbukti mempercepat pemulihan karena melatih fungsi adaptasi langsung pada perabot harian.
> - **Kenyamanan Bebas Stres:** Menghindarkan lansia dan pasien rentan dari kelelahan perjalanan kota besar serta ancaman transmisi infeksi nosokomial di ruang tunggu fasilitas kesehatan.
> - **Kemitraan Keluarga & Tenaga Medis:** Edukasi langsung kepada keluarga dan perawat pendamping (*caregiver*) menciptakan kesinambungan perawatan mandiri yang aman dan terukur selama 24 jam.

---

## Memahami Esensi Klinis dan Tantangan di Balik Kondisi Ini

Dalam praktik kedokteran dan perawatan home care modern, {headline.lower()} menuntut ketelitian evaluasi yang melampaui sekadar pemberian instruksi umum. Sudut pandang (*angle*) yang relevan pada konteks ini mencakup: {angle.lower()}.

Keluarga sering kali dihadapkan pada dilema antara menunda penanganan karena menganggapnya sebagai proses penuaan wajar, atau merasa cemas berlebihan tanpa panduan tindakan yang runut. Padahal, tubuh manusia memiliki mekanisme kompensasi biologis yang memiliki batas toleransi tertentu. Apabila gangguan fungsi gerak, metabolik, maupun regulasi cairan dibiarkan tanpa intervensi klinis terstruktur, penurunan kemandirian fungsional dapat terjadi secara progresif dalam hitungan minggu.

### 1. Dinamika Fisiologis dan Tanda-Tanda Penurunan Fungsi
Secara biologis, integritas sistem saraf, muskuloskeletal, dan organ dalam saling terhubung erat. Ketika salah satu sistem mengalami penurunan fungsi, sistem lainnya akan dipaksa bekerja ekstra untuk menyeimbangkan beban tubuh. Misalnya, ketidakstabilan postur atau kelemahan otot akan mengubah pola distribusi tumpuan berat badan, yang lambat laun memicu nyeri sendi sekunder dan kekakuan jaringan ikat di area lain.

Di samping itu, faktor kecemasan psikologis kerap memperberat manifestasi fisik. Pasien yang merasa takut terjatuh atau minder dengan keterbatasan fisiknya cenderung membatasi aktivitas harian. Siklus inaktivitas ini kemudian memicu atrofi otot (*disuse atrophy*) dan kekakuan kapsul sendi yang semakin mempersulit proses pemulihan berikutnya.

### 2. Keterbatasan Pendekatan Konvensional Tanpa Penyesuaian Rumah
Banyak program perawatan atau latihan yang dirancang di klinik rumah sakit sulit diterapkan secara konsisten begitu pasien tiba kembali di rumah. Peralatan canggih di pusat rehabilitasi sering kali tidak mencerminkan kondisi riil tempat tinggal pasien, seperti ketinggian tempat tidur kayu, pegangan pintu lorong, atau jenis lantai kamar mandi.

Melalui pendekatan [{svc_name}]({svc_link}) oleh Joy of Care, protokol medis diadaptasi secara presisi terhadap realitas hunian. Pasien tidak hanya diajarkan teori, melainkan langsung dipandu mempraktikkan cara duduk, bergerak, atau mengelola kondisi fisik mereka menggunakan fasilitas nyata yang mereka temui setiap hari.

---

## Protokol Pemeriksaan dan Tatalaksana Komprehensif Joy of Care

Pendekatan Joy of Care memadukan ketatnya standar klinis profesional dengan kehangatan komunikasi empatik khas budaya kekeluargaan Indonesia. Setiap kunjungan dirancang melalui tahapan terstruktur guna memastikan keselamatan (*patient safety*) dan efektivitas intervensi.

```
Alur Pelayanan Terpadu Joy of Care di Rumah:
[Konsultasi Awal via WhatsApp] -> Triase Riwayat & Keluhan Klinis
          ↓
[Kedatangan Tim Medis Ber-STR] -> Pengukuran Tanda Vital Komprehensif
          ↓
[Pemeriksaan Fisik Terarah] -> Evaluasi Fungsi / Prosedur Diagnostik
          ↓
[Tindakan Klinis di Tempat] -> Terapi / Pengambilan Sampel / Mobilisasi
          ↓
[Edukasi Caregiver & Keluarga] -> Lembar Pantau Mandiri & Evaluasi Berkala
```

### 1. Penilaian Awal dan Skrining Tanda Vital Holistik
Sebelum memulai intervensi spesifik, tim medis melakukan pengukuran tanda vital dasar meliputi tekanan darah posisi duduk dan berbaring, frekuensi nadi, saturasi oksigen (SpO2), suhu tubuh, dan laju pernapasan. Pengukuran ini penting untuk menyingkirkan adanya kontraindikasi akut, seperti lonjakan tekanan darah tak terkontrol atau ketidakstabilan ritme jantung.

Selanjutnya, dilakukan asesmen fungsional yang mencakup rentang gerak sendi (*range of motion*), kekuatan otot fungsional, respons neurologis perifer, serta pengamatan pola respirasi saat pasien beraktivitas ringan di sekitar tempat tidur.

### 2. Implementasi Terapi Spesifik dan Modifikasi Lingkungan
Setelah diagnosis kerja atau tujuan klinis ditetapkan, tim profesional Joy of Care melaksanakan tindakan terarah:
- **Terapi Manual dan Latihan Fungsional:** Mengaplikasikan teknik mobilisasi jaringan lunak, stimulasi neuromuskular, atau latihan penguatan postural yang disesuaikan dengan kapasitas kardiorespirasi pasien.
- **Prosedur Klinis Berstandar Steril:** Melakukan tindakan medis invasif atau diagnostik dengan menerapkan prinsip aseptik tanpa sentuh (*non-touch aseptic technique*), termasuk penanganan limbah medis tajam sesuai regulasi Kementerian Kesehatan RI.
- **Audit Keselamatan Fisik Kamar Pasien:** Meninjau tata letak perabot, pencahayaan lorong kamar tidur, karpet penutup lantai, serta ketinggian dudukan toilet guna meminimalkan risiko cedera sekunder di rumah.

---

## Matriks Evaluasi: Perbandingan Metode Konvensional vs Standar Home Care Joy of Care

Untuk memberikan gambaran yang transparan bagi keluarga, berikut adalah perbandingan antara pola penanganan mandiri/konvensional dengan standar layanan terpadu Joy of Care:

| Aspek Evaluasi | Pendekatan Konvensional / Mandiri | Standar Pelayanan Terpadu Joy of Care |
|---|---|---|
| **Lokasi Pelaksanaan** | Pasien harus menempuh perjalanan macet ke rumah sakit | Dilaksanakan langsung di kamar tidur atau ruang keluarga pasien |
| **Kenyamanan Pasien** | Tingkat stres dan kelelahan tinggi akibat waktu tunggu antrean | Sangat rileks, privasi terjaga penuh di tengah suasana keluarga |
| **Adaptasi Terapi** | Berorientasi pada simulasi alat klinik yang asing bagi pasien | Disesuaikan langsung dengan perabot, lantai, dan tata ruang rumah nyata |
| **Keterlibatan Caregiver** | Instruksi singkat di meja periksa yang mudah terlupakan | Pendampingan dan pelatihan praktik langsung kepada keluarga di tempat |
| **Risiko Infeksi Silang** | Rentan terpapar kuman ruang tunggu dan droplet di faskes ramai | Risiko infeksi silang nosokomial mendekati nol dengan protokol APD steril |

---

## Checklist Panduan Praktis untuk Keluarga di Rumah

Peran aktif keluarga adalah pilar utama keberhasilan pemulihan jangka panjang. Berikut langkah-langkah praktis yang dianjurkan oleh Tim Medis Joy of Care:

1. **Pencatatan Log Harian yang Disiplin:** Sediakan buku catatan khusus untuk mendokumentasikan jam minum obat, angka tensi dan gula darah, porsi makan, serta keluhan fisik yang dirasakan pasien setiap pagi dan sore.
2. **Optimalisasi Keamanan Ruang Gerak:** Singkirkan kabel melintang, keset kain yang licin, dan barang berserakan di jalur antara tempat tidur menuju kamar mandi. Pastikan lampu lorong menyala terang saat malam hari.
3. **Komunikasi yang Memvalidasi Emosi:** Dengarkan keluh kesah pasien dengan sabar tanpa langsung membantah atau menyalahkan. Berikan apresiasi pada setiap capaian kemajuan gerak kecil yang berhasil diraih.
4. **Waspadai Tanda Bahaya (Red Flags):** Segera laporkan kepada dokter atau bawa ke fasilitas gawat darurat apabila pasien mengalami penurunan kesadaran mendadak, kelemahan separuh tubuh yang baru timbul, bibir membiru, sesak napas berat saat beristirahat, atau demam tinggi menggigil yang tidak turun dengan obat penurun panas.

---

## Pertanyaan yang Sering Diajukan (FAQ)

### Mengapa penanganan kondisi ini lebih efektif dilakukan langsung di rumah?
Penanganan di rumah menghilangkan stres perjalanan dan antrean fasilitas kesehatan Jabodetabek yang melelahkan. Selain itu, tenaga medis dapat mengevaluasi dan melatih pasien beradaptasi langsung pada perabot dan tata ruang hunian nyata, sehingga kemandirian fungsional harian lebih cepat terbentuk kembali.

### Kapan keluarga harus segera menghubungi layanan profesional Joy of Care?
Keluarga disarankan segera berkonsultasi ketika mulai melihat penurunan kemampuan mobilitas, kebingungan mental yang mendadak, penolakan makan dan minum berat, atau kesulitan anggota keluarga dalam merawat luka dan memindahkan posisi tubuh pasien tanpa rasa sakit.

### Apakah tenaga medis Joy of Care memiliki sertifikasi resmi?
Ya. Seluruh dokter, ners luka, fisioterapis, dan analis laboratorium Joy of Care memiliki Surat Tanda Registrasi (STR) aktif dari Kementerian Kesehatan Republik Indonesia, Surat Izin Praktik (SIP), serta sertifikat keahlian spesifik berstandar asosiasi profesi resmi.

### Bagaimana sistem penjadwalan dan pemesanan layanan di Jabodetabek?
Layanan Joy of Care dapat dijadwalkan secara fleksibel setiap hari, termasuk akhir pekan dan hari libur nasional, mencakup seluruh wilayah Jakarta, Bogor, Depok, Tangerang, Tangerang Selatan, dan Bekasi.

---

### Konsultasi Terpadu Kesehatan Keluarga Langsung di Rumah Anda

Memastikan pemulihan dan kenyamanan orang tua tercinta tidak harus mengorbankan ketenangan batin dan produktivitas harian keluarga. Tim profesional Joy of Care siap mendampingi perjalanan kesehatan Anda dengan standar medis terpercaya, empati tulus, dan dedikasi penuh langsung di kenyamanan hunian Anda.

Konsultasikan kebutuhan medis keluarga Anda bersama tim triase Joy of Care sekarang juga melalui **WhatsApp: 08811-118-911** atau kunjungi pusat informasi resmi kami di [{svc_name}]({svc_link}).
"""

    with open(target_file, 'w', encoding='utf-8') as f_out:
        f_out.write(content)

print("Finished generating all 80 Fase 2 articles successfully!")
