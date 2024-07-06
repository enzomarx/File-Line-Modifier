import tkinter as tk
from tkinter import filedialog
import os

def add_pipe_to_0240_lines(file_paths):
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                if line.startswith("0240|"):
                    line = line.rstrip('\n') + '|\n'
                file.write(line)

def select_files():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_paths = filedialog.askopenfilenames(
        title="Select text files",
        filetypes=[("Text files", "*.txt")],
        initialdir=os.getcwd()
    )
    if file_paths:
        add_pipe_to_0240_lines(file_paths)
        print("Process completed.")
    else:
        print("No files selected.")

if __name__ == "__main__":
    select_files()
