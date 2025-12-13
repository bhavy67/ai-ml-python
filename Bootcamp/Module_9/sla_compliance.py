# Libraries (do not edit)
from ast import literal_eval

def failing_regions(wait_data, sla):
    failing = []

    for region, waits in wait_data.items():
        waits_sorted = sorted(waits)
        n = len(waits_sorted)

        if n % 2 == 1:
            median = waits_sorted[n // 2]
        else:
            median = (waits_sorted[n // 2 - 1] + waits_sorted[n // 2]) / 2

        median = round(median, 2)

        if median > sla:
            failing.append(region)

    return sorted(failing) if failing else 'All regions meet SLA'


# Input and output processing (do not edit)
print(failing_regions(*literal_eval(input())))