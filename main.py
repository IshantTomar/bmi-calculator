import math
while True:
    try:
        weight = (float(input("Enter your weight (kgs): ")))
        height = (float(input("Enter your height (m): ")))
        break
    except ValueError:
        print("Please enter numbers")

h = height * height
bmi = float(weight / h)
text = ""

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
