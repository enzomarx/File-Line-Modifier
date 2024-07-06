import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os

def modify_lines(file_paths, dest_dir, action, line_type, specific_line, new_value=None):
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        file_name = os.path.basename(file_path)
        dest_path = os.path.join(dest_dir, file_name)
        
        with open(dest_path, 'w', encoding='utf-8') as file:
            for i, line in enumerate(lines):
                if (line_type == "all" or
                    (line_type == "odd" and i % 2 != 0) or
                    (line_type == "even" and i % 2 == 0) or
                    (line_type == "every_3" and i % 3 == 2) or
                    (line_type == "every_4" and i % 4 == 3) or
                    (line_type == "specific" and i + 1 == specific_line)):
                    
                    if action == "add":
                        line = line.rstrip('\n') + '|\n'
                    elif action == "remove" and line.rstrip().endswith("|"):
                        line = line.rstrip('|') + '\n'
                    elif action == "change" and new_value is not None:
                        line = new_value + '\n'
                file.write(line)

def select_files():
    files = filedialog.askopenfilenames(
        title="Select text files",
        filetypes=[("Text files", "*.txt")],
        initialdir=os.getcwd()
    )
    file_list_var.set(files)

def select_destination():
    dest_dir = filedialog.askdirectory(
        title="Select destination directory",
        initialdir=os.getcwd()
    )
    dest_dir_var.set(dest_dir)

def on_process(action_var, file_list_var, dest_dir_var, new_value_entry, line_type_var, specific_line_entry, root):
    action = action_var.get()
    files = list(root.tk.splitlist(file_list_var.get()))
    dest_dir = dest_dir_var.get()
    new_value = new_value_entry.get() if action == "change" else None
    line_type = line_type_var.get()
    specific_line = int(specific_line_entry.get()) if line_type == "specific" else None
    modify_lines(files, dest_dir, action, line_type, specific_line, new_value)

def show_interface():
    global specific_line_entry, new_value_entry, action_var, file_list_var, dest_dir_var, line_type_var

    root = tk.Tk()
    root.title("File Line Modifier")
    root.geometry("600x400")
    root.resizable(False, False)
    
    # Adding a style
    style = ttk.Style()
    style.configure('TFrame', background='#ececec')
    style.configure('TButton', background='#4B0082', foreground='#0000FF', font=('Helvetica', 10, 'bold'))
    style.map('TButton', background=[('active', '#4B0082')])
    style.configure('TLabel', background='#ececec')
    style.configure('TEntry', background='#ffffff')
    style.configure('TRadiobutton', background='#ececec')

    main_frame = ttk.Frame(root, padding="10 10 10 10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    file_list_var = tk.StringVar(value=[])
    dest_dir_var = tk.StringVar()
    action_var = tk.StringVar(value="add")
    line_type_var = tk.StringVar(value="all")

    ttk.Label(main_frame, text="Select files to modify:").grid(row=0, column=0, sticky=tk.W)
    ttk.Button(main_frame, text="Browse...", command=select_files).grid(row=0, column=1, sticky=tk.E)
    
    file_listbox = tk.Listbox(main_frame, listvariable=file_list_var, height=5, selectmode=tk.MULTIPLE)
    file_listbox.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))
    
    ttk.Label(main_frame, text="Select destination directory:").grid(row=2, column=0, sticky=tk.W)
    ttk.Entry(main_frame, textvariable=dest_dir_var, width=30).grid(row=3, column=0, sticky=(tk.W, tk.E))
    ttk.Button(main_frame, text="Browse...", command=select_destination).grid(row=3, column=1, sticky=tk.E)
    
    ttk.Label(main_frame, text="Select action:").grid(row=4, column=0, sticky=tk.W)
    action_frame = ttk.Frame(main_frame)
    action_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))
    
    ttk.Radiobutton(action_frame, text="Add '|'", variable=action_var, value="add").pack(side=tk.LEFT)
    ttk.Radiobutton(action_frame, text="Remove '|'", variable=action_var, value="remove").pack(side=tk.LEFT)
    ttk.Radiobutton(action_frame, text="Change line", variable=action_var, value="change").pack(side=tk.LEFT)
    
    change_frame = ttk.Frame(main_frame)
    change_frame.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E))
    
    ttk.Label(change_frame, text="New value:").pack(side=tk.LEFT)
    new_value_entry = ttk.Entry(change_frame, width=30)
    new_value_entry.pack(side=tk.LEFT)
    
    ttk.Label(main_frame, text="Select lines to modify:").grid(row=7, column=0, sticky=tk.W)
    line_type_frame = ttk.Frame(main_frame)
    line_type_frame.grid(row=8, column=0, columnspan=2, sticky=(tk.W, tk.E))
    
    ttk.Radiobutton(line_type_frame, text="All lines", variable=line_type_var, value="all").pack(side=tk.LEFT)
    ttk.Radiobutton(line_type_frame, text="Odd lines", variable=line_type_var, value="odd").pack(side=tk.LEFT)
    ttk.Radiobutton(line_type_frame, text="Even lines", variable=line_type_var, value="even").pack(side=tk.LEFT)
    ttk.Radiobutton(line_type_frame, text="Every 3rd line", variable=line_type_var, value="every_3").pack(side=tk.LEFT)
    ttk.Radiobutton(line_type_frame, text="Every 4th line", variable=line_type_var, value="every_4").pack(side=tk.LEFT)
    ttk.Radiobutton(line_type_frame, text="Specific line", variable=line_type_var, value="specific").pack(side=tk.LEFT)

    specific_line_frame = ttk.Frame(main_frame)
    specific_line_frame.grid(row=9, column=0, columnspan=2, sticky=(tk.W, tk.E))
    
    ttk.Label(specific_line_frame, text="Line number:").pack(side=tk.LEFT)
    specific_line_entry = ttk.Entry(specific_line_frame, width=5)
    specific_line_entry.pack(side=tk.LEFT)
    
    process_button = ttk.Button(main_frame, text="Process Files", command=lambda: on_process(action_var, file_list_var, dest_dir_var, new_value_entry, line_type_var, specific_line_entry, root))
    process_button.grid(row=10, column=0, columnspan=2, pady=10)
    process_button.configure(style='TButton')

    root.mainloop()

if __name__ == "__main__":
    show_interface()
