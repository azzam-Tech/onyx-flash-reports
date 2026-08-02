import json
import codecs

output = []
with codecs.open(r"C:\Users\amarn\.gemini\antigravity-ide\brain\a13a9dc4-aed2-4d44-8428-795ef6bc3f02\.system_generated\logs\transcript.jsonl", "r", "utf-8") as f:
    for line in f:
        if "محاسب سابق" in line or "الخلل عندي" in line or "التكلفة الحقيقية" in line:
            data = json.loads(line)
            if data.get("type") == "USER_INPUT":
                output.append(data.get("content"))

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\out_transcript.txt", "w", "utf-8") as f:
    for text in output:
        f.write(text + "\n")
