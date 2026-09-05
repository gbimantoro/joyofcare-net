# -*- coding: utf-8 -*-
import json, os, yaml, glob

OVERHAULED_DIR = "/home/gobeam/Projects/joyofcare-net/articles-overhauled"
ARTICLES_DIR = "/home/gobeam/Projects/joyofcare-net/articles"
DRIVE_DIR = "/home/gobeam/Projects/joyofcare-net/drive_articles"
INDEX_FILE = "/home/gobeam/Projects/joyofcare-net/overhauled-articles-index.json"

DRIVE_MAPPING = {
    "bahaya-komplikasi-osteoporosis-dan-faktor-risiko-yang-wajib-diwaspadai-41": "bahaya-komplikasi-osteoporosis-dan-faktor-risiko-yang-wajib-.txt",
    "jenis-terapi-osteoporosis-lengkap-dari-obat-oral-injeksi-hingga-infus-40": "jenis-terapi-osteoporosis-lengkap-dari-obat-oral-injeksi-hin.txt",
    "layanan-terapi-infus-injeksi-osteoporosis-di-rumah-pasien-homecare-42": "layanan-terapi-infus-injeksi-osteoporosis-di-rumah-pasien-ho.txt",
    "panduan-fisioterapi-di-rumah-untuk-pasien-osteoporosis-mengurangi-nyeri-mencegah-jatuh-43": "panduan-fisioterapi-di-rumah-untuk-pasien-osteoporosis-mengu.txt"
}

def format_article_file(article):
    # Frontmatter format containing all required metadata
    fm_data = {
        "title": article["title"],
        "slug": article["slug"],
        "meta_description": article["meta_description"],
        "primary_keyword": article["primary_keyword"],
        "secondary_keywords": article["secondary_keywords"],
        "faq": article["faq"],
        "internal_links": article["internal_links"],
        "cta_text": article["cta_text"],
        "medical_reviewer": article.get("medical_reviewer", "Tim Medis Joy of Care (dr. Konsultan Geriatri & Dokter Umum Berizin Dinkes)"),
        "clinical_references": article.get("clinical_references", [])
    }
    fm_str = yaml.dump(fm_data, allow_unicode=True, sort_keys=False)
    output = f"---\n{fm_str}---\n\n{article['content'].strip()}\n"
    return output

def validate_article(article):
    title = article["title"]
    mdesc = article["meta_description"]
    slug = article["slug"]
    
    assert 50 <= len(title) <= 60, f"[{slug}] Title length {len(title)} not 50-60: '{title}'"
    assert 150 <= len(mdesc) <= 160, f"[{slug}] Meta desc length {len(mdesc)} not 150-160: '{mdesc}'"
    assert len(article["faq"]) >= 3, f"[{slug}] FAQ count {len(article['faq'])} < 3"
    assert len(article["internal_links"]) >= 2, f"[{slug}] Internal links count < 2"
    assert len(article["secondary_keywords"]) >= 2, f"[{slug}] Secondary keywords count < 2"
    assert len(article["content"].split()) >= 600, f"[{slug}] Content word count {len(article['content'].split())} < 600"

def save_articles(article_list):
    os.makedirs(OVERHAULED_DIR, exist_ok=True)
    
    # Load existing index if any
    current_index = []
    if os.path.exists(INDEX_FILE):
        try:
            with open(INDEX_FILE, "r", encoding="utf-8") as f:
                current_index = json.load(f)
        except Exception:
            current_index = []
            
    index_map = {item["slug"]: item for item in current_index}
    
    for art in article_list:
        validate_article(art)
        slug = art["slug"]
        file_content = format_article_file(art)
        
        # 1. Save to articles-overhauled/{slug}.txt
        overhauled_path = os.path.join(OVERHAULED_DIR, f"{slug}.txt")
        with open(overhauled_path, "w", encoding="utf-8") as f:
            f.write(file_content)
            
        # 2. Overwrite in articles/{slug}.txt
        article_path = os.path.join(ARTICLES_DIR, f"{slug}.txt")
        with open(article_path, "w", encoding="utf-8") as f:
            f.write(file_content)
            
        # 3. If it has a drive mapping, overwrite drive copy and articles/ copy of drive file
        if slug in DRIVE_MAPPING:
            drive_fname = DRIVE_MAPPING[slug]
            # drive_articles/ copy
            d_path = os.path.join(DRIVE_DIR, drive_fname)
            if os.path.exists(d_path):
                with open(d_path, "w", encoding="utf-8") as f:
                    f.write(file_content)
            # articles/ truncated copy
            a_d_path = os.path.join(ARTICLES_DIR, drive_fname)
            if os.path.exists(a_d_path):
                with open(a_d_path, "w", encoding="utf-8") as f:
                    f.write(file_content)
                    
        index_map[slug] = art
        print(f"Saved & validated: {slug} (words: {len(art['content'].split())})")

    # Write updated index
    sorted_index = [index_map[k] for k in sorted(index_map.keys())]
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted_index, f, ensure_ascii=False, indent=2)
        
    print(f"Total entries in {INDEX_FILE}: {len(sorted_index)}")

if __name__ == "__main__":
    print("Common writer module loaded.")
