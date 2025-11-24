# Import literal_eval to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
patient_data = literal_eval(input())
changes = literal_eval(input())

def modify_patient_record(patient_data, changes):
    record_list = list(patient_data)
    
    field_index = {
        'name': 0,
        'diagnosis': 1,
        'treatment': 2
    }
    
    for key, new_value in changes.items():
        if key in field_index:
            record_list[field_index[key]] = new_value

    return tuple(record_list)

# Print the output
print(modify_patient_record(patient_data, changes))