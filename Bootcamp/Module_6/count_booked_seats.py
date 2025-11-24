from ast import literal_eval

# Taking the input
seating_chart = literal_eval(input())

def count_booked_seats(seating_chart):
    if not isinstance(seating_chart, list) or len(seating_chart) == 0:
        return "Invalid seating chart"
    
    row_length = len(seating_chart[0])
    
    total_booked = 0
    
    for row in seating_chart:
        if not isinstance(row, list) or len(row) != row_length:
            return "Invalid seating chart"
        
        for seat in row:
            if seat not in (0, 1):
                return "Invalid seating chart"
            
            if seat == 1:
                total_booked += 1
    
    return total_booked

# Print the output
print(count_booked_seats(seating_chart))