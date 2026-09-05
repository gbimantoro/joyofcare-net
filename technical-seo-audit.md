# Technical SEO Audit: joyofcare.net Blog

**Date:** September 5, 2026  
**Target:** https://www.joyofcare.net/blog  
**Platform:** Odoo CMS  
**Total Blog Articles:** ~41 (indexed in sitemap)

---

## Executive Summary

The JoyofCare blog is built on Odoo CMS and has solid foundational SEO elements in place (canonical tags, OG tags, Open Graph images, proper heading hierarchy). However, there are several critical gaps that are holding back search visibility: **missing JSON-LD structured data**, **missing meta description on the blog listing page**, **thin content on articles**, **a robots.txt sitemap URL using HTTP instead of HTTPS**, and **no internal linking between blog articles**. Addressing these issues will significantly improve crawlability, indexability, and rich snippet eligibility.

---

## 1. Meta Tags (Title, Description, OG Tags)

### Blog Listing Page (`/blog`)
| Element | Status | Value |
|---------|--------|-------|
| Title | ✅ Present | `Blog Posts | Joy of Care` |
| Meta Description | ❌ **MISSING** | Not set |
| OG Title | ✅ Present | `Blog Posts | Joy of Care` |
| OG Description | ❌ **MISSING** | Not set |
| OG Image | ✅ Present | Logo image |
| Twitter Card | ✅ Present | `summary_large_image` |

### Sample Articles
| Article | Title | Meta Desc | OG Tags |
|---------|-------|-----------|---------|
| Panduan Fisioterapi Osteoporosis | ✅ `Fisioterapi di Rumah Osteoporosis | JoyofCare` | ✅ Present (155 chars) | ✅ Complete |
| Jenis Terapi Osteoporosis | ✅ `Terapi Osteroporosis Lengkap : Infus Nyaman di Rumah | JoyofCare` | ✅ Present (131 chars) | ✅ Complete |
| Bahaya Komplikasi Osteoporosis | ✅ `Bahaya komplikasi Osteoporosis dan Faktor Resiko | JoyofCare` | ✅ Present (91 chars) | ✅ Complete |
| Layanan Terapi Infus | ✅ `Homecare Terapi Injeksi Infus Osteoporosis | JoyofCare` | ✅ Present (147 chars) | ✅ Complete |

### Issues Found
- **Blog listing page has NO meta description** — Google will auto-generate one, often pulling irrelevant text
- **Blog listing OG description is missing** — poor social sharing preview
- **Title tag inconsistency**: Some articles use `JoyofCare` (no space), others `Joy of Care` — should be consistent
- **Typo in title**: "Terapi **Osteroporosis** Lengkap" — should be "Osteoporosis"
- **Meta descriptions are generic** — some are too short (91 chars) and don't include a call-to-action
- **`og:type` correctly set to `article`** on blog posts and `website` on listing — good

---

## 2. URL Structure & Slugs Quality

### Current URL Pattern
```
/blog/{category-slug}/{article-slug}-{numeric-id}
```

### Analysis
| Aspect | Rating | Notes |
|--------|--------|-------|
| Category in URL | ⚠️ Concern | `healthy-aging-3`, `vaksinasi-di-rumah-2`, `studi-luar-negeri-4` — numeric suffixes (`-3`, `-2`, `-4`) are auto-generated and confusing |
| Article slugs | ⚠️ Mixed | Some are excellent but very long; numeric IDs at end (`-43`, `-40`) are unnecessary |
| Readability | ⚠️ Fair | Indonesian slugs are SEO-friendly for the target market, but the numeric suffixes add clutter |
| URL length | ❌ Long | Some URLs exceed 100+ characters |

### Recommended Improvements
- Remove auto-generated numeric IDs from category and article slugs
- Keep URLs under 75 characters where possible
- Use `healthy-aging` instead of `healthy-aging-3`
- Use shorter, keyword-focused slugs

---

## 3. Schema Markup (Article, FAQ, MedicalWebPage)

| Schema Type | Status | Notes |
|-------------|--------|-------|
| JSON-LD | ❌ **NOT FOUND** | No `<script type="application/ld+json">` on any page checked |
| Article schema | ❌ Missing | No `Article`, `BlogPosting`, or `MedicalWebPage` markup |
| FAQ schema | ❌ Missing | Article about osteoporosis therapy has FAQ section but no `FAQPage` schema |
| BreadcrumbList | ❌ Missing | No breadcrumb structured data |
| Organization | ❌ Missing | No `Organization` or `LocalBusiness` schema |

### Impact
This is a **critical gap**. Without structured data:
- No rich snippets (FAQ dropdowns, article previews) in Google search results
- No eligibility for Google's "Medical content" enriched results
- No breadcrumb trail in SERPs
- Reduced authority signals for YMYL (Your Money Your Life) health content

### Recommendation
Add JSON-LD for:
1. `Article` or `MedicalWebPage` on every blog post
2. `FAQPage` on articles with FAQ sections (e.g., the osteoporosis therapy article)
3. `Organization` + `LocalBusiness` on the homepage
4. `BreadcrumbList` site-wide

---

## 4. Internal Linking Structure

### Current State
| Link Type | Status | Details |
|-----------|--------|---------|
| Blog listing to articles | ✅ Good | All articles linked from listing pages with pagination (4 pages) |
| Article to next/prev article | ⚠️ Limited | Each article links to only 1 related article (next in sequence) |
| Article to category page | ✅ Present | Category links available |
| Article to other articles | ❌ **Very Weak** | Only 1 outbound article link per post — no contextual cross-linking |
| Sidebar "related articles" | ⚠️ Generic | "Artikel Kesehatan" snippet appears but seems template-driven |

### Issues
- **No contextual internal links within article body** — articles don't link to related osteoporosis/Parkinson articles
- **No "Related Articles" widget** with topic-matched suggestions
- **No pillar/cluster linking strategy** — the osteoporosis articles (4 posts) should interlink heavily
- Footer CTA links are generic, not article-specific

### Recommendation
- Add 2-3 contextual internal links per article body linking to related posts
- Create topic clusters: link all osteoporosis articles together, all Parkinson articles together
- Add a "Related Articles" section at the bottom of each post

---

## 5. Sitemap.xml Blog Article Coverage

### Sitemap Analysis
| Metric | Value |
|--------|-------|
| Total URLs in sitemap | 61 |
| Blog articles (non-feed) | 41 |
| Blog feed URLs | 4 (one per category) |
| Service/landing pages | ~16 |

### Coverage by Category
| Category | Article Count |
|----------|---------------|
| Healthy Aging | 27 |
| Studi Luar Negeri | 7 |
| Vaksinasi di Rumah | 2 |
| Pengalaman | 1 |

### Issues
- **RSS feed URLs included in sitemap** — should be removed; feeds are not indexable content
- **Sitemap uses HTTP URLs** (`http://www.joyofcare.net/sitemap.xml`) while the site uses HTTPS — inconsistent
- **No sitemap index** — with 61 URLs it's fine now, but should use sitemap index as content grows
- **No `<lastmod>` accuracy** — many articles show the same date despite different content

### Recommendation
- Remove feed URLs from sitemap
- Update sitemap to use HTTPS URLs
- Add `<lastmod>` timestamps that reflect actual content updates

---

## 6. Robots.txt Configuration

### Current Content
```
User-agent: *
Sitemap: http://www.joyofcare.net/sitemap.xml
```

### Issues
- **Sitemap URL uses HTTP instead of HTTPS** — should be `https://www.joyofcare.net/sitemap.xml`
- **No Disallow rules** — the site doesn't block any paths, which is fine, but there's no protection against crawling admin or internal Odoo paths
- **No Crawl-delay** — acceptable for a small site
- **No specific user-agent rules** — could add rules for AI crawlers if desired

### Recommendation
- Fix the sitemap URL to HTTPS
- Consider adding `Disallow: /web/` to prevent crawling of Odoo backend assets
- Consider adding `Disallow: /id/` if the `/id/` prefix is just a language redirect (see Duplicate Content section)

---

## 7. Canonical Tags

| Page | Canonical | Status |
|------|-----------|--------|
| Blog listing (`/blog`) | `https://www.joyofcare.net/blog` | ✅ Correct |
| Article: Fisioterapi Osteoporosis | `https://www.joyofcare.net/blog/healthy-aging-3/...43` | ✅ Correct |
| Article: Jenis Terapi | `https://www.joyofcare.net/blog/healthy-aging-3/...40` | ✅ Correct |
| Article: Bahaya Komplikasi | `https://www.joyofcare.net/blog/healthy-aging-3/...41` | ✅ Correct |
| Article: Layanan Infus | `https://www.joyofcare.net/blog/healthy-aging-3/...42` | ✅ Correct |
| `/id/blog` (Indonesian prefix) | `https://www.joyofcare.net/id/blog` | ⚠️ Potential issue |

### Issues
- **Canonical tags are present and self-referencing** — good
- **⚠️ Duplicate content concern**: `/id/blog` exists as a separate URL with its own canonical (`/id/blog`). This creates a duplicate of `/blog` unless properly handled with `hreflang` tags
- **No `hreflang` tags found** — if the site serves both `/id/` and non-`/id/` versions, there should be hreflang declarations

### Recommendation
- Verify whether `/id/` is needed or if it's an Odoo language redirect artifact
- If both versions exist, add `hreflang` tags linking them
- If `/id/` is unnecessary, add `noindex` or 301 redirect to the canonical version

---

## 8. Open Graph & Twitter Card Tags

### Blog Listing Page
| Tag | Value | Status |
|-----|-------|--------|
| `og:type` | `website` | ✅ |
| `og:title` | `Blog Posts | Joy of Care` | ✅ |
| `og:url` | `https://www.joyofcare.net/blog` | ✅ |
| `og:image` | Logo image | ⚠️ Generic — should use a blog-specific banner |
| `og:description` | — | ❌ **MISSING** |
| `twitter:card` | `summary_large_image` | ✅ |
| `twitter:title` | `Blog Posts | Joy of Care` | ✅ |
| `twitter:image` | Logo (300x300) | ⚠️ Small for large image card |
| `twitter:description` | — | ❌ **MISSING** |

### Article Pages
| Tag | Status | Notes |
|-----|--------|-------|
| `og:type` | ✅ `article` | Correct |
| `og:title` | ✅ Present | Matches article topic |
| `og:description` | ✅ Present | Matches meta description |
| `og:image` | ✅ Present | Article-specific cover images (webp format) |
| `article:published_time` | ✅ Present | ISO format |
| `article:modified_time` | ✅ Present | ISO format |
| `twitter:card` | ✅ `summary_large_image` | Good |
| `twitter:title` | ✅ Present | — |
| `twitter:description` | ✅ Present | — |
| `twitter:image` | ✅ Present | Same as OG image |

### Issues
- **Blog listing page missing OG and Twitter descriptions**
- **OG image on listing is just the logo** — should be a branded blog banner
- **Twitter image is 300x300** — `summary_large_image` card works better with 1200x630 images

---

## 9. Mobile Responsiveness Signals

| Signal | Status | Details |
|--------|--------|---------|
| Viewport meta tag | ✅ Present | `width=device-width, initial-scale=1` |
| Responsive framework | ✅ Yes | Odoo's website builder is responsive by default |
| Mobile-friendly test | ⚠️ Not tested | Would need Google's Mobile-Friendly Test tool |
| Image lazy loading | ✅ Present | `loading="lazy"` on images |

### Observations
- The Odoo platform generates responsive HTML with proper viewport configuration
- No `AMP` version detected — not critical but an option for health content
- Image `loading="lazy"` is present — good for mobile performance

---

## 10. Page Speed Indicators

| Metric | Value | Assessment |
|--------|-------|------------|
| TTFB (Time to First Byte) | 387ms | ⚠️ Fair — could be faster (target: <200ms) |
| Total load time | 422ms | ✅ Good |
| Page size (HTML) | ~67KB | ✅ Reasonable |
| HTTP/2 | ✅ Yes | Modern protocol |
| HSTS | ✅ Enabled | `max-age=31536000; includeSubDomains` |
| X-Content-Type-Options | ✅ nosniff | Good security header |

### Performance Notes
- The site is served over HTTP/2 with HSTS — good security posture
- TTFB of 387ms is acceptable but not optimal; consider CDN or server-side caching
- HTML payload is reasonable for an Odoo site
- Lazy loading is implemented on images — positive signal

---

## 11. Duplicate Content Concerns

### `/id/` Prefix Issue
The site appears to have an Indonesian language version at `/id/blog` which:
- Returns HTTP 200
- Has its own canonical tag pointing to `/id/blog`
- Does NOT have `hreflang` tags linking it to the English version

This creates a **potential duplicate content issue** where Google may index both versions and split ranking signals.

### Recommendation
- Add `hreflang` tags: `<link rel="alternate" hreflang="id" href="https://www.joyofcare.net/id/blog" />` and `<link rel="alternate" hreflang="en" href="https://www.joyofcare.net/blog" />`
- Or redirect `/id/` to the main version if only one language is needed

---

## 12. Local Article Files SEO Review

The 4 articles in `/drive_articles/` have the following SEO characteristics:

| Article | Word Count | Target Keywords | SEO Quality |
|---------|-----------|-----------------|-------------|
| Bahaya Komplikasi Osteoporosis | 365 | ✅ 4 keywords defined | ⚠️ Thin content |
| Jenis Terapi Osteoporosis | 435 | ✅ 4 keywords defined | ⚠️ Thin content |
| Layanan Terapi Infus | 355 | ✅ 4 keywords defined | ⚠️ Thin content |
| Panduan Fisioterapi Osteoporosis | 345 | ✅ 4 keywords defined | ⚠️ Thin content |

### Issues
- **All articles are thin content** (345-435 words) — Google favors comprehensive content (1,500+ words for YMYL health topics)
- **No FAQ sections** in the draft files (though one published article does have FAQ)
- **No internal link placeholders** — articles don't reference other related content
- **No image alt text specifications** — articles have images but no alt text guidance
- **Good**: Each article has defined target keywords and search intent

### Recommendation
- Expand each article to 1,500-2,500 words for YMYL health content
- Add FAQ sections with schema markup
- Include 2-3 internal links to related articles
- Add image alt text with target keywords
- Include author byline and medical reviewer attribution (E-E-A-T signals)

---

## Priority Action Items

### Critical (Do This Week)
1. **Add JSON-LD structured data** — Article, FAQPage, and Organization schemas on all pages
2. **Add meta description to blog listing page** — it's completely missing
3. **Fix robots.txt sitemap URL** — change from `http://` to `https://`
4. **Remove RSS feed URLs from sitemap**

### High Priority (This Month)
5. **Add hreflang tags** for `/id/` and non-`/id/` versions
6. **Fix the "Osteroporosis" typo** in the article title
7. **Improve internal linking** — add 2-3 contextual links per article
8. **Expand thin articles** to 1,500+ words for YMYL compliance
9. **Remove numeric IDs from category and article slugs** (URL restructuring)

### Medium Priority (Next Quarter)
10. **Add BreadcrumbList schema** site-wide
11. **Create topic clusters** with pillar pages for osteoporosis, Parkinson, and vaccination
12. **Optimize OG images** — use 1200x630 branded banners instead of logos
13. **Add `twitter:site` and `twitter:creator`** meta tags
14. **Implement FAQ schema** on articles with Q&A sections

---

## Technical Summary

| Category | Score | Status |
|----------|-------|--------|
| Meta Tags | 7/10 | Good on articles, missing on listing |
| URL Structure | 5/10 | Functional but cluttered with IDs |
| Schema Markup | 1/10 | **Critical gap** — none found |
| Internal Linking | 3/10 | Very weak cross-linking |
| Sitemap Coverage | 7/10 | Good coverage, minor issues |
| Robots.txt | 6/10 | Works but HTTP sitemap URL |
| Canonical Tags | 8/10 | Present and correct |
| OG/Twitter Tags | 7/10 | Good on articles, missing on listing |
| Mobile | 7/10 | Responsive via Odoo, needs live testing |
| Page Speed | 6/10 | Acceptable TTFB, room for improvement |
| **Overall** | **5.7/10** | **Solid foundation with critical gaps** |

---

*Audit performed on September 5, 2026 using live site analysis, HTML source inspection, sitemap analysis, and local file review.*
