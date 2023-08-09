import tkinter as tk
from tkinter import filedialog


class color:
    WHITE = "#ffffff"
    BLACK = "#0f0f0f"
    GREY = "#615d53"
    

def initialize():
    color = color()

def create_window(Title, Geometry, Background):
    window = tk.Tk()
    window.title(Title)
    window.geometry(Geometry)
    if Background == "default":
        pass
    else:
        window.configure(bg=Background)
    return window

def add_button(window, text, command, X, Y, color=None):
    button = tk.Button(window, text=text, command=command, bg=color)
    button.place(x=X, y=Y)
    
def add_label(window, text, X, Y, color=None):
    label = tk.Label(window, text, bg=color)
    label.place(x=X, y=Y)

def add_textbox(window, color=None):
    entry = tk.Entry(window, bg=color)
    entry.pack()

def promptFileOpen(Title=None):
    if Title == None:
        Title = "File Menu"
    file_path = filedialog.askopenfilename(title=Title)
    return file_path