from nltk.grammar import FeatureGrammar
from nltk import FeatureChartParser

ugrammar = FeatureGrammar.fromstring("""\
# ###################
# Grammar Productions
# ###################
# Sentence
S    ->    NP[NUM=?n] VP[FORM=?f, NUM=?n, SUBCAT=nil] | AdvC S
S    ->    WH Aux[NUM=?n] NP[NUM=?n] VP[FORM=?f, NUM=pl, SUBCAT=nil]
# Noun Phrase
NP[NUM=?n]    ->    ProperNoun[NUM=?n] | ProNoun[NUM=?n] | Nominal | DET[NUM=?n] Nominal
NP[NUM=pl]    ->    NP[NUM=?n] CP
# Verb Phrase
VP[FORM=?f, NUM=?n, SUBCAT=?rest] -> VP[FORM=?f, NUM=?n, SUBCAT=[HEAD=?arg, TAIL=?rest]] ARG[CAT=?arg]
VP[FORM=?f, NUM=?n, SUBCAT=?args] -> V[FORM=?f, NUM=?n, SUBCAT=?args] | ADV V[FORM=?f, NUM=?n, SUBCAT=?args]
# Argument expansion productions
ARG[CAT=np]    ->    NP[NUM=?n]
ARG[CAT=pp]    ->    PP
ARG[CAT=subc]  ->    S
# Conjunction Phrase expansion productions
CP    ->    CONJ NP[NUM=?n]
# Prepositional Phrase expansion productions
PP    ->    Prep NP[NUM=?n]
AdvC  ->    CONJ S
# Nominal expansion productions
Nominal    ->    NOUN[NUM=?n] | Nominal PP | ADJ Nominal | Nominal NOUN[NUM=?n]
# ###################
# Lexical Productions
# ###################
# Determiners and Nouns
DET[NUM=sg]           ->    'a'
DET[NUM=?n]           ->    'the'
ProperNoun[NUM=sg]    ->    'Bart' | 'Homer' | 'Lisa'
ProNoun[NUM=sg]       ->    'he'
NOUN[NUM=sg]          ->    'milk' | 'salad' | 'kitchen' | 'midnight' | 'table' | 'bread'
NOUN[NUM=pl]          ->    'shoes'
# Conjunctions and Adverbs
CONJ   ->    'and' | 'when'
ADV    ->    'always' | 'never'
# Auxiliaries
Aux[NUM=pl]    ->    'do'
Aux[NUM=sg]    ->    'does'
# ###################
# Verbs
# VI
V[FORM=base, NUM=pl, SUBCAT=nil]    ->    'laugh'
V[FORM=vbz, NUM=sg, SUBCAT=nil]     ->    'laughs'
V[FORM=pret, NUM=?n, SUBCAT=nil]    ->    'laughed'
# VT + NP
V[FORM=base, NUM=pl, SUBCAT=[HEAD=np, TAIL=nil]]    ->    'drink' | 'wear'
V[FORM=vbz, NUM=sg, SUBCAT=[HEAD=np, TAIL=nil]]     ->    'wears' | 'serves' | 'drinks'
V[FORM=vbz, NUM=sg, SUBCAT=[HEAD=subc, TAIL=nil]]   ->    'thinks'
# VT + NP + PP
V[FORM=vbz, NUM=sg, SUBCAT=[HEAD=np, TAIL=[HEAD=pp, TAIL=nil]]] -> 'serves' | 'drinks' | 'puts'
# VT + NP + NP
V[FORM=vbz, NUM=sg, SUBCAT=[HEAD=np, TAIL=[HEAD=np, TAIL=nil]]] -> 'serves'
# Adjectives, Prepositions and WHs
ADJ    ->    'blue' | 'healthy' | 'green'
Prep   ->    'in' | 'before' | 'on'
WH     ->    'when'
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
when does Lisa drink the milk on the table
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
