import tkinter as tk

def calbmi():
    w = float(wentr.get())
    h = float(hentr.get())
    bmi = round(w/(h**2),2)
    bmilab.config(text=f"BMI : {bmi}")

root = tk.Tk()
root.title("BMI Cal")

wlab = tk.Label(root, text = "wight is (kg): ")
wlab.grid(row =0, column =0)
wentr = tk.Entry(root)
wentr.grid(row =0, column = 1)

hlab = tk.Label(root, text = "height is (mtrs): ")
hlab.grid(row =1, column = 0)
hentr = tk.Entry(root)
hentr.grid(row =1 , column =1)

calbmibtn = tk.Button(root , text = "CAL BMI", command = calbmi)
calbmibtn.grid(row =2, column = 0, columnspan =2)

bmilab = tk.Label(root, text = "BMI:")
bmilab.grid(row=3, column =0, columnspan =2)

root.mainloop()
