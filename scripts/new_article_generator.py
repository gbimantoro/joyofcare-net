# -*- coding: utf-8 -*-
import json, os, yaml

ARTICLES_NEW_DIR = "/home/gobeam/Projects/joyofcare-net/articles-new"
INDEX_FILE = "/home/gobeam/Projects/joyofcare-net/index-new-articles.json"
PROGRESS_FILE = "/home/gobeam/Projects/joyofcare-net/progress.md"

def format_new_article_file(article):
    fm_data = {
        "title": article["title"],
        "slug": article["slug"],
        "target_url": article.get("target_url", f"/blog/{article['slug']}"),
        "meta_description": article["meta_description"],
        "primary_keyword": article["primary_keyword"],
        "secondary_keywords": article["secondary_keywords"],
        "variation_type": article["variation_type"],
        "faq": article["faq"],
        "internal_links": article["internal_links"],
        "cta_text": article["cta_text"],
        "medical_reviewer": article.get("medical_reviewer", "Tim Medis Joy of Care (dr. Konsultan Geriatri & Dokter Umum Berizin Dinkes)"),
        "clinical_references": article.get("clinical_references", [])
    }
    fm_str = yaml.dump(fm_data, allow_unicode=True, sort_keys=False)
    output = f"---\n{fm_str}---\n\n{article['content'].strip()}\n"
    return output

def validate_new_article(article):
    title = article["title"]
    mdesc = article["meta_description"]
    slug = article["slug"]
    words = len(article["content"].split())
    
    assert 50 <= len(title) <= 60, f"[{slug}] Title length {len(title)} not in 50-60: '{title}'"
    assert 150 <= len(mdesc) <= 160, f"[{slug}] Meta desc length {len(mdesc)} not in 150-160: '{mdesc}'"
    assert len(article["faq"]) >= 3, f"[{slug}] FAQ count {len(article['faq'])} < 3"
    assert len(article["internal_links"]) >= 2, f"[{slug}] Internal links count < 2"
    assert len(article["secondary_keywords"]) >= 2, f"[{slug}] Secondary keywords count < 2"
    assert words >= 1000, f"[{slug}] Word count {words} < 1000 words requirement"
    assert "https://wa.me/628811118911" in article["content"], f"[{slug}] WhatsApp wa.me link missing"
    import re
    embedded_links = re.findall(r'\[([^\]]+)\]\((/(?:layanan|blog)/[^)]+)\)', article["content"])
    assert len(embedded_links) >= 3, f"[{slug}] Embedded internal links {len(embedded_links)} < 3"

def update_progress_file(all_articles):
    total = len(all_articles)
    pct = (total / 100.0) * 100.0
    
    # Group by keyword
    kw_groups = {}
    for a in all_articles:
        kw = a.get("primary_keyword", "Unknown")
        kw_groups.setdefault(kw, []).append(a)
        
    lines = [
        "# Progress Pelaksanaan: 100 Artikel Baru SEO-GEO-AIO Joy of Care",
        f"**Terakhir Diperbarui:** 5 September 2026",
        f"**Total Artikel Selesai:** {total} / 100 ({pct:.1f}%)",
        "",
        "## Ringkasan Eksekutif",
        "Pembuatan 100 artikel baru dirancang berbasis 20 kata kunci prioritas teratas dari riset kata kunci `keyword-research-top20.md`, di mana setiap kata kunci dikembangkan menjadi 5 variasi format konten:",
        "1. **Panduan Lengkap** (Pillar Content)",
        "2. **Tips & Cara** (Actionable Listicle)",
        "3. **Yang Perlu Anda Ketahui** (Awareness / Education)",
        "4. **Berapa Biaya / Perbandingan** (Cost / Comparison / Transactional)",
        "5. **Kapan Harus...** (Decision-Making Trigger)",
        "",
        "## Tabel Status Kata Kunci & Variasi Artikel",
        "",
        "| No | Kata Kunci Target | Prioritas | Variasi Dibuat | Status Batch | Kata/Artikel Rata-Rata |",
        "|---|---|:---:|:---:|:---:|:---:|"
    ]
    
    for idx, (kw, arts) in enumerate(kw_groups.items(), 1):
        vars_str = ", ".join([a.get("variation_type", "") for a in arts])
        avg_w = sum(len(a["content"].split()) for a in arts) // len(arts)
        status = "✅ Selesai (5/5)" if len(arts) == 5 else f"⏳ Berjalan ({len(arts)}/5)"
        lines.append(f"| {idx} | `{kw}` | Prioritas Tinggi | {vars_str} | {status} | {avg_w} kata |")
        
    lines.extend([
        "",
        "---",
        "*Dipantau secara berkala oleh JoC Writer.*"
    ])
    
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

def save_new_batch(batch_articles):
    os.makedirs(ARTICLES_NEW_DIR, exist_ok=True)
    
    # Load existing index
    current_index = []
    if os.path.exists(INDEX_FILE):
        try:
            with open(INDEX_FILE, "r", encoding="utf-8") as f:
                current_index = json.load(f)
        except Exception:
            current_index = []
            
    index_map = {item["slug"]: item for item in current_index}
    
    for art in batch_articles:
        validate_new_article(art)
        slug = art["slug"]
        file_content = format_new_article_file(art)
        
        filepath = os.path.join(ARTICLES_NEW_DIR, f"{slug}.txt")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(file_content)
            
        index_map[slug] = art
        print(f"Saved & validated new article: {slug} ({len(art['content'].split())} words)")
        
    sorted_index = [index_map[k] for k in sorted(index_map.keys())]
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted_index, f, ensure_ascii=False, indent=2)
        
    update_progress_file(sorted_index)
    print(f"Batch processed. Total new articles now: {len(sorted_index)} / 100")

if __name__ == "__main__":
    print("New article generator engine loaded.")
