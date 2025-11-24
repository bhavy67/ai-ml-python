from ast import literal_eval

# Taking the input 
sensors_data = literal_eval(input())

def combine_sensor_data(sensors_data):
    readings = {
        'light intensity': [],
        'temperature': [],
        'humidity': []
    }
    
    for sensor in sensors_data:
        for key in readings:
            if key in sensor:
                readings[key].append(sensor[key])
    
    final_values = []
    
    for key in readings:
        if readings[key]:
            avg = sum(readings[key]) / len(readings[key])
        else:
            avg = 0
        
        avg = float(round(avg, 2))
        final_values.append(avg)
    
    return tuple(final_values)

# Print the output 
print(combine_sensor_data(sensors_data))