# Convert distance from Miles to Kilometers or Kilometers to Miles

# Constants
CONVERSION_RATE : float = 1.609

# User Inputs
conversion_type : int = int(input("Enter 1 to convert miles to kilometers or enter 2 to convert kilometers to miles: "))
distance_input : float = float(input("Enter to distance value: "))

# Calculation and Output
if conversion_type == 1:
    distance_output : float = distance_input * CONVERSION_RATE
    print(f"\nConversion: {distance_input} Miles -> {distance_output:.2f} Kilometers")
else:
    distance_output : float = distance_input / CONVERSION_RATE
    print(f"\nConversion: {distance_input} Kilometers -> {distance_output:.2f} Miles")