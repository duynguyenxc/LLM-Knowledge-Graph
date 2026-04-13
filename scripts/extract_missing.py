import os
from PyPDF2 import PdfReader

# Ensure output is clean
output_file = "scratch_missing_docs.md"
with open(output_file, "w", encoding="utf-8") as out:
    
    docs = [
        r"d:\LLM-Knowledge-Graph\data\in4-about-28-studies-paper.pdf",
        r"d:\LLM-Knowledge-Graph\data\paper-Richmond-original.pdf",
        r"d:\LLM-Knowledge-Graph\documents\Human-Workflow-from-paper-Richmond.pdf",
        r"d:\LLM-Knowledge-Graph\documents\Plan-for-model-verification-professor-send-initial-when- begin-project.pdf",
        r"d:\LLM-Knowledge-Graph\documents\Richmond-KG-Specification-my-work-before-professor-send-more-documents.pdf",
        r"d:\LLM-Knowledge-Graph\documents\paper-Microsoft-GraphRAG.pdf"
    ]

    for pdf_path in docs:
        out.write(f"## {os.path.basename(pdf_path)}\n\n")
        try:
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    out.write(text.replace("\n", " ") + "\n")
        except Exception as e:
            out.write(f"Error reading {pdf_path}: {e}\n")
        out.write("\n========================================\n\n")

print("Done extracting missing docs.")
