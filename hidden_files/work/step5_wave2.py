import json, re, os, glob, urllib.request, time
W=os.path.expanduser("~/workspace/github/ai-papers/hidden_files/work")
repo=os.path.expanduser("~/workspace/github/ai-papers")
def norm(t):
    t=(t or '').lower(); t=re.sub(r'[^a-z0-9 ]+',' ',t); return re.sub(r'\s+',' ',t).strip()
# rebuild inventory
papers=[]
for tf in glob.glob(repo+"/topics/*.md"):
    for line in open(tf, encoding='utf-8'):
        if not line.startswith('|') or '---' in line or 'Paper |' in line: continue
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells)<3: continue
        m=re.search(r'arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5})', cells[2])
        papers.append(dict(title=cells[0], arxiv=m.group(1) if m else None, topic=os.path.basename(tf)))
json.dump(papers, open(W+'/inventory2.json','w'))
print("rows now:", len(papers))
# fetch refs for arxiv ids not yet in s2refs
refs=json.load(open(W+'/s2refs.json'))
ids=sorted({p['arxiv'] for p in papers if p['arxiv']})
todo=[i for i in ids if i not in refs]
print("new ref fetches:", len(todo))
B=300
for s in range(0,len(todo),B):
    batch=todo[s:s+B]
    body=json.dumps({"ids":["arXiv:"+i for i in batch]}).encode()
    for a in range(6):
        try:
            req=urllib.request.Request("https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,references.title,references.externalIds,references.year", data=body, headers={"Content-Type":"application/json"})
            data=json.load(urllib.request.urlopen(req, timeout=300))
            for axid,d in zip(batch,data): refs[axid]=d
            break
        except Exception as e: print("retry",s,e); time.sleep(20*(a+1))
    json.dump(refs, open(W+'/s2refs.json','w'))
    print("done", s+len(batch), flush=True); time.sleep(3)
# aggregate over enlarged collection
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
json.dump(allc, open(W+'/candidates2.json','w'), indent=1)
for n in (3,5,7,8,9,10):
    print(f"missing cited by >={n}:", sum(1 for c,_ in rows if c>=n))
# attempted/unobtainable exclusion set from wave1 state + log titles
s1=json.load(open(W+'/wave_state.json'))
attempted={norm(f['title']) for f in s1['failed']}
for t in ['the winograd schema challenge','rectified linear units improve restricted boltzmann machines','deepspeed system optimizations enable training deep learning models with over 100 billion parameters','backpropagation applied to handwritten zip code recognition','finding structure in time','imagenet a large scale hierarchical image database','rank analysis of incomplete block designs the method of paired comparisons','stanford alpaca an instruction following llama model','vicuna an open source chatbot impressing gpt 4 with 90 chatgpt quality','gpt neo large scale autoregressive language modeling with mesh tensorflow','gpt j 6b a 6 billion parameter autoregressive language model','reinforcement learning an introduction','jax composable transformations of python numpy programs','openwebtext corpus','alpacaeval an automatic evaluator of instruction following models','a mathematical framework for transformer circuits','jurassic 1 technical details and evaluation','choice of plausible alternatives an evaluation of commonsense causal reasoning','automatically constructing a corpus of sentential paraphrases','nuqmm quantized matmul for efficient inference of large scale generative language models','the commitmentbank investigating projection in naturally occurring discourse','gradient flow in recurrent nets the difficulty of learning long term dependencies','looking beyond the surface a challenge set for reading comprehension over multiple sentences']:
    attempted.add(t)
JUNK=['分で分かる','framework for few-shot language model evaluation','if the contribution is primarily','openai','nvidia','qwen team','huggingface','hugging face','the conference paper','anthropic','together computer','(preprint)','this paper is included in the proceedings','2023 vicuna','2023 stanford alpaca','acl anthology network','needle in a haystack','pascal recognising textual entailment','pascal recognizing textual entailment']
targets=[]
for r in allc:
    if r['count']<7: break
    nt=norm(r['title'])
    if nt in attempted: continue
    if any(j in nt for j in JUNK): continue
    targets.append(r)
json.dump(targets, open(W+'/targets2.json','w'), indent=1)
print("wave2 targets (>=7, filtered):", len(targets), "| with arxiv:", sum(1 for r in targets if r['arxiv']))
