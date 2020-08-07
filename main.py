from tkinter import *


root = Tk()
root.title("Calculator")


# global variables that control calc functions

first_number = None
second_number = None
procedure = None
new_number = True


def w_number(number):  # write number on screen
    global new_number
    if new_number == True:
        entry.delete(0,END)
    new_number = False
    entry.insert(END, number)


def clear_all():
    global first_number
    global second_number
    global procedure
    global new_number
    first_number = None
    second_number = None
    procedure = None
    new_number = True
    entry.delete(0,END)


def equalizer():
    global first_number
    global second_number
    second_number = entry.get()
    entry.delete(0,END)
    if procedure == '+':
        solution = int(first_number) + int(second_number)
        entry.insert(0, solution)
        first_number = solution
        return solution
    elif procedure == '-':
        solution = int(first_number) - int(second_number)
        entry.insert(0, solution)
        first_number = solution
        return solution
    elif procedure == '*':
        solution = int(first_number) * int(second_number)
        entry.insert(0, solution)
        first_number = solution
        return solution
    elif procedure == '/':
        solution = int(first_number) / int(second_number)
        entry.insert(0, solution)
        first_number = solution
        return solution
    else:
        print("i did nothing")


def add_numbers():
    global first_number
    global second_number
    global procedure
    global new_number
    new_number = True
    if first_number is None:
        first_number = entry.get()
        entry.delete(0,END)
    elif second_number is None:
        second_number = entry.get()
        first_number = equalizer()
        second_number = None
    else:
        second_number = None
    procedure = '+'


def minus_numbers():
    global first_number
    global second_number
    global procedure
    global new_number
    new_number = True
    if first_number is None:
        first_number = entry.get()
        entry.delete(0,END)
    elif second_number is None:
        second_number = entry.get()
        first_number = equalizer()
        second_number = None
    else:
        second_number = None
    procedure = '-'


def multiply_numbers():
    return

def divide_numbers():
    return

# define buttons


entry = Entry(root, width=35, borderwidth=2)

b_0 = Button(root, text="0", width=5, command=lambda: w_number(0))
b_1 = Button(root, text="1", width=5, command=lambda: w_number(1))
b_2 = Button(root, text="2", width=5, command=lambda: w_number(2))
b_3 = Button(root, text="3", width=5, command=lambda: w_number(3))
b_4 = Button(root, text="4", width=5, command=lambda: w_number(4))
b_5 = Button(root, text="5", width=5, command=lambda: w_number(5))
b_6 = Button(root, text="6", width=5, command=lambda: w_number(6))
b_7 = Button(root, text="7", width=5, command=lambda: w_number(7))
b_8 = Button(root, text="8", width=5, command=lambda: w_number(8))
b_9 = Button(root, text="9", width=5, command=lambda: w_number(9))

b_plus = Button(root, text="+", width=5, command=add_numbers)
b_minus = Button(root, text="-", width=5, command=minus_numbers)
b_clear = Button(root, text="Clear", width=5, command=clear_all)
b_ans = Button(root, text="Ans", width=18, command=equalizer)


# add buttons to root grid


entry.grid(row=0, column=0, columnspan=3, padx=5, pady=10)

b_1.grid(row=1, column=0,padx=5,pady=5)
b_2.grid(row=1, column=1,padx=5,pady=5)
b_3.grid(row=1, column=2,padx=5,pady=5)
b_4.grid(row=2, column=0,padx=5,pady=5)
b_5.grid(row=2, column=1,padx=5,pady=5)
b_6.grid(row=2, column=2,padx=5,pady=5)
b_7.grid(row=3, column=0,padx=5,pady=5)
b_8.grid(row=3, column=1,padx=5,pady=5)
b_9.grid(row=3, column=2,padx=5,pady=5)
b_0.grid(row=4, column=0,padx=5,pady=5)

b_plus.grid(row=4, column=1,padx=5,pady=5)
b_minus.grid(row=4,column=2)
b_ans.grid(row=5, column=1,columnspan=2,pady=5)
b_clear.grid(row=5 ,column=0,pady=5)

root.mainloop()








