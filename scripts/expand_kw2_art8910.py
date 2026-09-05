with open("scripts/kw2_stroke.py", "r", encoding="utf-8") as f:
    text = f.read()

# Expand Article 8
art8_extra = """
### Manajemen Waktu Produktif Keluarga & Efisiensi Energi Pasien
Salah satu kerugian terbesar dari terapi di klinik rumah sakit yang jarang diperhitungkan adalah fenomena 'stres antrean poliklinik'. Bagi keluarga pekerja di Jakarta, mendampingi orang tua berobat ke rumah sakit berarti mengorbankan setidaknya separuh hari kerja produktif (sekitar 4 hingga 5 jam untuk perjalanan, pendaftaran, antrean dokter, antrean kasir, hingga sesi fisioterapi). 

Sebaliknya, fisioterapi di rumah memungkinkan anggota keluarga tetap dapat bekerja dari rumah (*work from home*) atau beraktivitas normal sementara fisioterapis profesional membimbing pasien. Pasien juga menghemat energi tubuhnya 100% untuk fokus pada gerakan motorik murni di ranjang, bukan terkuras untuk menahan guncangan kendaraan di jalan raya.

### Pelaporan Rekam Medis & Koordinasi Multidisiplin Berkelanjutan
Di Joy of Care, setiap sesi fisioterapi rumahan dicatat secara digital. Terapis mendokumentasikan rentang gerak sendi (*Range of Motion*), kekuatan kontraksi otot (*Manual Muscle Testing - MMT*), serta skala spastisitas Ashworth. Laporan kemajuan klinis berkala ini dapat dibagikan kepada dokter spesialis saraf atau dokter rehabilitasi medik yang merawat pasien untuk sinkronisasi evaluasi terapi lanjutan.
"""
text = text.replace("## Analisis Efektivitas Klinis: Apa Kata Bukti Medis (*Evidence-Based*)?", art8_extra.strip() + "\n\n## Analisis Efektivitas Klinis: Apa Kata Bukti Medis (*Evidence-Based*)?", 1)

# Expand Article 9
art9_extra = """
### Protokol Stimulasi Sensorik Taktil untuk Mengatasi Baal dan Kebas Pascastroke
Selain kelemahan otot motorik, sekitar 60% penderita stroke mengalami gangguan sensorik berupa mati rasa, kebas, atau kesemutan pada separuh tubuh (*hemianesthesia*). Kondisi ini menyebabkan otak 'melupakan' keberadaan sisi tubuh yang sakit (*learned non-use*).

Fisioterapis Joy of Care menerapkan teknik stimulasi taktil terarah di rumah:
* **Desensitisasi Tekstur**: Mengusapkan berbagai tekstur berbeda (kain sutra halus, handuk katun kasar, spons cuci, hingga sikat lembut) pada telapak tangan dan lengan yang baal untuk membangunkan kembali reseptor sensorik kulit.
* **Diskriminasi Suhu Hangat dan Dingin**: Melatih pasien membedakan sentuhan kompres hangat dan kompres sejuk secara aman untuk mencegah cedera luka bakar saat mandi di rumah.
* **Pemberian Beban Kompresi Sendi (*Joint Approximation*)**: Memberikan tekanan lembut pada sendi bahu dan siku untuk mengirimkan umpan balik posisi (*proprioceptive feedback*) menuju korteks sensorik otak.
"""
text = text.replace("## 4 Alasan Mengapa Homecare Fisioterapi Menjadi Solusi Terbaik", art9_extra.strip() + "\n\n## 4 Alasan Mengapa Homecare Fisioterapi Menjadi Solusi Terbaik", 1)

# Expand Article 10
art10_extra = """
### Metrik Evaluasi Kemandirian Fungsional: Indeks Barthel (*Barthel Index*)
Untuk mengukur keberhasilan terapi secara kuantitatif dan ilmiah, tim fisioterapis Joy of Care menggunakan instrumen evaluasi *Barthel Index* yang mencakup 10 parameter kemandirian aktivitas hidup sehari-hari (ADL):
1. Kemampuan makan dan minum mandiri
2. Kemampuan berpindah dari tempat tidur ke kursi (*transfer*)
3. Kebersihan diri (mencuci muka, menyisir rambut, menyikat gigi)
4. Kemandirian buang air kecil (kontrol kandung kemih)
5. Kemandirian buang air besar (kontrol usus)
6. Kemampuan menggunakan kloset toilet secara aman
7. Kemampuan mandi sendiri
8. Kemampuan berjalan di permukaan datar minimal 50 meter
9. Kemampuan menaiki dan menuruni undakan tangga
10. Kemampuan memakai dan melepas pakaian

Setiap peningkatan skor Barthel Index merupakan bukti nyata bahwa sirkuit saraf otak pasien sedang mengalami pemulihan fungsional yang signifikan, memberikan harapan baru dan kebahagiaan bagi seluruh keluarga di rumah.
"""
text = text.replace("## Pertanyaan yang Sering Diajukan (FAQ)", art10_extra.strip() + "\n\n## Pertanyaan yang Sering Diajukan (FAQ)", 1)

with open("scripts/kw2_stroke.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Expansion applied to kw2 articles 8, 9, 10.")
