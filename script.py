import json
matches = []
for l in open(r'C:\Users\amarn\.gemini\antigravity-ide\brain\e688e573-846d-4e87-b775-315f1ae440a1\.system_generated\logs\transcript_full.jsonl', encoding='utf-8'):
  if 'TargetFile' in l and 'index.html' in l:
    try:
      d = json.loads(l)
      if 'tool_calls' in d:
        for tc in d['tool_calls']:
          if tc['name'] == 'write_to_file' and 'index.html' in tc['args'].get('TargetFile', ''):
            matches.append(tc['args']['CodeContent'])
    except: pass

for i, m in enumerate(matches):
  with open(f'restored_index_{i}.html', 'w', encoding='utf-8') as f:
    f.write(m)
