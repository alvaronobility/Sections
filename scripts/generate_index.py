import os, json

base_dir = "Sections"

for root, dirs, files in os.walk(base_dir):
    pdfs = [f for f in sorted(files) if f.lower().endswith(".pdf")]
    if not pdfs:
        continue

    index_path = os.path.join(root, "index.json")
    with open(index_path, "w") as f:
        json.dump(pdfs, f, indent=2)

    print(f"✅ Created {index_path} with {len(pdfs)} entries.")
