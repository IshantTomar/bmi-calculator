from tkinter import *
from tkinter import ttk

window = Tk()
window.title("BMI Calculator")
notebook = ttk.Notebook(window)

bmi_tab = Frame(notebook)
converter_tab = Frame(notebook)

notebook.add(bmi_tab, text="BMI Converter")
notebook.add(converter_tab, text="Units Converter")
notebook.pack()

def bmi_convert():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        h = height * height
        bmi = float(weight / h)
        bmi_right = f"{bmi:.2f}"
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
        label_incorrect = Label(bmi_tab, text="Please enter numbers.", font=5, fg="red")
        label_incorrect.grid(row=4,column=0, columnspan=2)

def cm_convert():
    try:
        centimeters = float(cm_label.get())
        cm_m = centimeters / 100
        cm = f"{cm_m:.2f}"
        m_label1.set(cm)
    except ValueError:
        label_incorrect1 = Label(converter_tab, text="Please enter numbers.", font=5, fg="red")
        label_incorrect1.grid(row=9, column=0, columnspan=3)

def foots_convert():
    try:
        foot = float(foot_label_en.get())
        foot_m = foot * 0.3048
        f = f"{foot_m:.2f}"
        m_label2.set(f)
    except ValueError:
        label_incorrect2 = Label(converter_tab, text="Please enter numbers.", font=5, fg="red")
        label_incorrect2.grid(row=9, column=0, columnspan=3)

def pounds_convert():
    try:
        pounds = float(pounds_label.get())
        lb_kg = pounds * 0.453
        lb = f"{lb_kg:.2f}"
        kg_label.set(lb)
    except ValueError:
        label_incorrect3 = Label(converter_tab, text="Please enter numbers.", font=5, fg="red")
        label_incorrect3.grid(row=9, column=0, columnspan=3)


entry_weight = StringVar()
entry_height = StringVar()
bmi_label = StringVar()
bmi_value = StringVar()

label_weight_en = ttk.Entry(bmi_tab, textvariable=entry_weight, font=5, justify=CENTER)
label_weight_en.grid(row=0,column=0)
label_weight = Label(bmi_tab, text="Weight(kgs)", font=5)
label_weight.grid(row=1,column=0)

label_height_en = ttk.Entry(bmi_tab, textvariable=entry_height, font=5, justify=CENTER)
label_height_en.grid(row=0,column=1)
label_height = Label(bmi_tab, text="Height(ms)", font=5)
label_height.grid(row=1,column=1)
label_equal = Label(bmi_tab, text="=", font=5)
label_equal.grid(row=0,column=2)
label_bmi = Label(bmi_tab, textvariable=bmi_label, font=5, justify=CENTER)
label_bmi.grid(row=0,column=3)
label_bmi = Label(bmi_tab, textvariable=bmi_value, font=5, justify=CENTER)
label_bmi.grid(row=1,column=3)

bmi_button = ttk.Button(bmi_tab, text="Convert", command=bmi_convert)
bmi_button.grid(row=2,column=0,columnspan=3)

cm_label = StringVar()
m_label1 = StringVar()
foot_label = StringVar()
m_label2 = StringVar()
pounds_label = StringVar()
kg_label = StringVar()

centimeter_label_en = ttk.Entry(converter_tab, textvariable=cm_label, font=5, justify=CENTER)
centimeter_label_en.grid(row=0,column=0)
centimeter_label = Label(converter_tab, text="Centimeters(cms)", font=5)
centimeter_label.grid(row=1,column=0)
equal_label1 = Label(converter_tab, text="=", font=5)
equal_label1.grid(row=0,column=1)
meter_label_en = ttk.Entry(converter_tab, textvariable=m_label1, font=5, state="readonly", justify=CENTER)
meter_label_en.grid(row=0,column=2)
meter_label = Label(converter_tab, text="Meters(ms)", font=5)
meter_label.grid(row=1,column=2)

m1_button = ttk.Button(converter_tab, text="Convert", command=cm_convert)
m1_button.grid(row=2,column=0,columnspan=3)


foot_label_en = ttk.Entry(converter_tab, textvariable=foot_label, font=5, justify=CENTER)
foot_label_en.grid(row=3,column=0)
foot_label = Label(converter_tab, text="Feet.Inches", font=5)
foot_label.grid(row=4,column=0)
equal_label2 = Label(converter_tab, text="=", font=5)
equal_label2.grid(row=3,column=1)
meter1_label_en = ttk.Entry(converter_tab, textvariable=m_label2, font=5, state="readonly", justify=CENTER)
meter1_label_en.grid(row=3,column=2)
meter_label1 = Label(converter_tab, text="Meters(ms)", font=5)
meter_label1.grid(row=4,column=2)

m2_button = ttk.Button(converter_tab, text="Convert", command=foots_convert)
m2_button.grid(row=5,column=0,columnspan=3)


pounds_label_en = ttk.Entry(converter_tab, textvariable=pounds_label, font=5, justify=CENTER)
pounds_label_en.grid(row=6,column=0)
pound_label = Label(converter_tab, text="Pounds(lbs)", font=5)
pound_label.grid(row=7,column=0)
equal_label3 = Label(converter_tab, text="=", font=5)
equal_label3.grid(row=6,column=1)
kg1_label_en = ttk.Entry(converter_tab, textvariable=kg_label, font=5, state="readonly", justify=CENTER)
kg1_label_en.grid(row=6,column=2)
kg_label1 = Label(converter_tab, text="Kilograms(kgs)", font=5)
kg_label1.grid(row=7,column=2)

k_button = ttk.Button(converter_tab, text="Convert", command=pounds_convert)
k_button.grid(row=8,column=0,columnspan=3)





















window.mainloop()
# print(f"{bmi:.1f}")
# print(text)
# print(f"{converted_weight:.1f}")
