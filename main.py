import math
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("BMI Calculator")

# weight = 1
# height = 1
# def inpvalues():
#     global weight, height
#     while True:
#         try:
#             weight = (float(input("Enter your weight (kgs): ")))
#             height = (float(input("Enter your height (m): ")))
#             break
#         except ValueError:
#             print("Please enter numbers.")
#     return weight, height

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

# inpvalues()
# h = height * height
# bmi = float(weight / h)
# cm_m = centimeters/100
# foot_m = foot * 0.3048
# converted_weight = pounds * 0.45359237

def bmi_convert():
    try:
        global weight, height, text, hh, bmi_right
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        h = height * height
        bmi = float(weight / h)
        bmi_right = f"{bmi:.1f}"
        bmi_label.set(bmi_right)
        if bmi < 18.5:
            text = "You're Underweight."
            bmi_value.set(text)
        elif bmi > 35:
            text = "You're extremely obese."
            bmi_value.set(text)
        elif bmi >= 30 and bmi <= 34.9:
            text = "You're obese."
            bmi_value.set(text)
        elif bmi >= 25 and bmi <= 29.9:
            text = "You're 0verweight."
            bmi_value.set(text)
        elif bmi >= 18.5 and bmi <= 24.9:
            text = "You're healthy."
            bmi_value.set(text)
    except ValueError:
        label_incorrect = Label(window, text="Please enter numbers", font=5, fg="red")
        label_incorrect.grid(row=4,column=0, columnspan=2)

test = ""
entry_weight = StringVar()
entry_height = StringVar()
bmi_label = StringVar()
bmi_value = StringVar()

label_weight_en = ttk.Entry(window, textvariable=entry_weight, font=5, justify=CENTER)
label_weight_en.grid(row=0,column=0)
label_weight = Label(window, text="Weight(kgs)", font=5)
label_weight.grid(row=1,column=0)

label_height_en = ttk.Entry(window, textvariable=entry_height, font=5, justify=CENTER)
label_height_en.grid(row=0,column=1)
label_height = Label(window, text="Height(ms)", font=5)
label_height.grid(row=1,column=1)
label_equal = Label(window, text="=", font=5)
label_equal.grid(row=0,column=2)
label_bmi = Label(window, textvariable=bmi_label, font=5, justify=CENTER)
label_bmi.grid(row=0,column=3)
label_bmi = Label(window, textvariable=bmi_value, font=5, justify=CENTER)
label_bmi.grid(row=1,column=3)

bmi_button = ttk.Button(window, text="Convert", command=bmi_convert)
bmi_button.grid(row=3,column=0,columnspan=3)


























window.mainloop()
# print(f"{bmi:.1f}")
# print(text)
# print(f"{converted_weight:.1f}")
