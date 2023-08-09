import tkinter as tk
from tkinter import filedialog

def create_window(Title, Geometry, Background):
    window = tk.Tk()
    window.title(Title)
    window.geometry(Geometry)
    if Background == "default":
        pass
    else:
        window.configure(bg=Background)
    return window
def add_button(window, text, command, X, Y):
    button = tk.Button(window, text=text, command=command)
    button.place(x=X, y=Y)
    
def add_label(window, text, X, Y):
    label = tk.Label(window, text)
    label.place(x=X, y=Y)

def promptFileOpen(Title):
    file_path = filedialog.askopenfilename(title=Title)
    return file_path
