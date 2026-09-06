#!/usr/bin/env python3
"""Phase 2 / Task 2.2: Build dedupe & canonical map from inventory vs existing MDX."""
import json, os

NET = "/home/gobeam/Projects/joyofcare-net"
WEB = "/home/gobeam/Projects/joyofcare-web"
inventory = json.load(open(os.path.join(NET, "scripts", "migration", "inventory.json")))
net_slugs = set(it["slug"] for it in inventory)

mdx_dir = os.path.join(WEB, "src", "content", "articles")
mdx_files = set(f[:-4] for f in os.listdir(mdx_dir) if f.endswith(".mdx"))

# Old / truncated / standalone pre-rewrite duplicates in MDX not in net canonical set
delete = sorted(mdx_files - net_slugs)

# Every net canonical slug is the final target
final = sorted(net_slugs)

canonical_map = {
    "DELETE_ARCHIVE": delete,
    "FINAL_SET": final,
    "NOTES": {
        "panduan-fisioterapi-osteoporosis": "pre-rewrite standalone duplicate of -43 family; archive",
        "bahaya-komplikasi-osteoporosis-dan-faktor-risiko-yang-wajib-": "truncated pre-rewrite dup of ...-wajib-diwaspadai-41; archive",
        "jenis-terapi-osteoporosis-lengkap-dari-obat-oral-injeksi-hin": "truncated pre-rewrite dup of ...-injeksi-hingga-infus-40; archive",
        "layanan-terapi-infus-injeksi-osteoporosis-di-rumah-pasien-ho": "truncated pre-rewrite dup of ...-pasien-homecare-42; archive",
        "panduan-fisioterapi-di-rumah-untuk-pasien-osteoporosis-mengu": "truncated pre-rewrite dup of ...-mengurangi-nyeri-mencegah-jatuh-43; archive",
    },
    "vaksinasi_-12_vs_-28": {
        "decision": "KEEP BOTH",
        "reason": "distinct articles, 17% 6-gram overlap (<60%), both ~1050 words",
    },
}

out = os.path.join(NET, "scripts", "migration", "canonical-map.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(canonical_map, f, ensure_ascii=False, indent=2)

print(f"DELETE_ARCHIVE ({len(delete)}):")
for d in delete: print("   ", d)
print(f"\nFINAL_SET count: {len(final)}")
# uniqueness check
assert len(final) == len(set(final)), "duplicate final slugs!"
print("Final set has no duplicate slugs: OK")