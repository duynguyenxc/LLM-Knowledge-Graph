import os
import re
from pypdf import PdfReader

# PDF extraction
pdf_dir = r"d:\LLM-Knowledge-Graph\documents\new-documents-from-professor"
pdf_files = [
    "NotebookLM output-agentic framework-sent-1.pdf",
    "grok output -KG and GraphRag-sent-2.pdf",
    "Grok output plugin agent-sent-3.pdf",
]

output_md = r"d:\LLM-Knowledge-Graph\scratch_documents_transcripts.md"

with open(output_md, "w", encoding="utf-8") as out_f:
    out_f.write("# PDF Documents from Professor\n\n")
    for pdf_name in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_name)
        out_f.write(f"## {pdf_name}\n\n")
        try:
            reader = PdfReader(pdf_path)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    out_f.write(text + "\n")
        except Exception as e:
            out_f.write(f"Error reading PDF: {e}\n")
        out_f.write("\n" + "="*40 + "\n\n")
        
    out_f.write("# Meeting Transcripts\n\n")
    transcript_dir = r"d:\LLM-Knowledge-Graph\transcript-meetings"
    vtt_files = sorted(os.listdir(transcript_dir))
    
    for vtt_name in vtt_files:
        if vtt_name.endswith(".vtt"):
            vtt_path = os.path.join(transcript_dir, vtt_name)
            out_f.write(f"## {vtt_name}\n\n")
            with open(vtt_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Clean up VTT timestamps and WEBVTT header
                content = re.sub(r"WEBVTT\n\n", "", content)
                content = re.sub(r"([0-9a-f\-]+)[\r\n]+", "", content) # removing uuids
                content = re.sub(r"\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\n", "", content)
                content = re.sub(r"<v [^>]+>", "", content)
                content = re.sub(r"</v>", "", content)
                # Remove empty lines
                lines = [line.strip() for line in content.split("\n") if line.strip()]
                out_f.write(" ".join(lines) + "\n\n")
            out_f.write("\n" + "="*40 + "\n\n")

print("Done extracting into markdown.")
