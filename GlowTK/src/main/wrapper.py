import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class Color:
    WHITE = "#ffffff"
    BLACK = "#0f0f0f"
    GREY = "#615d53"


def create_window(Title, Geometry, Background=None, Theme=None):
    window = tk.Tk()
    window.title(Title)
    window.geometry(Geometry)
    
    # Apply theme if provided
    if Theme != None:
        apply_theme(window, Theme)
        print("trying to add theme")
    
    if Background == None:
        pass
    else:
        window.configure(bg=Background)
    return window


def apply_theme(window, Theme):
    style = ttk.Style()
    
    if Theme == "Metro":
        style.configure("TButton", background=Color.GREY, font=("Helvetica", 12))
        style.configure("TLabel", foreground=Color.BLACK)
    elif Theme == "Dark":
        style.configure("TButton", background=Color.BLACK, foreground=Color.WHITE, font=("Helvetica", 12))
        style.configure("TLabel", foreground=Color.WHITE)
    # Add more theme configurations here. Will do in later update, im to tired right now.
    

def add_button(window, text, command, X, Y, color=None):
    button = ttk.Button(window, text=text, command=command, style=color)
    button.place(x=X, y=Y)
    

def add_label(window, text, X, Y, color=None):
    label = ttk.Label(window, text=text, style=color)
    label.place(x=X, y=Y)
    

def add_textbox(window, color=None):
    entry = ttk.Entry(window, style=color)
    entry.place(x=10, y=10)  # Adjust the coordinates as needed


def promptFileOpen(Title=None):
    if Title is None:
        Title = "File Menu"
    file_path = filedialog.askopenfilename(title=Title)
    return file_path