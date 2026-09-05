import os, yaml

with open("articles-overhauled/5-latihan-fisioterapi-untuk-mengatasi-nyeri-punggung-bawah-hnp-26.txt", "r", encoding="utf-8") as f:
    text = f.read()

parts = text.split("---", 2)
fm = yaml.safe_load(parts[1])
body = parts[2].strip()

# Check original word count
orig_words = len(body.split())
print(f"Original body words: {orig_words}")

extra_clinical = """
## Protokol Pencegahan Kekambuhan & Manajemen Ergonomi di Rumah

Untuk mencegah pergeseran bantalan sendi berulang, penderita HNP memerlukan modifikasi gaya hidup komprehensif. Tim fisioterapis kami selalu menekankan bahwa pemulihan sejati terjadi bukan hanya saat sesi terapi berlangsung, melainkan melalui disiplin menjaga postur tubuh selama 24 jam sehari di rumah.

### 1. Modifikasi Posisi Duduk dan Bekerja
Sebagian besar kasus HNP lumbal dipicu oleh tekanan intradiskal yang meningkat saat duduk membungkuk di depan komputer. Terapkan aturan ergonomi berikut:
* Gunakan kursi kerja dengan bantalan penopang kurva lumbal (*lumbar roll support*) yang mempertahankan lengkungan alami pinggang.
* Atur ketinggian kursi sehingga kedua telapak kaki menapak rata di lantai dan sudut lutut membentuk 90 hingga 100 derajat.
* Terapkan aturan *micro-break* setiap 30–45 menit: berdiri, regangkan kedua lengan ke atas, dan lakukan gerakan ekstensi punggung ringan. Pasien dapat memanfaatkan konsultasi bersama [layanan panggil dokter ke rumah](/layanan/panggil-dokter) untuk menilai apakah keluhan kesemutan saat duduk membutuhkan evaluasi neurologis lebih lanjut.

### 2. Teknik Mengangkat Beban yang Aman (Spine-Safe Lifting)
Jangan pernah membungkukkan pinggang saat mengambil benda di lantai. Selalu gunakan kekuatan otot paha dan bokong (*power lifter technique*): dekatkan benda ke dada, tekuk lutut, jaga punggung tetap tegak, lalu dorong dengan tumit untuk berdiri tegak. Program rehabilitasi komprehensif dari [Layanan Fisioterapi Homecare Joy of Care](/layanan/fisioterapi) melatih kembali memori motorik otot (*motor pattern re-education*) sehingga pasien tidak ragu bergerak dalam aktivitas sehari-hari.

### 3. Dukungan Perawatan Pasien Tirah Baring
Bagi pasien HNP derajat sedang hingga berat yang mengalami episode nyeri akut parah (*flare-up*) dan kesulitan beranjak dari tempat tidur, pendampingan dari [layanan perawat medis homecare](/layanan/perawat-homecare) sangat membantu dalam memposisikan tubuh secara berkala (*repositioning*), mengompres hangat area lumbal, dan memonitor asupan nutrisi serta hidrasi agar proses pemulihan jaringan saraf berjalan maksimal.
"""

extra_faqs = [
    {
        "question": "Apakah penderita saraf kejepit HNP disarankan memakai korset lumbal setiap hari?",
        "answer": "Korset lumbal penyangga hanya dianjurkan dipakai saat fase nyeri akut atau ketika harus bepergian dan beraktivitas berat. Penggunaan korset secara terus-menerus tanpa henti justru dapat menyebabkan otot-otot penopang pinggang (erector spinae dan transversus abdominis) mengalami pelemahan (atrofi) karena terlalu dimanjakan."
    },
    {
        "question": "Kapan penderita HNP harus mempertimbangkan tindakan operasi bedah saraf?",
        "answer": "Tindakan operasi biasanya hanya dipertimbangkan jika terapi fisioterapi konservatif terarah selama 6–8 minggu tidak memberikan perbaikan, atau jika muncul gejala darurat sindrom cauda equina (gangguan buang air dan kebas area panggul) serta penurunan kekuatan motorik kaki yang progresif."
    }
]

# Append extra FAQs to frontmatter
fm["faq"].extend(extra_faqs)

# Insert extra clinical before FAQ in body
faq_marker = "## Pertanyaan yang Sering Diajukan (FAQ)"
parts_body = body.split(faq_marker)
new_body = parts_body[0].strip() + "\n\n" + extra_clinical.strip() + "\n\n" + faq_marker + "\n\n"

# Add extra FAQ text into body
for q in extra_faqs:
    new_body += f"### {q['question']}\n{q['answer']}\n\n"

new_body += parts_body[1].split("---")[0].strip() + "\n\n---\n\n"

# CTA section with wa.me
cta_part = parts_body[1].split("---")[1].strip()
cta_part = cta_part.replace("https://api.whatsapp.com/send/?phone=628811118911&text=Hi,%20saya%20tahu%20dari%20web.%20Apa%20saja%20layanan%20Joy%20of%20Care?", "https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Apa%20saja%20layanan%20Joy%20of%20Care?")
new_body += cta_part + "\n"

new_words = len(new_body.split())
print(f"New body words: {new_words}")
import re
embedded_links = re.findall(r'\[([^\]]+)\]\((/layanan/[^)]+|/blog/[^)]+)\)', new_body)
print(f"Embedded internal links ({len(embedded_links)}):", embedded_links)
print("WhatsApp wa.me present:", "https://wa.me/628811118911" in new_body)

