import tkinter as tk
from tkinter import simpledialog, messagebox

def on_option_select(option):
    # Hide the initial options
    option_frame.pack_forget()
    
    # Create a new frame for file name input
    file_frame = tk.Frame(root)
    file_frame.pack(pady=20)

    # Create a label for file name input
    file_label = tk.Label(file_frame, text="Enter file name:")
    file_label.pack(side=tk.LEFT)

    # Create an entry box for file name
    file_entry = tk.Entry(file_frame)
    file_entry.pack(side=tk.LEFT)

    # Create a submit button
    submit_button = tk.Button(file_frame, text="Submit", command=lambda: submit_file_name(option, file_entry.get()))
    submit_button.pack(side=tk.LEFT)

def submit_file_name(option, file_name):
    if option == "Open":
        messagebox.showinfo("Open File", f"Opening file: {file_name}")
    elif option == "New":
        messagebox.showinfo("New File", f"Creating new file: {file_name}")
    else:
        messagebox.showwarning("Error", "Invalid option selected.")

# Create the main window
root = tk.Tk()
root.title("File Options")

# Create a frame for the initial options
option_frame = tk.Frame(root)
option_frame.pack(pady=20)

# Create buttons for "Open" and "New"
open_button = tk.Button(option_frame, text="Open", command=lambda: on_option_select("Open"))
open_button.pack(side=tk.LEFT, padx=10)

new_button = tk.Button(option_frame, text="New", command=lambda: on_option_select("New"))
new_button.pack(side=tk.LEFT, padx=10)

# Start the Tkinter event loop
root.mainloop()

