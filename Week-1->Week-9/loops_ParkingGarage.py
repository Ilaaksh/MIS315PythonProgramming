def calculate_parking_fee(hours_parked):
    base_fee = 5
    hourly_rate = 2.5
    minimum_fee = 10
    maximum_fee = 20
    fee = base_fee + (hours_parked * hourly_rate)

    if fee < minimum_fee:
        return minimum_fee
    elif fee > maximum_fee:
        return maximum_fee
    else:
        return fee

print("Hours Parked  Fee")
for hours in range(1, 9):
    fee = calculate_parking_fee(hours)
    print(f"{hours}            {fee:.1f}")

#Enhancement
def calculate_parking_fee1(hours_parked):
    base_fee = 5
    hourly_rate = 2.5
    minimum_fee = 10
    maximum_fee = 20
    
    fee = base_fee + (hours_parked * hourly_rate)
    
    if fee < minimum_fee:
        return minimum_fee
    elif fee > maximum_fee:
        return maximum_fee
    else:
        return fee

print("Hrs Fee")
for hours in range(1, 9):
    fee = calculate_parking_fee1(hours)
    print(f"{hours} {fee:.2f}")
