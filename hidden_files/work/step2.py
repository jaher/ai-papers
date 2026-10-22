import json, re, os, urllib.request, time
W=os.path.expanduser("~/workspace/github/ai-papers/hidden_files/work")
def norm(t):
    t=(t or '').lower(); t=re.sub(r'[^a-z0-9 ]+',' ',t); return re.sub(r'\s+',' ',t).strip()
inv=json.load(open(W+'/inventory.json'))
present_ax={p['arxiv'] for p in inv if p['arxiv']}
present_titles={norm(p['title']) for p in inv}
refs=json.load(open(W+'/s2refs.json'))
from collections import defaultdict
cand={}
for citer_ax,d in refs.items():
    if not d: continue
    for r in d.get('references') or []:
        ext=r.get('externalIds') or {}
        ax=ext.get('ArXiv'); title=r.get('title')
        if not title and not ax: continue
        key=('ax:'+ax) if ax else ('t:'+norm(title))
        c=cand.setdefault(key, dict(title=title, arxiv=ax, year=r.get('year'), citers=set()))
        if title and not c['title']: c['title']=title
        c['citers'].add(citer_ax)
rows=[]
for k,c in cand.items():
    if c['arxiv'] and c['arxiv'] in present_ax: continue
    if c['title'] and norm(c['title']) in present_titles: continue
    rows.append((len(c['citers']), c))
rows.sort(key=lambda x:-x[0])
allc=[dict(count=n, title=c['title'], arxiv=c['arxiv'], year=c['year']) for n,c in rows]
json.dump(allc, open(W+'/candidates.json','w'), indent=1)
print("distinct cited:", len(cand), "| >=3:", sum(1 for n,_ in rows if n>=3), "| >=5:", sum(1 for n,_ in rows if n>=5), "| >=9:", sum(1 for n,_ in rows if n>=9))
JUNK=['分で分かる','framework for few-shot language model evaluation','if the contribution is primarily','openai','nvidia','qwen team','huggingface','hugging face','the conference paper','anthropic','together computer','(preprint)','this paper is included in the proceedings','2023 vicuna','2023 stanford alpaca','acl anthology network','needle in a haystack']
targets=[]
for r in allc:
    if r['count']<9: break
    if any(j in norm(r['title']) for j in JUNK): continue
    targets.append(r)
json.dump(targets, open(W+'/targets.json','w'), indent=1)
print("targets:", len(targets))
axids=[r['arxiv'] for r in targets if r['arxiv']]
meta={}
for s in range(0,len(axids),300):
    batch=axids[s:s+300]
    body=json.dumps({"ids":["arXiv:"+i for i in batch]}).encode()
    for a in range(6):
        try:
            req=urllib.request.Request("https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,authors,year,publicationDate,abstract,tldr,externalIds,openAccessPdf", data=body, headers={"Content-Type":"application/json"})
            data=json.load(urllib.request.urlopen(req, timeout=300))
            for axid,d in zip(batch,data): meta[axid]=d
            break
        except Exception as e: print("retry",s,e); time.sleep(20*(a+1))
    time.sleep(3)
json.dump(meta, open(W+'/meta_ax.json','w'))
print("arxiv meta:", len(meta))
