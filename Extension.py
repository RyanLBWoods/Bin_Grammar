from nltk.grammar import FeatureGrammar
from nltk import FeatureChartParser

ugrammar = FeatureGrammar.fromstring("""\
# ###################
# Grammar Productions
# ###################
# Sentence
S   ->    NP[NUM=?n] VP[FORM=?f, NUM=?n, SUBCAT=nil] | AdvC S
S   ->    NP[NUM=?n] MVP[FORM=?f, NUM=?n, SUBCAT=nil]
S   ->    WhNP InvS
S   ->    WH InvS
# Inversed Sentence
InvS         ->   Aux[NUM=?n] IS[NUM=pl]
IS[NUM=pl]   ->   NP[NUM=?n] VP[FORM=?f, NUM=pl, SUBCAT=nil]
# Noun Phrase
NP[NUM=?n]   ->    ProperNoun[NUM=?n] | ProNoun[NUM=?n] | Nominal | DET[NUM=?n] Nominal | NP[NUM=?n] GerundNP
NP[NUM=pl]   ->    NP[NUM=?n] CP
# WH
WhNP    ->    WH NP[NUM=?n]
# Verb Phrase
VP[FORM=?f, NUM=?n, SUBCAT=?rest]   ->    VP[FORM=?f, NUM=?n, SUBCAT=[HEAD=?arg, TAIL=?rest]] ARG[CAT=?arg]
VP[FORM=?f, NUM=?n, SUBCAT=?args]   ->    V[FORM=?f, NUM=?n, SUBCAT=?args] | ADV V[FORM=?f, NUM=?n, SUBCAT=?args]
VP[FORM=?f, NUM=?n, SUBCAT=?args]   ->    Aux V[FORM=?f, NUM=?n, SUBCAT=?args]
# Modal Phrase
MVP[FORM=?f, NUM=?n, SUBCAT=nil]    ->    MP VP[FORM=?f, NUM=?n, SUBCAT=nil]
# Modal Verb
MP    ->    MV | MV ADV
# Arguments
ARG[CAT=np]   ->    NP[NUM=?n]
ARG[CAT=pp]   ->    PP
ARG[CAT=subc] ->    S
# Conjunction Phrase
CP      ->    CONJ NP[NUM=?n]
# Prepositional Phrase
PP      ->    Prep NP[NUM=?n]
# Adverbial Clause
AdvC    ->    CONJ S
# Nominal
Nominal     ->    NOUN[NUM=?n] | Nominal PP | ADJ Nominal | Nominal NOUN[NUM=?n] | GerundNP
# Gerund expansion productions
GerundNP    ->    GerundV NP
GerundV     ->    V[FORM=presP]
# ###################
# Lexical Productions
# ###################
# Determiners and Nouns
DET[NUM=sg]          ->    'a'
DET[NUM=?n]          ->    'the'
ProperNoun[NUM=sg]   ->    'Bart' | 'Homer' | 'Lisa'
ProNoun[NUM=sg]      ->    'he'
NOUN[NUM=sg]         ->    'milk' | 'salad' | 'kitchen' | 'midnight' | 'table' | 'bread'
NOUN[NUM=pl]         ->    'shoes'
# Conjunctions and Adverbs
CONJ    ->    'and' | 'when'
ADV     ->    'always' | 'never' | 'not'
# Auxiliaries
Aux[NUM=pl]    ->    'do' | 'have'
Aux[NUM=sg]    ->    'does'
# ###################
# Verbs
# VI
V[FORM=base, NUM=pl, SUBCAT=nil]    ->     'laugh' | 'think' | 'drink' | 'serve'
V[FORM=vbz, NUM=sg, SUBCAT=nil]     ->     'laughs'
V[FORM=pret, NUM=?n, SUBCAT=nil]    ->     'laughed'
# VT + NP
V[FORM=base, NUM=pl, SUBCAT=[HEAD=np, TAIL=nil]]    ->    'drink' | 'wear' | 'serve'
V[FORM=vbz, NUM=sg, SUBCAT=[HEAD=np, TAIL=nil]]     ->    'wears' | 'serves' | 'drinks' | 'thinks' | 'likes'
V[FORM=vbz, NUM=sg, SUBCAT=[HEAD=subc, TAIL=nil]]   ->    'thinks'
V[FORM=vbz, NUM=pl, SUBCAT=[HEAD=subc, TAIL=nil]]   ->    'think'
V[FORM=past, NUM=?n, SUBCAT=[HEAD=np, TAIL=nil]]    ->    'drunk' | 'seen'
V[FORM=presP, NUM=?n, SUBCAT=[HEAD=np, TAIL=nil]]   ->    'drinking'
# VT + NP + PP
V[FORM=vbz, NUM=sg, SUBCAT=[HEAD=np, TAIL=[HEAD=pp, TAIL=nil]]] -> 'serves' | 'drinks' | 'puts'
# VT + NP + NP
V[FORM=vbz, NUM=sg, SUBCAT=[HEAD=np, TAIL=[HEAD=np, TAIL=nil]]] -> 'serves'
# Adjectives, Prepositions and WHs
ADJ    ->    'blue' | 'healthy' | 'green'
Prep   ->    'in' | 'before' | 'on'
WH     ->    'when' | 'what' | 'whom'
MV     ->    'may'
""")

uparser = FeatureChartParser(ugrammar)
text = """\
Bart likes drinking milk
Lisa may have seen Bart
Lisa may have seen Bart drinking milk
Lisa may not have seen Bart drinking milk
what does Homer drink
what salad does Bart serve
whom does Homer serve salad
whom do Homer and Lisa serve
what salad does Bart think Homer serves Lisa
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
