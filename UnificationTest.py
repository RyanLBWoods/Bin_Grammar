from nltk.grammar import FeatureGrammar
from nltk import FeatureChartParser

ugrammar = FeatureGrammar.fromstring("""
S -> NP[NUM=?n] VP[FORM=?f, NUM=?n, SUBCAT=nil] | PP S | WH Aux NP[NUM=?n] VP[FORM=?f, NUM=?n, SUBCAT=nil]
NP[NUM=?n] -> ProperNoun[NUM=sing] | NOUN[NUM=?n] | NP[NUM=?n] CONJ NP[NUM=?n] | DET[NUM=?n] Nominal
VP[FORM=?f, NUM=?n, SUBCAT=?rest] -> VP[FORM=?f, NUM=?n, SUBCAT=[HEAD=?arg, TAIL=?rest]] ARG[CAT=?arg]
VP[FORM=?f, NUM=?n, SUBCAT=?rest] -> VP[FORM=?f, NUM=?n, SUBCAT=[HEAD=?arg, TAIL=?rest]] S
VP[FORM=?f, NUM=?n, SUBCAT=?args] -> V[FORM=?f, NUM=?n, SUBCAT=?args] | ADV V[FORM=?f, NUM=?n, SUBCAT=?args]
ARG[CAT=np] -> NP[NUM=?n]
ARG[CAT=pp] -> PP
ARG[CAT=nominal] -> Nominal
PP -> Prep NP[NUM=?n] | CONJ S
Nominal -> NOUN[NUM=?n] | Nominal PP | ADJ Nominal | DET[NUM=?n] Nominal | Nominal NOUN[NUM=?n]
ProperNoun[NUM=sing] -> 'Bart' | 'Homer' | 'Lisa'
CONJ -> 'and' | 'when'
ADV -> 'always' | 'never'
Aux -> 'do' | 'does'
V[FORM=base, NUM=plur, SUBCAT=nil] -> 'laugh'
V[FORM=base, NUM=plur, SUBCAT=[HEAD=np, TAIL=nil]] -> 'drink' | 'wear' | 'laugh'
V[FORM=vbz, NUM=sing, SUBCAT=[HEAD=?arg, TAIL=?rest]] -> 'wears' | 'serves' | 'drinks' | 'thinks' | 'laughs'
V[FORM=vbz, NUM=sing, SUBCAT=nil] -> 'laughs'
V[FORM=pret, NUM=?n, SUBCAT=nil] -> 'laughed'
DET[NUM=sing] -> 'a'
DET[NUM=?n] -> 'the'
NOUN[NUM=sing] -> 'milk' | 'salad' | 'kitchen' | 'midnight' | 'table'
NOUN[NUM=plur] -> 'shoes'
ADJ -> 'blue' | 'healthy' | 'green'
Prep -> 'in' | 'before' | 'on'
WH -> 'when'
""")

uparser = FeatureChartParser(ugrammar)
text = """
Lisa drinks milk in the kitchen
Lisa drinks milk
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
"""

sents = text.splitlines()
for sent in sents:
    parses = uparser.parse(sent.split())
    print(sent)
    for tree in parses:
        print(tree)
