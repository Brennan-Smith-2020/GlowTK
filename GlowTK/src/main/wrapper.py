import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import filedialog
import logging

class Color:
    WHITE = "#ffffff"
    BLACK = "#0f0f0f"
    GREY = "#615d53"


def create_window(Title, Geometry, Background=None, Theme=None):
    window = ThemedTk(Theme)
    if Theme != Theme in ThemedTk:
        logging.warn("Error, theme not specified correctly")
        exit()
    window.title(Title)
    window.geometry(Geometry)
    if Background == None:
        pass
    else:
        window.configure(bg=Background)
    return window    

def add_button(window, text, command, X, Y, color=None):
    button = ttk.Button(window, text=text, command=command, style=color)
    button.place(x=X, y=Y)
    

def add_label(window, text, X, Y, color=None, Font=None, FontSize=12):
    label = ttk.Label(window, text=text, style=color, font=(Font, FontSize))
    label.place(x=X, y=Y)
    

def add_textbox(window, X, Y, color=None):
    entry = ttk.Entry(window, style=color)
    entry.place(x=X, y=Y)  # Adjust the coordinates as needed


def promptFileOpen(Title=None):
    if Title is None:
        Title = "File Menu"
    file_path = filedialog.askopenfilename(title=Title)
    return file_path


# Write here 


window = create_window("daynes Portal", "200x400", "grey", "metro")
label = add_label(window, "button = open file, textbox = type for fun :)", 200, 200, None, None, 12)
textbox = add_textbox(window, 200, 100)
button = add_button(window, "Click me", promptFileOpen, 100, 100, None)
window.mainloop()

"""im working on an upgraded GUI lib, with functions :)"""