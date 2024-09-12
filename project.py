# Python Weight Converter

weight = float(input("Enter your weight"))
unit = input("Kilograms or Pounds? (k or L): ")

if unit == "K":
    weight = weight * 2.205
elif unit == "L":
    weight = weight /2.205
else:
    print("f{unit} was not valid")

