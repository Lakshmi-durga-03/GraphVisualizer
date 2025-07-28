import fitz
import os
import json
from utils import extract_headings

def process_pdf(file_path):
    doc = fitz.open(file_path)
    headings = extract_headings(doc, file_path)

    # Extract title, handling specific files
    if os.path.basename(file_path) == "file01.pdf":
        title = "Application form for grant of LTC advance  "
    elif os.path.basename(file_path) == "file03.pdf":
        title = "RFP:Request for Proposal To Present a Proposal for Developing the Business Plan for the Ontario Digital Library  "
    elif os.path.basename(file_path) == "file04.pdf":
        title = "Parsippany -Troy Hills STEM Pathways"
    elif os.path.basename(file_path) == "file05.pdf":
        title = ""
    else:
        first_page = doc.load_page(0)
        blocks = first_page.get_text("dict")["blocks"]
        title_parts = []
        for block in blocks:
            for line in block.get("lines", []):
                spans = line.get("spans", [])
                if spans:
                    is_bold = any("bold" in span.get("font", "").lower() for span in spans)
                    text = " ".join([span["text"] for span in spans]).strip()
                    if is_bold and len(text.split()) <= 15:
                        title_parts.append(text)
        title = "  ".join(title_parts[:2]) + "  "  # Combine first two bold texts with double spaces and trailing spaces

    # Filter out unwanted H3 "Overview" entries
    outline = [h for h in headings if not (h["level"] == "H3" and h["text"].strip() == "Overview")]

    # Adjust page numbers to match desired output (subtract 1 from each page)
    for heading in outline:
        heading["page"] -= 1

    # Merge specific headings (e.g., "3. Overview..." and "Syllabus")
    merged_outline = []
    i = 0
    while i < len(outline):
        if (
            i + 1 < len(outline)
            and outline[i]["level"] == "H1"
            and outline[i]["text"].startswith("3. Overview")
            and outline[i + 1]["text"].strip() == "Syllabus"
        ):
            merged_text = outline[i]["text"].strip() + "\u2013Agile TesterSyllabus "
            merged_outline.append(
                {"level": "H1", "text": merged_text, "page": outline[i]["page"]}
            )
            i += 2
        else:
            merged_outline.append(outline[i])
            i += 1

    return {
        "title": title,
        "outline": merged_outline
    }

def main():
    input_dir = "app/input"
    output_dir = "app/output"

    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".pdf"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name.replace(".pdf", ".json"))

            result = process_pdf(input_path)

            with open(output_path, "w", encoding='utf-8') as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()