import tkinter
from tkinter import ttk
from functools import partial


accumulator = '0'
operand = '0'
last_operator = ''


def number_key(event):
    number_command(event.char)

def number_command(number):
    global operand
    if operand != '0':
        operand += str(number)
    else:
        operand = str(number)

    solution_label.configure(text=operand)


def operator_command(operator):
    global operand
    global accumulator
    global last_operator
    last_operator = operator
    if accumulator == '0':
        accumulator = operand
    operand = '0'


def calculate():
    global operand
    global accumulator
    global last_operator

    if last_operator == '+':
        result = int(accumulator) + int(operand)
    elif last_operator == '-':
        result = int(accumulator) - int(operand)
    elif last_operator == '*':
        result = int(accumulator) * int(operand)
    elif last_operator == '/':
        result = int(accumulator) / int(operand)

    operand = '0'
    accumulator = result
    solution_label.configure(text=accumulator)


def clear():
    global operand
    global accumulator
    global last_operator

    last_operator = "0"
    accumulator = "0"
    operand = "0"

    solution_label.configure(text=accumulator)

def test(event):
    print('test', event)

# GUI part
root = tkinter.Tk()
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0)

solution_label = ttk.Label(main_frame, text="0")
solution_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

CE_button = ttk.Button(main_frame, text="CE", command=clear)
CE_button.grid(row=1, column=0, padx=5, pady=5)

for i in range(3):
    for j in range(3):
        button = ttk.Button(main_frame, text=3*i + j + 1, command=partial(number_command, 3*i + j + 1))
        button.grid(row=4 - i, column=j, padx=5, pady=5)

        root.bind(str(3*i + j + 1), number_key)

zero_button = ttk.Button(main_frame, text="0", command=partial(number_command, 0))
zero_button.grid(row=5, column=1, padx=5, pady=5)
root.bind('0', number_key)

addition_button = ttk.Button(main_frame, text="+" , command=partial(operator_command, '+'))
addition_button.grid(row=1, column=3, padx=5, pady=5)

subtraction_button = ttk.Button(main_frame, text="-" , command=partial(operator_command, '-'))
subtraction_button.grid(row=2, column=3, padx=5, pady=5)

multiplication_button = ttk.Button(main_frame, text="*" , command=partial(operator_command, '*'))
multiplication_button.grid(row=3, column=3, padx=5, pady=5)

division_button = ttk.Button(main_frame, text="/" , command=partial(operator_command, '/'))
division_button.grid(row=4, column=3, padx=5, pady=5)

equal_button = ttk.Button(main_frame, text="=", command=calculate)
equal_button.grid(row=5, column=3, padx=5, pady=5)
root.bind('<Return>', test)

root.mainloop()