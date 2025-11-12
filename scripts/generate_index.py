import os, json

root_dir = "Sections"

for subdir, dirs, files in os.walk(root_dir):
    pdfs = [f for f in files if f.lower().endswith(".pdf")]
    if pdfs:
        index_path = os.path.join(subdir, "index.json")
        data = {"pdfs": sorted(pdfs)}
        with open(index_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"✅ Updated {index_path} with {len(pdfs)} PDFs")
