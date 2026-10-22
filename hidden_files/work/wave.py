import json, re, os, glob, sys, urllib.request, time, subprocess, shutil
W=os.path.expanduser("~/workspace/github/ai-papers/hidden_files/work")
REPO=os.path.expanduser("~/workspace/github/ai-papers")
WAVE=sys.argv[1]; THRESH=int(sys.argv[2]); CAP=150
def norm(t):
    t=(t or '').lower(); t=re.sub(r'[^a-z0-9 ]+',' ',t); return re.sub(r'\s+',' ',t).strip()
# inventory
papers=[]
for tf in glob.glob(REPO+"/topics/*.md"):
    for line in open(tf, encoding='utf-8'):
        if not line.startswith('|') or '---' in line or 'Paper |' in line: continue
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells)<3: continue
        m=re.search(r'arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5})', cells[2])
        papers.append(dict(title=cells[0], arxiv=m.group(1) if m else None, topic=os.path.basename(tf)))
json.dump(papers, open(W+f'/inventory_w{WAVE}.json','w'))
print(f"[wave{WAVE}] rows:", len(papers), flush=True)
# refs for new ids
refs=json.load(open(W+'/s2refs.json'))
ids=sorted({p['arxiv'] for p in papers if p['arxiv']})
todo=[i for i in ids if i not in refs]
print("new ref fetches:", len(todo), flush=True)
for s in range(0,len(todo),300):
    batch=todo[s:s+300]
    body=json.dumps({"ids":["arXiv:"+i for i in batch]}).encode()
    for a in range(6):
        try:
            req=urllib.request.Request("https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,references.title,references.externalIds,references.year", data=body, headers={"Content-Type":"application/json"})
            data=json.load(urllib.request.urlopen(req, timeout=300))
            for axid,d in zip(batch,data): refs[axid]=d
            break
        except Exception as e: print("retry",s,e); time.sleep(20*(a+1))
    json.dump(refs, open(W+'/s2refs.json','w')); time.sleep(3)
present_ax={p['arxiv'] for p in papers if p['arxiv']}
present_titles={norm(p['title']) for p in papers}
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
json.dump(allc, open(W+f'/candidates_w{WAVE}.json','w'), indent=1)
print("missing >=3:", sum(1 for n,_ in rows if n>=3), "| >=5:", sum(1 for n,_ in rows if n>=5), flush=True)
# attempted set: all previous state files' failed + unobtainable list
attempted=set()
for fn in glob.glob(W+'/wave_state*.json'):
    st=json.load(open(fn))
    for f in st.get('failed',[]): attempted.add(norm(f['title']))
for t in ['the winograd schema challenge','rectified linear units improve restricted boltzmann machines','deepspeed system optimizations enable training deep learning models with over 100 billion parameters','backpropagation applied to handwritten zip code recognition','finding structure in time','imagenet a large scale hierarchical image database','rank analysis of incomplete block designs the method of paired comparisons','stanford alpaca an instruction following llama model','vicuna an open source chatbot impressing gpt 4 with 90 chatgpt quality','gpt neo large scale autoregressive language modeling with mesh tensorflow','gpt j 6b a 6 billion parameter autoregressive language model','reinforcement learning an introduction','jax composable transformations of python numpy programs','openwebtext corpus','alpacaeval an automatic evaluator of instruction following models','a mathematical framework for transformer circuits','jurassic 1 technical details and evaluation','choice of plausible alternatives an evaluation of commonsense causal reasoning','automatically constructing a corpus of sentential paraphrases','nuqmm quantized matmul for efficient inference of large scale generative language models','the commitmentbank investigating projection in naturally occurring discourse','gradient flow in recurrent nets the difficulty of learning long term dependencies','looking beyond the surface a challenge set for reading comprehension over multiple sentences']:
    attempted.add(t)
JUNK=['分で分かる','framework for few-shot language model evaluation','if the contribution is primarily','openai','nvidia','qwen team','huggingface','hugging face','the conference paper','anthropic','together computer','(preprint)','this paper is included in the proceedings','2023 vicuna','2023 stanford alpaca','acl anthology network','needle in a haystack','pascal recognising textual entailment','pascal recognizing textual entailment']
targets=[]
for r in allc:
    if r['count']<THRESH: break
    nt=norm(r['title'])
    if nt in attempted: continue
    if any(j in nt for j in JUNK): continue
    targets.append(r)
print(f"targets (>={THRESH}):", len(targets), "| arxiv:", sum(1 for r in targets if r['arxiv']), flush=True)
# resolve arxiv targets via S2 batch
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
        except Exception as e: print("retry meta",s,e); time.sleep(20*(a+1))
    time.sleep(3)
items=[]
for ax,d in meta.items():
    if not d: continue
    items.append(dict(title=d.get('title'), authors=[a.get('name') for a in d.get('authors') or []],
        published=d.get('publicationDate') or (str(d['year']) if d.get('year') else None),
        abstract=d.get('abstract') or ((d.get('tldr') or {}).get('text')), arxiv=ax,
        pdf_url=f"https://arxiv.org/pdf/{ax}", link=f"[{ax}](https://arxiv.org/abs/{ax})", key=('ax',ax), citers=citers.get(ax,0)))
items.sort(key=lambda x:-x['citers'])
json.dump(items, open(W+f'/items_w{WAVE}.json','w'), indent=1)
json.dump(papers, open(W+'/inventory.json','w'))
print("items:", len(items), flush=True)
