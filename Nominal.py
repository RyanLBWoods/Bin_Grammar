from nltk import CFG, ChartParser

cfg = CFG.fromstring("""
S -> NP VP | PP NP VP
NP -> ProperNoun | NP CONJ NP | NOUN | ADJ Nominal | DET Nominal | NP VP | Nominal PP | WH | NP Nominal
VP -> V | V NP | ADV VP
Nominal -> NOUN | Nominal PP | ADJ Nominal | DET Nominal | Nominal NOUN
PP -> Prep NP | CONJ NP
ProperNoun -> 'Bart' | 'Homer' | 'Lisa'
CONJ -> 'and' | 'when'
ADV -> 'always' | 'never'
V -> 'laughs' | 'laughed' | 'drink' | 'wears' | 'serves' | 'drinks' | 'thinks' | 'does' | 'do' | 'wear'
DET -> 'a' | 'the'
NOUN -> 'milk' | 'shoes' | 'salad' | 'kitchen' | 'midnight' | 'table'
ADJ -> 'blue' | 'healthy' | 'green'
Prep -> 'in' | 'before' | 'on'
WH -> 'when'
""")

cfparser = ChartParser(cfg)
text = """
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
"""

sents = text.splitlines()
for sent in sents:
    parses = cfparser.parse(sent.split())
    print sent
    for tree in parses:
        print(tree)
