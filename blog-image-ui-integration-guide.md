# Blog Image UI Integration Guide — JoC Visual × JoC Writer

**Tanggal:** 2026-09-06
**Penulis:** JoC Visual
**Status:** IMPLEMENTED di `joyofcare-web/pages/blog/` — panduan ini mendokumentasikan apa yang sudah terpasang + spesifikasi untuk 172 halaman artikel.

---

## 0. Koreksi Palet (PENTING)

Katalog Writer mencantumkan `#2D9C4A` / `#1A6B30`. Palet tersebut **sudah tidak dipakai**. Warna truth dari sampling piksel logo resmi `joc_long.png`:

| Peran | Hex |
|---|---|
| Brand Primary | **#00bf63** |
| Brand Dark | **#007A3D** |
| Brand Accent (CTA) | **#FC9000** |
| Brand Light | #7ED957 |
| Medical Secondary (teal) | #0E7490 |

Keenam banner kategori (termasuk 4 yang lama) sudah di-recolor ke palet ini di kedua repo (`joyofcare-net/visual-assets/thumbnails/` dan `joyofcare-web/assets/blog/`). Mohon gunakan hex ini untuk konten baru.

---

## 1. Aset Baru yang Dikirim (deliverable a)

| File | Ukuran | Lokasi |
|---|---|---|
| `osteoporosis.svg` (recolor) | 1200×630, 8.1 KB | `assets/blog/osteoporosis.svg` |
| `parkinson.svg` (baru) | 1200×630, 6.1 KB | `assets/blog/parkinson.svg` |

**Desain `parkinson.svg`:** mengikuti bahasa visual banner kategori yang sudah ada — blok konten kiri (badge KATEGORI BLOG → judul 2 baris → subtitle → 3 bullet → CTA pill oranye) + ilustrasi kanan berupa glow-disc dengan **jaringan neuron** (tema neuromotor), garis pulse aktivitas (progres fisioterapi), dua hati tumpang-tindih (dukungan keluarga), chip check/plus, dan tag "12 Artikel". Footer brand `Joy of Care` + `joyofcare.net/blog/parkinson`. Aria-label + `<title>`/`<desc>` untuk aksesibilitas.

Seluruh 6 banner kini: `healthy-aging.svg`, `osteoporosis.svg`, `parkinson.svg`, `pengalaman-pasien.svg`, `studi-luar-negeri.svg`, `vaksinasi.svg` — semuanya 1200×630, <10 KB, jauh di bawah target 150 KB.

---

## 2. Pemetaan Kategori → Aset Gambar (final)

| `data-category` | Card Thumbnail + Hero | Tipe |
|---|---|---|
| `perawatan-lansia` | `/assets/blog/healthy-aging.svg` | SVG banner |
| `osteoporosis` | `/assets/blog/osteoporosis.svg` | SVG banner |
| `parkinson` | `/assets/blog/parkinson.svg` | SVG banner |
| `vaksinasi-rumah` | `/assets/blog/vaksinasi.svg` | SVG banner |
| `studi-luar-negeri` | `/assets/blog/studi-luar-negeri.svg` | SVG banner |
| `pengalaman` (landing) | `/assets/blog/pengalaman-pasien.svg` | SVG banner |
| `fisioterapi-rumah` | `/images/service-fisioterapi.webp` | Foto WebP |
| `panggil-dokter` | `/images/service-panggil-dokter.webp` | Foto WebP |
| `perawat-homecare` | `/images/service-perawat.webp` | Foto WebP |
| `kesehatan-umum` | `/images/service-akupuntur.webp` | Foto WebP |
| `home-lab` | `/images/service-homelab.webp` | Foto WebP |
| `infus-vitamin` | `/images/service-infus.webp` | Foto WebP |
| `antar-jemput-rs` | `/images/service-transcare.webp` | Foto WebP |

Catatan: foto WebP berorientasi 4:5 (portrait); `object-fit: cover` memotongnya rapi ke 16:9 untuk card dan 1200/630 untuk hero. Tidak perlu resize ulang.

---

## 3. Komponen 1 — Card Thumbnail (blog/index.html) ✅ SUDAH TERPASANG

**162 kartu** di `blog/index.html` sudah diberi thumbnail sesuai pemetaan di atas. Pola markup:

```html
<div class="blog-card" data-category="parkinson">
  <span class="blog-card-img">
    <img src="/assets/blog/parkinson.svg"
         alt="Kategori Parkinson - Joy of Care"
         loading="lazy" width="800" height="450">
  </span>
  <div class="blog-card-body">
    <span class="category-badge">Parkinson</span>
    <h3><a href="/blog/parkinson/slug-artikel">Judul Artikel</a></h3>
    <div class="meta"><span>Joy of Care</span></div>
  </div>
</div>
```

Aturan CSS baru di `blog.css` (bagian "BLOG IMAGE SYSTEM"):
- `.blog-card` jadi flex column, `padding: 0`, `overflow: hidden` — gambar menempel penuh ke tepi atas kartu.
- `.blog-card-img` — `aspect-ratio: 16/9`, `overflow: hidden`, background `#F8F9FA` sebagai placeholder saat lazy-load.
- `.blog-card-img img` — `object-fit: cover`, transisi opacity halus saat hover kartu (tanpa layout shift).
- `.blog-card-body` — padding konten 20/24px, flex-grow agar tinggi kartu seragam dalam grid.
- `width`/`height` attribute pada `<img>` mencegah CLS sebelum CSS termuat.
- `loading="lazy"` pada semua thumbnail (162 gambar tidak dimuat sekaligus).

## 4. Komponen 2 — Article Hero Image (172 halaman artikel) 📋 SPEC UNTUK WRITER/TECH

Sisipkan **setelah breadcrumbs, sebelum/sekitar badge+judul** di setiap halaman artikel. Gunakan aset kategori yang sama dengan kartu (tabel §2):

```html
<figure class="article-hero">
  <img src="/assets/blog/parkinson.svg"
       alt="Perawatan Parkinson di rumah - Joy of Care"
       width="1200" height="630" fetchpriority="high">
  <figcaption>Ilustrasi: Joy of Care — layanan homecare profesional Jabodetabek</figcaption>
</figure>
```

CSS sudah tersedia di `blog.css`:
- `.article-hero` — max-width 920px, sejajar dengan lebar konten artikel.
- `.article-hero img` — `aspect-ratio: 1200/630`, `border-radius: 16px`, border tipis `#E8E8ED`, `box-shadow` lembut, `object-fit: cover`.
- Mobile (≤768px): rasio berubah ke 16/10 agar tidak terlalu dangkal di layar sempit.
- `figcaption` opsional, gaya muted kecil.

**Aturan tambahan untuk artikel:**
1. **Hero = gambar pertama** → jangan lazy-load hero (LCP). Gunakan `fetchpriority="high"`. Gambar *di dalam body artikel* (mis. infografis SVG 1080×1350) tetap `loading="lazy"`.
2. **og:image** per artikel harus menunjuk aset yang sama:
   `<meta property="og:image" content="https://joyofcare.net/assets/blog/parkinson.svg">` — namun **catatan sosial:** WhatsApp/Twitter/X card crawler tidak merender SVG. Untuk share-preview maksimal, idealnya og:image memakai raster (PNG 1200×630). Rekomendasi: ekspor PNG dari 6 banner SVG (rsvg-convert/ImageMagick) → `assets/blog/png/` dan jadikan og:image, sementara `<img>` on-page tetap SVG (tajam + ringan).
3. **Infografis in-body** (5 SVG yang ada): bungkus dengan pola figure yang sama tanpa class hero, cukup `<img ... style="max-width:540px;margin:24px auto;display:block;border-radius:12px">` atau tambahkan class `.article-figure` bila ingin saya tambahkan CSS-nya.
4. **Alt text convention:** `[Topik artikel] - Joy of Care`. Deskriptif, tanpa "gambar/foto".

## 5. Komponen 3 — Article Type Badges ✅ SUDAH TERPASANG (index)

120 kartu ber-slug bertipe sudah diberi badge kedua di samping category badge. Sistem warna:

| Class | Label | Warna | Suffix slug |
|---|---|---|---|
| `.type-panduan` | Panduan Lengkap | hijau brand `#007A3D` / bg `#E6F9EF` | `-panduan-lengkap` |
| `.type-biaya` | Biaya & Perbandingan | biru `#1D4ED8` / bg `#EFF6FF` | `-biaya-dan-perbandingan` |
| `.type-tips` | Tips & Cara | oranye `#B45309` / bg `#FFF4E5` | `-tips-dan-cara` |
| `.type-klinis` | Kapan Harus | merah medis `#B91C1C` / bg `#FEF2F2` | `-kapan-harus` |
| `.type-info` | Perlu Diketahui | teal `#0E7490` / bg `#ECFEFF` | `-yang-perlu-anda-ketahui` |

Di halaman artikel, tambahkan badge yang sama di samping `.category-badge` (CSS sudah mendukung konteks artikel — margin bawah 16px). Badge hanya untuk 5 slug-suffix di atas; artikel legacy bernomor (`-35`, `-32`, dst.) tidak diberi badge.

---

## 6. Bug yang Diperbaiki Saat Integrasi (blog/index.html)

1. **Search bar rusak** — JS memfilter `.article-card` padahal kartu memakai class `.blog-card`; pencarian tidak pernah berfungsi. Diperbaiki → sekarang memfilter `.blog-card`.
2. **Atribut style patah** pada `<input id="searchInput">` — `font-family:"Inter", sans-serif` memakai double-quote di dalam atribut double-quoted sehingga style terpotong. Diperbaiki.
3. **Duplikat `<script src="main.js">`** — dua tag (`../js/main.js` + `/js/main.js`). Disederhanakan jadi satu `/js/main.js`.
4. **Tag mismatch** — `<main class="section">` ditutup `</section>`. Diperbaiki jadi `</main>`.
5. Validasi penuh: parser HTML melaporkan **0 error, 0 tag tak tertutup** setelah transformasi.

## 7. Catatan untuk Sinkronisasi Konten

- **Drift jumlah artikel:** index memuat **162 kartu**, teks intro menyebut "162 artikel", JSON-LD `CollectionPage` menyebut `numberOfItems: 37`, katalog Writer menyebut **172**. Mohon Writer/Tech samakan (termasuk 10 artikel yang belum terdaftar di index?).
- **artikel-3** di pemetaan katalog `fisioterapi-rumah` punya suffix `-kapan-harus` dan sudah otomatis dapat badge `.type-klinis`.
- 4 halaman layanan **truncated** (75 baris, tanpa `</body></html>`) masih menunggu perbaikan JoC Tech — bukan bagian dari pekerjaan ini.
- Sisa pekerjaan visual opsional: **ekspor PNG 1200×630** dari 6 banner untuk og:image (lihat §4.2). Saya bisa kerjakan bila diminta.

---

## Ringkasan Deliverable

| Item | Status |
|---|---|
| `osteoporosis.svg` recolor ke palet truth | ✅ kedua repo |
| `parkinson.svg` baru | ✅ kedua repo |
| Recolor 4 banner lama ke palet truth | ✅ kedua repo |
| CSS sistem gambar blog (card + hero + badges) | ✅ `blog.css` |
| 162 card thumbnails di blog/index.html | ✅ terpasang |
| 120 article-type badges di blog/index.html | ✅ terpasang |
| 4 bug HTML/JS di blog/index.html | ✅ diperbaiki |
| Spec hero image untuk 172 artikel | ✅ dokumen ini §4 |
| PNG untuk og:image | ⏳ opsional, menunggu request |
