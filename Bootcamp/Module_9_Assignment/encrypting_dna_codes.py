def encrypt_bases(input_bases):
    standard = ['A', 'C', 'G', 'T']
    non_standard = ['H', 'I', 'M', 'O', 'P', 'Q']

    # Build pair mapping (a–p)
    pair_map = {}
    letter = ord('a')
    for b1 in standard:
        for b2 in standard:
            pair_map[b1 + b2] = chr(letter)
            letter += 1

    # Single standard base mapping (q–t)
    single_map = {'A': 'q', 'C': 'r', 'G': 's', 'T': 't'}

    # Non-standard mapping (u–z)
    non_standard_map = {
        base: chr(ord('u') + i)
        for i, base in enumerate(non_standard)
    }

    result = []
    i = 0
    n = len(input_bases)

    while i < n:
        if (
            i + 1 < n and
            input_bases[i] in standard and
            input_bases[i + 1] in standard
        ):
            result.append(pair_map[input_bases[i:i+2]])
            i += 2
        else:
            base = input_bases[i]
            if base in single_map:
                result.append(single_map[base])
            else:
                result.append(non_standard_map[base])
            i += 1

    return ''.join(result)


# Input and output processing (do not edit)
print(encrypt_bases(input()))