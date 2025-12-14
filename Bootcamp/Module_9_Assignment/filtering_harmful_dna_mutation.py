# Libraries (do not edit)
from ast import literal_eval
from itertools import product

def filter_dna_mutations(bases, length, harmful_patterns):
    harmful_set = set(harmful_patterns)

    all_sequences = [
        ''.join(p)
        for p in product(bases, repeat=length)
        if ''.join(p) not in harmful_set
    ]

    return sorted(all_sequences)


# Input and output processing (do not edit)
print(filter_dna_mutations(*literal_eval(input())))