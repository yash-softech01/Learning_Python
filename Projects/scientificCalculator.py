import tkinter as tk
import math
import tkinter.messagebox

# Function to evaluate basic arithmetic expressions
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception:
        return "Error"

# Function to handle button clicks
def button_click(value):
    current_expression = disp.get()
    new_expression = current_expression + str(value)
    disp.delete(0, tk.END)
    disp.insert(0, new_expression)

# Function to handle the factorial calculation
def fact_clicked():
    try:
        ans = float(disp.get())
        if ans < 0 or not ans.is_integer():  # Check for non-negative integer
            raise ValueError("Factorial is defined for non-negative integers only.")
        
        ans = math.factorial(int(ans))  # Convert to int before calculating factorial
        disp.delete(0, tk.END)
        disp.insert(0, str(ans))
    except ValueError as ve:
        tkinter.messagebox.showerror("Value Error", str(ve))
    except Exception:
        tkinter.messagebox.showerror("Error", "Check your values and operators")

# Function to clear the display
def clear_display():
    disp.delete(0, tk.END)

# Function to calculate and display the result
def calculate_result():
    current_expression = disp.get()
    result = evaluate_expression(current_expression)
    disp.delete(0, tk.END)
    disp.insert(0, str(result))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")
root.configure(bg="#f0f0f0")

# Create the display
disp = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
disp.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('!', 5, 0)
]

for (text, row, column) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, font=("Arial", 18), command=clear_display, bg="#ffdddd")
    elif text == '=':
        button = tk.Button(root, text=text, font=("Arial", 18), command=calculate_result, bg="#ddffdd")
    elif text == '!':
        button = tk.Button(root, text=text, font=("Arial", 18), command=fact_clicked, bg="#ddffff")
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: button_click(t))

    button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)

# Configure grid weights for better resizing
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the main loop
root.mainloop()
