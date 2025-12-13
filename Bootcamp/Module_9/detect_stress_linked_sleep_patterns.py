# Libraries (do not edit)
from ast import literal_eval
import math

def find_stress_linked_users(user_data):
    stress_users = []

    for user_id, records in user_data:
        heart_rates = [r[0] for r in records]
        sleep_durations = [r[1] for r in records]
        n = len(records)

        mean_hr = sum(heart_rates) / n
        mean_sleep = sum(sleep_durations) / n

        numerator = sum(
            (heart_rates[i] - mean_hr) * (sleep_durations[i] - mean_sleep)
            for i in range(n)
        )

        denom_hr = math.sqrt(sum((hr - mean_hr) ** 2 for hr in heart_rates))
        denom_sleep = math.sqrt(sum((sd - mean_sleep) ** 2 for sd in sleep_durations))

        if denom_hr == 0 or denom_sleep == 0:
            corr = 0
        else:
            corr = numerator / (denom_hr * denom_sleep)

        corr = round(corr, 2)

        if corr <= -0.70:
            stress_users.append(user_id)

    return sorted(stress_users) if stress_users else 'No stress-linked patterns detected'


# Input and output processing (do not edit)
print(find_stress_linked_users(literal_eval(input())))