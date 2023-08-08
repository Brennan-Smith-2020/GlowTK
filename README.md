# GlowTK

GlowTK is a wrapper for the tkinter library, designed to enhance functionality and improve aesthetics in your Python GUI applications.

## `promptFileOpen` Function

### Description

The `promptFileOpen` function displays a file selection dialog, allowing the user to choose a file to open. It provides an easy way to interact with the user's file system and retrieve the selected file path.

### Parameters

- `Title` (str): The title to be displayed in the file dialog.

- `varname` (str): The name of the variable where the selected file path will be stored.

### Returns

- `Selected File Path` (str): The path of the file selected by the user.

### Example Usage

Here's an example of how to use the `promptFileOpen` function:

```python
selected_path = promptFileOpen("Example", "path")
print("Selected file path:", selected_path)
