# Taking input
n = int(input())
lst = eval(input())
target = int(input())

def find_indices(lst, target):
    result = []
    for i in range(len(lst)):
        if lst[i] == target:
            result.append(i)
    return result

# Print result
print(find_indices(lst, target))