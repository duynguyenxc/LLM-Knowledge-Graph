import os
import re
import textwrap

transcript_dir = r"d:\LLM-Knowledge-Graph\transcript-meetings"
vtt_files = sorted([f for f in os.listdir(transcript_dir) if f.endswith(".vtt")])

for vtt_name in vtt_files:
    vtt_path = os.path.join(transcript_dir, vtt_name)
    out_path = os.path.join(transcript_dir, vtt_name + ".txt")
    with open(vtt_path, "r", encoding="utf-8") as f:
        content = f.read()
        content = re.sub(r"WEBVTT\n\n", "", content)
        content = re.sub(r"([0-9a-f\-]+)[\r\n]+", "", content)
        content = re.sub(r"\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\n", "", content)
        content = re.sub(r"<v [^>]+>", "", content)
        content = re.sub(r"</v>", "", content)
        lines = [line.strip() for line in content.split("\n") if line.strip()]
        full_text = " ".join(lines)
        wrapped = textwrap.fill(full_text, width=80)
    with open(out_path, "w", encoding="utf-8") as out_f:
        out_f.write(wrapped)

print("Transcripts cleaned and wrapped.")
