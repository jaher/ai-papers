import json, re, os, urllib.request, xml.etree.ElementTree as ET
W=os.path.expanduser("~/workspace/github/ai-papers/hidden_files/work")
def norm(t):
    t=(t or '').lower(); t=re.sub(r'[^a-z0-9 ]+',' ',t); return re.sub(r'\s+',' ',t).strip()
targets=json.load(open(W+'/targets.json'))
citers={norm(r['title']): r['count'] for r in targets}
tgt_ax={r['arxiv']:r['count'] for r in targets if r['arxiv']}
items=[]
meta_ax=json.load(open(W+'/meta_ax.json'))
for ax,d in meta_ax.items():
    if not d: continue
    items.append(dict(title=d.get('title'), authors=[a.get('name') for a in d.get('authors') or []],
        published=d.get('publicationDate') or (str(d['year']) if d.get('year') else None),
        abstract=d.get('abstract') or ((d.get('tldr') or {}).get('text')), arxiv=ax,
        pdf_url=f"https://arxiv.org/pdf/{ax}", link=f"[{ax}](https://arxiv.org/abs/{ax})", key=('ax',ax)))
IDMAP={'winogrande an adversarial winograd schema challenge at scale':'1907.10641',
 'transformers state of the art natural language processing':'1910.03771',
 'zero memory optimization towards training a trillion parameter models':'1910.02054',
 'specinfer accelerating generative llm serving with speculative inference and token tree verification':'2305.09781',
 'a method for stochastic optimization':'1412.6980',
 'ultrafeedback boosting language models with high quality feedback':'2310.01377',
 'optq accurate quantization for generative pre trained transformers':'2210.17323',
 'model alignment as prospect theoretic optimization':'2402.01306',
 'pipedream generalized pipeline parallelism for dnn training':'1806.03377',
 'gpt3 int8 8 bit matrix multiplication for transformers at scale':'2208.07339',
 'multiple a scalable and polyglot approach to benchmarking neural code generation':'2208.08227',
 'lm infinite simple on the fly length generalization for large language models':'2308.16137',
 'from live data to high quality benchmarks the arena hard pipeline':'2406.11939',
 'unifying language learning paradigms':'2205.05131',
 'socialiqa commonsense reasoning about social interactions':'1904.09728',
 'end to end memory networks':'1503.08895',
 'binarized neural networks':'1602.02505',
 'crosslingual generalization through multitask finetuning':'2211.01786'}
NS={'a':'http://www.w3.org/2005/Atom'}
ids=','.join(sorted(set(IDMAP.values())))
url=f"http://export.arxiv.org/api/query?id_list={ids}&max_results=50"
req=urllib.request.Request(url, headers={"User-Agent":"ai-papers-closure/1.0"})
root=ET.fromstring(urllib.request.urlopen(req, timeout=120).read())
idl={}
for e in root.findall('a:entry', NS):
    aid=re.sub(r'v\d+$','',e.find('a:id',NS).text.rsplit('/',1)[-1])
    idl[aid]=dict(title=e.find('a:title',NS).text.strip().replace('\n',' '),
        authors=[a.find('a:name',NS).text for a in e.findall('a:author',NS)],
        published=e.find('a:published',NS).text[:10], abstract=e.find('a:summary',NS).text.strip())
for nk,ax in IDMAP.items():
    d=idl.get(ax)
    if not d: print("IDLIST MISS", ax); continue
    items.append(dict(title=d['title'], authors=d['authors'], published=d['published'], abstract=d['abstract'], arxiv=ax,
        pdf_url=f"https://arxiv.org/pdf/{ax}", link=f"[{ax}](https://arxiv.org/abs/{ax})", key=('t',nk)))
CLASSICS=[
 ('language models are unsupervised multitask learners', dict(title='Language Models are Unsupervised Multitask Learners',
   authors=['Alec Radford','Jeffrey Wu','Rewon Child','David Luan','Dario Amodei','Ilya Sutskever'], published='2019-02-14', abstract=None,
   pdf_url='https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf', label='OpenAI 2019')),
 ('natural questions a benchmark for question answering research', dict(title='Natural Questions: A Benchmark for Question Answering Research',
   authors=['Tom Kwiatkowski','Jennimaria Palomaki','Olivia Redfield','Michael Collins','Ankur Parikh','Chris Alberti','Danielle Epstein','Illia Polosukhin','Jacob Devlin','Kenton Lee','Kristina Toutanova','Llion Jones','Matthew Kelcey','Ming-Wei Chang','Andrew M. Dai','Jakob Uszkoreit','Quoc Le','Slav Petrov'], published='2019-07-01', abstract=None,
   pdf_url='https://aclanthology.org/Q19-1026.pdf', label='TACL 2019')),
 ('recursive deep models for semantic compositionality over a sentiment treebank', dict(title='Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank',
   authors=['Richard Socher','Alex Perelygin','Jean Y. Wu','Jason Chuang','Christopher D. Manning','Andrew Y. Ng','Christopher Potts'], published='2013-10-01', abstract=None,
   pdf_url='https://nlp.stanford.edu/~socherr/EMNLP2013_RNTN.pdf', label='EMNLP 2013')),
 ('rouge a package for automatic evaluation of summaries', dict(title='ROUGE: A Package for Automatic Evaluation of Summaries',
   authors=['Chin-Yew Lin'], published='2004-07-01', abstract=None, pdf_url='https://aclanthology.org/W04-1013.pdf', label='ACL 2004')),
 ('bleu a method for automatic evaluation of machine translation', dict(title='BLEU: a Method for Automatic Evaluation of Machine Translation',
   authors=['Kishore Papineni','Salim Roukos','Todd Ward','Wei-Jing Zhu'], published='2002-07-01', abstract=None,
   pdf_url='https://aclanthology.org/P02-1040.pdf', label='ACL 2002')),
 ('glove global vectors for word representation', dict(title='GloVe: Global Vectors for Word Representation',
   authors=['Jeffrey Pennington','Richard Socher','Christopher D. Manning'], published='2014-10-01', abstract=None,
   pdf_url='https://nlp.stanford.edu/pubs/glove.pdf', label='EMNLP 2014')),
 ('building a large annotated corpus of english the penn treebank', dict(title='Building a Large Annotated Corpus of English: The Penn Treebank',
   authors=['Mitchell P. Marcus','Beatrice Santorini','Mary Ann Marcinkiewicz'], published='1993-01-01', abstract=None,
   pdf_url='https://aclanthology.org/J93-2004.pdf', label='Computational Linguistics 1993')),
 ('backpropagation applied to handwritten zip code recognition', dict(title='Backpropagation Applied to Handwritten Zip Code Recognition',
   authors=['Yann LeCun','Bernhard Boser','John S. Denker','Donnie Henderson','Richard E. Howard','Wayne Hubbard','Lawrence D. Jackel'], published='1989-12-01', abstract=None,
   pdf_url='http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf', label='Neural Computation 1989')),
 ('optimal brain damage', dict(title='Optimal Brain Damage', authors=['Yann LeCun','John S. Denker','Sara A. Solla'], published='1989-01-01', abstract=None,
   pdf_url='https://proceedings.neurips.cc/paper_files/paper/1989/file/6c9882bbac1c7093bd25041881277658-Paper.pdf', label="NeurIPS 1989")),
 ('learning word vectors for sentiment analysis', dict(title='Learning Word Vectors for Sentiment Analysis',
   authors=['Andrew L. Maas','Raymond E. Daly','Peter T. Pham','Dan Huang','Andrew Y. Ng','Christopher Potts'], published='2011-06-01', abstract=None,
   pdf_url='https://aclanthology.org/P11-1015.pdf', label='ACL 2011')),
 ('semantic parsing on freebase from question answer pairs', dict(title='Semantic Parsing on Freebase from Question-Answer Pairs',
   authors=['Jonathan Berant','Andrew Chou','Roy Frostig','Percy Liang'], published='2013-10-01', abstract=None,
   pdf_url='https://aclanthology.org/D13-1160.pdf', label='EMNLP 2013')),
 ('understanding the difficulty of training deep feedforward neural networks', dict(title='Understanding the Difficulty of Training Deep Feedforward Neural Networks',
   authors=['Xavier Glorot','Yoshua Bengio'], published='2010-03-01', abstract=None,
   pdf_url='https://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf', label='AISTATS 2010')),
 ('adaptive subgradient methods for online learning and stochastic optimization', dict(title='Adaptive Subgradient Methods for Online Learning and Stochastic Optimization',
   authors=['John Duchi','Elad Hazan','Yoram Singer'], published='2011-01-01', abstract=None,
   pdf_url='https://www.jmlr.org/papers/volume12/duchi11a/duchi11a.pdf', label='JMLR 2011')),
 ('findings of the 2014 workshop on statistical machine translation', dict(title='Findings of the 2014 Workshop on Statistical Machine Translation',
   authors=['Ondřej Bojar','Christian Buck','Christian Federmann','Barry Haddow','Philipp Koehn','Johannes Leveling','Christof Monz','Pavel Pecina','Matt Post','Hervé Saint-Amand','Radu Soricut','Lucia Specia','Aleš Tamchyna'], published='2014-06-01', abstract=None,
   pdf_url='https://aclanthology.org/W14-3302.pdf', label='ACL 2014')),
 ('policy gradient methods for reinforcement learning with function approximation', dict(title='Policy Gradient Methods for Reinforcement Learning with Function Approximation',
   authors=['Richard S. Sutton','David McAllester','Satinder Singh','Yishay Mansour'], published='1999-01-01', abstract=None,
   pdf_url='https://proceedings.neurips.cc/paper_files/paper/1999/file/464d828b85b0da0dc63ca37afefa4a29-Paper.pdf', label="NeurIPS 1999")),
 ('deep neural networks for acoustic modeling in speech recognition the shared views of four research groups', dict(title='Deep Neural Networks for Acoustic Modeling in Speech Recognition: The Shared Views of Four Research Groups',
   authors=['Geoffrey Hinton','Li Deng','Dong Yu','George E. Dahl','Abdel-rahman Mohamed','Navdeep Jaitly','Andrew Senior','Vincent Vanhoucke','Patrick Nguyen','Tara N. Sainath','Brian Kingsbury'], published='2012-11-01', abstract=None,
   pdf_url='https://www.cs.toronto.edu/~hinton/absps/DNN-2012.pdf', label='IEEE SPM 2012')),
 ('rectified linear units improve restricted boltzmann machines', dict(title='Rectified Linear Units Improve Restricted Boltzmann Machines',
   authors=['Vinod Nair','Geoffrey E. Hinton'], published='2010-06-01', abstract=None,
   pdf_url='https://www.cs.toronto.edu/~hinton/absps/reluICML.pdf', label='ICML 2010')),
 ('finding structure in time', dict(title='Finding Structure in Time', authors=['Jeffrey L. Elman'], published='1990-01-01', abstract=None,
   pdf_url='https://cseweb.ucsd.edu/~elman/Papers/fsit.pdf', label='Cognitive Science 1990')),
 ('deepspeed system optimizations enable training deep learning models with over 100 billion parameters', dict(title='DeepSpeed: System Optimizations Enable Training Deep Learning Models with over 100 Billion Parameters',
   authors=['Jeff Rasley','Samyam Rajbhandari','Olatunji Ruwase','Yuxiong He'], published='2020-08-01', abstract=None,
   pdf_url='https://www.microsoft.com/en-us/research/wp-content/uploads/2020/09/DeepSpeed_KDD2020.pdf', label='KDD 2020')),
 ('imagenet a large scale hierarchical image database', dict(title='ImageNet: A Large-Scale Hierarchical Image Database',
   authors=['Jia Deng','Wei Dong','Richard Socher','Li-Jia Li','Kai Li','Li Fei-Fei'], published='2009-06-01', abstract=None,
   pdf_url='https://image-net.org/static_files/papers/imagenet_cvpr09.pdf', label='CVPR 2009')),
 ('the winograd schema challenge', dict(title='The Winograd Schema Challenge', authors=['Hector J. Levesque','Ernest Davis','Leora Morgenstern'], published='2011-08-01', abstract=None,
   pdf_url='https://cdn.aaai.org/ocs/4492/4492-21852-1-PB.pdf', label='AAAI 2011')),
 ('the claude 3 model family opus sonnet haiku', dict(title='The Claude 3 Model Family: Opus, Sonnet, Haiku', authors=['Anthropic'], published='2024-03-04', abstract=None,
   pdf_url='https://assets.anthropic.com/m/61ae7ef2a8605a33/original/The-Cluade-3-Model-Family-Opus-Sonnet-Haiku.pdf', label='Anthropic 2024')),
]
for nk,d in CLASSICS:
    d=dict(d); d['arxiv']=None; d['link']=f"[{d.pop('label')}]({d['pdf_url']})"; d['key']=('t',nk)
    items.append(d)
for it in items:
    c=None
    if it.get('arxiv') and it['arxiv'] in tgt_ax: c=tgt_ax[it['arxiv']]
    if c is None: c=citers.get(norm(it['title']))
    if c is None and it['key'][0]=='t': c=citers.get(it['key'][1])
    it['citers']=c or 0
items.sort(key=lambda x:-x['citers'])
json.dump(items, open(W+'/items_wave1.json','w'), indent=1)
print("items:", len(items), "| >=9 citers:", sum(1 for i in items if i['citers']>=9))
