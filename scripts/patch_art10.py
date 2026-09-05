with open("scripts/kw2_stroke.py", "r", encoding="utf-8") as f:
    text = f.read()

art10_extra = """
### Metrik Evaluasi Kemandirian Fungsional: Indeks Barthel (Barthel Index)
Untuk mengukur keberhasilan terapi secara kuantitatif dan ilmiah, tim fisioterapis Joy of Care menggunakan instrumen evaluasi *Barthel Index* yang mencakup 10 parameter kemandirian aktivitas hidup sehari-hari (ADL):
1. Kemampuan makan dan minum mandiri
2. Kemampuan berpindah dari tempat tidur ke kursi (*transfer*)
3. Kebersihan diri (mencuci muka, menyisir rambut, menyikat gigi)
4. Kemandirian buang air kecil (kontrol kandung kemih)
5. Kemandirian buang air besar (kontrol usus)
6. Kemampuan menggunakan kloset toilet secara aman
7. Kemampuan mandi sendiri di kamar mandi
8. Kemampuan berjalan di permukaan datar minimal 50 meter
9. Kemampuan menaiki dan menuruni undakan tangga
10. Kemampuan memakai dan melepas pakaian

Setiap peningkatan skor Barthel Index merupakan bukti nyata bahwa sirkuit saraf otak pasien sedang mengalami pemulihan fungsional yang signifikan, memberikan harapan baru dan kebahagiaan bagi seluruh keluarga di rumah.
"""

target_marker = "Pelajari panduan terstruktur langkah pemulihan pada [Panduan Lengkap Fisioterapi Pasca Stroke di Rumah](/blog/fisioterapi-pasca-stroke-di-rumah-panduan-lengkap)."
replacement = target_marker + "\n\n" + art10_extra.strip()

text = text.replace(target_marker, replacement)

with open("scripts/kw2_stroke.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Article 10 patched!")
