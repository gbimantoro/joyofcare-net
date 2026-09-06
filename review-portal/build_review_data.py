import os
import glob
import json
import re
import html

CLUSTER_NAMES = {
    1: "Kluster 1: Panggil Dokter ke Rumah",
    2: "Kluster 2: Layanan Perawat & Home Care Medis",
    3: "Kluster 3: Fisioterapi ke Rumah",
    4: "Kluster 4: Infus Vitamin & Terapi Booster",
    5: "Kluster 5: Home Lab & Cek Darah di Rumah",
    6: "Kluster 6: Perawatan Lansia & Geriatri Terpadu",
    7: "Kluster 7: Manajemen Penyakit Degeneratif & Pasca-Bedah",
    8: "Kluster 8: Medical Escort, Transportasi Medis & Studi Luar Negeri"
}

def md_to_html(md_text):
    lines = md_text.split('\n')
    out = []
    in_table = False
    in_code = False
    in_blockquote = False
    in_ul = False
    in_ol = False
    table_rows = []
    
    def inline_format(text):
        text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank" class="text-teal-600 hover:text-teal-800 font-medium underline decoration-teal-300 underline-offset-2">\1</a>', text)
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong class="font-bold text-slate-900">\1</strong>', text)
        text = re.sub(r'\*(.*?)\*', r'<em class="italic text-slate-800">\1</em>', text)
        text = re.sub(r'(?<!\w)_(.*?)_(?!\w)', r'<em class="italic text-slate-800">\1</em>', text)
        text = re.sub(r'`(.*?)`', r'<code class="px-1.5 py-0.5 rounded bg-slate-100 text-slate-800 text-xs font-mono border border-slate-200">\1</code>', text)
        return text

    def close_lists():
        nonlocal in_ul, in_ol
        res = []
        if in_ul:
            res.append('</ul>')
            in_ul = False
        if in_ol:
            res.append('</ol>')
            in_ol = False
        return res

    def close_table():
        nonlocal in_table, table_rows
        if not in_table or not table_rows:
            in_table = False
            table_rows = []
            return []
        
        res = ['<div class="overflow-x-auto my-6 rounded-xl border border-slate-200 shadow-sm"><table class="w-full text-left text-sm text-slate-700">']
        if len(table_rows) > 0:
            res.append('<thead class="bg-teal-50/90 text-xs uppercase tracking-wider font-semibold text-teal-900 border-b border-slate-200"><tr>')
            for cell in table_rows[0]:
                res.append(f'<th class="px-4 py-3.5">{inline_format(cell.strip())}</th>')
            res.append('</tr></thead>')
        
        res.append('<tbody class="divide-y divide-slate-200 bg-white">')
        data_rows = table_rows[1:]
        if data_rows and all(re.match(r'^:?-+:?$', c.strip()) for c in data_rows[0] if c.strip()):
            data_rows = data_rows[1:]
            
        for row in data_rows:
            res.append('<tr class="hover:bg-teal-50/30 transition-colors">')
            for cell in row:
                res.append(f'<td class="px-4 py-3.5 align-top leading-relaxed">{inline_format(cell.strip())}</td>')
            res.append('</tr>')
        res.append('</tbody></table></div>')
        
        in_table = False
        table_rows = []
        return res

    for line in lines:
        stripped = line.strip()
        
        if stripped.startswith('```'):
            if in_code:
                out.append('</code></pre></div>')
                in_code = False
            else:
                out.extend(close_lists())
                out.extend(close_table())
                out.append('<div class="my-5 rounded-xl bg-slate-900 text-slate-100 p-4 font-mono text-xs overflow-x-auto shadow-md border border-slate-800"><pre><code>')
                in_code = True
            continue
            
        if in_code:
            out.append(html.escape(line) + '\n')
            continue
            
        if stripped.startswith('|') and stripped.endswith('|'):
            out.extend(close_lists())
            in_table = True
            cols = [c for c in stripped.split('|')[1:-1]]
            table_rows.append(cols)
            continue
        elif in_table:
            out.extend(close_table())
            
        if stripped.startswith('>'):
            out.extend(close_lists())
            content = stripped.lstrip('>').strip()
            if not in_blockquote:
                out.append('<div class="my-6 p-5 rounded-2xl bg-teal-50 border-l-4 border-teal-600 text-slate-800 shadow-sm leading-relaxed">')
                in_blockquote = True
            if content.startswith('###'):
                out.append(f'<h4 class="font-bold text-teal-900 text-base mb-2.5 flex items-center gap-2">{inline_format(content.lstrip("#").strip())}</h4>')
            elif content.startswith('-') or content.startswith('*'):
                out.append(f'<div class="flex items-start gap-2.5 text-sm my-2"><span class="text-teal-600 font-bold text-base leading-tight">•</span><span class="text-slate-700">{inline_format(content.lstrip("-*").strip())}</span></div>')
            else:
                out.append(f'<p class="text-sm my-1 text-slate-700 leading-relaxed">{inline_format(content)}</p>')
            continue
        elif in_blockquote:
            out.append('</div>')
            in_blockquote = False

        if stripped.startswith('### '):
            out.extend(close_lists())
            out.append(f'<h3 class="text-lg font-bold text-slate-900 mt-7 mb-3 pb-1 border-b border-slate-100">{inline_format(stripped[4:])}</h3>')
            continue
        elif stripped.startswith('## '):
            out.extend(close_lists())
            out.append(f'<h2 class="text-xl font-bold text-slate-900 mt-9 mb-4 flex items-center gap-2.5"><span class="w-2.5 h-6 bg-teal-600 rounded-full inline-block shrink-0"></span><span>{inline_format(stripped[3:])}</span></h2>')
            continue
        elif stripped.startswith('# '):
            out.extend(close_lists())
            out.append(f'<h1 class="text-2xl font-extrabold text-slate-900 mt-7 mb-5">{inline_format(stripped[2:])}</h1>')
            continue

        if stripped in ['---', '***', '___']:
            out.extend(close_lists())
            out.append('<hr class="my-8 border-t border-slate-200" />')
            continue

        if stripped.startswith('- ') or stripped.startswith('* '):
            if in_ol:
                out.append('</ol>')
                in_ol = False
            if not in_ul:
                out.append('<ul class="list-disc list-inside my-3.5 space-y-2 text-slate-700 text-sm md:text-base leading-relaxed">')
                in_ul = True
            out.append(f'<li>{inline_format(stripped[2:].strip())}</li>')
            continue

        m_ol = re.match(r'^(\d+)\.\s+(.*)', stripped)
        if m_ol:
            if in_ul:
                out.append('</ul>')
                in_ul = False
            if not in_ol:
                out.append('<ol class="list-decimal list-inside my-3.5 space-y-2 text-slate-700 text-sm md:text-base leading-relaxed">')
                in_ol = True
            out.append(f'<li>{inline_format(m_ol.group(2).strip())}</li>')
            continue

        if not stripped:
            out.extend(close_lists())
            continue

        out.extend(close_lists())
        out.append(f'<p class="my-4 text-slate-700 leading-relaxed text-sm md:text-base">{inline_format(stripped)}</p>')

    if in_table:
        out.extend(close_table())
    if in_blockquote:
        out.append('</div>')
    out.extend(close_lists())
    if in_code:
        out.append('</code></pre></div>')
        
    return '\n'.join(out)

def parse_frontmatter(fm_text):
    fm = {
        'secondaryKeywords': [],
        'internalLinks': [],
        'faq': [],
        'clinicalReferences': []
    }
    
    current_list_key = None
    faq_current = None
    
    for line in fm_text.split('\n'):
        raw_line = line
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        if line.startswith('secondaryKeywords:'):
            current_list_key = 'secondaryKeywords'
            continue
        elif line.startswith('internalLinks:'):
            current_list_key = 'internalLinks'
            continue
        elif line.startswith('clinicalReferences:'):
            current_list_key = 'clinicalReferences'
            continue
        elif line.startswith('faq:'):
            current_list_key = 'faq'
            continue
            
        if current_list_key == 'faq':
            if line.startswith('- question:'):
                if faq_current:
                    fm['faq'].append(faq_current)
                q_val = line[len('- question:'):].strip().strip('"').strip("'")
                faq_current = {'question': q_val, 'answer': ''}
            elif line.startswith('answer:'):
                if faq_current:
                    a_val = line[len('answer:'):].strip().strip('"').strip("'")
                    faq_current['answer'] = a_val
            elif faq_current and raw_line.startswith('    '):
                faq_current['answer'] += ' ' + line.strip('"').strip("'")
            elif not line.startswith('-') and ':' in line:
                if faq_current:
                    fm['faq'].append(faq_current)
                    faq_current = None
                current_list_key = None
            continue
            
        if current_list_key in ['secondaryKeywords', 'internalLinks', 'clinicalReferences']:
            if line.startswith('- '):
                val = line[2:].strip().strip('"').strip("'")
                fm[current_list_key].append(val)
                continue
            elif not line.startswith('-') and ':' in line:
                current_list_key = None
                
        if ':' in line:
            parts = line.split(':', 1)
            k = parts[0].strip()
            v = parts[1].strip().strip('"').strip("'")
            fm[k] = v
            
    if faq_current:
        fm['faq'].append(faq_current)
        
    return fm

# Gather all 200 files
f1_files = sorted(glob.glob('/home/gobeam/Projects/joyofcare-net/fase-1-draft-articles/*/*.mdx'))
f2_files = sorted(glob.glob('/home/gobeam/Projects/joyofcare-net/fase-2-draft-articles/*/*.mdx'))
f3_files = sorted(glob.glob('/home/gobeam/Projects/joyofcare-net/fase-3-draft-articles/*/*.mdx'))

all_file_entries = []
for f in f1_files:
    c = 1 if 'kluster-1' in f else 2
    all_file_entries.append((1, 'Fase 1 (Mei–Jun 2026)', c, f))
    
for f in f2_files:
    if 'kluster-3' in f:
        c = 3
    elif 'kluster-5' in f:
        c = 5
    elif 'kluster-6' in f:
        c = 6
    else:
        c = 7
    all_file_entries.append((2, 'Fase 2 (Jun–Jul 2026)', c, f))
    
for f in f3_files:
    if 'kluster-4' in f:
        c = 4
    elif 'kluster-7' in f:
        c = 7
    else:
        c = 8
    all_file_entries.append((3, 'Fase 3 (Jul–Ags 2026)', c, f))

# Sort chronologically by date
parsed_articles = []
for idx, (fase_num, fase_label, c_num, filepath) in enumerate(all_file_entries, 1):
    with open(filepath, 'r', encoding='utf-8') as fl:
        content = fl.read()
        
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    body = content
    fm = {}
    if fm_match:
        fm = parse_frontmatter(fm_match.group(1))
        body = content[fm_match.end():].strip()
        
    words = len(re.findall(r'\b\w+\b', body))
    html_body = md_to_html(body)
    
    title = fm.get('title') or os.path.basename(filepath).replace('.mdx', '').replace('-', ' ').title()
    slug = fm.get('slug') or os.path.basename(filepath).replace('.mdx', '')
    cat = fm.get('category') or 'kesehatan-umum'
    date = fm.get('date') or '2026-05-01'
    kw = fm.get('primaryKeyword') or fm.get('primary_keyword') or slug.replace('-', ' ')
    
    parsed_articles.append({
        'id': idx,
        'fase': fase_num,
        'faseLabel': fase_label,
        'cluster': c_num,
        'clusterName': CLUSTER_NAMES.get(c_num, f"Kluster {c_num}"),
        'filePath': filepath,
        'fileRelPath': os.path.relpath(filepath, '/home/gobeam/Projects/joyofcare-net'),
        'fileUri': f"file://{filepath}",
        'slug': slug,
        'title': title,
        'metaTitle': fm.get('metaTitle') or f"{title} | Joy of Care",
        'metaDescription': fm.get('metaDescription') or '',
        'category': cat,
        'author': fm.get('author') or 'Tim Kontributor Artikel',
        'reviewer': fm.get('reviewer') or 'Tim Medis Joy of Care',
        'date': date,
        'featuredImage': fm.get('featuredImage') or f"/visual-assets/thumbnails/{cat}.svg",
        'primaryKeyword': kw,
        'secondaryKeywords': fm.get('secondaryKeywords', []),
        'internalLinks': fm.get('internalLinks', []),
        'faq': fm.get('faq', []),
        'clinicalReferences': fm.get('clinicalReferences', []),
        'wordCount': words,
        'htmlContent': html_body,
        'rawContent': content
    })

# Sort by Phase, then Cluster, then Date
parsed_articles.sort(key=lambda x: (x['fase'], x['cluster'], x['date']))
# Re-assign sequential ID 1-200
for i, item in enumerate(parsed_articles, 1):
    item['id'] = i

print(f"Total parsed articles: {len(parsed_articles)}")

# Write to articles-data.js
js_output = "const ARTICLES_DATA = " + json.dumps(parsed_articles, ensure_ascii=False, indent=2) + ";\n"
with open('/home/gobeam/Projects/joyofcare-net/review-portal/articles-data.js', 'w', encoding='utf-8') as fl:
    fl.write(js_output)

# Write to articles.json
with open('/home/gobeam/Projects/joyofcare-net/review-portal/articles.json', 'w', encoding='utf-8') as fl:
    json.dump(parsed_articles, fl, ensure_ascii=False, indent=2)

print("Saved articles-data.js and articles.json in review-portal/")
print(f"Size of articles-data.js: {os.path.getsize('/home/gobeam/Projects/joyofcare-net/review-portal/articles-data.js'):,} bytes")
