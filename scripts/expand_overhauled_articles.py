# -*- coding: utf-8 -*-
"""
Expansion Engine for Joy of Care Overhauled Articles
Ensures:
- Word count >= 1000 words per article
- Embedded contextual internal links in body text (3-5 links)
- WhatsApp link uses wa.me format
- Title (50-60 chars) and Meta Description (150-160 chars) maintained
- Rich clinical E-E-A-T depth and FAQs
"""

import os, glob, yaml, re, json

OVERHAULED_DIR = "/home/gobeam/Projects/joyofcare-net/articles-overhauled"
ARTICLES_DIR = "/home/gobeam/Projects/joyofcare-net/articles"
DRIVE_DIR = "/home/gobeam/Projects/joyofcare-net/drive_articles"
INDEX_FILE = "/home/gobeam/Projects/joyofcare-net/overhauled-articles-index.json"

WA_OLD = "https://api.whatsapp.com/send/?phone=628811118911&text=Hi,%20saya%20tahu%20dari%20web.%20Apa%20saja%20layanan%20Joy%20of%20Care?"
WA_NEW = "https://wa.me/628811118911?text=Hi,%20saya%20tahu%20dari%20web.%20Apa%20saja%20layanan%20Joy%20of%20Care?"

print("Expansion script initialized.")
