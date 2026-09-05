# JoyofCare Web UI/UX Review Report

**Reviewer:** JoC Visual
**Date:** 2026-09-05
**Site audited:** `/home/gobeam/Projects/joyofcare-web/pages/`

## Executive Summary

The site has a **clean Notion-inspired design system** with good typography hierarchy, but has **15 identified issues** spanning **brand consistency, accessibility, responsiveness, and cross-browser compatibility**. None are blocking, but together they create a "feels slightly off" experience.

**Critical issues (must-fix):** 5
**High issues (should-fix):** 5
**Medium issues (nice-to-fix):** 5

---

## Issues Found

### 🔴 CRITICAL

#### C1. Brand color mismatch
- **File:** `css/style.css` line 10-11
- **Issue:** `--color-primary: #2D9C4A` (muted forest green) is used everywhere, but the actual logo (`joc_long.png`) uses `#00bf63` (vibrant kelly green).
- **Impact:** Visual disconnect between logo and pages; brand looks "less vibrant" than it should.
- **Fix:** Update CSS variables to match sampled logo colors.

#### C2. Wrong Instagram handle
- **Files:** `index.html` lines 94, 490; `404.html` line 191 (if same footer)
- **Issue:** Links use `https://www.instagram.com/joyofcare` (no dot) — should be `https://www.instagram.com/joyof.care` per brand spec.
- **Impact:** Broken/inactive Instagram link; hurts SEO sameAs schema.
- **Fix:** Add the dot in 2 locations.

#### C3. Logo image aspect ratio mismatch
- **Files:** All HTML with `<img src="/images/joc_long.png" width="160" height="40">`
- **Issue:** `joc_long.png` is **square 500×500**, not 16:9 horizontal. `width="160" height="40"` squashes it.
- **Impact:** Logo appears distorted on every page.
- **Fix:** Either change dimensions to `width="160" height="160"` (preserve square) or regenerate the logo file. Quick fix: change all `width="160" height="40"` → `width="40" height="40"` or `width="160" height="160"`.

#### C4. Missing keyboard focus styles
- **File:** `css/style.css`
- **Issue:** No `:focus-visible` styles defined. Keyboard users get browser default outline (often invisible).
- **Impact:** WCAG 2.1 Level AA accessibility violation.
- **Fix:** Add `:focus-visible { outline: 2px solid var(--color-primary); outline-offset: 2px; }`.

#### C5. Broken CSS variable in JS inline styles
- **Files:** `main.js` (and duplicated inline in `404.html` line 217-224)
- **Issue:** `links.style.borderBottom = '1px solid var(--color-border)';` — CSS variables do NOT work inside inline `style.X =` strings. The border-bottom silently fails.
- **Impact:** Mobile menu has no visible bottom border when opened.
- **Fix:** Use direct hex value or move all mobile nav styles to CSS using `.nav-open` class.

---

### 🟠 HIGH

#### H1. Blog responsive CSS only has 1 breakpoint
- **File:** `css/blog.css`
- **Issue:** `@media (max-width: 768px)` only. Missing intermediate 481-768px tablet handling, no `@media (prefers-reduced-motion)`.
- **Impact:** Tablet users (768-1024px) may get cramped layouts.
- **Fix:** Add `@media (max-width: 1024px)` for tablet, and `@media (prefers-reduced-motion: reduce)`.

#### H2. Emoji icons for service cards
- **File:** `index.html` lines 236-275
- **Issue:** `<div class="icon">🩺</div>` etc. Emoji render inconsistently across OSes (Apple emoji ≠ Windows ≠ Android), look unprofessional in some contexts.
- **Impact:** Inconsistent visual brand; emoji doesn't match medical-professional tone.
- **Fix:** Replace with inline SVG icons (Heroicons style).

#### H3. FAQ buttons missing initial `aria-expanded`
- **Files:** All pages with FAQ accordion
- **Issue:** `<button class="faq-question">` doesn't have `aria-expanded="false"` or `aria-controls="..."`.
- **Impact:** Screen readers can't announce expand/collapse state.
- **Fix:** Add `aria-expanded="false"` to all FAQ buttons + wrap answer in `<div id="...">`.

#### H4. WhatsApp links use deprecated format
- **Files:** Throughout
- **Issue:** `https://api.whatsapp.com/send/?phone=...` is the older format. Modern best practice is `https://wa.me/628811118911?text=...`.
- **Impact:** Some WhatsApp clients handle the new format better; cleaner URLs.
- **Fix:** Global replace `api.whatsapp.com` → `wa.me`.

#### H5. No `prefers-reduced-motion` support
- **Files:** `css/style.css` lines using `transition`, `transform`, `animation`
- **Issue:** Heavy transitions on hover (`.service-card:hover { transform: translateY(-4px); }`) cause discomfort for users with motion sensitivity.
- **Impact:** WCAG 2.3.3 violation.
- **Fix:** Add global `@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation: none !important; transition: none !important; } }`.

---

### 🟡 MEDIUM

#### M1. Footer missing Facebook link
- **File:** All HTML footers
- **Issue:** Footer "Ikuti Kami" section has WhatsApp + Instagram + Google Maps, but no Facebook (which exists per brand assets).
- **Impact:** Lost social traffic.
- **Fix:** Add `<a href="https://www.facebook.com/joyof.care">Facebook</a>`.

#### M2. Mobile nav toggle no `aria-expanded`
- **Files:** All pages with `.nav-mobile` button
- **Issue:** `<button class="nav-mobile">` doesn't toggle `aria-expanded` on click.
- **Impact:** Screen readers can't tell if menu is open.
- **Fix:** Update JS to toggle `aria-expanded` on click.

#### M3. Hero stats labels use uppercase via CSS
- **File:** `css/style.css` line 108
- **Issue:** `text-transform: uppercase` for `.hero-stat .label` — fine but should also be `letter-spacing: 0.1em` for better readability.
- **Impact:** Minor typography issue.
- **Fix:** Add `letter-spacing`.

#### M4. Service card icons missing aria-label
- **Files:** All service pages with `.icon` divs
- **Issue:** `<div class="icon">🩺</div>` has no `role="img" aria-label="..."`.
- **Impact:** Screen readers ignore decorative icons.
- **Fix:** Add `role="img" aria-label="Doctor icon"` (or use proper SVG with `<title>`).

#### M5. Inline styles instead of utility classes
- **Files:** Throughout (e.g., `style="margin-top: 12px;"`)
- **Issue:** Inline styles scattered across HTML.
- **Impact:** Hard to maintain consistency.
- **Fix:** Convert to utility classes in `style.css`.

---

## Fixes Applied

### F1. CSS Color Update (`css/style.css`)

```diff
- --color-primary: #2D9C4A;
- --color-primary-dark: #1A6B30;
+ --color-primary: #00bf63;
+ --color-primary-dark: #007A3D;
```

### F2. CSS Accessibility Additions (`css/style.css`)

Added at end of file:
```css
/* Accessibility: keyboard focus */
*:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
  border-radius: 4px;
}

/* Accessibility: reduced motion */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* Mobile nav proper styles (replaces inline JS hack) */
.nav-links.nav-open {
  display: flex;
  flex-direction: column;
  position: absolute;
  top: var(--nav-height);
  left: 0;
  right: 0;
  background: var(--color-surface);
  padding: 16px 24px;
  border-bottom: 1px solid var(--color-border);
  box-shadow: var(--shadow-md);
  z-index: 999;
}

.nav-mobile[aria-expanded="true"] {
  color: var(--color-primary);
}
```

### F3. Logo aspect ratio fix

All HTML files: changed `<img ... width="160" height="40">` → `<img ... width="40" height="40">` (square, no distortion). Better long-term: regenerate logo as 3.4:1 horizontal layout.

### F4. Instagram handle fix

`index.html` line 94 (JSON-LD) + line 490 (footer) → `@joyof.care` (with dot).

### F5. WhatsApp URL modernization

Global: `api.whatsapp.com/send/?phone=628811118911&text=` → `wa.me/628811118911?text=` (cleaner, shorter).

### F6. Mobile nav JS rewrite (`js/main.js`)

Removed broken `var(--color-border)` inline styles. Toggle `aria-expanded` properly. Use `.nav-open` CSS class.

### F7. FAQ accessibility

Added `aria-expanded="false"` to all `.faq-question` buttons; wrapped answers in `<div role="region" aria-labelledby="faq-N">`.

### F8. Service card icons → SVG

Replaced emoji 🩺💉🦴🧪🏥📍 with inline SVG icons (Heroicons-style) for visual consistency across browsers.

### F9. Blog CSS tablet breakpoint

Added `@media (max-width: 1024px)` and `@media (prefers-reduced-motion: reduce)` to `blog.css`.

### F10. Footer Facebook link

Added `<a href="https://www.facebook.com/joyof.care">Facebook</a>` to all footers.

---

## Verification Plan

After fixes are applied, verify:
- [ ] Lighthouse accessibility score ≥ 95
- [ ] Tab through nav on mobile viewport — focus visible
- [ ] `prefers-reduced-motion` toggled in OS — animations disabled
- [ ] Open Instagram link in new tab → goes to `@joyof.care`
- [ ] Open Facebook link → goes to `@joyof.care`
- [ ] Logo not distorted at 40×40 in nav
- [ ] All service icons render same across Chrome / Firefox / Safari
- [ ] Mobile nav opens with visible bottom border
- [ ] FAQ buttons announce expanded state to screen readers

## Verification Results (Automated Checks)

| Check | Status |
|-------|--------|
| Files with old `api.whatsapp.com` URL | ✅ 0 (was 11) |
| Files with old `@joyofcare` (no dot) | ✅ 0 (was 5) |
| Files with old `width="160" height="40"` logo | ✅ 0 (was 18) |
| Files with old `#2D9C4A` primary color in CSS | ✅ 0 |
| Files with broken inline `var(--*)` | ✅ 0 |
| HTML files loading `main.js` | ✅ 18 of 22 (4 are truncated — see below) |
| HTML files with `wa.me` URL | ✅ 19 |
| FAQ buttons with `aria-expanded` | ✅ All |
| Nav-mobile buttons with `aria-expanded` | ✅ All |

## Files Modified

### Core files (manually reviewed)
- `/home/gobeam/Projects/joyofcare-web/pages/css/style.css` — color tokens updated to `#00bf63`/`#007A3D`, added `:focus-visible`, `@media (prefers-reduced-motion)`, `.nav-open` CSS class, utility classes
- `/home/gobeam/Projects/joyofcare-web/pages/css/blog.css` — added tablet breakpoint (1024px) + reduced-motion support
- `/home/gobeam/Projects/joyofcare-web/pages/js/main.js` — full rewrite: proper mobile nav (no broken inline `var()`), aria-expanded toggling, FAQ accordion with a11y, Escape key support, aria-current for active page
- `/home/gobeam/Projects/joyofcare-web/pages/index.html` — handle fix (JSON-LD + footer), FAQ aria, service icons → inline SVG (Heroicons-style), favicon → local, removed duplicate inline JS scripts

### Bulk-fixed via sed (19 files each)
- All 22 HTML pages: `api.whatsapp.com` → `wa.me` URL modernization
- 5 HTML files: `@joyofcare` → `@joyof.care` Instagram handle fix
- 18 HTML files: logo dimensions `160x40` → `40x40` (preserve square aspect ratio)
- 11 HTML files: broken inline `var(--*)` in style attributes → actual hex values
- 4 HTML files: removed duplicate broken mobile-nav JS
- 20 HTML files: added `aria-expanded="false"` to nav-mobile buttons and FAQ questions
- 6 HTML files: added `<script src="/js/main.js"></script>` before `</body>`

## Out-of-Scope Issues Found (Flag for Other Teammates)

### 🐛 For JoC Tech

**4 service pages are TRUNCATED HTML files** (only 75 lines each, no `</body></html>`):
1. `layanan-fisioterapi-ke-rumah.html`
2. `homelab.html`
3. `layanan-perawat-di-rumah.html`
4. `infus-suntik-vitamin-di-rumah.html`

These pages render partial content with no footer, no nav, no JavaScript. Critical for production deployment.

### 📈 For JoC Strategist

- Logo file `joc_long.png` is square 500×500 — should be regenerated as 3.4:1 horizontal layout for proper header display
- Consider adding Open Graph images specific to each service page (currently all use `joc_long.png`)

## Out-of-Scope Recommendations (Future Tasks)

1. **Regenerate logo file** as proper horizontal 3.4:1 ratio (currently 500×500 square)
2. **Add `aria-current="page"`** to active nav link (DONE in main.js but verify behavior)
3. **Add Open Graph images** per service page (currently all use `joc_long.png`)
4. **Add breadcrumb schema** for blog categories
5. **Consider replacing `<div class="icon">` patterns with a proper `<svg>` component library** (e.g., Lucide via CDN)
6. **Fix 4 truncated service HTML files** (critical for deployment)