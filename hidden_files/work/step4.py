import json, re, os, subprocess, sys, shutil
W=os.path.expanduser("~/workspace/github/ai-papers/hidden_files/work")
REPO=os.path.expanduser("~/workspace/github/ai-papers")
ART=os.path.expanduser("~/workspace/articles")
ADDED_DATE="2026-10-21"
def norm(t):
    t=(t or '').lower(); t=re.sub(r'[^a-z0-9 ]+',' ',t); return re.sub(r'\s+',' ',t).strip()
def kebab(t):
    k=re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-')
    if len(k)>100: k=k[:100].rsplit('-',1)[0]
    return k
inv=json.load(open(os.environ.get('INV_FILE', W+'/inventory.json')))
present_ax={p['arxiv'] for p in inv if p['arxiv']}
present_titles={norm(p['title']) for p in inv}
sp=os.environ.get('STATE_FILE', W+'/wave_state.json')
state=json.load(open(sp)) if os.path.exists(sp) else dict(added=[], skipped=[], failed=[])
done_titles={norm(a['title']) for a in state['added']}
done_ax={a['arxiv'] for a in state['added'] if a.get('arxiv')}
def topic_for(title):
    t=title.lower()
    if 'speculative' in t: return 'speculative-decoding.md'
    if 'quantiz' in t or 'int8' in t or 'binarized' in t or 'binary neural' in t or 'low precision' in t or 'quantized neural' in t: return 'quantization.md'
    if 'kv cache' in t or 'key-value' in t: return 'kv-cache-eviction.md'
    if 'lora' in t: return 'lora.md'
    if 'serving' in t or 'inference system' in t: return 'serving-engines.md'
    if any(k in t for k in ['distributed','parallel','deepspeed','zero:','pipedream','megatron','model parallelism']): return 'distributed-inference.md'
    if any(k in t for k in ['pruning','prune','distillation','compression','sparsity','sparse model']): return 'model-compression.md'
    if 'attention' in t and any(k in t for k in ['kernel','flash','efficient','fast']): return 'attention-kernels.md'
    if any(k in t for k in ['human feedback','preference','alignment','instruction','feedback','chatbot','reinforcement learning from']): return 'post-training.md'
    if 'visual instruction' in t or 'visual language' in t: return 'model-reports.md'
    if 'tokeniz' in t: return 'tokenizers.md'
    return 'foundational.md'
def stars(c):
    if c>=45: return '★★★★★',5
    if c>=25: return '★★★★☆',4
    if c>=13: return '★★★☆☆',3
    if c>=8: return '★★☆☆☆',2
    return '★☆☆☆☆',1
def pubkey(s):
    if not s: return (0,0,0)
    p=[int(x) for x in re.findall(r'\d+', str(s))[:3]]
    return tuple(p+[0]*(3-len(p)))
def authors_str(authors):
    authors=[a for a in (authors or []) if a]
    if not authors: return 'Unknown'
    if len(authors)==1: return authors[0]
    if len(authors)==2: return f"{authors[0]} and {authors[1]}"
    return f"{authors[0]} et al."
def summary_of(it, pdftext=None):
    ab=it.get('abstract')
    if not ab and pdftext:
        m=re.search(r'\bAbstract\b(.{200,3000}?)(?:\n\s*1\.?\s+Introduction|\nIntroduction\b)', pdftext, re.S)
        if m: ab=re.sub(r'\s+',' ',m.group(1)).strip()
    if not ab: return 'Summary unavailable from source.'
    ab=re.sub(r'\s+',' ',ab).strip().replace('|','/')
    if len(ab)>260:
        cut=ab[:260]; sent=cut.rfind('. ')
        ab=(cut[:sent+1] if sent>120 else cut.rsplit(' ',1)[0])
    return ab
def insert_row(topicfile, row, tier, pk):
    path=os.path.join(REPO,'topics',topicfile)
    lines=open(path,encoding='utf-8').read().split('\n')
    rowidx=[i for i,l in enumerate(lines) if l.startswith('| ') and '---' not in l and not l.startswith('| Paper')]
    def rowinfo(l):
        cells=[c.strip() for c in l.strip().strip('|').split('|')]
        t=cells[1].count('★') if len(cells)>1 else 0
        return t,(pubkey(cells[4]) if len(cells)>4 else (0,0,0))
    ins=None
    for i in rowidx:
        t,p2=rowinfo(lines[i])
        if t<tier or (t==tier and p2>pk): ins=i; break
    if ins is None: ins=rowidx[-1]+1 if rowidx else len(lines)
    lines.insert(ins,row)
    open(path,'w',encoding='utf-8').write('\n'.join(lines))
def first_pages_text(pdf):
    r=subprocess.run(['pdftotext','-f','1','-l','2',pdf,'-'],capture_output=True,text=True)
    return r.stdout or ''
STOP=set('the a an of for and in on to with by from as at are is be or via using used use'.split())
def title_ok(title, text):
    words=[w for w in norm(title).split() if len(w)>3 and w not in STOP]
    if not words: return True
    nt=norm(text)
    hit=sum(1 for w in set(words) if w in nt)
    return hit/max(1,len(set(words)))>=0.6
items=json.load(open(os.environ.get('ITEMS_FILE', W+'/items_wave1.json')))
LIMIT=int(sys.argv[1]) if len(sys.argv)>1 else 100000
CAP=int(sys.argv[2]) if len(sys.argv)>2 else 141
n=0
for it in items:
    if len(state['added'])>=CAP: break
    if n>=LIMIT: break
    title=it['title']
    if norm(title) in done_titles or norm(title) in present_titles:
        state['skipped'].append(dict(title=title, reason='already present (title)')); continue
    if it.get('arxiv') and (it['arxiv'] in present_ax or it['arxiv'] in done_ax):
        state['skipped'].append(dict(title=title, reason=f"already present (arXiv {it['arxiv']})")); continue
    n+=1
    fname=kebab(title)+(f"_{it['arxiv'].replace('/','-')}" if it.get('arxiv') else '')+'.pdf'
    dest=os.path.join(REPO,'papers',fname)
    if os.path.exists(dest):
        state['skipped'].append(dict(title=title, reason='pdf file already exists')); continue
    tmp=W+f"/dl_{abs(hash(title))%99999}.pdf"
    ok=False; txt=''
    for attempt in range(2):
        subprocess.run(['curl','-sL','--max-time','90','-A','Mozilla/5.0 (X11; Linux x86_64) ai-papers-closure','-o',tmp,it['pdf_url']], capture_output=True)
        if os.path.exists(tmp) and subprocess.run(['file','-b',tmp],capture_output=True,text=True).stdout.startswith('PDF'):
            txt=first_pages_text(tmp); ok=title_ok(title, txt)
        if ok: break
    if not ok:
        state['failed'].append(dict(title=title, arxiv=it.get('arxiv'), url=it['pdf_url'], reason='download failed or title mismatch'))
        if os.path.exists(tmp): os.remove(tmp)
        json.dump(state, open(sp,'w'), indent=1); continue
    shutil.copy(tmp, dest); shutil.copy(tmp, os.path.join(ART, fname)); os.remove(tmp)
    st,tier=stars(it['citers'])
    topic=topic_for(title)
    pub=it.get('published') or ''
    row=f"| {title} | {st} | {it['link']} | {authors_str(it['authors'])} | {pub} | {ADDED_DATE} | {summary_of(it, txt)} |"
    insert_row(topic, row, tier, pubkey(pub))
    state['added'].append(dict(title=title, arxiv=it.get('arxiv'), topic=topic, stars=st, citers=it['citers'], file=fname))
    done_titles.add(norm(title))
    if it.get('arxiv'): done_ax.add(it['arxiv'])
    print("ADDED", it['citers'], st, topic, title[:65], flush=True)
    json.dump(state, open(sp,'w'), indent=1)
print("added this state:", len(state['added']), "| skipped:", len(state['skipped']), "| failed:", len(state['failed']))
