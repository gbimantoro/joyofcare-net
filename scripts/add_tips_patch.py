with open('scripts/patch_price_engine.py', 'r', encoding='utf-8') as f:
    code = f.read()

new_func = '''def h_tips_mahasiswa_biaya_perbandingan(text):
    old_row = "| **Estimasi Biaya Tahunan** | AUD $600 – $800 per tahun (~Rp 6–8 juta) | GBP £776 per tahun (~Rp 15–16 juta) | USD $2.000 – $4.000 per tahun (~Rp 32–64 juta) |"
    new_row = "| **Estimasi Biaya Tahunan** | Sesuai regulasi resmi premi OSHC Australia | Sesuai tarif wajib retribusi IHS visa UK | Premi tahunan student health plan universitas |"
    text = text.replace(old_row, new_row)
    text = text.replace(
        "Pembayaran *copayment* (USD $20–50) + *deductible* tahunan",
        "Pembayaran *copayment* terjangkau + pemenuhan *deductible* tahunan"
    )
    text = text.replace(
        "Namun, banyak dokter swasta mematok tarif konsultasi di atas tarif MBS (misalnya tarif MBS AUD $40, namun dokter mematok AUD $75). Selisih AUD $35 inilah yang disebut *gap fee* dan wajib dibayar langsung oleh mahasiswa dari kantong pribadi. Carilah klinik yang menerapkan sistem *bulk billing* untuk mahasiswa agar bebas dari gap fee.",
        f"Namun, beberapa dokter swasta mematok tarif konsultasi di atas batas standar MBS. Selisih biaya inilah yang disebut *gap fee* dan wajib dibayar langsung oleh mahasiswa dari kantong pribadi. Carilah klinik yang menerapkan sistem *bulk billing* khusus mahasiswa agar bebas dari biaya selisih tersebut. {PRIMARY_CTA}"
    )
    text = text.replace(
        "* **Deductible**: Jumlah biaya pengobatan yang wajib Anda bayar sendiri sebelum perusahaan asuransi mulai menanggung biaya. Misalnya deductible USD $500: Anda harus membayar USD $500 pertama dari biaya perawatan Anda dalam setahun.",
        "* **Deductible**: Batas akumulasi nominal pengobatan yang wajib Anda bayar mandiri sebelum perusahaan asuransi mulai menanggung biaya tanggungan medis dalam satu periode tahunan polis asuransi."
    )
    text = text.replace(
        "* **Copayment (Copay)**: Biaya tetap yang wajib Anda bayar setiap kali berkunjung ke dokter (biasanya USD $20 hingga $40 per kunjungan), sementara sisa tagihan ditanggung oleh asuransi.",
        "* **Copayment (Copay)**: Biaya partisipasi bernominal tetap yang wajib dibayar pasien setiap kali berkonsultasi dengan dokter faskes, sementara sisa porsi tagihan medis ditanggung oleh pihak asuransi."
    )
    return text
'''

code = new_func + '\n' + code
code = code.replace(
    "'vaksin-di-rumah-jakarta-lansia-panduan-lengkap.txt': (h_vaksin_lansia_panduan_lengkap, 'articles-new'),",
    "'vaksin-di-rumah-jakarta-lansia-panduan-lengkap.txt': (h_vaksin_lansia_panduan_lengkap, 'articles-new'),\n    'tips-kesehatan-untuk-mahasiswa-kuliah-di-luar-negeri-biaya-dan-perbandingan.txt': (h_tips_mahasiswa_biaya_perbandingan, 'articles-new'),"
)

with open('scripts/patch_price_engine.py', 'w', encoding='utf-8') as f:
    f.write(code)
print("Updated patch_price_engine.py with tips_mahasiswa patch!")
