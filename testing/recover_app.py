import json
import re

lines_dict = {}
max_line = 0

with open(r'C:\Users\amarn\.gemini\antigravity-ide\brain\a13a9dc4-aed2-4d44-8428-795ef6bc3f02\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') == 'PLANNER_RESPONSE':
                # look for view_file tool calls? No, the tool output is in the next step, or in the SYSTEM/MODEL message.
                pass
            if data.get('content'):
                content = data['content']
                # if it's a tool output from view_file
                if "File Path: `file:///C:/Users/amarn/OneDrive/Desktop/dbOnyxOnAntigravity/privet/onyx_reports/app.py`" in content:
                    # Parse the lines
                    for line_text in content.split('\n'):
                        m = re.match(r'^(\d+):\s(.*)$', line_text)
                        if m:
                            line_num = int(m.group(1))
                            text = m.group(2)
                            lines_dict[line_num] = text
                            if line_num > max_line:
                                max_line = line_num
        except Exception:
            pass

print(f"Recovered {len(lines_dict)} unique lines from transcript.")
if len(lines_dict) > 0:
    print(f"Max line number: {max_line}")
    # Write to a dump file to inspect
    with open('testing/recovered_app.py', 'w', encoding='utf-8') as out:
        for i in range(1, max_line + 1):
            out.write(lines_dict.get(i, f"# MISSING LINE {i}\n") + '\n')
    print("Wrote recovered lines to testing/recovered_app.py")
