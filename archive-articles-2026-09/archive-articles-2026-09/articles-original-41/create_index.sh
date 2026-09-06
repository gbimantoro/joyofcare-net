#!/bin/bash

# Create index.json from extracted articles
ARTICLES_DIR="/home/gobeam/Projects/joyofcare-net/articles"
INDEX_FILE="$ARTICLES_DIR/index.json"

echo "[" > "$INDEX_FILE"

FIRST=true
for f in "$ARTICLES_DIR"/*.txt; do
    [ -f "$f" ] || continue
    
    SLUG=$(basename "$f" .txt)
    TITLE=$(grep -m1 "^Title:" "$f" | sed 's/^Title: //' | sed 's/"/\\"/g' | head -c 200)
    URL=$(grep -m1 "^URL:" "$f" | sed 's/^URL: //')
    CATEGORY=$(grep -m1 "^Category:" "$f" | sed 's/^Category: //')
    WORD_COUNT=$(wc -w < "$f")
    
    if [ "$FIRST" = true ]; then
        FIRST=false
    else
        echo "," >> "$INDEX_FILE"
    fi
    
    echo "  {\"slug\":\"$SLUG\",\"title\":\"$TITLE\",\"url\":\"$URL\",\"category\":\"$CATEGORY\",\"word_count\":$WORD_COUNT}" >> "$INDEX_FILE"
done

echo "" >> "$INDEX_FILE"
echo "]" >> "$INDEX_FILE"

# Validate JSON
if jq empty "$INDEX_FILE" 2>/dev/null; then
    echo "Index created successfully with $(jq length "$INDEX_FILE") articles"
else
    echo "JSON validation failed, attempting to fix..."
    # Try to fix common issues
    sed -i 's/"/\\"/g; s/\\"/"/g' "$INDEX_FILE"
    if jq empty "$INDEX_FILE" 2>/dev/null; then
        echo "Fixed and validated: $(jq length "$INDEX_FILE") articles"
    else
        echo "Could not fix JSON automatically"
    fi
fi