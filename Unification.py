from nltk.grammar import FeatureGrammar
from nltk import FeatureChartParser

ugrammar = FeatureGrammar.fromstring("""
S -> NP[NUM=?n] VP[NUM=?n, SUBCAT=nil] | PP NP[NUM=?n] VP[NUM=?n, SUBCAT=nil]
NP[NUM=?n] -> ProperNoun[NUM=sing] | NP CONJ NP | NOUN | ADJ Nominal | DET Nominal | NP VP | Nominal PP | WH | NP Nominal
VP[NUM=?n] -> V[FORM=?f, NUM=?n, SUBCAT=nil] | V[FORM=?f, NUM=?n] NP[NUM=?n] | ADV VP[NUM=?n]
Nominal -> NOUN | Nominal PP | ADJ Nominal | DET Nominal | Nominal NOUN
PP -> Prep NP | CONJ NP
ProperNoun[NUM=sing] -> 'Bart' | 'Homer' | 'Lisa'
CONJ -> 'and' | 'when'
ADV -> 'always' | 'never'
V[FORM=base, NUM=plur] -> 'drink' | 'do' | 'wear'
V[FORM=vbz, NUM=sing] -> 'wears' | 'serves' | 'drinks' | 'thinks' | 'does'
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
Lisa drinks milk
Bart laughs
Homer laughed
"""
# Bart and Lisa drink milk
# Bart wears blue shoes
# Lisa serves Bart a healthy green salad
# Homer serves Lisa
# Bart always drinks milk
# Lisa thinks Homer thinks Bart drinks milk
# Homer never drinks milk in the kitchen before midnight
# when Homer drinks milk Bart laughs
# when does Lisa drinks the milk on the table
# when do Lisa and Bart wear shoes
# """

sents = text.splitlines()
for sent in sents:
    parses = uparser.parse(sent.split())
    print(sent)
    for tree in parses:
        print(tree)
