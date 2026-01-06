from ast import literal_eval

def marginal_revenue(data):
    coeffs, day = data

    n = len(coeffs) - 1  # highest power
    result = 0

    for c in coeffs[:-1]:  # constant term disappears after differentiation
        result += c * n * (day ** (n - 1))
        n -= 1

    return result


# (do not edit)
print(marginal_revenue(literal_eval(input())))