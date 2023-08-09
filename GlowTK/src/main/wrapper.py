import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import logging

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
        try:
            apply_theme(window, Theme)
            print("trying to add theme")
        except Exception as e:
            logging.warning(f"Theme couldnt add, maybe none was specified? Error msg = {e}")
    
    if Background == None:
        pass
    else:
        window.configure(bg=Background)
    return window

def apply_theme(window, Theme=None):
    style = ttk.Style()
    style.theme_use(Theme)  # Initialize the default theme

    style.configure("TButton", background=Color.GREY)
    style.configure("TLabel", foreground=Color.BLACK)

    window.tk_setPalette(background=style.lookup("TButton", "background"),
                         foreground=style.lookup("TLabel", "foreground"))

    

def add_button(window, text, command, X, Y, color=None):
    button = ttk.Button(window, text=text, command=command, style=color)
    button.place(x=X, y=Y)
    

def add_label(window, text, X, Y, color=None, Font=None, FontSize=12):
    label = ttk.Label(window, text=text, style=color, font=(Font, FontSize))
    label.place(x=X, y=Y)
    

def add_textbox(window, color=None):
    entry = ttk.Entry(window, style=color)
    entry.place(x=10, y=10)  # Adjust the coordinates as needed


def promptFileOpen(Title=None):
    if Title is None:
        Title = "File Menu"
    file_path = filedialog.askopenfilename(title=Title)
    return file_path