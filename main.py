import math

weight = 1
height = 1
def inpvalues():
    global weight, height
    while True:
        try:
            weight = (float(input("Enter your weight (kgs): ")))
            height = (float(input("Enter your height (m): ")))
            break
        except ValueError:
            print("Please enter numbers.")
    return weight, height

pounds = 1
def pound():
    global pounds
    while True:
        try:
            pounds = (float(input("Pounds : ")))
            break
        except ValueError:
            print("Please enter numbers.")
    return pounds

centimeters = 1
def centimeter():
    global centimeters
    while True:
        try:
            centimeters = (float(input("Centimeters: ")))
            break
        except ValueError:
            print("Please enter numbers.")
    return centimeters

foot = 1
def foots():
    global foot
    while True:
        try:
            foot = (float(input("Foot: ")))
            break
        except ValueError:
            print("Please enter numbers.")
    return foot

inpvalues()
h = height * height
bmi = float(weight / h)
cm_m = centimeters/100
foot_m = foot * 0.3048
converted_weight = pounds * 0.45359237

if bmi < 18.5:
    text = "You're Underweight."
elif bmi > 35:
    text = "You're extremely obese."
elif bmi >= 30 and bmi <= 34.9:
    text = "You're obese."
elif bmi >= 25 and bmi <= 29.9:
    text = "You're 0verweight."
elif bmi >= 18.5 and bmi <= 24.9:
    text = "You're healthy."

print(f"{bmi:.1f}")
print(text)

# print(f"{converted_weight:.1f}")
