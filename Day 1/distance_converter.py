# Convert distance from Miles to Kilometers or Kilometers to Miles

# Constants
CONVERSION_RATE = 1.609

# User Inputs
conversion_type = int(input("Enter 1 to convert miles to kilometers or enter 2 to convert kilometers to miles: "))
distance_input = int(input("Enter to distance value: "))

# Calculation and Output
match conversion_type:
    case 1:
        distance_output = distance_input * CONVERSION_RATE
        print(f"\nConversion: {distance_input} Miles -> {distance_output:.2f} Kilometers")
    case 2:
        distance_output = distance_input / CONVERSION_RATE
        print(f"\nConversion: {distance_input} Kilometers -> {distance_output:.2f} Miles")