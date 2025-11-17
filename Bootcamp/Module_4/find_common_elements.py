# Import the literal_eval library to evaluate string input as a Python safely 
from ast import literal_eval

# Taking input
list1 = literal_eval(input())  
list2 = literal_eval(input())  
list3 = literal_eval(input())  

# Efficient linear traversal using three pointers
def find_common_elements(l1, l2, l3):
    i = j = k = 0
    result = []
    prev = None  # to avoid adding duplicates to result
    
    while i < len(l1) and j < len(l2) and k < len(l3):
        if l1[i] == l2[j] == l3[k]:
            if l1[i] != prev:          # ensure uniqueness in output
                result.append(l1[i])
                prev = l1[i]
            i += 1
            j += 1
            k += 1
        elif l1[i] < l2[j]:
            i += 1
        elif l2[j] < l3[k]:
            j += 1
        else:
            k += 1

    return result

common_elements = find_common_elements(list1, list2, list3)

# Print the output
print(" ".join(map(str, common_elements)) if common_elements else "None")