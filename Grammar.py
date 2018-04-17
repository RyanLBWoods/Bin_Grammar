from nltk import CFG, ChartParser

cfg = CFG.fromstring("""
S -> NP VP | WH Aux NP VP | AdvC S
NP -> ProperNoun | NP CONJ NP | NOUN | ADJ NP | DET NP | NOUN PP
VP -> V | V NP | ADV VP | V NP NP | VP S
PP -> Prep NP
AdvC -> CONJ S
ProperNoun -> 'Bart' | 'Homer' | 'Lisa'
CONJ -> 'and' | 'when'
ADV -> 'always' | 'never'
V -> 'laughs' | 'laughed' | 'drink' | 'wears' | 'serves' | 'drinks' | 'thinks' | 'wear'
DET -> 'a' | 'the'
NOUN -> 'milk' | 'shoes' | 'salad' | 'kitchen' | 'midnight' | 'table'
ADJ -> 'blue' | 'healthy' | 'green'
Prep -> 'in' | 'before' | 'on'
WH -> 'when'
Aux -> 'does' | 'do'
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
