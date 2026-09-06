# Joy of Care Web — Blog Images Catalog & Mapping Strategy

Dokumen ini menyajikan audit menyeluruh, taksonomi visual, inventaris aset, dan pemetaan gambar (*featured images & thumbnails*) untuk seluruh **172 artikel blog** di `joyofcare-web`.

---

## 1. Standar Desain & Spesifikasi Gambar

| Properti | Standar / Spesifikasi |
|---|---|
| **Rasio Gambar Utama (Hero/OG)** | 16:9 (1200 × 675 px) atau 1.91:1 (1200 × 630 px) |
| **Rasio Kartu Blog (Grid Thumbnail)**| 16:9 (600 × 338 px / 800 × 450 px) |
| **Format Rekomendasi** | WebP (foto/raster terkompresi) & SVG (vektor/infografis) |
| **Palet Warna Brand** | - Primary Green: `#2D9C4A`<br>- Dark Green: `#1A6B30`<br>- Accent Orange: `#FC9000`<br>- Medical Teal/Cyan: `#0E7490`<br>- Neutral Light: `#F8F9FA`<br>- Neutral Dark: `#1A1A2E` |
| **Typography Visual** | Montserrat (Heading), Inter (Body) |
| **Tone & Style** | Medis profesional, hangat, terpercaya, empati geriatri Asia/Indonesia |

---

## 2. Inventaris Aset Visual yang Tersedia

### A. Foto Layanan Riil Beresolusi Tinggi (`/images/`)
1. **Layanan Panggil Dokter ke Rumah**:
   - `pages/images/panggil-dokter-ke-rumah/1.jpg` – `4.jpg` (1366 × 768 px)
   - `pages/images/service-panggil-dokter.webp` (690 × 387 px)
2. **Layanan Fisioterapi ke Rumah**:
   - `pages/images/layanan-fisioterapi-ke-rumah/1.jpg` (1920 × 1314 px)
   - `pages/images/layanan-fisioterapi-ke-rumah/2.jpg` (1366 × 768 px)
   - `pages/images/service-fisioterapi.webp` (690 × 472 px)
3. **Layanan Perawat di Rumah**:
   - `pages/images/layanan-perawat-di-rumah/1.jpg` – `3.jpg` (1366 × 768 px)
   - `pages/images/service-perawat.webp` (690 × 387 px)
4. **Layanan Infus & Suntik Vitamin di Rumah**:
   - `pages/images/infus-suntik-vitamin-di-rumah/1.jpg` – `3.jpg` (1920 × 1080 px)
   - `pages/images/service-infus.webp` (690 × 388 px)
5. **Layanan Homelab & Cek Darah di Rumah**:
   - `pages/images/homelab/1.jpg` (1366 × 768 px)
   - `pages/images/homelab/2.png` (1080 × 1080 px)
   - `pages/images/service-homelab.webp` (690 × 387 px)
   - `pages/images/service-homelab-paket.webp` (1080 × 1080 px)
6. **Layanan TransCare (Antar Jemput Medis RS)**:
   - `pages/images/transcare-antar-jemput-ke-rs-jakarta-tangerang/1.jpg` – `4.jpg` (551–718 × 560 px)
   - `pages/images/service-transcare.webp` (690 × 538 px)
7. **Layanan Akupuntur Medis di Rumah**:
   - `pages/images/layanan-akupuntur-di-rumah/1.png` – `3.png` (1366 × 768 px)
   - `pages/images/service-akupuntur.webp` (690 × 387 px)

### B. Infografis Vektor Edukatif (`/assets/infographics/`)
1. `biaya-panggil-dokter.svg`: Tabel komparasi faskes vs visit dokter rumah.
2. `panduan-merawat-orang-tua.svg`: 10 langkah emas merawat lansia di rumah.
3. `fisioterapi-lansia.svg`: 5 latihan gerak fungsional mobilitas geriatri.
4. `persyaratan-kesehatan-studi-luar-negeri.svg`: Checklist MCU & vaksinasi visa pelajar.
5. `vaksinasi-untuk-lansia.svg`: Jadwal dan jenis vaksinasi wajib lansia.

### C. Category Banners (`/assets/blog/`)
1. `healthy-aging.svg`: Ikon rumah, hati, lansia sehat (1200 × 630 px).
2. `pengalaman-pasien.svg`: Testimoni & kisah pemulihan pasien (1200 × 630 px).
3. `studi-luar-negeri.svg`: Globe, travel medical, visa study abroad (1200 × 630 px).
4. `vaksinasi.svg`: Shield medis, syringe, vaksinasi vial (1200 × 630 px).

---

## 3. Pemetaan Gambar untuk 12 Kategori Artikel (172 Artikel)

| No | Kategori Blog | Jumlah Artikel | Hero Image / Featured Asset | Fallback / Card Thumbnail | Infografis Terkait |
|:---|:---|:---:|:---|:---|:---|
| 1 | **Perawatan Lansia** (`perawatan-lansia/`) | 38 | `/assets/blog/healthy-aging.svg` | `/images/layanan-perawat-di-rumah/1.jpg` | `panduan-merawat-orang-tua.svg` |
| 2 | **Fisioterapi Rumah** (`fisioterapi-rumah/`) | 22 | `/images/service-fisioterapi.webp` | `/images/layanan-fisioterapi-ke-rumah/1.jpg` | `fisioterapi-lansia.svg` |
| 3 | **Osteoporosis** (`osteoporosis/`) | 17 | `/assets/blog/osteoporosis.svg` *(Baru)* | `/images/service-infus.webp` | `fisioterapi-lansia.svg` |
| 4 | **Panggil Dokter** (`panggil-dokter/`) | 15 | `/images/service-panggil-dokter.webp` | `/images/panggil-dokter-ke-rumah/1.jpg` | `biaya-panggil-dokter.svg` |
| 5 | **Vaksinasi Rumah** (`vaksinasi-rumah/`) | 14 | `/assets/blog/vaksinasi.svg` | `/images/service-panggil-dokter.webp` | `vaksinasi-untuk-lansia.svg` |
| 6 | **Studi Luar Negeri** (`studi-luar-negeri/`) | 14 | `/assets/blog/studi-luar-negeri.svg` | `/images/service-homelab.webp` | `persyaratan-kesehatan-studi-luar-negeri.svg` |
| 7 | **Parkinson** (`parkinson/`) | 12 | `/assets/blog/parkinson.svg` *(Baru)* | `/images/layanan-fisioterapi-ke-rumah/2.jpg` | `fisioterapi-lansia.svg` |
| 8 | **Perawat Homecare** (`perawat-homecare/`) | 12 | `/images/service-perawat.webp` | `/images/layanan-perawat-di-rumah/2.jpg` | `panduan-merawat-orang-tua.svg` |
| 9 | **Kesehatan Umum & Akupuntur** (`kesehatan-umum/`) | 9 | `/images/service-akupuntur.webp` | `/images/layanan-akupuntur-di-rumah/1.png` | `panduan-merawat-orang-tua.svg` |
| 10 | **Home Lab & Cek Darah** (`home-lab/`) | 5 | `/images/service-homelab.webp` | `/images/homelab/1.jpg` | `biaya-panggil-dokter.svg` |
| 11 | **Infus Vitamin** (`infus-vitamin/`) | 5 | `/images/service-infus.webp` | `/images/infus-suntik-vitamin-di-rumah/1.jpg` | `vaksinasi-untuk-lansia.svg` |
| 12 | **Antar Jemput RS** (`antar-jemput-rs/`) | 5 | `/images/service-transcare.webp` | `/images/transcare-antar-jemput-ke-rs-jakarta-tangerang/1.jpg` | `biaya-panggil-dokter.svg` |
| 13 | **Root / Landing** (`.`) | 4 | `/assets/blog/pengalaman-pasien.svg` | `/images/joc_long.png` | - |

---

## 4. Kebutuhan Kolaborasi dengan JoC Visual

Untuk melengkapi aset visual agar seluruh 172 artikel memiliki gambar spesifik berdaya tarik tinggi:
1. **Pembuatan 2 Category Banners Baru (SVG 1200 × 630 px)**:
   - `osteoporosis.svg`: Tema kesehatan tulang geriatri, kalsium, postur tegak lansia, warna hijau-cyan brand Joy of Care.
   - `parkinson.svg`: Tema pemulihan neuromotor, latihan stabilitas gerak, dukungan keluarga dan fisioterapi.
2. **Standardisasi Template Thumbnail Kartu Blog (600 × 338 px)**:
   - Membuat variasi badge visual atau frame kartu blog untuk membedakan 5 variasi tipe artikel:
     - *Panduan Lengkap* (Badge Emas / Hijau)
     - *Biaya & Perbandingan* (Badge Biru / Kalkulator)
     - *Tips & Cara* (Badge Oranye / Checklist)
     - *Protokol Klinis / Kapan Harus* (Badge Merah Medis / Stetoskop)
     - *Yang Perlu Anda Ketahui* (Badge Teal / Lampu Edukasi)
3. **Optimasi Ukuran & Lazy Loading**:
   - Memastikan seluruh gambar berukuran di bawah 150 KB untuk menjaga skor Core Web Vitals (LCP & CLS).

