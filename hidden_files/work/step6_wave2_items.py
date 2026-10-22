import json, os, urllib.request, time
W=os.path.expanduser("~/workspace/github/ai-papers/hidden_files/work")
targets=json.load(open(W+'/targets2.json'))
citers={r['arxiv']: r['count'] for r in targets if r['arxiv']}
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
items=[]
for ax,d in meta.items():
    if not d: continue
    items.append(dict(title=d.get('title'), authors=[a.get('name') for a in d.get('authors') or []],
        published=d.get('publicationDate') or (str(d['year']) if d.get('year') else None),
        abstract=d.get('abstract') or ((d.get('tldr') or {}).get('text')), arxiv=ax,
        pdf_url=f"https://arxiv.org/pdf/{ax}", link=f"[{ax}](https://arxiv.org/abs/{ax})", key=('ax',ax), citers=citers.get(ax,0)))
items.sort(key=lambda x:-x['citers'])
json.dump(items, open(W+'/items_wave2.json','w'), indent=1)
print("wave2 items:", len(items))
