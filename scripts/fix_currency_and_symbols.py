import re

# 1. fisioterapi-untuk-lansia-menjaga-mobilitas-dan-keseimbangan-30.txt
f30 = 'articles-overhauled/fisioterapi-untuk-lansia-menjaga-mobilitas-dan-keseimbangan-30.txt'
with open(f30, 'r', encoding='utf-8') as f:
    c = f.read()
target30 = 'takut jatuh $\nightarrow$ membatasi gerak $\nightarrow$ otot semakin mengecil $\nightarrow$ risiko jatuh justru berlipat ganda.'
repl30 = 'takut jatuh -> membatasi gerak -> otot semakin mengecil -> risiko jatuh justru berlipat ganda.'
if target30 in c:
    c = c.replace(target30, repl30)
    with open(f30, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed f30")
else:
    print("f30 target not found")

# 2. perhatikan-persyaratan-tambahan-bagi-beberapa-jurusan-studi-di-australia-17.txt
f17 = 'articles-overhauled/perhatikan-persyaratan-tambahan-bagi-beberapa-jurusan-studi-di-australia-17.txt'
with open(f17, 'r', encoding='utf-8') as f:
    c = f.read()
if 'HBsAb $\\ge$ 10 mIU/mL' in c:
    c = c.replace('HBsAb $\\ge$ 10 mIU/mL', 'HBsAb ≥ 10 mIU/mL')
    with open(f17, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed f17")
else:
    print("f17 target not found")

# 3. vaksinasi-yang-wajib-dan-disarankan-untuk-studi-di-australia-16.txt
f16 = 'articles-overhauled/vaksinasi-yang-wajib-dan-disarankan-untuk-studi-di-australia-16.txt'
with open(f16, 'r', encoding='utf-8') as f:
    c = f.read()
if 'HBsAb kuantitatif $\\ge$ 10 mIU/mL' in c:
    c = c.replace('HBsAb kuantitatif $\\ge$ 10 mIU/mL', 'HBsAb kuantitatif ≥ 10 mIU/mL')
old_aud = "Biaya satu kali suntik vaksin di klinik Australia (misalnya Bupa Health Services atau GP Clinic) bisa mencapai $150 hingga $300 AUD per dosis di luar biaya konsultasi dokter ($80–$120 AUD). Di Indonesia, biayanya jauh lebih terjangkau."
new_aud = "Biaya satu kali suntik vaksin di klinik Australia (misalnya Bupa Health Services atau GP Clinic) relatif sangat mahal per dosis di luar biaya konsultasi dokter umum. Di Indonesia melalui layanan vaksinasi Joy of Care, biayanya jauh lebih hemat dan terjangkau."
if old_aud in c:
    c = c.replace(old_aud, new_aud)
with open(f16, 'w', encoding='utf-8') as f:
    f.write(c)
print("Fixed f16")

# 4. tips-kesehatan-untuk-mahasiswa-kuliah-di-luar-negeri-kapan-harus.txt
fkapan = 'articles-new/tips-kesehatan-untuk-mahasiswa-kuliah-di-luar-negeri-kapan-harus.txt'
with open(fkapan, 'r', encoding='utf-8') as f:
    c = f.read()
old_gigi = "Bila belum memiliki asuransi gigi tambahan, biaya penanganan darurat di klinik gigi luar negeri berkisar antara AUD $150–$300 hanya untuk pemeriksaan awal dan obat pereda nyeri. Inilah mengapa dokter Joy of Care selalu mewajibkan seluruh calon mahasiswa untuk melakukan pemeriksaan gigi komprehensif di Indonesia sebelum terbang."
new_gigi = "Bila belum memiliki asuransi gigi tambahan, biaya penanganan darurat di klinik gigi luar negeri sangat mahal hanya untuk pemeriksaan awal dan obat pereda nyeri. Inilah mengapa tim dokter Joy of Care selalu menyarankan seluruh calon mahasiswa untuk melakukan pemeriksaan gigi komprehensif di Indonesia sebelum keberangkatan."
if old_gigi in c:
    c = c.replace(old_gigi, new_gigi)
    with open(fkapan, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed fkapan")
else:
    print("fkapan target not found")
