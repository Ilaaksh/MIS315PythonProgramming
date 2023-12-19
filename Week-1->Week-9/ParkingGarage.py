########################################################
#
# Initial Program
#
########################################################
def calculate_parking_fee(hours_parked):
    base_fee = 5.0
    hourly_rate = 2.5
    max_hours = 24

    if hours_parked <= 0:
        return "Invalid input. Hours parked must be greater than zero."
    elif hours_parked > max_hours:
        return "Invalid input. Hours parked cannot exceed 24 hours."
    elif hours_parked <= 3:
        return base_fee
    else:
        additional_hours = hours_parked - 3
        extra_fee = additional_hours * hourly_rate
        return base_fee + extra_fee

try:
    hours_parked = float(input("Enter the number of hours parked: "))
    parking_fee = calculate_parking_fee(hours_parked)
    print(f"The parking fee is: ${parking_fee:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid number of hours.")

########################################################
#
# Enhanced Program
#
########################################################

print("\n Enhanced Program\n")

try:
    hours_parked = float(input("Enter hours parked: "))

    if hours_parked < 0:
        print("Invalid entry. Please enter a non-negative number of hours.")
    else:
        max_fee = 20.00
        fee_per_hour = 2.50
        base_fee = 5.00

        parking_fee = min(base_fee + hours_parked * fee_per_hour, max_fee)

        formatted_fee = round(parking_fee, 2)
        print(f"Parking fee: $ {formatted_fee:.2f}")

except ValueError:
    print("Invalid entry. Please enter a valid number of hours.")