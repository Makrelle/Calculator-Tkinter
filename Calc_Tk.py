# Calculator app using Tkinter
from tkinter import *

root = Tk()
root.title("Calculator")
root.config(background="black")
root.resizable(width=False, height=False)

operation_buttons = ["C", "+", "- ", "* ", "/ "]
color_palette = ["#84e5cd", "#ff5560", "#f6b158", "#28c09a"]

# create entry window
e = Entry(root, font=("Helvetica", 14), bd=2, width=15, bg="lightblue")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10, ipady=10)


def button_click(number):
    e.insert(END, number)


def button_clear():
    e.delete(0, END)


def give_result(event=None):
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, result)
    except ZeroDivisionError:
        e.delete(0, END)
        e.insert(0, "Can't divide by zero")
    except SyntaxError or NameError:
        e.delete(0, END)
        e.insert(0, "ERROR")


root.bind_all('<Return>', give_result)  # gives result by pressing 'Enter'


def buttons(text, row, column):
    command = lambda: button_click(text)
    bg_color = color_palette[0]
    if text == "C":
        bg_color = color_palette[1]
        command = button_clear
    if text in operation_buttons[1:]:
        bg_color = color_palette[2]

    b = Button(root, bd=5, text=text, padx=20, pady=20, bg=bg_color,
               command=command, font=("Helvetica", 14, "bold"))
    b.grid(row=row, column=column)


def create_num_buttons():
    num = 9
    for i in range(3):
        for j in range(3, 0, -1):
            buttons(str(num), i + 1, j - 1)
            num -= 1
    buttons("0", 4, 0)


def create_equals_button():
    eq_b = Button(root, bd=5, text="=", padx=56, pady=20, bg=color_palette[3],
                  command=give_result, font=("Helvetica", 14, "bold"))
    eq_b.grid(row=4, column=1, columnspan=2)


def create_operation_buttons():
    for i, b in enumerate(operation_buttons):
        buttons(b, i, 3)


def main():
    create_num_buttons()
    create_equals_button()
    create_operation_buttons()
    root.mainloop()


main()
