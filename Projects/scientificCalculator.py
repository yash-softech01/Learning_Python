from tkinter import *
from math import sin, cos, tan, sqrt, log, pi, radians, degrees

# Initialize the window
window = Tk()
window.title("Scientific Calculator")

# Global variables
switch = None  # To toggle between radians and degrees

# Function to handle button click
def click(event):
    current = display.get()
    button_text = event.widget.cget("text")
    
    if button_text == "=":
        try:
            result = eval(current)
            display.delete(0, END)
            display.insert(END, result)
        except Exception as e:
            display.delete(0, END)
            display.insert(END, "Error")
    elif button_text == "C":
        display.delete(0, END)
    else:
        display.insert(END, button_text)

# Function to switch between Radians and Degrees
def conv_clicked():
    global switch
    if switch is None:
        switch = True
        conv_btn['text'] = "Deg"
    else:
        switch = None
        conv_btn['text'] = "Rad"

# Function to calculate the result for trigonometric functions
def calculate_trig(operation):
    value = float(display.get())
    result = None
    if switch:  # Degrees
        value = radians(value)
    
    if operation == 'sin':
        result = sin(value)
    elif operation == 'cos':
        result = cos(value)
    elif operation == 'tan':
        result = tan(value)
    
    display.delete(0, END)
    display.insert(END, result)

# Function to handle sqrt, log, etc.
def special_operation(operation):
    value = float(display.get())
    result = None
    
    if operation == 'sqrt':
        result = sqrt(value)
    elif operation == 'log':
        result = log(value)
    
    display.delete(0, END)
    display.insert(END, result)

# Create display
display = Entry(window, width=35, borderwidth=5, font=('Arial', 18))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons
buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', 'sqrt',
    '1', '2', '3', '-', 'log',
    '0', '.', '=', '+', 'sin', 'cos', 'tan'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'sin':
        btn = Button(window, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda op='sin': calculate_trig(op))
    elif button == 'cos':
        btn = Button(window, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda op='cos': calculate_trig(op))
    elif button == 'tan':
        btn = Button(window, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda op='tan': calculate_trig(op))
    elif button == 'sqrt':
        btn = Button(window, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda op='sqrt': special_operation(op))
    elif button == 'log':
        btn = Button(window, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda op='log': special_operation(op))
    else:
        btn = Button(window, text=button, padx=20, pady=20, font=('Arial', 14))
        btn.bind("<Button-1>", click)

    btn.grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# Conversion button (Rad/Deg)
conv_btn = Button(window, text="Rad", padx=20, pady=20, font=('Arial', 14), command=conv_clicked)
conv_btn.grid(row=row_val, column=0, columnspan=2)

# Run the application
window.mainloop()
