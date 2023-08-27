# class Calculator:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self):
#         return self.x + self.y
    
#     def __sub__(self):
#         return self.x - self.y
    
#     def __mul__(self):
#         return self.x * self.y
    
#     def __div__(self):
#         try:
#             if self.y != 0:
#                 return self.x / self.y
#             else:
#                 raise ZeroDivisionError("Cannot divide by zero")
#         except ZeroDivisionError as e:
#             print(e)

#     def data(self,n):
#         self.n = n
#         if n == '+':
#             print("The Sum is = ", self.__add__())
#         elif n == '-':
#             print('The subtraction is =', self.__sub__())
#         elif n == '*':
#             print('The multiplication is =', self.__mul__())
#         elif n == '/':
#             print('The division is =', self.__div__())
#         else:
#             print('Select a valid choice first')

# x = int(input("Enter the First Number: "))
# print('1. for add=+\n2. for sub=-\n3. for multiply=*\n4. for divide=/')
# n = input("Enter the choice: ")
# y = int(input("Enter the Second Number: "))
# calc = Calculator(x,y)
# calc.data(n)


import tkinter as tk
from tkinter import messagebox
import math

BackGround_Color = "#f0f0f0" 

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("CALCULATOR")
        self.root.geometry("400x500")
        self.root.configure(bg = BackGround_Color)

        self.result_Var = tk.StringVar()

        self.result_Label = tk.Label(root, textvariable=self.result_Var, font=("Xenara", 24), anchor="e", padx=20, pady=10, bg= BackGround_Color )
        self.result_Label.pack(fill="both", expand=True)

        self.Button_Frame = tk.Frame(root, bg=BackGround_Color)
        self.Button_Frame.pack(fill="both", expand=True)

        self.Create_Buttons()

    def Create_Buttons(self):
        Button_Layout = [
            ("C", 1, 0), ("←", 1, 1),  ("%", 1, 2),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2),
            (".", 5, 0), ("0", 5, 1), ("√", 5, 2), 
            ("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3),
            ("=", 5, 3)
        ]

        for label, row, col in Button_Layout:
            Button = tk.Button(self.Button_Frame, text=label, font=("Xenara", 18), bg= "#4876ff", fg="White", relief="flat", command=lambda lbl= label: self.Button_Click(lbl))
            Button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            self.Button_Frame.grid_columnconfigure(col, weight=1)
            self.Button_Frame.grid_rowconfigure(row, weight=1)

    def Button_Click(self, label):
        current_result = self.result_Var.get()

        if label == "=":
            try:
                result = eval(current_result)
                self.result_Var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Math Error")
        
        elif label == "C":
            self.result_Var.set("")

        elif label == "√":
            try:
                result = math.sqrt(float(current_result))
                self.result_Var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Syntax Error")

        elif label == "←":
            self.result_Var.set(current_result[:-1])

        elif label == "%":
            try:
                result = float(current_result)/100
                self.result_Var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Syntax Error")

        else:
            self.result_Var.set(current_result + label)
        
root = tk.Tk()
app = Calculator(root)
root.mainloop()


