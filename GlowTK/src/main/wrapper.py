import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import filedialog
from tkinter import colorchooser
from pynput import keyboard
import win32api

WelcomeMsg = True
def welcomeMsg():
    print("Hello from the devs of GlowTK! You can see the docs here: https://github.com/PackageCreator/GlowTK \n")
    print("Suppress this message with WelcomeMsg = False")

class Color:
    WHITE = "#ffffff"
    BLACK = "#000000"
    GREY = "#808080"
    RED = "#ff0000"
    GREEN = "#00ff00"
    BLUE = "#0000ff"
    YELLOW = "#ffff00"
    ORANGE = "#ffa500"
    PURPLE = "#800080"
    PINK = "#ffc0cb"
    CYAN = "#00ffff"
    MAGENTA = "#ff00ff"
    BROWN = "#a52a2a"
    LIME = "#00ff00"
    INDIGO = "#4b0082"
    TEAL = "#008080"
    OLIVE = "#808000"
    MAROON = "#800000"
    NAVY = "#000080"
    SILVER = "#c0c0c0"
    GOLD = "#ffd700"
    DARK_GREEN = "#006400"
    DARK_RED = "#8b0000"
    DARK_BLUE = "#00008b"
    DARK_GREY = "#272927"
    LIGHT_GREY = "#d3d3d3"

def create_window(Title, Geometry, Background=None, Theme=None):
    global mousex, mousey
    window = ThemedTk(Theme)
    window.title(Title)
    window.geometry(Geometry)
    
    if Background is not None:
        window.configure(bg=Background)

    # Initialize mouse coordinates attributes
    mousex = 0
    mousey = 0

    def motion(event):
        global mousex, mousey
        mousex, mousey = event.x, event.y
    window.bind('<Motion>', motion)

    return window

def add_button(window, text, command, X, Y, color=None):
    button = ttk.Button(window, text=text, command=command, style=color)
    button.place(x=X, y=Y)
    return button

def add_label(window, text, X, Y, color=None, Font=None, FontSize=12):
    label = ttk.Label(window, text=text, style=color, font=(Font, FontSize))
    label.place(x=X, y=Y)
    return label

def add_textbox(window, X, Y, color=None):
    entry = ttk.Entry(window, style=color)
    entry.place(x=X, y=Y)
    return entry

def promptFileOpen(Title=None):
    if Title is None:
        Title = "File Menu"
    file_path = filedialog.askopenfilename(title=Title)
    return file_path

def draw(canvas, x, y, color):
    canvas.create_oval(x, y, x+2, y+2, fill=color)

if WelcomeMsg:
    welcomeMsg()
    


