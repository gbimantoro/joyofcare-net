#!/usr/bin/env python3
"""Phase 3 / Task 3.1: Migrate net article .txt -> clean MDX.

Tolerant parser handles glued `---title:`, folded/multiline values, empty+unindented
`cta_text:` continuation, and HTML-corrupted list blocks. Omits malformed optional
fields (keeps frontmatter valid) and emits YAML via yaml.dump (guaranteed valid).
Writes to joyofcare-web/src/content/articles/<slug>.mdx.
"""
import json, os, re, sys, yaml

NET = "/home/gobeam/Projects/joyofcare-net"
WEB = "/home/gobeam/Projects/joyofcare-web"
SRC_DIRS = ["articles-final-37", "articles-new-final-100"]
OUT_DIR = os.path.join(WEB, "src", "content", "articles")
DRY = "--dry-run" in sys.argv

# Category label per slug (for clean title building / metaTitle)
CAT_LABEL = {
    "perawatan-lansia": "Perawatan Lansia", "fisioterapi-rumah": "Fisioterapi Rumah",
    "panggil-dokter": "Panggil Dokter", "parkinson": "Parkinson",
    "studi-luar-negeri": "Studi Luar Negeri", "osteoporosis": "Osteoporosis",
    "antar-jemput-rs": "Antar Jemput RS", "vaksinasi-rumah": "Vaksinasi Rumah",
    "infus-vitamin": "Infus Vitamin", "perawat-homecare": "Perawat Homecare",
    "kesehatan-umum": "Kesehatan Umum", "home-lab": "Home Lab",
}


def split_frontmatter(raw):
    """Return (frontmatter_lines, body_text, body_line_index)."""
    lines = raw.split("\n")
    fm = []
    # line 0: glued `---title:` -> strip leading `---`
    if lines and lines[0].startswith("---"):
        fm.append(lines[0][3:])
    else:
        fm.append(lines[0])
    body_start = None
    for i in range(1, len(lines)):
        if lines[i] == "---":
            body_start = i + 1
            break
        fm.append(lines[i])
    if body_start is None:
        body_start = len(lines)
    return fm, "\n".join(lines[body_start:]), body_start


def clean_title(t):
    t = t.strip()
    # strip surrounding quote chars (single/double) repeated
    while len(t) >= 2 and t[0] in "'\"" and t[-1] in "'\"":
        t = t[1:-1].strip()
    t = re.sub(r"\s*\|\s*Joy of Care\s*$", "", t)
    return t.strip()


def parse_frontmatter(fm_lines):
    """Parse known scalar + list fields with tolerant handling."""
    fm = {"faq": [], "secondary_keywords": [], "internal_links": [], "clinical_references": []}
    cur_key = None
    pending_value = []  # folded continuation lines for current scalar
    # current structured list (faq/internal_links) being filled
    cur_list = None
    # current FAQ entry being built: dict with question/answer
    cur_faq = None

    def flush_scalar():
        if cur_key and cur_key in ("title", "meta_description", "primary_keyword",
                                   "slug", "category", "author", "reviewer",
                                   "target_url", "variation_type"):
            v = " ".join(x.strip() for x in pending_value).strip()
            fm[cur_key] = v
        elif cur_key == "cta_text":
            pass  # drop
        pending_value.clear()

    # top-level line regex: 'key:' or 'key: value'  (no leading whitespace)
    key_re = re.compile(r"^([A-Za-z_]+):\s*(.*)$")

    for ln in fm_lines:
        if not ln.strip():
            continue
        if ln.startswith("- "):
            flush_scalar()
            item = ln[2:].strip()
            m = re.match(r"^(question|answer|anchor|url|label):\s*(.*)$", item)
            if m:
                k, v = m.group(1), m.group(2)
                if cur_list is None:
                    cur_list = []
                # FAQ grouping
                if cur_list is fm["faq"]:
                    if k == "question":
                        cur_faq = {"question": v, "answer": ""}
                        cur_list.append(cur_faq)
                    elif k == "answer" and cur_faq is not None:
                        cur_faq["answer"] = v
                    continue
                # internal_links grouping by anchor
                if cur_list is fm["internal_links"]:
                    cur_list.append({"anchor": v if k == "anchor" else "", "url": v if k == "url" else ""})
                    continue
            else:
                # plain list item (secondary_keywords / clinical_references)
                if cur_key in ("secondary_keywords", "clinical_references"):
                    fm[cur_key].append(item)
                elif cur_list is not None and cur_list and cur_list is not fm["faq"]:
                    # folded continuation of last internal_link value
                    last = cur_list[-1]
                    if "url" in last:
                        last["url"] = last["url"] + " " + item
                continue
        m = key_re.match(ln)
        if m:
            flush_scalar()
            cur_key = m.group(1)
            val = m.group(2).strip()
            if cur_key == "faq":
                cur_list = fm["faq"]
                cur_faq = None
                continue
            if cur_key == "internal_links":
                cur_list = fm["internal_links"]
                continue
            if cur_key in ("secondary_keywords", "clinical_references"):
                cur_list = None
                pending_value = []
                continue
            cur_list = None
            pending_value = [val] if val else []
            continue
        # continuation line (indented) -> fold
        if cur_list is fm["faq"] and cur_faq is not None:
            # `  answer:` line inside a faq entry
            am = re.match(r"^\s*answer:\s*(.*)$", ln)
            if am:
                cur_faq["answer"] = cur_faq.get("answer", "") + " " + am.group(1)
                continue
            # folded continuation of question/answer
            if cur_faq.get("answer"):
                cur_faq["answer"] += " " + ln.strip()
            elif cur_faq.get("question"):
                cur_faq["question"] += " " + ln.strip()
            continue
        if cur_list is fm["internal_links"] and cur_list:
            am = re.match(r"^\s*(anchor|url):\s*(.*)$", ln)
            if am:
                cur_list[-1][am.group(1)] = cur_list[-1].get(am.group(1), "") + " " + am.group(2)
                continue
        if cur_key in ("title", "meta_description", "primary_keyword",
                       "slug", "category", "author", "reviewer",
                       "target_url", "variation_type", "cta_text"):
            pending_value.append(ln.strip())
        # else: unindented continuation (malformed) -> ignore
    flush_scalar()
    # normalize internal_links into list of urls
    fm["internal_links"] = [x for x in fm["internal_links"] if isinstance(x, dict)]
    return fm


def build_faq(fm):
    out = []
    for item in fm.get("faq", []):
        if not isinstance(item, dict):
            continue
        q = (item.get("question") or "").strip()
        a = (item.get("answer") or "").strip()
        if q and a:
            out.append({"question": q, "answer": a})
    return out


def clean_body(body, fm_title):
    body = body.strip("\n")
    # Remove leading H1 (both `# ` and `<h1>`), layout renders H1 from FM title
    stripped = body.lstrip()
    if stripped.startswith("# "):
        # remove first line
        idx = body.find("\n")
        body = body[idx + 1:] if idx != -1 else ""
        body = body.lstrip("\n")
    elif stripped.startswith("<h1>"):
        body = re.sub(r"^\s*<h1>.*?</h1>\s*", "", body, count=1, flags=re.DOTALL)
    return body.strip("\n")


def normalize_info_boxes(body):
    """Convert the (unbalanced) HTML info-box blocks into clean markdown."""
    # Opening: <blockquote><div class="info-box"><h3>Title</h3></blockquote>
    body = re.sub(
        r'<blockquote><div class="info-box"><h3>(.*?)</h3></blockquote>',
        r"\n\n### \1\n",
        body,
        flags=re.DOTALL,
    )
    # Info-box list items: <blockquote>* item</blockquote>
    body = re.sub(r"<blockquote>\*\s*(.*?)</blockquote>", r"- \1\n", body, flags=re.DOTALL)
    return body


def html_to_markdown(b):
    """Convert HTML tags to markdown so MDX has no raw-JSX ambiguity."""
    # headings
    b = re.sub(r"<h1>(.*?)</h1>", r"\n\n# \1\n\n", b, flags=re.DOTALL)
    b = re.sub(r"<h2>(.*?)</h2>", r"\n\n## \1\n\n", b, flags=re.DOTALL)
    b = re.sub(r"<h3>(.*?)</h3>", r"\n\n### \1\n\n", b, flags=re.DOTALL)
    b = re.sub(r"<h4>(.*?)</h4>", r"\n\n#### \1\n\n", b, flags=re.DOTALL)
    # unordered list items (wrap question/answer blocks)
    b = re.sub(r"<ul>\s*<li>(.*?)</li>\s*</ul>", r"- \1\n", b, flags=re.DOTALL)
    b = re.sub(r"<li>(.*?)</li>", r"- \1\n", b, flags=re.DOTALL)
    b = re.sub(r"</?ul>", "\n", b)
    b = re.sub(r"</?ol>", "\n", b)
    # links
    b = re.sub(r'<a href="([^"]+)">(.*?)</a>', r"[\2](\1)", b, flags=re.DOTALL)
    b = re.sub(r"<a href='([^']+)'>(.*?)</a>", r"[\2](\1)", b, flags=re.DOTALL)
    # emphasis (do strong before em so markers nest correctly)
    b = re.sub(r"<strong>(.*?)</strong>", r"**\1**", b, flags=re.DOTALL)
    b = re.sub(r"<b>(.*?)</b>", r"**\1**", b, flags=re.DOTALL)
    b = re.sub(r"<em>(.*?)</em>", r"*\1*", b, flags=re.DOTALL)
    b = re.sub(r"<i>(.*?)</i>", r"*\1*", b, flags=re.DOTALL)
    # remaining blockquotes -> markdown
    b = re.sub(r"<blockquote>\s*(.*?)\s*</blockquote>", r"\n> \1\n", b, flags=re.DOTALL)
    # paragraphs, divs, spans, line breaks
    b = re.sub(r"</?p[^>]*>", "\n", b)
    b = re.sub(r"</?div[^>]*>", "\n", b)
    b = re.sub(r"</?span[^>]*>", "", b)
    b = re.sub(r"<br\s*/?>", "\n", b)
    # Final: strip any remaining orphaned/mismatched HTML tags
    b = re.sub(r"</?[a-zA-Z][a-zA-Z0-9]*[^>]*>", "", b)
    return b


def main():
    inventory = json.load(open(os.path.join(NET, "scripts", "migration", "inventory.json")))
    os.makedirs(OUT_DIR, exist_ok=True)
    ok = 0
    errors = []
    generated = []
    for it in inventory:
        path = os.path.join(NET, it["source"], it["slug"] + ".txt")
        raw = open(path, encoding="utf-8", errors="replace").read()
        fm_lines, body, _ = split_frontmatter(raw)
        fm = parse_frontmatter(fm_lines)

        title = clean_title(fm.get("title") or it["slug"])
        slug = fm.get("slug") or it["slug"]
        category = fm.get("category") or it["category"]
        meta_desc = fm.get("meta_description") or ""
        meta_desc = " ".join(meta_desc.split())

        mdx = {
            "title": title,
            "metaTitle": f"{title} | Joy of Care",
            "metaDescription": meta_desc,
            "category": category,
            "author": "Tim Medis Joy of Care",
            "reviewer": "dr. Sarah Wijaya, Sp.FR",
            "date": "2026-09-05",
            "slug": slug,
        }
        if fm.get("primary_keyword"):
            mdx["primaryKeyword"] = fm["primary_keyword"]
        if fm.get("secondary_keywords"):
            mdx["secondaryKeywords"] = fm["secondary_keywords"]
        links = []
        for item in fm.get("internal_links", []):
            if not isinstance(item, dict):
                continue
            url = (item.get("url") or "").strip()
            if url:
                links.append(url)
        if links:
            mdx["internalLinks"] = links
        faq = build_faq(fm)
        if faq:
            mdx["faq"] = faq
        if fm.get("clinical_references"):
            refs = [r for r in fm["clinical_references"] if isinstance(r, str)]
            if refs:
                mdx["clinicalReferences"] = refs

        # Validate required
        missing = [k for k in ("title", "slug", "category", "metaDescription") if not mdx.get(k)]
        if missing:
            errors.append((slug, f"missing {missing}"))
            continue

        body_clean = clean_body(body, title)
        body_clean = normalize_info_boxes(body_clean)
        body_clean = html_to_markdown(body_clean)
        # Escape stray '<' that MDX would treat as JSX (not an HTML tag)
        body_clean = re.sub(r"<(?=\s|\d|<|$)", "&lt;", body_clean)

        if DRY:
            generated.append(slug)
            ok += 1
            continue

        # emit MDX
        fm_yaml = yaml.dump(mdx, allow_unicode=True, sort_keys=False, default_flow_style=False).strip()
        content = "---\n" + fm_yaml + "\n---\n\n" + body_clean + "\n"
        out_path = os.path.join(OUT_DIR, slug + ".mdx")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        generated.append(slug)
        ok += 1

    print(f"{'DRY-RUN ' if DRY else ''}Processed: {ok}, Errors: {len(errors)}")
    for e in errors[:15]:
        print("  ERR", e)
    # Validate generated YAML parseable
    if not DRY:
        bad = 0
        import glob
        for f in glob.glob(os.path.join(OUT_DIR, "*.mdx")):
            txt = open(f, encoding="utf-8").read()
            try:
                yaml.safe_load(txt.split("---")[1])
            except Exception:
                bad += 1
                print("  YAML FAIL:", os.path.basename(f))
        print(f"Generated MDX YAML-parse failures: {bad}")
    else:
        print("(dry-run: no files written)")


if __name__ == "__main__":
    main()