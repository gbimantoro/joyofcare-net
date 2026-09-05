# Odoo Site Analysis — joc-web.odoo.com

**Date:** 5 September 2026  
**Auditor:** JoC SEO  
**Site:** https://joc-web.odoo.com  
**Purpose:** Learn SEO-GEO-AIO insights from the old Odoo site to improve joyofcare-web  

---

## Executive Summary

The Odoo site (joc-web.odoo.com) is a **staging/testing site** with `noindex, nofollow` on all pages. It cannot be indexed by search engines. However, it contains several SEO patterns worth learning from — particularly **BlogPosting schema** on articles, which joyofcare-web currently lacks.

| Aspect | Odoo Site | joyofcare-web | Winner |
|--------|-----------|---------------|--------|
| Indexing | ❌ noindex, nofollow | ✅ index, follow | joyofcare-web |
| lang attribute | ❌ en-US (wrong) | ✅ id (correct) | joyofcare-web |
| Homepage schema | LocalBusiness | MedicalBusiness | joyofcare-web |
| Article schema | ✅ BlogPosting | ❌ None (txt files) | Odoo site |
| FAQ schema | ❌ None | ✅ FAQPage | joyofcare-web |
| Breadcrumb schema | ❌ None | ✅ BreadcrumbList | joyofcare-web |
| robots.txt AI rules | ❌ None | ✅ GPTBot, ClaudeBot allowed | joyofcare-web |
| llms.txt | ❌ None | ✅ Complete | joyofcare-web |
| Sitemap HTTPS | ✅ HTTPS | ✅ HTTPS | Tie |
| Meta descriptions | ⚠️ Short/generic | ✅ Custom with CTA | joyofcare-web |

---

## 1. Odoo Site Technical Findings

### Homepage
- **lang="en-US"** — Wrong for Indonesian content
- **robots: noindex, nofollow** — Site is deindexed (staging)
- **Title:** "Joy of Care | Panggil Dokter • Fisioterapi • Akupuntur"
- **Meta description:** Generic, no CTA
- **JSON-LD:** LocalBusiness schema (1 block)
- **OG tags:** Present (type, title, description, image, site_name)
- **Twitter Card:** summary_large_image
- **Canonical:** Present (https://joc-web.odoo.com/)

### Blog Articles
- **BlogPosting JSON-LD schema** — Present on article pages ✅
- **OG type: article** — Proper article markup
- **H1 + H2 structure** — Proper heading hierarchy
- **Meta descriptions:** Short/generic ("Memahami faktor risiko...")
- **noindex, nofollow** — All articles deindexed

### robots.txt
```
User-agent: *
Sitemap: https://joc-web.odoo.com/sitemap.xml
```
- No AI crawler rules (unlike joyofcare-web)
- Simple, minimal

### Sitemap
- HTTPS URLs ✅
- lastmod dates present ✅
- 9+ service page URLs
- Blog articles included

---

## 2. Key Insight: BlogPosting Schema

The most important learning from the Odoo site is that **blog articles have BlogPosting JSON-LD schema**. This is something joyofcare-web is currently missing because articles are stored as .txt files, not rendered HTML.

### What Odoo Has
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Bahaya Komplikasi Osteoporosis...",
  "description": "Memahami faktor risiko...",
  "author": { "@type": "Organization", "name": "Joy of Care" }
}
```

### What joyofcare-web Needs
Blog articles should be rendered as HTML with JSON-LD during the CMS build process. The frontmatter already contains all the data needed:
- title → headline
- meta_description → description
- primary_keyword → keywords
- faq → FAQPage schema
- clinical_references → citation

---

## 3. What joyofcare-web Does Better

### Schema Coverage
- **MedicalBusiness** (better than LocalBusiness for healthcare)
- **MedicalProcedure** on service pages (Odoo has none)
- **BreadcrumbList** on service pages (Odoo has none)
- **FAQPage** on service pages (Odoo has none)
- **CollectionPage + ItemList** on blog category pages (Odoo has none)

### GEO/AIO Optimization
- **robots.txt** explicitly allows AI crawlers (GPTBot, ClaudeBot, PerplexityBot)
- **llms.txt** provides structured data for AI citation
- **AIO Summary blocks** in articles for citation-ready passages

### Content Quality
- **Average 1,160 words** per article (vs Odoo's ~600-800)
- **Rich frontmatter** with FAQ, internal links, medical reviewer, clinical references
- **WhatsApp CTA** in every article

---

## 4. Recommendations for joyofcare-web

### 🔴 CRITICAL
1. **Render blog articles as HTML with JSON-LD** — The CMS (Keystatic + Next.js) should generate HTML pages from .txt frontmatter, including:
   - BlogPosting schema (author, datePublished, dateModified)
   - FAQPage schema (from FAQ section in frontmatter)
   - BreadcrumbList schema (Home > Blog > Category > Article)

### 🟡 HIGH
2. **Add BlogPosting schema to all blog articles** — Use the frontmatter data already present
3. **Ensure sitemap-articles.xml includes all 254 articles** — Currently only 42

### 🟢 MEDIUM
4. **Learn from Odoo's BlogPosting structure** — Include author, datePublished, dateModified, image
5. **Add sameAs links** to social media profiles in MedicalBusiness schema

---

## 5. Comparison Summary

The Odoo site is a staging environment with noindex, so it has zero SEO value in practice. However, it demonstrates that **BlogPosting schema** should be part of the article rendering pipeline. joyofcare-web already surpasses the Odoo site in every other SEO dimension — the only gap is article-level schema markup, which can be addressed through the CMS build process.

**Bottom line:** joyofcare-web is significantly more advanced than the Odoo site. The one improvement to adopt is rendering blog articles as HTML with BlogPosting + FAQPage JSON-LD schemas.
