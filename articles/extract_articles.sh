#!/bin/bash

# JoyofCare Blog Article Extraction Script
# Extracts all blog articles using firecrawl scrape

ARTICLES_DIR="/home/gobeam/Projects/joyofcare-net/articles"
INDEX_FILE="$ARTICLES_DIR/index.json"

# All article URLs with categories
declare -A ARTICLES=(
    # healthy-aging-3 (29 articles)
    ["http://www.joyofcare.net/blog/healthy-aging-3/panduan-fisioterapi-di-rumah-untuk-pasien-osteoporosis-mengurangi-nyeri-mencegah-jatuh-43"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/layanan-terapi-infus-injeksi-osteoporosis-di-rumah-pasien-homecare-42"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/bahaya-komplikasi-osteoporosis-dan-faktor-risiko-yang-wajib-diwaspadai-41"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/jenis-terapi-osteoporosis-lengkap-dari-obat-oral-injeksi-hingga-infus-40"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/vaksinasi-pneumonia-lindungi-opa-oma-39"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/7-makanan-super-indonesia-yang-wajib-dimakan-aturan-makan-obat-rahasia-dapur-pasien-parkinson-38"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/rumah-anda-berbahaya-cek-5-perubahan-kecil-di-rumah-yang-bisa-mencegah-pasien-parkinson-terjatuh-fatal-37"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/suara-menghilang-kenali-hipofonia-begini-cara-terapi-wicara-mengembalikan-kekuatan-suara-dan-kelancaran-menelan-pada-parkinson-36"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/3-jenis-latihan-fisik-yang-terbukti-mampu-melawan-kekakuan-parkinson-panduan-fisioterapi-rumahan-35"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/pil-ajaib-parkinson-kenapa-obat-levodopa-jadi-pahlawan-utama-panduan-cerdas-mengelola-dosis-agar-gerakan-tetap-normal-34"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/tips-rahasia-keluarga-5-jurus-ajaib-merawat-pasien-parkinson-di-rumah-agar-lebih-aktif-dan-bahagia-33"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/jangan-anggap-remeh-tangan-gemetar-saat-santai-32"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/latihan-fisioterapi-untuk-bahu-beku-frozen-shoulder-yang-bisa-dilakukan-di-rumah-31"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/fisioterapi-untuk-lansia-menjaga-mobilitas-dan-keseimbangan-30"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/pentingnya-vaksinasi-untuk-lansia-jenis-vaksin-yang-direkomendasikan-28"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/5-latihan-fisioterapi-untuk-mengatasi-nyeri-punggung-bawah-hnp-26"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/mencegah-jatuh-pada-lansia-7-modifikasi-aman-untuk-rumah-anda-25"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/fisioterapi-di-rumah-solusi-praktis-pemulihan-pasca-operasi-lutut-23"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/panduan-nutrisi-untuk-lansia-makanan-wajib-untuk-tulang-kuat-energi-22"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/ortu-sering-lupa-awas-mungkin-ini-10-tanda-demensia-yang-sering-kelewat-21"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/lanjutan-panduan-perawatan-pasca-operasi-untuk-pemulihan-optimal-di-rumah-penggantian-panggul-total-total-hip-replacement-thr-pada-lansia-20"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/perawatan-pasca-operasi-penggantian-panggul-total-total-hip-replacement-thr-pada-lansia-panduan-lengkap-untuk-pemulihan-optimal-di-rumah-19"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/pentingnya-vaksinasi-untuk-lansia-jenis-vaksin-yang-direkomendasikan-12"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/6-peran-anda-dan-dokter-dalam-mendukung-proses-fisioterapi-untuk-lansia-di-rumah-6"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/7-hal-yang-dilakukan-saat-fisioterapi-di-rumah-untuk-lansia-5"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/fisioterapi-di-rumah-untuk-lansia-dengan-masalah-tulang-belakang-4"]="healthy-aging-3"
    ["http://www.joyofcare.net/blog/healthy-aging-3/ini-dia-kunci-memahami-dan-memperlambat-proses-penuaan-dna-methylation-2"]="healthy-aging-3"
    # pengalaman-1 (1 article)
    ["http://www.joyofcare.net/blog/pengalaman-1/pemulihan-pasca-patah-tulang-peran-vital-fisioterapi-di-rumah-29"]="pengalaman-1"
    # studi-luar-negeri-4 (7 articles)
    ["http://www.joyofcare.net/blog/studi-luar-negeri-4/cara-menyiapkan-persyaratan-kesehatan-untuk-studi-di-australia-18"]="studi-luar-negeri-4"
    ["http://www.joyofcare.net/blog/studi-luar-negeri-4/perhatikan-persyaratan-tambahan-bagi-beberapa-jurusan-studi-di-australia-17"]="studi-luar-negeri-4"
    ["http://www.joyofcare.net/blog/studi-luar-negeri-4/vaksinasi-yang-wajib-dan-disarankan-untuk-studi-di-australia-16"]="studi-luar-negeri-4"
    ["http://www.joyofcare.net/blog/studi-luar-negeri-4/persyaratan-medis-untuk-melanjutkan-studi-di-australia-14"]="studi-luar-negeri-4"
    ["http://www.joyofcare.net/blog/studi-luar-negeri-4/persyaratan-kesehatan-kuliah-di-inggris-panduan-lengkap-untuk-mahasiswa-internasional-11"]="studi-luar-negeri-4"
    ["http://www.joyofcare.net/blog/studi-luar-negeri-4/surat-keterangan-sehat-dokumen-kesehatan-yang-vital-untuk-berbagai-keperluan-10"]="studi-luar-negeri-4"
    ["http://www.joyofcare.net/blog/studi-luar-negeri-4/persyaratan-kesehatan-untuk-perjalanan-internasional-dan-pendidikan-9"]="studi-luar-negeri-4"
    # vaksinasi-di-rumah-2 (2 articles)
    ["http://www.joyofcare.net/blog/vaksinasi-di-rumah-2/kenapa-bersekolah-di-luar-negeri-memerlukan-serangkaian-vaksinasi-8"]="vaksinasi-di-rumah-2"
    ["http://www.joyofcare.net/blog/vaksinasi-di-rumah-2/vaksinasi-mudah-di-rumah-solusi-praktis-untuk-kesehatan-keluarga-anda-7"]="vaksinasi-di-rumah-2"
)

# Function to extract slug from URL
extract_slug() {
    local url="$1"
    local slug=$(echo "$url" | sed 's|.*/||' | sed 's|-[0-9]*$||')
    echo "$slug"
}

# Initialize index JSON
echo "[]" > "$INDEX_FILE"

# Process articles in batches of 5
URLS=(${!ARTICLES[@]})
TOTAL=${#URLS[@]}
BATCH_SIZE=5
BATCH_NUM=0

echo "Starting extraction of $TOTAL articles..."

for ((i=0; i<TOTAL; i+=BATCH_SIZE)); do
    BATCH_NUM=$((BATCH_NUM+1))
    BATCH_URLS=(${URLS[@]:$i:$BATCH_SIZE})
    BATCH_COUNT=${#BATCH_URLS[@]}
    
    echo "Processing batch $BATCH_NUM ($BATCH_COUNT articles)..."
    
    # Create batch directory
    BATCH_DIR="$ARTICLES_DIR/batch_$BATCH_NUM"
    mkdir -p "$BATCH_DIR"
    
    # Scrape batch of URLs
    for url in "${BATCH_URLS[@]}"; do
        SLUG=$(extract_slug "$url")
        CATEGORY="${ARTICLES[$url]}"
        OUTPUT_FILE="$BATCH_DIR/${SLUG}.txt"
        
        echo "  Scraping: $SLUG"
        
        # Use firecrawl scrape
        firecrawl scrape "$url" --only-main-content -o "$OUTPUT_FILE" 2>/dev/null
        
        # Add metadata header to the file
        if [ -f "$OUTPUT_FILE" ]; then
            TEMP_FILE="$OUTPUT_FILE.tmp"
            echo "Title: $(head -1 "$OUTPUT_FILE" | sed 's/^# //')" > "$TEMP_FILE"
            echo "URL: $url" >> "$TEMP_FILE"
            echo "Category: $CATEGORY" >> "$TEMP_FILE"
            echo "Slug: $SLUG" >> "$TEMP_FILE"
            echo "---" >> "$TEMP_FILE"
            cat "$OUTPUT_FILE" >> "$TEMP_FILE"
            mv "$TEMP_FILE" "$OUTPUT_FILE"
            
            # Get word count
            WORD_COUNT=$(wc -w < "$OUTPUT_FILE")
            
            # Add to index
            jq --arg title "$(head -1 "$OUTPUT_FILE" | sed 's/^Title: //')" \
               --arg url "$url" \
               --arg category "$CATEGORY" \
               --arg slug "$SLUG" \
               --argjson word_count "$WORD_COUNT" \
               '. += [{"title": $title, "url": $url, "category": $category, "slug": $slug, "word_count": $word_count}]' \
               "$INDEX_FILE" > "$INDEX_FILE.tmp" && mv "$INDEX_FILE.tmp" "$INDEX_FILE"
        fi
    done
    
    # Move batch files to main articles directory
    mv "$BATCH_DIR"/*.txt "$ARTICLES_DIR/" 2>/dev/null || true
    rmdir "$BATCH_DIR" 2>/dev/null || true
    
    echo "Batch $BATCH_NUM complete."
    
    # Small delay between batches to be respectful
    sleep 2
done

echo "Extraction complete! Total articles processed: $TOTAL"
echo "Index file created at: $INDEX_FILE"