import os, sys, re, json, yaml

PRIMARY_CTA = "Hubungi WhatsApp JoC untuk informasi harga: https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Berapa%20biaya%20layanan%20Joy%20of%20Care?"
PRIMARY_URL = "https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Berapa%20biaya%20layanan%20Joy%20of%20Care?"
PRIMARY_LABEL = "Hubungi WhatsApp JoC untuk informasi harga"

ALTERNATE_CTA = "Konsultasi Dokter Gratis via WhatsApp: https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Mau%20konsultasi%20gratis%20dengan%20dokter"
ALTERNATE_URL = "https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Mau%20konsultasi%20gratis%20dengan%20dokter"
ALTERNATE_LABEL = "Konsultasi Dokter Gratis via WhatsApp"

LEGACY_URL = "https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Apa%20saja%20layanan%20Joy%20of%20Care?"

import scripts.price_overhaul_engine as poe
import scripts.patch_price_engine as ppe

# Update poe.HANDLERS with patches
poe.HANDLERS.update(ppe.PATCHES)

NET_OVERHAULED_DIR = "/home/gobeam/Projects/joyofcare-net/articles-overhauled"
NET_NEW_DIR = "/home/gobeam/Projects/joyofcare-net/articles-new"
WEB_BLOG_DIR = "/home/gobeam/Projects/joyofcare-web/pages/blog"
OVERHAULED_INDEX_PATH = "/home/gobeam/Projects/joyofcare-net/overhauled-articles-index.json"
NEW_INDEX_PATH = "/home/gobeam/Projects/joyofcare-net/index-new-articles.json"

price_regex = re.compile(r'Rp[\s\.]*\d+')
currency_regex = re.compile(r'\b(?:USD|AUD|GBP|EUR|\$|\£)\s*[\d\.,]+')

print("Starting Master Price Removal and CTA Overhaul...")

# 1. Gather all files in net
overhauled_files = sorted([f for f in os.listdir(NET_OVERHAULED_DIR) if f.endswith('.txt')])
new_files = sorted([f for f in os.listdir(NET_NEW_DIR) if f.endswith('.txt')])

print(f"Found {len(overhauled_files)} overhauled articles and {len(new_files)} new articles.")
total_articles = len(overhauled_files) + len(new_files)
assert total_articles == 137, f"Expected 137 articles, found {total_articles}"

# Combine all 137 articles in a deterministic order for alternating CTAs
# We sort all filenames together
all_article_items = []
for f in overhauled_files:
    all_article_items.append((f, 'articles-overhauled', os.path.join(NET_OVERHAULED_DIR, f)))
for f in new_files:
    all_article_items.append((f, 'articles-new', os.path.join(NET_NEW_DIR, f)))

all_article_items.sort(key=lambda x: x[0])

processed_contents = {}

for idx, (fname, dname, fpath) in enumerate(all_article_items):
    with open(fpath, 'r', encoding='utf-8') as fl:
        content = fl.read()

    # Step A: Apply price overhaul handler if applicable
    if fname in poe.HANDLERS:
        handler_func, _ = poe.HANDLERS[fname]
        content = handler_func(content)

    # Step B: Determine rotated CTA
    # Even idx -> Primary CTA, Odd idx -> Alternate CTA
    if idx % 2 == 0:
        assigned_cta = PRIMARY_CTA
        assigned_url = PRIMARY_URL
        assigned_label = PRIMARY_LABEL
    else:
        assigned_cta = ALTERNATE_CTA
        assigned_url = ALTERNATE_URL
        assigned_label = ALTERNATE_LABEL

    # Step C: Replace legacy WhatsApp links with assigned CTA URL
    content = content.replace(LEGACY_URL, assigned_url)

    # Step D: Update the end-of-article WhatsApp CTA line
    # Match various formats of:
    # 📲 **Hubungi WhatsApp Resmi Joy of Care**: [Chat WhatsApp 08811-118-911](...)
    # or similar
    end_cta_pattern = r'📲 \*\*Hubungi WhatsApp Resmi Joy of Care\*\*:.*'
    replacement_end_cta = f'📲 **Hubungi WhatsApp Resmi Joy of Care**: [{assigned_label}]({assigned_url})'
    
    if re.search(end_cta_pattern, content):
        content = re.sub(end_cta_pattern, replacement_end_cta, content)
    else:
        # If not present in exact format, ensure it's appended cleanly
        content = content.rstrip() + f'\n\n📲 **Hubungi WhatsApp Resmi Joy of Care**: [{assigned_label}]({assigned_url})\n'

    # Step E: Update cta_text in frontmatter if present
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            if 'cta_text:' in fm_text:
                fm_text = re.sub(r'cta_text:.*', f'cta_text: {assigned_label}', fm_text)
                content = f'---{fm_text}---{parts[2]}'

    # Step F: Validate zero prices and word count >= 1000
    p_matches = price_regex.findall(content)
    c_matches = currency_regex.findall(content)
    wc = len(content.split())

    if p_matches:
        raise ValueError(f"[{fname}] Still contains Rp prices: {p_matches}")
    if c_matches:
        raise ValueError(f"[{fname}] Still contains currency: {c_matches}")
    if wc < 1000:
        raise ValueError(f"[{fname}] Word count too low: {wc} words")

    processed_contents[fname] = (content, fpath, dname, wc)

print(f"Validation successful for all {len(processed_contents)} articles in memory!")

# Write all updated files back to disk in joyofcare-net
for fname, (content, fpath, dname, wc) in processed_contents.items():
    with open(fpath, 'w', encoding='utf-8') as fl:
        fl.write(content)

print("Saved all 137 articles to joyofcare-net directories.")

# Synchronize to joyofcare-web/pages/blog
synced_count = 0
for root, dirs, files in os.walk(WEB_BLOG_DIR):
    for f in files:
        if f in processed_contents:
            target_path = os.path.join(root, f)
            content, _, _, _ = processed_contents[f]
            with open(target_path, 'w', encoding='utf-8') as fl:
                fl.write(content)
            synced_count += 1

print(f"Synchronized {synced_count} files in {WEB_BLOG_DIR}.")

# Audit web_blog for any remaining prices
web_errors = []
for root, dirs, files in os.walk(WEB_BLOG_DIR):
    for f in files:
        if f.endswith('.txt'):
            target_path = os.path.join(root, f)
            with open(target_path, 'r', encoding='utf-8') as fl:
                c = fl.read()
            p_matches = price_regex.findall(c)
            c_matches = currency_regex.findall(c)
            if p_matches or c_matches:
                web_errors.append((target_path, p_matches, c_matches))

if web_errors:
    print(f"WARNING: {len(web_errors)} files in web_blog still have prices:")
    for w_err in web_errors:
        print("  ", w_err)
    raise ValueError("Web blog audit failed!")
else:
    print("SUCCESS: Zero prices found across all .txt files in joyofcare-web/pages/blog!")

# Update overhauled-articles-index.json
if os.path.exists(OVERHAULED_INDEX_PATH):
    with open(OVERHAULED_INDEX_PATH, 'r', encoding='utf-8') as fl:
        overhauled_idx = json.load(fl)
    for entry in overhauled_idx:
        fname = entry.get('filename')
        if fname in processed_contents:
            _, _, _, wc = processed_contents[fname]
            entry['word_count'] = wc
    with open(OVERHAULED_INDEX_PATH, 'w', encoding='utf-8') as fl:
        json.dump(overhauled_idx, fl, indent=2, ensure_ascii=False)
    print("Updated overhauled-articles-index.json.")

# Update index-new-articles.json
if os.path.exists(NEW_INDEX_PATH):
    with open(NEW_INDEX_PATH, 'r', encoding='utf-8') as fl:
        new_idx = json.load(fl)
    for entry in new_idx:
        slug = entry.get('slug')
        fname = f"{slug}.txt"
        if fname in processed_contents:
            content, _, _, _ = processed_contents[fname]
            # extract body content without frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                body = parts[2].strip() if len(parts) >= 3 else content
            else:
                body = content
            entry['content'] = body
    with open(NEW_INDEX_PATH, 'w', encoding='utf-8') as fl:
        json.dump(new_idx, fl, indent=2, ensure_ascii=False)
    print("Updated index-new-articles.json.")

print("All steps completed successfully!")
