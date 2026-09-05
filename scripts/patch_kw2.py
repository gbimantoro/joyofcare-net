with open("scripts/kw2_stroke.py", "r", encoding="utf-8") as f:
    text = f.read()

# Fix save_new_batch call to run under if __name__ == "__main__":
text = text.replace("save_new_batch(articles)", 'if __name__ == "__main__":\n    save_new_batch(articles)')

# Add clinical paragraph to Article 6 (was 990 words)
art6_add = """
### Peran Kognitif dan Motivasi Psikologis dalam Neurorehabilitasi
Pemulihan pasca stroke bukan semata-mata latihan fisik mekanis, melainkan sangat dipengaruhi oleh kesiapan mental dan motivasi pasien. Sekitar 30–40% pasien stroke mengalami depresi pascastroke (*post-stroke depression*) yang menghambat partisipasi aktif. Fisioterapis Joy of Care memadukan stimulasi gerak dengan pendekatan psikologis suportif, memberikan apresiasi pada setiap pencapaian kecil, serta mengedukasi keluarga untuk menciptakan atmosfer rumah yang penuh optimisme dan kasih sayang.
"""
marker6 = "## Pertanyaan yang Sering Diajukan (FAQ)"
text = text.replace(marker6, art6_add.strip() + "\n\n" + marker6, 1)

with open("scripts/kw2_stroke.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Patch applied to kw2.")
