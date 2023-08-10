# GlowTK: Enhancing Tkinter Experience

GlowTK is a collection of utility functions designed to enhance the experience of using Tkinter, the standard GUI (Graphical User Interface) library in Python.

Choosing colors:
The code has a builtin class for choosing colors. It currently has 3 builtin. White, Grey and black. do color.WHITE/whatever color in all caps here to use.
If you get an error try importing + running initialize()

## How to import
in this tutorial I said you needed to do import GlowTK, however if that provides an error make a parent folder to the GlowTK folder (Doesnt have to be a parent folder but is easier) than write your code by importing as follows: `from GlowTK.src.main.wrapper import [functions here, seperated by commas].
Do this until this (hopefully) this gets ported to pip.
## Functions:

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
   - `color` (class)
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
   GlowTK.add_button(window, "Click me", my_function, X=100, Y=100, color.WHITE) # Deafults to NONE/Null if you leave empty
   window.mainloop()
   ```

4. `add_label`

Description: Adds a label to a tkinter window
Parameters:
- `window` (Tk)
- `text` (str)
- `X` (int)
- `Y` (int)
- `color` (class)
- `Font` (str), has deafult therfor not needed to add
- `FontSize` (int), has deafult therfor not needed to add
Example:
```python
import tkinter as tk
import GlowTK
window = create_window("TEST", "400x400", "white")
add_label(window, "hi :)", 100, 100, color.WHITE) # Deafults to NONE/Null if you leave empty
window.mainloop()
```

5. `add_textbox`

Description: Adds a textbox to window
Parameters:
- `window` (Tk)
- `color` (class)
Example:
```python
import tkinter as tk
import GlowTk
window = create_window("TEST", "400x400")
textbox = add_textbox(window)
window.mainloop()
```

# LICENSE
```
MIT License (Modified)

Copyright (c) 2023-2024 PackageCreator

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute and sublicense the software, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

2. You must provide proper attribution to PackageCreator in commercial redistributions
   or modifications of the software.

3. The software may not be sold for monetary gain or exchanged for items, software, or any other form of value, whether in currency or trade.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Failing to comply with the above conditions constitutes a violation of the
copyright law of the software.
```
