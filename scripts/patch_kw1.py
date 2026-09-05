with open("scripts/build_kw1_1000w.py", "r", encoding="utf-8") as f:
    text = f.read()

# Add extra paragraph to Article 3
art3_addition = """
### Peran Edukasi Dokter bagi Caregiver Keluarga di Rumah
Dalam kunjungan medis rumahan, dokter tidak hanya memeriksa pasien, melainkan juga bertindak sebagai pendidik klinis bagi keluarga. Dokter melatih caregiver cara memposisikan lansia agar tidak tersedak, cara mengenali fluktuasi saturasi oksigen, serta cara membuat catatan harian tanda vital yang akurat. Edukasi langsung ini memberikan rasa tenang dan memperkuat kesiapan mental keluarga dalam merawat orang tua sakit.
"""

old_art3_marker = "## Kapan Layanan Ini Menjadi Pilihan Paling Tepat?"
new_art3_replacement = art3_addition.strip() + "\n\n## Kapan Layanan Ini Menjadi Pilihan Paling Tepat?"
text = text.replace(old_art3_marker, new_art3_replacement, 1)

# Add extra paragraph to Article 4
art4_addition = """
### Transparansi Rincian Resep Obat dan Alur Klaim Asuransi
Seluruh resep obat yang diterbitkan dokter Joy of Care menggunakan formularium resmi yang transparan. Pasien dan keluarga berhak memilih antara obat generik berkualitas atau obat paten sesuai anggaran. Bagi pemegang asuransi swasta dengan fasilitas reimbursement, dokter kami akan melengkapi resume medis, tanda tangan, dan cap klinik resmi pada lembar klaim rawat jalan tanpa biaya administrasi tambahan.
"""
old_art4_marker = "## Tips Memaksimalkan Biaya Layanan Home Visit"
new_art4_replacement = art4_addition.strip() + "\n\n## Tips Memaksimalkan Biaya Layanan Home Visit"
text = text.replace(old_art4_marker, new_art4_replacement, 1)

# Add extra paragraph to Article 5
art5_addition = """
### Evaluasi Menyeluruh Polifarmasi pada Pasien Geriatri
Sering kali penurunan kondisi fisik lansia di rumah bukan disebabkan oleh penyakit baru, melainkan akibat efek samping interaksi obat jamak (*polypharmacy*). Dokter kunjungan rumah melakukan audit obat komprehensif, memeriksa tanggal kedaluwarsa obat di kotak obat pasien, serta menyederhanakan jadwal minum obat agar tidak membebani fungsi ginjal dan hati lansia.
"""
old_art5_marker = "## ⚠️ Kapan Pasien TIDAK Boleh Menunggu Dokter dan WAJIB Langsung ke IGD?"
new_art5_replacement = art5_addition.strip() + "\n\n## ⚠️ Kapan Pasien TIDAK Boleh Menunggu Dokter dan WAJIB Langsung ke IGD?"
text = text.replace(old_art5_marker, new_art5_replacement, 1)

with open("scripts/build_kw1_1000w.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Patch applied to kw1 script.")
