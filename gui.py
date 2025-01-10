import tkinter as tk
from binary_tree import *
from tree_generator import *

root = tk.Tk()
user_input = ""

def open_textbox():
    global user_input

    label = tk.Label(root, text="Please enter file name:")
    label.pack(pady=5)

    textbox = tk.Text(root, height=5, width=20)
    textbox.pack(pady=20)

    def on_button_click():
        global user_input
        user_input = textbox.get("1.0", tk.END).strip()
        if user_input:
            print("User   Input:", user_input)
            textbox.delete("1.0", tk.END)
            read_file(user_input)
        else:
            print("No input provided. Please enter a valid file path.")

    enter_button = tk.Button(root, text="Enter", command=on_button_click)
    enter_button.pack(pady=5)

def run_gui():
    root.title("Language Evolution Simulator")
    root.geometry("400x300")
    label = tk.Label(root, text="Welcome to the Language Evolution Simulator!")
    label.pack(pady=5)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    new_button = tk.Button(text="Open", command=open_textbox)
    new_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()
