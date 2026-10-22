import re, os, json, glob, urllib.request, time
W=os.path.expanduser("~/workspace/github/ai-papers/hidden_files/work")
repo=os.path.expanduser("~/workspace/github/ai-papers")
def norm(t):
    t=(t or '').lower(); t=re.sub(r'[^a-z0-9 ]+',' ',t); return re.sub(r'\s+',' ',t).strip()
papers=[]
for tf in glob.glob(repo+"/topics/*.md"):
    topic=os.path.basename(tf)
    for line in open(tf, encoding='utf-8'):
        if not line.startswith('|') or '---' in line or 'Paper |' in line: continue
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells)<3: continue
        m=re.search(r'arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5})', cells[2])
        papers.append(dict(title=cells[0], arxiv=m.group(1) if m else None, topic=topic,
                           added=cells[5] if len(cells)>5 else ''))
json.dump(papers, open(W+'/inventory.json','w'))
print("rows:", len(papers), "arxiv:", sum(1 for p in papers if p['arxiv']))
# pilot additions = rows added 2026-10-21 beyond Orca (orca added by parent before job start; identify by file presence in git untracked)
ids=sorted({p['arxiv'] for p in papers if p['arxiv']})
out={}
p=W+'/s2refs.json'
if os.path.exists(p): out=json.load(open(p))
todo=[i for i in ids if i not in out]
print("s2 todo:", len(todo))
B=300
for s in range(0,len(todo),B):
    batch=todo[s:s+B]
    body=json.dumps({"ids":["arXiv:"+i for i in batch]}).encode()
    for a in range(6):
        try:
            req=urllib.request.Request("https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,references.title,references.externalIds,references.year", data=body, headers={"Content-Type":"application/json"})
            data=json.load(urllib.request.urlopen(req, timeout=300))
            for axid,d in zip(batch,data): out[axid]=d
            break
        except Exception as e: print("retry",s,e); time.sleep(20*(a+1))
    json.dump(out, open(p,'w'))
    print("done", s+len(batch), "of", len(todo), flush=True)
    time.sleep(3)
print("s2 total:", len(out), "nulls:", sum(1 for v in out.values() if not v))
