with open("scripts/build_kw1_1000w.py", "r", encoding="utf-8") as f:
    text = f.read()

# Expand Article 4 further
art4_extra = """
### Simulasi Penghematan Finansial Jangka Panjang bagi Keluarga
Bagi keluarga dengan anggota lansia penderita penyakit degeneratif (seperti pasca-stroke atau demensia), rutinitas berobat ke poliklinik rumah sakit setiap 2 minggu sekali menimbulkan beban biaya tersembunyi yang sangat besar. Selain ongkos sewa kendaraan khusus atau ambulans penjemputan berkisar Rp 400.000–800.000 per perjalanan, ada biaya kehilangan jam kerja produktif anak yang mendampingi mengantre berjam-jam. Dengan memanggil dokter ke rumah, seluruh proses pemeriksaan, evaluasi obat, hingga pengambilan sampel darah selesai dalam 1 jam di ranjang pasien, memberikan penghematan biaya total hingga 40-50% per bulan.
"""

marker4 = "## Tips Memaksimalkan Biaya Layanan Home Visit"
text = text.replace(marker4, art4_extra.strip() + "\n\n## Tips Memaksimalkan Biaya Layanan Home Visit", 1)

# Expand Article 5 further
art5_extra = """
### Deteksi Dini Tanda Dekompensasi Klinis Lansia di Rumah
Sering kali penurunan kondisi kesehatan orang tua lansia tidak diawali dengan keluhan dramatis, melainkan perubahan halus seperti mendadak tidur lebih lama dari biasanya, menolak minum air putih, atau tatapan mata kosong. Dokter kunjungan rumah dilatih khusus untuk mendeteksi tanda-tanda dekompensasi klinis geriatri (seperti infeksi saluran kemih tersembunyi, dehidrasi subklinis, atau retensi sputum) sebelum berkembang menjadi sepsis atau syok yang mengancam nyawa.
"""
marker5 = "## 5 Kondisi Utama yang Tepat Memanggil Dokter ke Rumah"
text = text.replace(marker5, "## 5 Kondisi Utama yang Tepat Memanggil Dokter ke Rumah\n\n" + art5_extra.strip(), 1)

with open("scripts/build_kw1_1000w.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Patch 2 applied.")
