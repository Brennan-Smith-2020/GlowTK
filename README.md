# My Tkinter Utilities

A collection of utility functions for working with Tkinter, the standard GUI (Graphical User Interface) library in Python.

## Functions

### `promptFileOpen`

**Description:** Opens a file selection dialog to prompt the user for opening a file.

**Parameters:**
- `Title` (`str`): The title to be displayed in the file dialog.

**Returns:**
- `Selected File Path` (`str`): The path of the file selected by the user.

**Example Usage:**
```python
import tkinter as tk
from tkinter import filedialog


# Using promptFileOpen
file_path = promptFileOpen("Select a file")
print("Selected file path:", file_path)
```
### `createWindow`

**Description** Opens a window with the specified attributes

**Parameters:**
- `Title` (`str`): Title of the window
- `Geometry` (`str`): Geometry of window, works like vanilla tkinter. Example: `400x400`.
- `Background` (`str`): Background color, works like vanilla tkinter.

  **example usage**
  ```python
  import tkinter as tk

  # Using createWindow
  createWindow("My window", "400x400", "white")
  ```
