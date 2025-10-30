# Taking input
total_amount = float(input())
people_count = int(input())
service_charge_percent = int(input())

def calculate_individual_share(total_amount, people_count, service_charge_percent):
    total_with_service = total_amount + (total_amount * service_charge_percent / 100)
    
    # 5% for sc > 10%
    if service_charge_percent > 10:
        total_with_service -= total_with_service * 0.05

    share = 0
    for _ in range(1):
        share = total_with_service / people_count

    return round(share, 2)

# Print the output
print(calculate_individual_share(total_amount, people_count, service_charge_percent))