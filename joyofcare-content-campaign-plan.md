# Joy of Care – Content & Campaign Plan Report

**Prepared:** 6 September 2026  
**Target:** joyofcare.net  
**Current SEO Score:** 34/100 (Critical)  
**Content Scope:** 100 articles (20 keywords × 5 content types) over 20 weeks  

---

## 1. Executive Summary

Joy of Care provides home‑healthcare services (doctor/nurse visits, physiotherapy, infusions, lab, vaccination) in Jakarta, Tangerang, BSD, and surrounding areas. Current SEO score is **34/100 (Critical)**. A 100‑article content calendar and a 4‑article osteoporosis topic cluster have been drafted. The campaign plan outlines five phases over 20 weeks to raise the site’s authority, fix technical issues, and drive organic traffic & AI citations.

---

## 2. Current Content Status (Osteoporosis Cluster Analysis)

*Source: `content-analysis.md`*

| Metric | Avg Score (1‑10) | Key Findings |
|--------|------------------|--------------|
| Title Effectiveness | 8.5 | Good keyword inclusion; slugs truncated (see below). |
| Content Structure & Flow | 7.8 | Logical TOFU→MOFU→BOFU flow; thin content (325‑430 words). |
| Keyword Strategy & Density | 8.1 | Target keywords present; raw keyword leakage on line 2 of each file. |
| Readability & Formatting | 7.8 | Acceptable ASL; Article 2 has formatting glitches (excess blank lines). |
| Call‑to‑Action | 6.4 | Placeholder CTAs lack phone number, WhatsApp deep link, UTM. |
| Internal Linking | **1.0** | **Zero internal links** – critical gap. |
| Medical Accuracy & E‑E‑A‑T | 7.5 | Missing reviewer byline, citations (PEROSI/WHO), disclaimer. |
| AI Citability (GEO/AIO) | 7.8 | Structured definitions & FAQs present; needs schema & expanded Q&A. |
| **Overall Grade** | **6.8 (B‑)** | Limited by thin content, no internal links, weak CTAs, missing E‑E‑A‑T. |

### Specific Issues Across All 4 Articles
1. **Thin content** (350 words avg) – YMYL risk.  
2. **Slug truncation** (filenames cut off, e.g., `bahaya-komplikasi-osteoporosis-dan-faktor-risiko-yang-wajib-`).  
3. **Raw keyword leakage** (line 2: `Target Keyword / Search Intent: …`).  
4. **Zero internal linking** – isolated island pages.  
5. **CTA placeholders** missing `08811-118-911` and `https://wa.me/628811118911?text=…`.  
6. **No medical reviewer byline or citations**.  
7. **Formatting glitches** (Article 2: 10‑15 blank lines).  

### Recommended Fixes
- Expand each article to **750‑1,100 words** (add statistics, T‑score tables, 3‑5 FAQs).  
- Rename files to canonical slugs (e.g., `bahaya-komplikasi-osteoporosis-dan-faktor-risiko-lansia`).  
- Strip line 2 into CMS metadata; remove from body.  
- Implement hub‑and‑spoke internal linking (see Section 4).  
- Replace CTA with verified WhatsApp deep link: `<a href="https://wa.me/628811118911?text=Halo%20Joy%20of%20Care%2C%20saya%20ingin%20konsultasi%20layanan%20osteoporosis" class="cta-button">📲 Konsultasi WhatsApp: 08811-118-911</a>`.  
- Add Medical Review box: `Ditinjau oleh: Tim Medis Joy of Care (dr. [Nama], Sp.PD/Sp.OT) | Terakhir diperbarui: 5 Sept 2026 | Referensi: PEROSI, WHO, IOF`.  
- Run markdown normalization to remove excess blank lines.  
- Add FAQPage schema & MedicalWebPage/MedicalCondition schema where appropriate.  

---

## 3. Campaign Plan Overview

*Source: `campaign-plan.md`*

| Phase | Timeline | Key Actions |
|-------|----------|-------------|
| **Phase 1: Technical Fixes** | Week 1 | - Fix `lang="id"` on Odoo templates.<br>- Add JSON‑LD MedicalBusiness schema to homepage.<br>- Correct meta title mismatches (perawat, transcare pages).<br>- Update sitemap to HTTPS.<br>- Create `/llms.txt`.<br>- Update robots.txt to allow AI crawlers. |
| **Phase 2: Content & Structure** | Week 2 | - Ensure one H1 per page.<br>- Add alt text to all images (≈12).<br>- Implement breadcrumbs navigation.<br>- Expand homepage to 800+ words.<br>- Add FAQ sections to top 3 service pages.<br>- Add “last updated” timestamps. |
| **Phase 3: Schema & GEO** | Week 3 | - Add FAQPage schema to service pages.<br>- Add BreadcrumbList schema.<br>- Add author bios with credentials.<br>- Create 3 data‑driven blog posts.<br>- Add original statistics to homepage. |
| **Phase 4: Brand & Authority** | Week 4 | - Launch YouTube channel.<br>- Register on Halodoc/Alodokter.<br>- Set up Google Business Profile.<br>- Create LinkedIn company page.<br>- Outreach to 5 health blogs for guest posts. |
| **Phase 5: Ongoing** | Week 5+ | - Publish 2‑4 blog posts/month.<br>- Monitor AI citations weekly.<br>- Track keyword rankings monthly.<br>- Refresh content every 3 months. |

### Target Keywords (Primary Focus)
- `panggil dokter ke rumah tangerang`  
- `fisioterapi di rumah jakarta`  
- `homecare services indonesia`  
- `perawat homecare tangerang`  
- `cek lab di rumah`  
- `akupuntur di rumah tangerang`  

### Brand Presence Targets
- YouTube: 50 videos in 6 months.  
- Reddit: r/indonesia health answers.  
- LinkedIn: weekly posts.  
- TikTok: health‑tip shorts.  

---

## 4. Content Calendar (100 Articles)

*Source: `content-calendar.md`*

### Framework
20 seed keywords × 5 content types = 100 articles.

| # | Content Type | Purpose | Word Count | Funnel Stage |
|---|--------------|---------|------------|--------------|
| 1 | **Pillar Page** | Comprehensive guide, cluster hub | 1,500‑2,000 | TOFU/MOFU |
| 2 | **How‑To Guide** | Step‑by‑step tutorial | 1,000‑1,500 | TOFU/MOFU |
| 3 | **Comparison/Versus** | Compare options/providers | 800‑1,200 | MOFU |
| 4 | **FAQ/Q&A** | AI‑citation ready | 800‑1,000 | TOFU/MOFU |
| 5 | **Case Study/Data** | Patient story, stats, infographic | 800‑1,200 | MOFU/BOFU |

### Publication Schedule
20 weeks, 5 articles/week.

- **Weeks 1‑2**: Critical Quick Wins (keywords #1, #2, #4, #5, #7) – highest priority.  
- **Weeks 3‑4**: Competitive Response (#3, #6, #8, #9, #11).  
- **Weeks 5‑6**: Authority Building (#10‑#15).  
- **Weeks 7‑8**: Cluster Expansion (#16‑#20).  
- **Weeks 9‑10**: Supporting Content (long‑tail).  
- **Weeks 11‑12**: Location Pages (Jakarta Selatan, Barat, Pusat, Depok, Bogor, BSD, Gading Serpong, Tangerang Selatan).  
- **Weeks 13‑14**: Pillar Page Refresh & Cluster Consolidation (e.g., osteoporosis cluster, fisioterapi cluster).  
- **Weeks 15‑16**: E‑E‑A‑T & Authority Content (doctor/physio/nurse profiles, SOPs, testimonials, partnerships).  
- **Weeks 17‑18**: GEO/AIO Optimization (What is homecare?, BPJS coverage, pricing, etc.).  
- **Weeks 19‑20**: Final Expansion (price checklists, mitos vs fakta, savings tips, etc.).  

### Quality Checklist (per article)
- Title tag 50‑60 chars with primary keyword.  
- Meta description 150‑160 chars + keyword + CTA.  
- One H1 with primary keyword.  
- H2/H3 structure with secondary keywords.  
- Word count per type (see above).  
- 3‑5 contextual internal links.  
- 1‑2 external authoritative sources (PEROSI, WHO, etc.).  
- Alt text on all images.  
- FAQ section with FAQPage schema.  
- CTA with WhatsApp deep link (`https://wa.me/628811118911`).  
- Author/medical reviewer byline.  
- “Last updated” timestamp.  
- JSON‑LD structured data (Article, FAQPage, MedicalWebPage).  
- Readability check (Flesch‑Kincaid appropriate for Bahasa Indonesia).  
- Mobile responsiveness check.  

### KPIs
- **Weekly**: 5 articles published, avg 1,000+ words, 3‑5 internal links/article, 5 FAQ sections, 5 WhatsApp CTAs.  
- **Monthly**: Organic traffic +25% (M1), +75% (M3), +150% (M6); Top‑10 keyword rankings: 3 → 10 → 20; AI citations: 1 → 3 → 5; Schema rich snippets: 5 → 15 → 25.  

---

## 5. Branding Assets

*Source: `joc-branding.json`*

| Asset | Details |
|-------|---------|
| Color Scheme | Light |
| Primary Color | `#7ED957` (green) |
| Secondary Color | `#489C23` (darker green) |
| Accent Color | `#FC9000` (orange) – used for primary CTAs |
| Background | `#FFFFFF` |
| Text Primary | `#212529` (dark gray) |
| Link Color | `#FC9000` |
| Fonts | Headings: Montserrat; Body: Open Sans |
| Logo | [https://www.joyofcare.net/web/image/website/1/logo/Joy%20of%20Care?unique=0f2033a](https://www.joyofcare.net/web/image/website/1/logo/Joy%20of%20Care?unique=0f2033a) (header, links to homepage) |
| Favicon | [https://www.joyofcare.net/web/image/website/1/favicon?unique=0f2033a](https://www.joyofcare.net/web/image/website/1/favicon?unique=0f2033a) |
| OG Image | [https://www.joyofcare.net/web/image/458-a2433bf7/33.jpg](https://www.joyofcare.net/web/image/458-a2433bf7/33.jpg) |
| Button Styles | Primary: Orange background (`#FC9000`), 9.6 px border radius; Secondary: Dark background (`#212529`), white text, 6.4 px radius. |

> **Note**: These assets should be applied consistently across the Odoo CMS, blog images, social media graphics, and email templates.  

---

## 6. Strategic Recommendations & Next Steps

| Area | Action | Owner | Timeline |
|------|--------|-------|----------|
| Technical SEO | Implement Phase 1 fixes (lang, JSON‑LD, meta titles, sitemap, llms.txt, robots). | Tech / SEO | Week 1 |
| Content Production | Rewrite & expand the 4 osteoporosis articles per the fixes in Section 2; add internal linking hub‑and‑spoke. | Writer | Week 1‑2 (parallel with tech fixes) |
| On‑Page Optimization | Apply Phase 2‑3 actions (H1, alt text, breadcrumbs, FAQ schema, author bios, statistics). | SEO / Writer | Week 2‑3 |
| Content Calendar Kick‑off | Begin Week 1 content production: 5 articles (panggil dokter ke rumah jakarta cluster). | Writer | Week 1 |
| Visual Assets | Create featured images & infographics for each new article (10 images/week target). | Visual | Ongoing |
| Publishing | Schedule & publish to Odoo CMS; verify in Search Console. | Publisher | Week 2+ (2‑week lag from creation) |
| Authority & Trust | Add medical reviewer bylines, PEROSI/WHO citations, disclaimer, SOP clips, doctor/nurse profiles. | Writer / SEO | Week 15‑16 (per calendar) |
| GEO/AIO | Publish GEO‑targeted FAQs (What is homecare?, BPJS coverage, pricing) and monitor AI citations. | Writer / SEO | Week 17‑18 |
| Brand Amplification | Launch YouTube, GBP, LinkedIn; start outreach for guest posts. | Visual / Writer | Week 4 |
| Monitoring & Reporting | Weekly traffic, keyword rankings, AI citation tracking; monthly KPI review. | SEO | Ongoing |

### Immediate Next Steps (Today)
1. Run a quick audit of the existing Odoo templates to confirm `lang="id"` is missing.  
2. Rename the four osteoporosis article files to their canonical slugs and strip the keyword leakage line.  
3. Draft the WhatsApp CTA HTML snippet and prepare to insert into all articles.  
4. Create a short internal‑linking map for the osteoporosis cluster (to be inserted during rewrite).  

All actions should be tracked in the shared Google Sheet `job_log` as the single source of truth, with explicit handoffs between Writer, SEO, Visual, and Publisher roles.  

---  

**Document Version:** 1.1  
**Last Updated:** 6 September 2026  
**Next Review:** 13 September 2026  
*© 2026 Joy of Care. All rights reserved.*  
*Brand: [joyofcare.net](https://www.joyofcare.net) | WhatsApp: [08811-118-911](https://wa.me/628811118911)*