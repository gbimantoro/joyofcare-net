# -*- coding: utf-8 -*-
import os, sys, re, json, yaml

dirs_to_check = {
    'articles-rewritten': 37,
    'articles-new-rewritten': 100,
    'articles-overhauled': 37,
    'articles-new': 100
}

slop_patterns = {
    'aio_summary': re.compile(r'\*\*Ringkasan Eksekutif \(AIO Summary\)\*\*:', re.I),
    'studi_kasus': re.compile(r'## Studi Kasus Nyata:', re.I),
    'fake_persona_age': re.compile(r'\b(?:Ibu|Bapak|Pak|Oma|Opa)\s+[A-Z][a-z]+\s*\(\d+\s*tahun\)', re.I),
    'bukan_sekadar_contrast': re.compile(r'bukan (?:hanya |cuma )?sekadar\s+.*?,\s*(?:melainkan|tetapi|namun)', re.I),
    'memegang_peranan': re.compile(r'memegang peranan\s+(?:penting|vital|krusial|utama)', re.I),
    'tahukah_anda': re.compile(r'tahukah anda', re.I),
    'pada_akhirnya_opener': re.compile(r'(?:^|\.\s+)pada akhirnya[, ]', re.I | re.M),
    'kesimpulannya_opener': re.compile(r'(?:^|\.\s+)kesimpulannya[, ]', re.I | re.M),
    'sebagai_penutup_opener': re.compile(r'(?:^|\.\s+)sebagai penutup[, ]', re.I | re.M),
    'price_rp': re.compile(r'Rp[\s\.]*\d+'),
    'currency': re.compile(r'\b(?:USD|AUD|GBP|EUR|\$|\£)\s*[\d\.,]+'),
}

personas_to_check = [
    'Ibu Harsono', 'Bapak Suryadi', 'Ibu Halimah', 'Bapak Irwan', 'Ibu Maryam',
    'Bapak Hartono', 'Ibu Mira (48', 'Ibu Ratna', 'Bapak Adrian', 'Ibu Dewi',
    'Bapak Soemitro', 'Oma Ratna', 'Bapak Subagio', 'Ibu Kartini', 'Bapak Hendra (52',
    'Ibu Nuraini', 'Bapak Suwandi', 'Ibu Soekotjo', 'Ibu Sukmawati', 'Bapak Hendra (72'
]

total_errors = 0

for dname, expected_count in dirs_to_check.items():
    files = sorted([f for f in os.listdir(dname) if f.endswith('.txt')])
    print(f"\nChecking directory: {dname} (found {len(files)} files, expected {expected_count})")
    assert len(files) == expected_count, f"Count mismatch in {dname}: {len(files)} != {expected_count}"
    
    for f in files:
        fp = os.path.join(dname, f)
        with open(fp, 'r', encoding='utf-8') as fl:
            c = fl.read()
        
        # Check YAML frontmatter
        parts = c.split('---', 2)
        if len(parts) < 3:
            print(f"[{dname}/{f}] ERROR: Invalid frontmatter structure")
            total_errors += 1
            continue
        try:
            yaml.safe_load(parts[1])
        except Exception as e:
            print(f"[{dname}/{f}] ERROR: Invalid YAML in frontmatter: {e}")
            total_errors += 1
        
        body = parts[2]
        wc = len(body.split())
        if wc < 1000:
            print(f"[{dname}/{f}] ERROR: Word count {wc} < 1000")
            total_errors += 1

        for pname, regex in slop_patterns.items():
            matches = regex.findall(c)
            if matches:
                print(f"[{dname}/{f}] ERROR: Pattern '{pname}' matched: {matches}")
                total_errors += 1
        
        for persona in personas_to_check:
            if persona.lower() in c.lower():
                print(f"[{dname}/{f}] ERROR: Found persona '{persona}'")
                total_errors += 1

print("\n--- Summary ---")
if total_errors == 0:
    print("AUDIT SUCCESS: 0 errors found across all 274 checked files!")
else:
    print(f"AUDIT FAILED: {total_errors} errors found.")

