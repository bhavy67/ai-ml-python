def compute_covariance(data):
    time_spent, questions_attempted = data
    n = len(time_spent)

    mean_time = sum(time_spent) / n
    mean_questions = sum(questions_attempted) / n

    covariance = sum(
        (time_spent[i] - mean_time) * (questions_attempted[i] - mean_questions)
        for i in range(n)
    ) / n

    return covariance


# Input and output processing (do not edit)
from ast import literal_eval
print(round(compute_covariance(literal_eval(input())), 2))