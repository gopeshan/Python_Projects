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



