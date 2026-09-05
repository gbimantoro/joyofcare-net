import os, re

patterns = {
    "aio_summary_label": re.compile(r'\*\*Ringkasan Eksekutif \(AIO Summary\)\*\*:\s*', re.I),
    "memegang_peranan": re.compile(r'memegang peranan\s+(?:penting|vital|krusial|utama)', re.I),
    "bukan_sekadar": re.compile(r'bukan (?:hanya |cuma )?sekadar\s+.*?,\s*(?:melainkan|tetapi|namun)', re.I),
    "tidak_dapat_dipungkiri": re.compile(r'tidak dapat di(?:pungkiri|mungkiri)', re.I),
    "menjadi_bukti": re.compile(r'menjadi bukti (?:nyata|otentik|jelas)', re.I),
    "pada_akhirnya": re.compile(r'(?:^|\.\s+)pada akhirnya[, ]', re.I | re.M),
    "kesimpulannya": re.compile(r'(?:^|\.\s+)kesimpulannya[, ]', re.I | re.M),
    "sebagai_penutup": re.compile(r'(?:^|\.\s+)sebagai penutup[, ]', re.I | re.M),
    "tahukah_anda": re.compile(r'tahukah anda', re.I),
    "perlu_dipahami": re.compile(r'perlu dipahami bahwa', re.I),
    "rahasianya_kuncinya": re.compile(r'(?:rahasianya|kuncinya|jawabannya)\s*:', re.I),
    "game_changer": re.compile(r'game changer', re.I),
    "cutting_edge": re.compile(r'cutting[- ]edge', re.I),
    "paradigm_shift": re.compile(r'paradigm shift', re.I),
    "studi_kasus": re.compile(r'studi kasus', re.I),
    "fake_patients": re.compile(r'(?:ibu|bapak|pak)\s+[A-Z][a-z]+\s*\(\d+\s*tahun\)', re.I),
}

for d in ['articles-overhauled', 'articles-new']:
    print(f"=== Analyzing {d} ===")
    counts = {k: 0 for k in patterns}
    file_hits = {k: [] for k in patterns}
    for f in sorted(os.listdir(d)):
        if not f.endswith('.txt'): continue
        with open(os.path.join(d, f), 'r', encoding='utf-8') as fl:
            c = fl.read()
        for k, regex in patterns.items():
            matches = regex.findall(c)
            if matches:
                counts[k] += len(matches)
                file_hits[k].append((f, len(matches)))
    for k, cnt in counts.items():
        if cnt > 0:
            print(f"  {k}: {cnt} hits across {len(file_hits[k])} files")
