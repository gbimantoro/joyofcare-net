import os, glob, yaml

# Let's inspect the exact layout of one article before designing the full expansion
with open("articles-overhauled/5-latihan-fisioterapi-untuk-mengatasi-nyeri-punggung-bawah-hnp-26.txt", "r", encoding="utf-8") as f:
    text = f.read()

parts = text.split("---", 2)
fm = yaml.safe_load(parts[1])
body = parts[2]
print("Slug:", fm["slug"])
print("Original words:", len(body.split()))
print("Internal links in fm:", fm.get("internal_links"))
