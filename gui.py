import tkinter as tk
from binary_tree import *
from tree_generator import *

root = tk.Tk()
user_input = ""
god = Node(1)  # This is just an easy way to keep track of the root node

def read_user_input(textbox):
    user_input = textbox.get("1.0", tk.END).strip()
    read_file(user_input, god)
    user_label = tk.Label(root, text=user_input)
    user_label.pack(pady=5)

def open_textbox():

    label = tk.Label(root, text="Please enter file name:")
    label.pack(pady=5)

    open_textbox = tk.Text(root, height=1, width=20)
    open_textbox.pack(pady=3)

    enter_button = tk.Button(root, text="Enter", command=lambda: read_user_input(open_textbox))
    enter_button.pack(pady=5)



def run_gui():
    root.title("Language Evolution Simulator")
    root.geometry("400x300")
    label = tk.Label(root, text="Welcome to the Language Evolution Simulator!")
    label.pack(pady=5)

    new_button = tk.Button(root, text="Open", command=open_textbox)
    new_button.pack(padx=10)

    root.mainloop()

# Start the GUI
run_gui()
