**check wiki for more information**


# GlowTK: Enhancing Tkinter Experience

GlowTK is a collection of utility functions designed to enhance the experience of using Tkinter, the standard GUI (Graphical User Interface) library in Python.

Functions:

1. `promptFileOpen`

   Description: Opens a file selection dialog to prompt the user for opening a file.
   Parameters:
   - `Title` (str): The title to be displayed in the file dialog.
   Returns:
   - `Selected File Path` (str): The path of the file selected by the user.
   Example Usage:
   
   Example:
   ```python
   import tkinter as tk
   from tkinter import filedialog
   import GlowTK
   file_path = GlowTK.promptFileOpen("Select a file")
   print("Selected file path:", file_path)
   ```


2. `create_window`

   Description: Opens a window with the specified attributes.
   Parameters:
   - `Title` (str): The title of the window.
   - `Geometry` (str): Geometry of the window. Example: 400x400.
   - `Background` (str): Background color.
   Example:
   ```python
   import tkinter as tk
   import GlowTK
   
   window = GlowTK.create_window("My window", "400x400", "white")
   window.mainloop()
   ```


3. `add_button`

   Description: Adds a button to a tkinter window.
   Parameters:
   - `window` (Tk): The window instance to add the button to.
   - `text` (str): The label text for the button.
   - `command` (callable): The function to execute when the button is clicked.
   - `X` (int): The x-coordinate for placing the button.
   - `Y` (int): The y-coordinate for placing the button.
   Example:
   ```python
   import tkinter as tk
   import GlowTK
   def my_function():
       print("Button clicked!")
   
   window = GlowTK.create_window("My window", "400x400", "white")
   GlowTK.add_button(window, "Click me", my_function, X=100, Y=100)
   window.mainloop()
   ```

4. `add_label`

Description: Adds a label to a tkinter window
Parameters:
- `window` (Tk)
- `text` (str)
- `X` (int)
- `Y` (int)
Example:
```python
import tkinter as tk
import GlowTK
window = create_window("TEST", "400x400", "white")
add_label(window, "hi :)", 100, 100)
window.mainloop()
```

5. `add_textbox`

Description: Adds a textbox to window
Parameters:
`window` (Tk)
Example:
```python
import tkinter as tk
import GlowTk
textbox = add_textbox(window)
```
