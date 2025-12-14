# Libraries (do not edit)
from ast import literal_eval

def count_mutation_risk_groups(scores, label):
    scores_sorted = sorted(scores)
    n = len(scores_sorted)

    def percentile(p):
        pos = p * (n - 1)
        lower = int(pos)
        upper = lower + 1

        if upper < n:
            return scores_sorted[lower] + (pos - lower) * (scores_sorted[upper] - scores_sorted[lower])
        else:
            return scores_sorted[lower]

    Q1 = percentile(0.25)
    Q3 = percentile(0.75)

    count = 0
    for score in scores:
        if label == 'Low Risk' and score <= Q1:
            count += 1
        elif label == 'Moderate Risk' and Q1 < score < Q3:
            count += 1
        elif label == 'High Risk' and score >= Q3:
            count += 1

    return count


# Input and output handling (do not edit)
print(count_mutation_risk_groups(*literal_eval(input())))