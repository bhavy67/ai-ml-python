from ast import literal_eval
import math

def analyze_price_time_relation(data):
    prices, times = data
    n = len(prices)

    mean_price = sum(prices) / n
    mean_time = sum(times) / n

    numerator = sum(
        (prices[i] - mean_price) * (times[i] - mean_time)
        for i in range(n)
    )

    denom_price = math.sqrt(sum((p - mean_price) ** 2 for p in prices))
    denom_time = math.sqrt(sum((t - mean_time) ** 2 for t in times))

    if denom_price == 0 or denom_time == 0:
        corr = 0
    else:
        corr = numerator / (denom_price * denom_time)

    corr = abs(corr)

    if corr >= 0.7:
        return 'Strong'
    elif corr >= 0.3:
        return 'Weak'
    else:
        return 'Neutral'


# (do not edit)
print(analyze_price_time_relation(literal_eval(input())))