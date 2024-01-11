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





