import tkinter as tk
from tkinter import ttk
from binary_tree import *
from tree_generator import *
import os

root = tk.Tk() 
user_input = "" 
god = Node(4)  
current_file = ""  

def display_node_information(x, nodes_list):
    node_name = x.get()

    for nodes in nodes_list:
        print(nodes.id_value, node_name.replace(" ", ""))
        if nodes.id_value == int(node_name.replace(" ", "")):
            print("MATCH!")
            user_label = tk.Label(root, text=nodes.id_value, font=('Courier New', 10)) 
            user_label.pack(pady=0)
            user_label = tk.Label(root, text=nodes.left, font=('Courier New', 10)) 
            user_label.pack(pady=0)            
            user_label = tk.Label(root, text=nodes.right, font=('Courier New', 10)) 
            user_label.pack(pady=0)  

def get_selection(box_name):
    selected_option = box_name.get()  # Get the selected option

    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_directory, 'test') + "\\" + selected_option
    
    read_user_input(file_name)

def destroy_labels():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):  # Check if the widget is a Label
            widget.destroy() 

def read_user_input(file_name):
    
    god = read_file(file_name) 
    output = display(god) 

    destroy_labels()

    for element in output: 
        user_label = tk.Label(root, text=element, font=('Courier New', 10)) 
        user_label.pack(pady=0) 

    nodes_list = get_all_nodes(god)
    names_list = [] 
    for nodes in nodes_list:
        names_list.append(nodes.id_value)
        print(nodes.id_value)

    combobox = ttk.Combobox(root, values=names_list)
    combobox.pack(pady=10)

    combo_button = tk.Button(root, text="View2", command=lambda: display_node_information(combobox, nodes_list))
    combo_button.pack(padx=10)

   

def display_files():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print(script_directory)
    
    directory = os.path.join(script_directory, 'test')
    print(directory)
    
    contents = os.listdir(directory)  
   
    combobox = ttk.Combobox(root, values=contents)
    combobox.pack(pady=10)

    combo_button = tk.Button(root, text="View", command=lambda: get_selection(combobox))
    combo_button.pack(pady=10)

def open_textbox():
    display_files()

    label = tk.Label(root, text="Please enter file name:")
    label.pack(pady=5)

    open_textbox = tk.Text(root, height=1, width=20)
    open_textbox.pack(pady=3)

    enter_button = tk.Button(root, text="Enter", command=lambda: read_user_input(open_textbox.get("1.0", tk.END).strip()))
    enter_button.pack(pady=5)

def run_gui():
    root.title("Language Evolution Simulator")
    root.geometry("400x400")
    label = tk.Label(root, text="Welcome to the Language Evolution Simulator!")
    label.pack(pady=5)

    new_button = tk.Button(root, text="Open", command=lambda: [display_files(), new_button.destroy()])
    new_button.pack(padx=10)

    root.mainloop()


