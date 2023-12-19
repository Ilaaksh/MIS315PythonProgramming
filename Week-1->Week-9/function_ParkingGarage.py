# Define a function to calculate the parking fee
def calcFee(hours):
    base_fee = 5
    hourly_rate = 2.50
    total_fee = base_fee + (hours * hourly_rate)
    return total_fee

# Prompt the user for the number of hours parked
try:
    hours_parked = float(input("Enter hours parked: "))
    if hours_parked < 0:
        print("Please enter a valid number of hours (non-negative).")
    else:
        # Calculate the parking fee
        parking_fee = calcFee(hours_parked)
        print("Parking fee: $", format(parking_fee, ".2f"))
except ValueError:
    print("Invalid input. Please enter a valid number of hours.")

def calcFee1(hours, rate=3.75, decimals=2):
    fee = hours * rate
    return round(fee, decimals)

def displayFee(fee):
    print(f"Parking fee: $ {fee}")

try:
    hours_parked = float(input("Enter hours parked: "))
    fee = calcFee1(hours_parked, decimals=2)
    displayFee(fee)
except ValueError:
    print("Invalid input. Please enter a valid number of hours.")

