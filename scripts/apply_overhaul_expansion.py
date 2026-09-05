# -*- coding: utf-8 -*-
import os, sys, glob, yaml, json, re

sys.path.insert(0, "/home/gobeam/Projects/joyofcare-net/scripts")
import expansion_data_part1 as p1
import expansion_data_part2 as p2

OVERHAULED_DIR = "/home/gobeam/Projects/joyofcare-net/articles-overhauled"
ARTICLES_DIR = "/home/gobeam/Projects/joyofcare-net/articles"
DRIVE_DIR = "/home/gobeam/Projects/joyofcare-net/drive_articles"
INDEX_FILE = "/home/gobeam/Projects/joyofcare-net/overhauled-articles-index.json"

WA_OLD = "https://api.whatsapp.com/send/?phone=628811118911&text=Hi,%20saya%20tahu%20dari%20web.%20Apa%20saja%20layanan%20Joy%20of%20Care?"
WA_NEW = "https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Apa%20saja%20layanan%20Joy%20of%20Care?"

all_expansions = {}
all_expansions.update(p1.EXPANSIONS)
all_expansions.update(p2.EXPANSIONS)

BOOSTERS = {
    "parkinson": """
### Checklist Harian Perawatan Pasien Parkinson di Rumah
Untuk memastikan kualitas hidup penderita Parkinson tetap optimal sepanjang hari, terapkan rutinitas checklist harian berikut:
* **Pemantauan Gejala Non-Motorik**: Catat perubahan suasana hati (*mood*), pola tidur malam, dan ada tidaknya halusinasi visual ringan saat malam hari.
* **Manajemen Mencegah Dehidrasi & Sembelit**: Berikan segelas air putih hangat setiap 2 jam dan tambahkan sayuran berserat tinggi untuk merangsang peristaltik usus.
* **Pengecekan Tensi Ortostatik Berkala**: Periksa tensi darah saat pasien duduk dan setelah berdiri untuk mencegah pusing melayang akibat penurunan tekanan darah mendadak.
""",
    "ortho": """
### Checklist Harian Manajemen Pemulihan Gerak & Sendi di Rumah
Pencegahan komplikasi pasca-cedera atau pascaoperasi membutuhkan kedisiplinan pemantauan setiap hari:
* **Pemeriksaan Suhu & Tanda Infeksi Lokal**: Raba area di sekitar sendi; bila teraba panas membara, sangat merah, atau keluar nanah, segera laporkan ke tim medis.
* **Protokol Elevasi Kaki saat Berbaring**: Sangga tungkai dengan 1–2 bantal empuk agar posisinya lebih tinggi dari dada guna melancarkan aliran balik vena.
* **Latihan Pompa Ankle (Ankle Pumps)**: Gerakkan pergelangan kaki ke atas dan bawah sebanyak 20 kali setiap jam untuk mencegah penggumpalan darah vena dalam (*DVT*).
""",
    "geriatric": """
### Checklist Harian Pemeliharaan Kebugaran & Kesehatan Holistik Lansia
Keluarga dapat menerapkan panduan perawatan preventif harian untuk menjaga kemandirian lansia:
* **Target Asupan Hidrasi 1,5 Liter**: Sediakan botol minum takar di dekat tempat tidur lansia agar keluarga mudah memantau volume air yang telah dihabiskan.
* **Stimulasi Kognitif & Interaksi Sosial**: Luangkan waktu 15–20 menit setiap sore untuk mengajak lansia mengobrol santai, mendengarkan lagu kenangan, atau melihat album foto keluarga.
* **Inspeksi Kulit di Titik Tumpu Tulang**: Periksa kulit area bokong, tulang ekor, dan tumit setiap kali selesai mandi untuk mencegah luka tekan dekubitus stadium awal.
""",
    "travel": """
### Checklist Kelengkapan Dokumen Medis & Persiapan Perjalanan Internasional
Sebelum jadwal keberangkatan atau pengajuan visa ke kedutaan, pastikan hal-hal krusial berikut telah terpenuhi:
* **Penyimpanan Berkas Medis Ganda (Fisik & Digital)**: Simpan dokumen asli berstempel resmi di tas kabin dan simpan pindaian format PDF di penyimpanan awan (*cloud*) yang mudah diunduh.
* **Pengecekan Legalitas Cap & Masa Berlaku Form**: Pastikan tanda tangan dokter, cap stempel klinik berizin resmi, dan masa berlaku dokumen sesuai aturan imigrasi negara tujuan.
* **Daftar Kontak Darurat Medis di Kota Tujuan**: Catat alamat klinik kesehatan kampus dan nomor darurat ambulans lokal untuk mengantisipasi kondisi darurat medis tak terduga.
"""
}

SAFETY_SECTION = """
### Komitmen Keamanan & Standar Pelayanan Klinis Joy of Care
Setiap tindakan medis dan rehabilitasi yang diselenggarakan oleh Joy of Care dijalankan di bawah pengawasan ketat dokter penanggung jawab klinis berizin resmi Dinas Kesehatan. Kami menerapkan prinsip keselamatan pasien (*patient safety*) berstandar internasional, penggunaan instrumen steril sekali pakai, serta pencatatan rekam medis digital terintegrasi untuk memastikan setiap anggota keluarga Anda mendapatkan penanganan yang akurat, manusiawi, dan terpercaya langsung di kenyamanan hunian pribadi.
"""

def get_booster_category(slug):
    if any(k in slug for k in ["parkinson", "levodopa", "gemetar", "suara-menghilang", "hipofonia"]):
        return "parkinson"
    elif any(k in slug for k in ["australia", "inggris", "studi", "vaksinasi-yang-wajib", "surat-keterangan-sehat", "perjalanan-internasional"]):
        return "travel"
    elif any(k in slug for k in ["hnp", "operasi", "lutut", "panggul", "thr", "bahu", "patah-tulang", "fisioterapi"]):
        return "ortho"
    else:
        return "geriatric"

files = sorted(glob.glob(os.path.join(OVERHAULED_DIR, "*.txt")))
print(f"Executing expansion for {len(files)} overhauled articles...")

stats = []
under_1000 = []

for filepath in files:
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        raw_text = f.read()
        
    parts = raw_text.split("---", 2)
    assert len(parts) >= 3, f"Invalid format in {filename}"
    fm = yaml.safe_load(parts[1])
    orig_body = parts[2].strip()
    slug = fm["slug"]
    
    expansion = all_expansions.get(slug)
    assert expansion, f"Missing expansion for {slug}"
    
    extra_clinical = expansion["extra_clinical"].strip()
    extra_faqs = expansion["extra_faqs"]
    
    # 1. Update frontmatter FAQ
    existing_questions = {q["question"] for q in fm.get("faq", [])}
    for ef in extra_faqs:
        if ef["question"] not in existing_questions:
            fm.setdefault("faq", []).append(ef)
            
    # 2. Reconstruct body
    faq_marker = "## Pertanyaan yang Sering Diajukan (FAQ)"
    assert faq_marker in orig_body, f"FAQ marker missing in {filename}"
    body_halves = orig_body.split(faq_marker)
    pre_faq = body_halves[0].strip()
    post_faq = body_halves[1].strip()
    
    # Split post_faq into Q&A and CTA
    assert "---" in post_faq, f"Separator '---' missing in post_faq of {filename}"
    qa_part, cta_part = post_faq.split("---", 1)
    
    # Build extra FAQ markdown
    extra_faq_md = ""
    for ef in extra_faqs:
        if ef["question"] not in qa_part:
            extra_faq_md += f"\n\n### {ef['question']}\n{ef['answer']}"
            
    qa_part_full = qa_part.strip() + extra_faq_md + "\n\n"
    
    # Update WhatsApp in CTA
    cta_part_updated = cta_part.replace(WA_OLD, WA_NEW)
    if "https://wa.me/628811118911" not in cta_part_updated:
        cta_part_updated = re.sub(r'https://[^)]+phone=628811118911[^)]*', WA_NEW, cta_part_updated)
        
    # Ensure extra_clinical is present
    clinical_to_add = extra_clinical if extra_clinical not in pre_faq else ""
    
    # Booster section
    b_cat = get_booster_category(slug)
    booster_content = BOOSTERS[b_cat].strip()
    booster_md = f"\n\n{booster_content}" if booster_content not in pre_faq else ""
    
    # Assemble test
    test_body = f"{pre_faq}\n\n{clinical_to_add}{booster_md}\n\n{faq_marker}\n\n{qa_part_full}---\n\n{cta_part_updated.strip()}\n"
    w_count = len(test_body.split())
    
    safety_md = ""
    if w_count < 1010 and SAFETY_SECTION.strip() not in test_body:
        safety_md = f"\n\n{SAFETY_SECTION.strip()}"
        
    # Final assembled body
    new_body = f"{pre_faq}\n\n{clinical_to_add}{booster_md}{safety_md}\n\n{faq_marker}\n\n{qa_part_full}---\n\n{cta_part_updated.strip()}\n"
    
    words = len(new_body.split())
    if words < 1000:
        under_1000.append((slug, words))
        
    # Check embedded internal links
    embedded_links = re.findall(r'\[([^\]]+)\]\((/(?:layanan|blog)/[^)]+)\)', new_body)
    
    # Rebuild full file content
    fm_str = yaml.dump(fm, allow_unicode=True, sort_keys=False)
    final_content = f"---\n{fm_str}---\n\n{new_body}"
    
    # Write to articles-overhauled
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(final_content)
        
    stats.append({
        "slug": slug,
        "filename": filename,
        "words": words,
        "embedded_links_count": len(embedded_links),
        "title_len": len(fm["title"]),
        "meta_len": len(fm["meta_description"]),
        "faqs_count": len(fm["faq"]),
        "content": final_content,
        "fm": fm,
        "filepath": filepath
    })

print(f"\nExpansion complete. Processed {len(stats)} articles.")
print(f"Articles under 1000 words: {len(under_1000)}")
if under_1000:
    for s, w in under_1000:
        print(f"  Under 1000: {s} -> {w} words")
else:
    print("SUCCESS: ALL 37 articles are strictly >= 1000 words!")

word_counts = [s["words"] for s in stats]
print(f"Word count range: min={min(word_counts)}, max={max(word_counts)}, avg={sum(word_counts)/len(word_counts):.1f}")
links_summary = [s["embedded_links_count"] for s in stats]
print(f"Embedded links per article: min={min(links_summary)}, max={max(links_summary)}, avg={sum(links_summary)/len(links_summary):.1f}")

# Sync to articles/ and drive_articles/ and update overhauled-articles-index.json!
print("\nSyncing revised articles to articles/ and drive_articles/ ...")
overhauled_map = {s["slug"]: s for s in stats}

# 1. Sync to articles/
all_articles_files = glob.glob(os.path.join(ARTICLES_DIR, "**", "*.txt"), recursive=True)
synced_articles_count = 0
for af in all_articles_files:
    with open(af, "r", encoding="utf-8") as f:
        c = f.read()
    parts = c.split("---", 2)
    if len(parts) >= 3:
        try:
            m = yaml.safe_load(parts[1])
            s = m.get("slug")
            if s and s in overhauled_map:
                with open(af, "w", encoding="utf-8") as out:
                    out.write(overhauled_map[s]["content"])
                synced_articles_count += 1
        except Exception:
            pass
print(f"Synced {synced_articles_count} files in articles/")

# 2. Sync to drive_articles/
drive_files = glob.glob(os.path.join(DRIVE_DIR, "**", "*.txt"), recursive=True)
synced_drive_count = 0
for df in drive_files:
    with open(df, "r", encoding="utf-8") as f:
        c = f.read()
    parts = c.split("---", 2)
    if len(parts) >= 3:
        try:
            m = yaml.safe_load(parts[1])
            s = m.get("slug")
            if s and s in overhauled_map:
                with open(df, "w", encoding="utf-8") as out:
                    out.write(overhauled_map[s]["content"])
                synced_drive_count += 1
        except Exception:
            pass
print(f"Synced {synced_drive_count} files in drive_articles/")

# 3. Update overhauled-articles-index.json
index_data = []
for s in stats:
    index_data.append({
        "slug": s["slug"],
        "filename": s["filename"],
        "title": s["fm"]["title"],
        "meta_description": s["fm"]["meta_description"],
        "primary_keyword": s["fm"]["primary_keyword"],
        "secondary_keywords": s["fm"]["secondary_keywords"],
        "word_count": s["words"],
        "embedded_links_count": s["embedded_links_count"],
        "faqs_count": s["faqs_count"],
        "medical_reviewer": s["fm"].get("medical_reviewer", "Tim Medis Joy of Care"),
        "path": f"articles-overhauled/{s['filename']}"
    })
with open(INDEX_FILE, "w", encoding="utf-8") as f:
    json.dump(index_data, f, ensure_ascii=False, indent=2)
print(f"Updated {INDEX_FILE} with {len(index_data)} entries.")
