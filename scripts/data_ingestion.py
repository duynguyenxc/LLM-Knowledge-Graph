import os
import json
import logging
from pypdf import PdfReader

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def ingest_data():
    metadata_file = r"d:\LLM-Knowledge-Graph\data\studies_metadata.jsonl"
    pdf_dir = r"d:\LLM-Knowledge-Graph\data\20-paper-of-Richmond"
    output_dir = r"d:\LLM-Knowledge-Graph\graphrag\input"
    
    os.makedirs(output_dir, exist_ok=True)
    
    processed_count = 0
    missing_docs = []

    with open(metadata_file, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
                source_file = record.get("source_id")
                
                if not source_file or not source_file.endswith(".pdf"):
                    continue
                
                pdf_path = os.path.join(pdf_dir, source_file)
                
                if not os.path.exists(pdf_path):
                    logging.warning(f"PDF not found: {source_file}")
                    missing_docs.append(source_file)
                    continue

                # Prepare metadata header
                title = record.get("title", "Unknown Title")
                authors = ", ".join(record.get("authors", []))
                year = record.get("year", "Unknown Year")
                doi = record.get("doi", "No DOI")
                
                header = f"TITLE: {title}\nAUTHORS: {authors}\nYEAR: {year}\nDOI: {doi}\n\nCONTENT:\n"
                
                # Extract text
                extracted_text = []
                try:
                    reader = PdfReader(pdf_path)
                    for page in reader.pages:
                        text = page.extract_text()
                        if text:
                            extracted_text.append(text)
                except Exception as e:
                    logging.error(f"Error parsing PDF {pdf_path}: {e}")
                    continue
                
                # Write to GraphRAG input
                output_filename = f"{source_file}.txt"
                output_path = os.path.join(output_dir, output_filename)
                
                with open(output_path, "w", encoding="utf-8") as out_f:
                    out_f.write(header)
                    out_f.write("\n".join(extracted_text))
                
                processed_count += 1
                logging.info(f"Processed: {source_file}")

            except json.JSONDecodeError:
                logging.error(f"JSON decode error on line {line_num}")
                
    logging.info(f"\nIngestion Complete. Processed {processed_count} files.")
    if missing_docs:
        logging.info(f"Missing PDFs: {len(missing_docs)}")

if __name__ == "__main__":
    ingest_data()
