#!/usr/bin/env python3
"""Phase 2 / Task 2.1: Build read-only JSON inventory of net article .txt files.

Parse each articles-final-37/*.txt and articles-new-final-100/*.txt with a tolerant
line-prefix parser (PyYAML fails on the glued `---title:` and folded/multiline values).
Emit inventory.json with: slug, source dir, category, word count, md5.
"""
import json, re, hashlib, os

BASE = "/home/gobeam/Projects/joyofcare-net"
DIRS = ["articles-final-37", "articles-new-final-100"]
OUT = os.path.join(BASE, "scripts", "migration", "inventory.json")


def parse_simple(txt, key):
    """Return value for a top-level scalar key that appears at column 0 (key: ...)."""
    for line in txt.splitlines():
        m = re.match(rf"^{re.escape(key)}:\s*(.*)$", line)
        if m:
            v = m.group(1).strip()
            return v
    return None


def word_count(txt):
    return len(re.findall(r"\S+", txt))


def main():
    inventory = []
    for d in DIRS:
        dpath = os.path.join(BASE, d)
        for fn in sorted(os.listdir(dpath)):
            if not fn.endswith(".txt"):
                continue
            path = os.path.join(dpath, fn)
            with open(path, encoding="utf-8", errors="replace") as f:
                raw = f.read()
            slug = parse_simple(raw, "slug")
            category = parse_simple(raw, "category")
            wc = word_count(raw)
            md5 = hashlib.md5(raw.encode("utf-8")).hexdigest()
            inventory.append({
                "slug": slug,
                "source": d,
                "category": category,
                "word_count": wc,
                "md5": md5,
            })
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)
    # Report
    print(f"Total entries: {len(inventory)}")
    cats = {}
    for it in inventory:
        cats[it["category"]] = cats.get(it["category"], 0) + 1
    print("By category:")
    for c, n in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {c}: {n}")
    missing = [it for it in inventory if not it["slug"] or not it["category"]]
    print(f"Missing slug/category: {len(missing)}")


if __name__ == "__main__":
    main()