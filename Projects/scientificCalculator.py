from tkinter import *
import tkinter.messagebox
import math

root = Tk()
root.geometry("650x400+300+300")
root.title("Scientific Calculator")
switch = None

# Button press functions
def btn_num_clicked(num):
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, num)

def btn_op_clicked(op):
    pos = len(disp.get())
    disp.insert(pos, op)

def btnc_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')

def sin_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else:
            ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def cos_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else:
            ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def tan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else:
            ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def logarithm_clicked():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def ln_clicked():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def pow_clicked():
    pos = len(disp.get())
    disp.insert(pos, '**')

def fact_clicked():
    try:
        ans = int(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def sqr_clicked():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def pi_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))

def e_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))

def mod_clicked():
    pos = len(disp.get())
    disp.insert(pos, '%')

def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])

def btneq_clicked(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)
    except:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# Conversion button function
def conv_clicked():
    global switch
    if switch is None:
        switch = True
        conv_btn['text'] = "Deg"
    else:
        switch = None
        conv_btn['text'] = "Rad"

# Display
data = StringVar()
disp = Entry(root, font="Verdana 20", fg="black", bg="mistyrose", bd=0, justify=RIGHT,
              insertbackground="#abbab1", cursor="arrow")
disp.insert(0, '0')
disp.pack(expand=TRUE, fill=BOTH)

# Row 1 Buttons
btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)

# Adding buttons to Row 1
for i in range(1, 4):
    Button(btnrow1, text=str(i), font="Segoe 23", relief=GROOVE, bd=0,
           command=lambda i=i: btn_num_clicked(i), fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow1, text="+", font="Segoe 23", relief=GROOVE, bd=0,
       command=lambda: btn_op_clicked('+'), fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 2 Buttons
btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)

for i in range(4, 7):
    Button(btnrow2, text=str(i), font="Segoe 23", relief=GROOVE, bd=0,
           command=lambda i=i: btn_num_clicked(i), fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow2, text="-", font="Segoe 23", relief=GROOVE, bd=0,
       command=lambda: btn_op_clicked('-'), fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 3 Buttons
btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

for i in range(7, 10):
    Button(btnrow3, text=str(i), font="Segoe 23", relief=GROOVE, bd=0,
           command=lambda i=i: btn_num_clicked(i), fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow3, text="*", font="Segoe 23", relief=GROOVE, bd=0,
       command=lambda: btn_op_clicked('*'), fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 4 Buttons
btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

Button(btnrow4, text="0", font="Segoe 23", relief=GROOVE, bd=0,
       command=lambda: btn_num_clicked(0), fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow4, text=".", font="Segoe 23", relief=GROOVE, bd=0,
       command=lambda: btn_op_clicked('.'), fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow4, text="/", font="Segoe 23", relief=GROOVE, bd=0,
       command=lambda: btn_op_clicked('/'), fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 5 Buttons
btnrow5 = Frame(root)
btnrow5.pack(expand=TRUE, fill=BOTH)

Button(btnrow5, text="sin", font="Segoe 18", relief=GROOVE, bd=0,
       command=sin_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow5, text="cos", font="Segoe 18", relief=GROOVE, bd=0,
       command=cos_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow5, text="tan", font="Segoe 18", relief=GROOVE, bd=0,
       command=tan_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 6 Buttons
btnrow6 = Frame(root)
btnrow6.pack(expand=TRUE, fill=BOTH)

Button(btnrow6, text="log", font="Segoe 18", relief=GROOVE, bd=0,
       command=logarithm_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow6, text="ln", font="Segoe 18", relief=GROOVE, bd=0,
       command=ln_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow6, text="√x", font="Segoe 18", relief=GROOVE, bd=0,
       command=sqr_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 7 Buttons
btnrow7 = Frame(root)
btnrow7.pack(expand=TRUE, fill=BOTH)

Button(btnrow7, text="π", font="Segoe 18", relief=GROOVE, bd=0,
       command=pi_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow7, text="e", font="Segoe 18", relief=GROOVE, bd=0,
       command=e_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow7, text="x^y", font="Segoe 18", relief=GROOVE, bd=0,
       command=pow_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 8 Buttons
btnrow8 = Frame(root)
btnrow8.pack(expand=TRUE, fill=BOTH)

Button(btnrow8, text="!", font="Segoe 18", relief=GROOVE, bd=0,
       command=fact_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow8, text="Mod", font="Segoe 18", relief=GROOVE, bd=0,
       command=mod_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow8, text="Del", font="Segoe 18", relief=GROOVE, bd=0,
       command=del_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 9 Buttons
btnrow9 = Frame(root)
btnrow9.pack(expand=TRUE, fill=BOTH)

Button(btnrow9, text="C", font="Segoe 18", relief=GROOVE, bd=0,
       command=btnc_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

Button(btnrow9, text="=", font="Segoe 18", relief=GROOVE, bd=0,
       command=btneq_clicked, fg="white", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)

# Conversion Button
conv_btn = Button(btnrow9, text="Rad", font="Segoe 18", relief=GROOVE, bd=0,
                  command=conv_clicked, fg="white", bg="#333333")
conv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

root.mainloop()

