import tkinter as tk
from tkinter import font
from functools import partial

def get_input(entry, argu):
    entry.insert(tk.END, argu)

def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)

def clear(entry):
    entry.delete(0, tk.END)

def calc(entry):
    input_info = entry.get()
    try:
        output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg()
        output = ""
    clear(entry)
    entry.insert(tk.END, output)

def popupmsg():
    popup = tk.Tk()
    popup.resizable(0, 0)
    popup.geometry("120x100")
    popup.title("Alert")
    label = tk.Label(popup, text="Cannot divide by 0!\nEnter valid values")
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
    B1.pack()

def create_button(master, text, command, row, column, bg, width=10, height=3):
    button = tk.Button(master, text=text, command=command, bg=bg, width=width, height=height)
    button.grid(row=row, column=column, pady=5)
    return button

def create_entry(master, font_size=15):
    entry_font = font.Font(size=font_size)
    entry = tk.Entry(master, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4, sticky=tk.N + tk.W + tk.S + tk.E, padx=5, pady=5)
    return entry

def create_calculator():
    root = tk.Tk()
    root.title("Calculator")
    root.resizable(0, 0)

    entry = create_entry(root)

    button_colors = {
        "cal": '#FF6600',
        "num": '#4B4B4B',
        "other": '#DDDDDD',
        "active": '#C0C0C0',
    }

    num_button = partial(create_button, root, bg=button_colors["num"])
    cal_button = partial(create_button, root, bg=button_colors["cal"])

    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 4, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 2, 3),
        ('0', 5, 0), ('.', 5, 1), ('/', 1, 3), ('<-', 1, 0, button_colors["other"], 5),
        ('C', 1, 2, button_colors["other"]), ('=', 5, 3, button_colors["cal"]), ('^', 5, 2, button_colors["cal"]),
    ]

    for button in buttons:
        create_button(*button, width=5, height=2, fg='white')

    exit_button = create_button(root, text='Quit', command=root.quit, bg='black', width=7, height=1, row=6, column=1, fg='white')

    root.mainloop()

if __name__ == '__main__':
    create_calculator()

