# File Line Modifier

**File Line Modifier** is a Python application with a graphical user interface that allows users to select multiple text files and perform specific operations on lines that start with "0240|". The available operations are adding, changing, or removing these lines.

## Features

- **Add '|' to '0240|' lines**: Adds a pipe ('|') to the end of lines that start with "0240|".
- **Remove '|' from '0240|' lines**: Removes the pipe ('|') from the end of lines that start with "0240|" if it exists.
- **Change '0240|' lines**: Replaces lines that start with "0240|" with a new value provided by the user.

## Requirements

- Python 3.x
- Tkinter (usually included in the standard Python installation)

## Installation

1. Clone this repository or download the files directly.
2. Ensure you have Python 3.x installed on your machine.
3. Install any necessary dependencies (if any).

## Usage

1. Run the `file_line_modifier.py` script.

```sh
python file_line_modifier.py
```
2. A graphical interface will open.
3. Select the desired operation:
  - Add '|' to '0240|' lines
  - Remove '|' from '0240|' lines
  - Change '0240|' lines
4. For the change operation, enter the new desired value for the '0240|' lines.
5. Select the text files you want to process.
6. The process will be completed, and a confirmation message will be displayed.