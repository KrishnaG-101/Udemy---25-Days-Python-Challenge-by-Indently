# Convert temprature from Celcius to Fahrenheit or Fahrenheit to Celcius

# Constants
FAHRENHEIT_TO_CELCIUS : float = 5 / 9
CELCIUS_TO_FAHRENHEIT : float = 9 / 5
OFFSET : int = 32

# User Inputs
conversion_type : int = int(input("Enter 1 to convert from Celcius to Fahrenheit or enter 2 to convert Fahrenheit to Celcius: "))
temprature_input : int = int(input("Enter the temprature value: "))

# Conversion and Output
if conversion_type == 1:
    temprature_output = (temprature_input * CELCIUS_TO_FAHRENHEIT) + OFFSET
    print(f"\n{temprature_input} degrees Celcius -> {temprature_output:.1f} degrees Fahrenheit")
else:
    temprature_output = (temprature_input - OFFSET) * FAHRENHEIT_TO_CELCIUS
    print(f"\n{temprature_input} degrees Fahrenheit -> {temprature_output:.1f} degrees Celcius")
# ----END----