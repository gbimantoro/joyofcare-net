# Headless CMS Evaluation for JoyofCare Web

## Executive Summary

**Recommended Stack: Astro + MDX + Keystatic**

After evaluating 6 headless CMS options against JoyofCare's requirements (static site generation, non-technical editors, SEO fields, category management, Indonesian language support, low cost), **Astro + MDX with Keystatic CMS** is the clear winner.

---

## Requirements Checklist

| Requirement | Astro+MDX+Keystatic | Next.js+Sanity | Hugo+Decap | Eleventy+Decap | Payload CMS | Keystatic Only |
|-------------|:------------------:|:--------------:|:----------:|:--------------:|:-----------:|:--------------:|
| Static site generation (SSG) | ✅ Native | ⚠️ Needs config | ✅ Native | ✅ Native | ❌ SSR | ✅ Native |
| Non-technical editor UX | ✅ Keystatic UI | ✅ Sanity Studio | ✅ Decap UI | ✅ Decap UI | ⚠️ Complex | ✅ Keystatic UI |
| Markdown/rich text editing | ✅ MDX + Visual | ✅ Rich text | ✅ Markdown | ✅ Markdown | ✅ Rich text | ✅ Markdown |
| SEO fields (title, meta, OG, canonical, slug) | ✅ Frontmatter | ✅ Schema fields | ✅ Frontmatter | ✅ Frontmatter | ✅ Fields | ✅ Frontmatter |
| Category/tag management | ✅ Content Collections | ✅ Reference fields | ✅ Collections | ✅ Collections | ✅ Collections | ✅ Collections |
| Image management + alt text | ✅ Assets + Fields | ✅ Asset pipeline | ✅ Media library | ✅ Media library | ✅ Uploads | ✅ Git-based |
| JSON-LD schema support | ✅ Components | ✅ Custom fields | ✅ Shortcodes | ✅ Custom | ✅ Hooks | ✅ Components |
| Indonesian language support | ✅ i18n ready | ✅ Localization | ✅ i18n | ✅ i18n | ✅ Localization | ⚠️ Manual |
| Free/low-cost | ✅ $0 CMS | ⚠️ $99+/mo | ✅ $0 CMS | ✅ $0 CMS | ✅ Self-hosted free | ✅ $0 CMS |
| Easy deployment (CF/Vercel/Netlify) | ✅ All platforms | ✅ Vercel native | ✅ All platforms | ✅ All platforms | ⚠️ Self-hosted | ✅ All platforms |

---

## Detailed Option Analysis

### 1. Astro + MDX + Keystatic ⭐ RECOMMENDED

**Overview:** Astro is a static-first framework that ships zero JavaScript by default. MDX allows Markdown with React components. Keystatic provides a visual admin UI for non-technical editors.

**Pros:**
- **Best performance:** Static HTML, zero JS bloat, perfect Core Web Vitals
- **Free forever:** No CMS subscription costs
- **Non-technical editor friendly:** Keystatic provides visual editing interface
- **Git-based content:** Full version control, no database needed
- **TypeScript schema:** Type-safe content collections with Zod validation
- **SEO-native:** Full control over meta tags, structured data, canonical URLs
- **Indonesian support:** i18n ready with content collections
- **Deploy anywhere:** Cloudflare Pages, Vercel, Netlify (all free tiers)
- **Medical content ready:** Perfect for JSON-LD Article, FAQ, MedicalWebPage schemas

**Cons:**
- Keystatic requires Node.js server for admin route (hybrid mode)
- Smaller ecosystem than WordPress
- Learning curve for developers new to Astro

**Cost:** $0/month (CMS + hosting on free tiers)

**Setup complexity:** Medium (2-3 days for developer)

---

### 2. Next.js + Sanity/Contentful

**Overview:** Next.js is a React framework with SSR/SSG. Sanity/Contentful are cloud-hosted headless CMS platforms.

**Pros:**
- Excellent developer experience
- Real-time collaboration (Sanity)
- Rich text editing with embeds
- Strong ecosystem

**Cons:**
- **Expensive:** Sanity Growth $99/mo, Contentful $300+/mo
- **Overkill:** SSR not needed for static blog content
- **Complex:** Requires React knowledge for both frontend and CMS customization
- **Vendor lock-in:** Content lives on their servers

**Cost:** $99-$300+/month

**Setup complexity:** High (1-2 weeks)

**Verdict:** ❌ Too expensive and complex for JoyofCare's needs

---

### 3. Hugo + Netlify/Decap CMS

**Overview:** Hugo is a fast static site generator written in Go. Decap CMS (formerly Netlify CMS) provides Git-based content management.

**Pros:**
- Extremely fast builds
- Mature ecosystem
- Free and open source
- Good Netlify integration

**Cons:**
- **YAML configuration:** Less intuitive than TypeScript schemas
- **Slower development:** Decap CMS development has slowed since 2023
- **Limited editor UX:** Not as polished as Keystatic
- **No MDX support:** Limited component embedding
- **Go templates:** Steeper learning curve for templating

**Cost:** $0/month

**Setup complexity:** Medium

**Verdict:** ⚠️ Viable but less modern than Astro + Keystatic

---

### 4. Eleventy + Decap CMS

**Overview:** Eleventy (11ty) is a simpler static site generator with flexible templating.

**Pros:**
- Very simple and flexible
- Multiple template languages
- Fast builds
- Free and open source

**Cons:**
- **Smaller community:** Less documentation and examples
- **Decap CMS limitations:** Same as Hugo + Decap
- **No native TypeScript:** Requires additional setup
- **Less SEO tooling:** Manual implementation needed

**Cost:** $0/month

**Setup complexity:** Medium

**Verdict:** ⚠️ Good but Astro offers better DX and performance

---

### 5. Payload CMS (Self-hosted)

**Overview:** Payload is an open-source, TypeScript-first headless CMS built on Next.js.

**Pros:**
- Full control over data
- TypeScript-first
- Self-hosted = data ownership
- Rich admin panel

**Cons:**
- **Complex setup:** Requires MongoDB/PostgreSQL, server management
- **Not static-first:** SSR by default, SSG requires configuration
- **DevOps burden:** Server maintenance, backups, security
- **Overkill for blog:** Too much infrastructure for content site
- **MongoDB dependency:** Additional complexity

**Cost:** $0 (self-hosted) + server costs ($5-20/mo)

**Setup complexity:** High (1-2 weeks + ongoing maintenance)

**Verdict:** ❌ Too complex for a startup blog content site

---

### 6. Keystatic (Standalone)

**Overview:** Keystatic is a Git-based CMS that stores content as Markdown/JSON/YAML files.

**Pros:**
- Free and open source
- TypeScript schema
- Visual editor for non-technical users
- No database required

**Cons:**
- **Requires framework:** Needs Astro, Next.js, or Remix as frontend
- **Newer project:** Smaller community (2.3k GitHub stars)
- **Limited features:** No advanced workflows or scheduling
- **GitHub dependency:** Limited to GitHub for collaboration features

**Cost:** $0 (free forever)

**Setup complexity:** Low-Medium

**Verdict:** ✅ Great CMS choice, but needs a framework (Astro recommended)

---

## Final Recommendation: Astro + MDX + Keystatic

### Why This Stack Wins

1. **Performance:** Astro ships zero JavaScript by default, ensuring perfect Core Web Vitals scores critical for SEO
2. **Cost:** Entire stack is free - no CMS subscription, no database, free hosting on Cloudflare Pages/Vercel
3. **Editor Experience:** Keystatic provides visual editing for the health team without requiring Git knowledge
4. **SEO Control:** Full frontmatter control for title, meta description, OG tags, canonical URLs, slugs
5. **Medical Content:** Perfect for JSON-LD Article, FAQ, and MedicalWebPage schemas
6. **Indonesian Support:** Content collections with i18n support
7. **Scalability:** Can grow from 40 to 400+ articles without performance degradation
8. **Deployment:** One-click deploy to Cloudflare Pages, Vercel, or Netlify

### Architecture

```
joyofcare-web/
├── src/
│   ├── content/
│   │   └── blog/           # MDX articles with frontmatter
│   │       ├── osteoporosis-guide.mdx
│   │       └── parkinson-care.mdx
│   ├── components/
│   │   ├── ArticleSchema.astro    # JSON-LD schema
│   │   ├── FAQ.astro              # FAQ component
│   │   └── WhatsAppCTA.astro      # CTA button
│   ├── layouts/
│   │   └── BlogLayout.astro       # SEO-optimized layout
│   └── pages/
│       ├── blog/
│       │   ├── index.astro        # Blog listing
│       │   └── [...slug].astro    # Dynamic article pages
│       └── keystatic/             # Admin UI route
├── keystatic.config.ts            # Keystatic schema
├── astro.config.mjs               # Astro config
└── package.json
```

### Keystatic Schema Example

```typescript
// keystatic.config.ts
import { config, fields, collection } from '@keystatic/core';

export default config({
  storage: { kind: 'github', repo: 'joyofcare/joyofcare-web' },
  collections: {
    blog: collection({
      label: 'Blog Articles',
      slugField: 'slug',
      path: 'src/content/blog/*',
      schema: {
        slug: fields.slug({ name: { label: 'Slug' } }),
        title: fields.text({ label: 'Title', validation: { isRequired: true } }),
        metaTitle: fields.text({ label: 'Meta Title (50-60 chars)' }),
        metaDescription: fields.text({ label: 'Meta Description (150-160 chars)' }),
        category: fields.select({
          label: 'Category',
          options: [
            { label: 'Healthy Aging', value: 'healthy-aging' },
            { label: 'Pengalaman', value: 'pengalaman' },
            { label: 'Studi Luar Negeri', value: 'studi-luar-negeri' },
            { label: 'Vaksinasi', value: 'vaksinasi' },
          ],
        }),
        author: fields.text({ label: 'Author', defaultValue: 'JoyofCare Medical Team' }),
        date: fields.date({ label: 'Publish Date' }),
        featuredImage: fields.image({
          label: 'Featured Image',
          publicPath: '/images/',
        }),
        body: fields.mdx({ label: 'Content', description: 'Article body in MDX' }),
      },
    }),
  },
});
```

### Article Frontmatter (MDX)

```markdown
---
title: "Panduan Fisioterapi di Rumah untuk Pasien Osteoporosis"
metaTitle: "Panduan Fisioterapi Osteoporosis | JoyofCare"
metaDescription: "Panduan lengkap fisioterapi di rumah untuk pasien osteoporosis. Kurangi nyeri dan cegah jatuh dengan latihan yang tepat. Konsultasi gratis via WhatsApp."
slug: "panduan-fisioterapi-osteoporosis"
category: "healthy-aging"
date: 2026-09-05
author: "Dr. Sarah Wijaya, Sp.FR"
featuredImage: "/images/osteoporosis-physiotherapy.jpg"
keywords: ["fisioterapi osteoporosis", "latihan osteoporosis", "fisioterapi rumah"]
---

## Mengapa Fisioterapi Penting untuk Osteoporosis?

Pada penderita osteoporosis, latihan fisik bertujuan untuk menstimulasi pembentukan tulang...

## Prinsip Gerakan Fisioterapi yang Aman

### 1. Latihan Beban (Weight-Bearing Exercise)

Berjalan kaki santai, marching on the spot...

## FAQ

**Q: Berapa kali seminggu harus melakukan fisioterapi?**
A: Minimal 3-4 kali seminggu dengan durasi 30-45 menit per sesi.

**Q: Apakah fisioterapi bisa dilakukan di rumah?**
A: Ya, dengan panduan yang tepat dari fisioterapis profesional.

---

Butuh bantuan? [Konsultasi Gratis via WhatsApp](https://api.whatsapp.com/send/?phone=628811118911)
```

### JSON-LD Schema Component

```astro
---
// src/components/ArticleSchema.astro
const { title, description, url, image, datePublished, author } = Astro.props;
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalWebPage",
  "name": "{title}",
  "description": "{description}",
  "url": "{url}",
  "image": "{image}",
  "datePublished": "{datePublished}",
  "author": {
    "@type": "Organization",
    "name": "JoyofCare"
  },
  "publisher": {
    "@type": "Organization",
    "name": "JoyofCare",
    "logo": {
      "@type": "ImageObject",
      "url": "https://joyofcare.net/logo.png"
    }
  }
}
</script>
```

---

## Implementation Timeline

| Phase | Duration | Tasks |
|-------|----------|-------|
| **Phase 1: Setup** | 2-3 days | Astro project, Keystatic config, content collections |
| **Phase 2: Templates** | 2-3 days | Blog layout, article template, category pages |
| **Phase 3: Migration** | 3-4 days | Convert 37 articles to MDX, setup SEO fields |
| **Phase 4: Schema** | 1-2 days | JSON-LD Article, FAQ, MedicalWebPage schemas |
| **Phase 5: Testing** | 1-2 days | SEO audit, performance testing, editor training |
| **Total** | **9-14 days** | Full production-ready blog |

---

## Cost Comparison (Annual)

| Option | CMS Cost | Hosting | Total Year 1 |
|--------|----------|---------|--------------|
| **Astro + Keystatic** | $0 | $0 (free tier) | **$0** |
| Hugo + Decap | $0 | $0 (free tier) | $0 |
| Next.js + Sanity | $1,188/yr | $0 (Vercel free) | $1,188 |
| Next.js + Contentful | $3,600/yr | $0 (Vercel free) | $3,600 |
| Payload (self-hosted) | $0 | $60-240/yr (VPS) | $60-240 |

---

## Conclusion

**Astro + MDX + Keystatic** is the optimal choice for JoyofCare because:

1. **Zero cost** - No CMS subscription, no database, free hosting
2. **Best SEO** - Static HTML with full control over meta tags and structured data
3. **Non-technical friendly** - Keystatic provides visual editing for the health team
4. **Medical content ready** - Perfect for Article, FAQ, and MedicalWebPage schemas
5. **Indonesian support** - i18n ready with content collections
6. **Scalable** - Can handle 40 to 4000+ articles without performance issues
7. **Future-proof** - Modern stack with active development and community

**Next Steps:**
1. Approve this recommendation
2. Create proof-of-concept with 3 sample articles
3. Train health team on Keystatic editor
4. Migrate all 37 existing articles
5. Deploy to Cloudflare Pages

---

*Document prepared by JoC Tech | September 2026*
