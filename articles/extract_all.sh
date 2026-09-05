#!/bin/bash

# JoyofCare Blog Article Extraction - Direct firecrawl approach
# Processes all articles and saves as .txt files

ARTICLES_DIR="/home/gobeam/Projects/joyofcare-net/articles"
cd "$ARTICLES_DIR"

# Clean up test files
rm -f batch1_article1.md

# All URLs with their categories and slugs
declare -a URLS=(
    "healthy-aging-3|panduan-fisioterapi-di-rumah-untuk-pasien-osteoporosis-mengurangi-nyeri-mencegah-jatuh-43|http://www.joyofcare.net/blog/healthy-aging-3/panduan-fisioterapi-di-rumah-untuk-pasien-osteoporosis-mengurangi-nyeri-mencegah-jatuh-43"
    "healthy-aging-3|layanan-terapi-infus-injeksi-osteoporosis-di-rumah-pasien-homecare-42|http://www.joyofcare.net/blog/healthy-aging-3/layanan-terapi-infus-injeksi-osteoporosis-di-rumah-pasien-homecare-42"
    "healthy-aging-3|bahaya-komplikasi-osteoporosis-dan-faktor-risiko-yang-wajib-diwaspadai-41|http://www.joyofcare.net/blog/healthy-aging-3/bahaya-komplikasi-osteoporosis-dan-faktor-risiko-yang-wajib-diwaspadai-41"
    "healthy-aging-3|jenis-terapi-osteoporosis-lengkap-dari-obat-oral-injeksi-hingga-infus-40|http://www.joyofcare.net/blog/healthy-aging-3/jenis-terapi-osteoporosis-lengkap-dari-obat-oral-injeksi-hingga-infus-40"
    "healthy-aging-3|vaksinasi-pneumonia-lindungi-opa-oma-39|http://www.joyofcare.net/blog/healthy-aging-3/vaksinasi-pneumonia-lindungi-opa-oma-39"
    "healthy-aging-3|7-makanan-super-indonesia-yang-wajib-dimakan-aturan-makan-obat-rahasia-dapur-pasien-parkinson-38|http://www.joyofcare.net/blog/healthy-aging-3/7-makanan-super-indonesia-yang-wajib-dimakan-aturan-makan-obat-rahasia-dapur-pasien-parkinson-38"
    "healthy-aging-3|rumah-anda-berbahaya-cek-5-perubahan-kecil-di-rumah-yang-bisa-mencegah-pasien-parkinson-terjatuh-fatal-37|http://www.joyofcare.net/blog/healthy-aging-3/rumah-anda-berbahaya-cek-5-perubahan-kecil-di-rumah-yang-bisa-mencegah-pasien-parkinson-terjatuh-fatal-37"
    "healthy-aging-3|suara-menghilang-kenali-hipofonia-begini-cara-terapi-wicara-mengembalikan-kekuatan-suara-dan-kelancaran-menelan-pada-parkinson-36|http://www.joyofcare.net/blog/healthy-aging-3/suara-menghilang-kenali-hipofonia-begini-cara-terapi-wicara-mengembalikan-kekuatan-suara-dan-kelancaran-menelan-pada-parkinson-36"
    "healthy-aging-3|3-jenis-latihan-fisik-yang-terbukti-mampu-melawan-kekakuan-parkinson-panduan-fisioterapi-rumahan-35|http://www.joyofcare.net/blog/healthy-aging-3/3-jenis-latihan-fisik-yang-terbukti-mampu-melawan-kekakuan-parkinson-panduan-fisioterapi-rumahan-35"
    "healthy-aging-3|pil-ajaib-parkinson-kenapa-obat-levodopa-jadi-pahlawan-utama-panduan-cerdas-mengelola-dosis-agar-gerakan-tetap-normal-34|http://www.joyofcare.net/blog/healthy-aging-3/pil-ajaib-parkinson-kenapa-obat-levodopa-jadi-pahlawan-utama-panduan-cerdas-mengelola-dosis-agar-gerakan-tetap-normal-34"
    "healthy-aging-3|tips-rahasia-keluarga-5-jurus-ajaib-merawat-pasien-parkinson-di-rumah-agar-lebih-aktif-dan-bahagia-33|http://www.joyofcare.net/blog/healthy-aging-3/tips-rahasia-keluarga-5-jurus-ajaib-merawat-pasien-parkinson-di-rumah-agar-lebih-aktif-dan-bahagia-33"
    "healthy-aging-3|jangan-anggap-remeh-tangan-gemetar-saat-santai-32|http://www.joyofcare.net/blog/healthy-aging-3/jangan-anggap-remeh-tangan-gemetar-saat-santai-32"
    "healthy-aging-3|latihan-fisioterapi-untuk-bahu-beku-frozen-shoulder-yang-bisa-dilakukan-di-rumah-31|http://www.joyofcare.net/blog/healthy-aging-3/latihan-fisioterapi-untuk-bahu-beku-frozen-shoulder-yang-bisa-dilakukan-di-rumah-31"
    "healthy-aging-3|fisioterapi-untuk-lansia-menjaga-mobilitas-dan-keseimbangan-30|http://www.joyofcare.net/blog/healthy-aging-3/fisioterapi-untuk-lansia-menjaga-mobilitas-dan-keseimbangan-30"
    "healthy-aging-3|pentingnya-vaksinasi-untuk-lansia-jenis-vaksin-yang-direkomendasikan-28|http://www.joyofcare.net/blog/healthy-aging-3/pentingnya-vaksinasi-untuk-lansia-jenis-vaksin-yang-direkomendasikan-28"
    "healthy-aging-3|5-latihan-fisioterapi-untuk-mengatasi-nyeri-punggung-bawah-hnp-26|http://www.joyofcare.net/blog/healthy-aging-3/5-latihan-fisioterapi-untuk-mengatasi-nyeri-punggung-bawah-hnp-26"
    "healthy-aging-3|mencegah-jatuh-pada-lansia-7-modifikasi-aman-untuk-rumah-anda-25|http://www.joyofcare.net/blog/healthy-aging-3/mencegah-jatuh-pada-lansia-7-modifikasi-aman-untuk-rumah-anda-25"
    "healthy-aging-3|fisioterapi-di-rumah-solusi-praktis-pemulihan-pasca-operasi-lutut-23|http://www.joyofcare.net/blog/healthy-aging-3/fisioterapi-di-rumah-solusi-praktis-pemulihan-pasca-operasi-lutut-23"
    "healthy-aging-3|panduan-nutrisi-untuk-lansia-makanan-wajib-untuk-tulang-kuat-energi-22|http://www.joyofcare.net/blog/healthy-aging-3/panduan-nutrisi-untuk-lansia-makanan-wajib-untuk-tulang-kuat-energi-22"
    "healthy-aging-3|ortu-sering-lupa-awas-mungkin-ini-10-tanda-demensia-yang-sering-kelewat-21|http://www.joyofcare.net/blog/healthy-aging-3/ortu-sering-lupa-awas-mungkin-ini-10-tanda-demensia-yang-sering-kelewat-21"
    "healthy-aging-3|lanjutan-panduan-perawatan-pasca-operasi-untuk-pemulihan-optimal-di-rumah-penggantian-panggul-total-total-hip-replacement-thr-pada-lansia-20|http://www.joyofcare.net/blog/healthy-aging-3/lanjutan-panduan-perawatan-pasca-operasi-untuk-pemulihan-optimal-di-rumah-penggantian-panggul-total-total-hip-replacement-thr-pada-lansia-20"
    "healthy-aging-3|perawatan-pasca-operasi-penggantian-panggul-total-total-hip-replacement-thr-pada-lansia-panduan-lengkap-untuk-pemulihan-optimal-di-rumah-19|http://www.joyofcare.net/blog/healthy-aging-3/perawatan-pasca-operasi-penggantian-panggul-total-total-hip-replacement-thr-pada-lansia-panduan-lengkap-untuk-pemulihan-optimal-di-rumah-19"
    "healthy-aging-3|pentingnya-vaksinasi-untuk-lansia-jenis-vaksin-yang-direkomendasikan-12|http://www.joyofcare.net/blog/healthy-aging-3/pentingnya-vaksinasi-untuk-lansia-jenis-vaksin-yang-direkomendasikan-12"
    "healthy-aging-3|6-peran-anda-dan-dokter-dalam-mendukung-proses-fisioterapi-untuk-lansia-di-rumah-6|http://www.joyofcare.net/blog/healthy-aging-3/6-peran-anda-dan-dokter-dalam-mendukung-proses-fisioterapi-untuk-lansia-di-rumah-6"
    "healthy-aging-3|7-hal-yang-dilakukan-saat-fisioterapi-di-rumah-untuk-lansia-5|http://www.joyofcare.net/blog/healthy-aging-3/7-hal-yang-dilakukan-saat-fisioterapi-di-rumah-untuk-lansia-5"
    "healthy-aging-3|fisioterapi-di-rumah-untuk-lansia-dengan-masalah-tulang-belakang-4|http://www.joyofcare.net/blog/healthy-aging-3/fisioterapi-di-rumah-untuk-lansia-dengan-masalah-tulang-belakang-4"
    "healthy-aging-3|ini-dia-kunci-memahami-dan-memperlambat-proses-penuaan-dna-methylation-2|http://www.joyofcare.net/blog/healthy-aging-3/ini-dia-kunci-memahami-dan-memperlambat-proses-penuaan-dna-methylation-2"
    "pengalaman-1|pemulihan-pasca-patah-tulang-peran-vital-fisioterapi-di-rumah-29|http://www.joyofcare.net/blog/pengalaman-1/pemulihan-pasca-patah-tulang-peran-vital-fisioterapi-di-rumah-29"
    "studi-luar-negeri-4|cara-menyiapkan-persyaratan-kesehatan-untuk-studi-di-australia-18|http://www.joyofcare.net/blog/studi-luar-negeri-4/cara-menyiapkan-persyaratan-kesehatan-untuk-studi-di-australia-18"
    "studi-luar-negeri-4|perhatikan-persyaratan-tambahan-bagi-beberapa-jurusan-studi-di-australia-17|http://www.joyofcare.net/blog/studi-luar-negeri-4/perhatikan-persyaratan-tambahan-bagi-beberapa-jurusan-studi-di-australia-17"
    "studi-luar-negeri-4|vaksinasi-yang-wajib-dan-disarankan-untuk-studi-di-australia-16|http://www.joyofcare.net/blog/studi-luar-negeri-4/vaksinasi-yang-wajib-dan-disarankan-untuk-studi-di-australia-16"
    "studi-luar-negeri-4|persyaratan-medis-untuk-melanjutkan-studi-di-australia-14|http://www.joyofcare.net/blog/studi-luar-negeri-4/persyaratan-medis-untuk-melanjutkan-studi-di-australia-14"
    "studi-luar-negeri-4|persyaratan-kesehatan-kuliah-di-inggris-panduan-lengkap-untuk-mahasiswa-internasional-11|http://www.joyofcare.net/blog/studi-luar-negeri-4/persyaratan-kesehatan-kuliah-di-inggris-panduan-lengkap-untuk-mahasiswa-internasional-11"
    "studi-luar-negeri-4|surat-keterangan-sehat-dokumen-kesehatan-yang-vital-untuk-berbagai-keperluan-10|http://www.joyofcare.net/blog/studi-luar-negeri-4/surat-keterangan-sehat-dokumen-kesehatan-yang-vital-untuk-berbagai-keperluan-10"
    "studi-luar-negeri-4|persyaratan-kesehatan-untuk-perjalanan-internasional-dan-pendidikan-9|http://www.joyofcare.net/blog/studi-luar-negeri-4/persyaratan-kesehatan-untuk-perjalanan-internasional-dan-pendidikan-9"
    "vaksinasi-di-rumah-2|kenapa-bersekolah-di-luar-negeri-memerlukan-serangkaian-vaksinasi-8|http://www.joyofcare.net/blog/vaksinasi-di-rumah-2/kenapa-bersekolah-di-luar-negeri-memerlukan-serangkaian-vaksinasi-8"
    "vaksinasi-di-rumah-2|vaksinasi-mudah-di-rumah-solusi-praktis-untuk-kesehatan-keluarga-anda-7|http://www.joyofcare.net/blog/vaksinasi-di-rumah-2/vaksinasi-mudah-di-rumah-solusi-praktis-untuk-kesehatan-keluarga-anda-7"
)

TOTAL=${#URLS[@]}
echo "Total articles to extract: $TOTAL"

# Process in batches of 5
BATCH_SIZE=5
BATCH_COUNT=$(( (TOTAL + BATCH_SIZE - 1) / BATCH_SIZE ))

for ((batch=0; batch<BATCH_COUNT; batch++)); do
    START=$((batch * BATCH_SIZE))
    END=$((START + BATCH_SIZE))
    if [ $END -gt $TOTAL ]; then
        END=$TOTAL
    fi
    
    echo ""
    echo "=== Processing batch $((batch+1)) of $BATCH_COUNT (articles $((START+1))-$END) ==="
    
    for ((i=START; i<END; i++)); do
        IFS='|' read -r CATEGORY SLUG URL <<< "${URLS[$i]}"
        
        OUTPUT_FILE="${ARTICLES_DIR}/${SLUG}.txt"
        
        if [ -f "$OUTPUT_FILE" ]; then
            echo "  [SKIP] $SLUG (already exists)"
            continue
        fi
        
        echo "  [EXTRACT] $SLUG"
        
        # Extract using firecrawl
        TEMP_MD="${ARTICLES_DIR}/temp_${SLUG}.md"
        firecrawl scrape "$URL" --only-main-content -o "$TEMP_MD" 2>/dev/null
        
        if [ -f "$TEMP_MD" ]; then
            # Extract title from first heading
            TITLE=$(grep -m1 "^#" "$TEMP_MD" | sed 's/^#* //' | head -c 200)
            if [ -z "$TITLE" ]; then
                TITLE="$SLUG"
            fi
            
            # Create final .txt file with metadata
            {
                echo "Title: $TITLE"
                echo "URL: $URL"
                echo "Category: $CATEGORY"
                echo "Slug: $SLUG"
                echo "---"
                echo ""
                cat "$TEMP_MD"
            } > "$OUTPUT_FILE"
            
            # Remove temp file
            rm -f "$TEMP_MD"
            
            echo "    -> Saved: $(basename "$OUTPUT_FILE")"
        else
            echo "    -> FAILED to extract"
        fi
        
        # Small delay between requests
        sleep 1
    done
    
    echo "Batch $((batch+1)) complete."
done

echo ""
echo "=== Extraction Summary ==="
ls -1 "$ARTICLES_DIR"/*.txt 2>/dev/null | wc -l
echo "articles extracted to $ARTICLES_DIR"