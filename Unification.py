from nltk.grammar import FeatureGrammar
from nltk import FeatureChartParser

ugrammar = FeatureGrammar.fromstring("""\
S -> NP[NUM=?n] VP[FORM=?f, NUM=?n, SUBCAT=nil] | PP S | WH Aux[NUM=?n] NP[NUM=?n] VP[FORM=?f, NUM=?n, SUBCAT=nil]
NP[NUM=?n] -> ProperNoun[NUM=?n] | ProNoun[NUM=?n] | Nominal | DET[NUM=?n] Nominal
NP[NUM=pl] -> NP[NUM=?n] CP
VP[FORM=?f, NUM=?n, SUBCAT=?rest] -> VP[FORM=?f, NUM=?n, SUBCAT=[HEAD=?arg, TAIL=?rest]] ARG[CAT=?arg]
VP[FORM=?f, NUM=?n, SUBCAT=?rest] -> VP[FORM=?f, NUM=?n, SUBCAT=[HEAD=?arg, TAIL=?rest]] S
VP[FORM=?f, NUM=?n, SUBCAT=?args] -> V[FORM=?f, NUM=?n, SUBCAT=?args] | ADV V[FORM=?f, NUM=?n, SUBCAT=?args]
ARG[CAT=np] -> NP[NUM=?n]
ARG[CAT=pp] -> PP
CP -> CONJ NP[NUM=?n]
PP -> Prep NP[NUM=?n] | CONJ S
Nominal -> NOUN[NUM=?n] | Nominal PP | ADJ Nominal | Nominal NOUN[NUM=?n]
ProperNoun[NUM=sg] -> 'Bart' | 'Homer' | 'Lisa'
ProNoun[NUM=sg] -> 'he'
CONJ -> 'and' | 'when'
ADV -> 'always' | 'never'
Aux[NUM=pl] -> 'do'
Aux[NUM=sg] -> 'does'
V[FORM=base, NUM=pl, SUBCAT=nil] -> 'laugh'
V[FORM=base, NUM=pl, SUBCAT=[HEAD=np, TAIL=nil]] -> 'drink' | 'wear'
V[FORM=vbz, NUM=sg, SUBCAT=[HEAD=np, TAIL=nil]] -> 'wears' | 'serves' | 'drinks' | 'thinks'
V[FORM=vbz, NUM=sg, SUBCAT=[HEAD=np, TAIL=[HEAD=pp, TAIL=nil]]] -> 'wears' | 'serves' | 'drinks' | 'thinks' | 'puts'
V[FORM=vbz, NUM=sg, SUBCAT=[HEAD=np, TAIL=[HEAD=np, TAIL=nil]]] -> 'serves'
V[FORM=vbz, NUM=sg, SUBCAT=nil] -> 'laughs'
V[FORM=pret, NUM=?n, SUBCAT=nil] -> 'laughed'
DET[NUM=sg] -> 'a'
DET[NUM=?n] -> 'the'
NOUN[NUM=sg] -> 'milk' | 'salad' | 'kitchen' | 'midnight' | 'table' | 'bread'
NOUN[NUM=pl] -> 'shoes'
ADJ -> 'blue' | 'healthy' | 'green'
Prep -> 'in' | 'before' | 'on'
WH -> 'when'
""")

uparser = FeatureChartParser(ugrammar)
text = """\
Bart laughs
Homer laughed
Bart and Lisa drink milk
Bart wears blue shoes
Lisa serves Bart a healthy green salad
Homer serves Lisa
Bart always drinks milk
Lisa thinks Homer thinks Bart drinks milk
Homer never drinks milk in the kitchen before midnight
when Homer drinks milk Bart laughs
when does Lisa drinks the milk on the table
when do Lisa and Bart wear shoes
Bart laugh
when do Homer drinks milk
Bart laughs the kitchen
he puts bread on the table
"""

sents = text.splitlines()
for sent in sents:
    parses = uparser.parse(sent.split())
    print(sent)
    for tree in parses:
        print(tree)
