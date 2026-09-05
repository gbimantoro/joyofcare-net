with open('scripts/patch_price_engine.py') as f:
    code = f.read()

old_table = """    old_table = \"\"\"|---|---|---|
| **Konsultasi Dokter** | Rp 400.000 – Rp 600.000 | Rp 450.000 – Rp 550.000 |
| **Biaya Administrasi RS** | Rp 75.000 – Rp 150.000 | **Rp 0 (Bebas Biaya Admin)** |
| **Transportasi Khusus (Taksi/Ambulans)** | Rp 300.000 – Rp 800.000 (PP) | **Rp 0 (Pasien di Rumah)** |
| **Waktu Terbuang (Perjalanan & Antre)** | 3 – 5 Jam (Sangat melelahkan) | **0 Jam (Dokter yang Menunggu Anda)** |
| **Risiko Tertular Penyakit Lain** | Tinggi (Ruang tunggu faskes ramai) | **Sangat Rendah (Lingkungan Rumah Steril)** |
| **Estimasi Total Pengeluaran** | **Rp 775.000 – Rp 1.550.000** | **Rp 450.000 – Rp 550.000** |\"\"\"

    new_table = f\"\"\"|---|---|---|
| **Konsultasi Dokter** | Sesuai tarif poliklinik RS | Tarif Visit Flat Transparan |
| **Biaya Administrasi RS** | Biaya loket kartu pasien faskes | **Bebas Biaya Admin** |
| **Transportasi Khusus (Taksi/Ambulans)** | Biaya sewa armada & argo fluktuatif | **Bebas Biaya Transport (Pasien di Rumah)** |
| **Waktu Terbuang (Perjalanan & Antre)** | 3 – 5 Jam (Sangat melelahkan) | **Bebas Antrean (Dokter Hadir Tepat Waktu)** |
| **Risiko Tertular Penyakit Lain** | Tinggi (Ruang tunggu faskes ramai) | **Sangat Rendah (Lingkungan Hunian Nyaman)** |
| **Estimasi Total Pengeluaran** | **Total Biaya Membengkak Tinggi** | **Transparan & Jauh Lebih Hemat** |

{PRIMARY_CTA}\"\"\""""

new_table = """    old_table = \"\"\"|---|---|---|
| **Konsultasi Dokter** | Rp 400.000 – Rp 600.000 | Rp 450.000 – Rp 550.000 |
| **Biaya Administrasi RS** | Rp 75.000 – Rp 150.000 | **Rp 0 (Bebas Biaya Admin)** |
| **Transportasi Khusus (Taksi/Ambulans)** | Rp 300.000 – Rp 800.000 (PP) | **Rp 0 (Pasien di Rumah)** |
| **Waktu Terbuang (Perjalanan & Antrean)** | 3 hingga 5 jam | **0 jam (Bebas Antre)** |
| **Risiko Infeksi Kuman RS (Nosokomial)** | Tinggi (di ruang tunggu umum) | **Sangat Rendah (Lingkungan Rumah Sendiri)** |
| **Kenyamanan & Stres Pasien** | Sangat Lelah & Rentan Jatuh | **Tenang di Tempat Tidur Sendiri** |
| **Estimasi Total Pengeluaran** | **Rp 775.000 – Rp 1.550.000** | **Rp 450.000 – Rp 550.000** |\"\"\"

    new_table = f\"\"\"|---|---|---|
| **Konsultasi Dokter** | Sesuai tarif poliklinik faskes | Tarif Visit Flat Transparan |
| **Biaya Administrasi RS** | Biaya administrasi & kartu pasien RS | **Bebas Biaya Admin (Sudah Termasuk)** |
| **Transportasi Khusus (Taksi/Ambulans)** | Biaya sewa transportasi & argo fluktuatif | **Bebas Biaya Transportasi (Pasien di Rumah)** |
| **Waktu Terbuang (Perjalanan & Antrean)** | 3 hingga 5 jam | **0 jam (Dokter Hadir Tepat Waktu)** |
| **Risiko Infeksi Kuman RS (Nosokomial)** | Tinggi (di ruang tunggu umum) | **Sangat Rendah (Lingkungan Rumah Nyaman)** |
| **Kenyamanan & Stres Pasien** | Sangat Lelah & Rentan Jatuh | **Tenang di Tempat Tidur Sendiri** |
| **Estimasi Total Pengeluaran** | **Biaya Kumulatif Membengkak Tinggi** | **Transparan & Jauh Lebih Hemat** |

{PRIMARY_CTA}\"\"\""""

if old_table in code:
    code = code.replace(old_table, new_table)
    with open('scripts/patch_price_engine.py', 'w') as f:
        f.write(code)
    print('Replaced table successfully!')
else:
    print('Pattern not found!')
