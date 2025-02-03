import tkinter as tk
import subprocess
from tkinter import ttk
from binary_tree import *
from tree_generator import *
import os

root = tk.Tk() 
user_input = "" 
god = Node(4)  
current_file = ""  

def clear_menu(): #this will completely clear the GUI menu
    for widget in root.winfo_children():
        widget.destroy()


def get_selection(box_name):

    selected_option = box_name.get()  # Get the selected option

    if selected_option != "":
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(script_directory, 'test') + "\\" + selected_option
        display_tree(file_name)

def edit_in_notepad(box_name):
    selected_option = box_name.get()  # Get the selected option

    if selected_option != "":
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(script_directory, 'test') + "\\" + selected_option
        
        subprocess.run(['notepad.exe', file_name])


def new_in_notepad(local_file_name):
    local_file_name = local_file_name.strip()

    if local_file_name != "":
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(script_directory, 'test', local_file_name)

        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        
        with open(file_name, 'w') as f:
            pass  # Create an empty file
        
        subprocess.run(['notepad.exe', file_name])



def destroy_labels():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):  # Check if the widget is a Label
            widget.destroy() 

def open_textbox():
    display_files()

    label = tk.Label(root, text="Please enter file name:")
    label.pack(pady=5)

    open_textbox = tk.Text(root, height=1, width=20)
    open_textbox.pack(pady=3)

    enter_button = tk.Button(root, text="Enter", command=lambda: display_tree(open_textbox.get("1.0", tk.END).strip()))
    enter_button.pack(pady=5)


def display_node_information(node_name, nodes_list, file_name):
    if node_name != "":
        clear_menu()
        back_button = tk.Button(root, text="Back", command=lambda:display_tree(file_name))
        back_button.pack(pady = 3)

        for nodes in nodes_list:
            print(nodes.id_value, node_name.replace(" ", ""))
            if nodes.id_value == int(node_name.replace(" ", "")):
                print("MATCH!")
                user_label = tk.Label(root, text=("ID value: " + str(nodes.id_value))) 
                user_label.pack(pady=0)
                user_label = tk.Label(root, text=("Left: " + str(nodes.left))) 
                user_label.pack(pady=0)            
                user_label = tk.Label(root, text=("Right: " + str(nodes.right))) 
                user_label.pack(pady=0)
                user_label = tk.Label(root, text=("Time: " + str(nodes.time))) 
                user_label.pack(pady=0)   



def display_tree(file_name): #Display Tree
    clear_menu()

    god = read_file(file_name) 
    output = display(god) 
    nodes_list = get_all_nodes(god)
    nodes_list.append(god)
    names_list = [] 

    for nodes in nodes_list:
        names_list.append(nodes.id_value)
        print(nodes.id_value)


    combobox = ttk.Combobox(root, values=names_list)
    combobox.place(x = 40)

    combo_button = tk.Button(root, text="View Node", command=lambda: display_node_information(combobox.get(), nodes_list, file_name))
    combo_button.place(x = 210)

    back_button = tk.Button(root, text = "Back", command=lambda: display_files())
    back_button.place(x = 300)

    user_label = tk.Label(root)
    user_label.pack(pady= 10)
    for element in output: 
        user_label = tk.Label(root, text=element, font=('Courier New', 10)) 
        user_label.pack(pady=0) 

    
def display_files():
    clear_menu()
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print(script_directory)
    
    directory = os.path.join(script_directory, 'test')
    print(directory)
    
    contents = os.listdir(directory)  
   
    combobox = ttk.Combobox(root, values=contents)
    combobox.place(x=40)

    combo_button = tk.Button(root, text="View", command=lambda: get_selection(combobox))
    combo_button.place(x = 215)
    back_button = tk.Button(root, text="Back", command=lambda: display_main_menu())
    back_button.place(x = 300)



def display_edit_menu():
    clear_menu()
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print(script_directory)
    
    directory = os.path.join(script_directory, 'test')
    print(directory)
    
    contents = os.listdir(directory)  
   
    combobox = ttk.Combobox(root, values=contents)
    combobox.place(x=40)

    combo_button = tk.Button(root, text="Open", command=lambda: edit_in_notepad(combobox))
    combo_button.place(x = 215)

    back_button = tk.Button(root, text="Back", command=lambda: display_main_menu())
    back_button.place(x = 300)

def display_new_menu():
    clear_menu()
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print(script_directory)
    
    directory = os.path.join(script_directory, 'test')
    print(directory)
    
    contents = os.listdir(directory)  
   
    textbox = tk.Text(root, height = 1, width = 15)
    textbox.place(x=40)

    open_button = tk.Button(root, text="Create file", command=lambda: new_in_notepad(textbox.get("1.0", tk.END)))
    open_button.place(x = 215)

    back_button = tk.Button(root, text="Back", command=lambda: display_main_menu())
    back_button.place(x = 300)


def display_main_menu():
    clear_menu()
    root.title("Language Evolution Simulator")
    root.geometry("400x400")
    label = tk.Label(root, text="Welcome to the Language Evolution Simulator!")
    label.pack(pady=5)
    open_button = tk.Button(root, text="Open", command=lambda: display_files())
    open_button.place(x=75, y=25)
    new_button = tk.Button(root, text="New", command=lambda: display_new_menu())
    new_button.place(x=175, y=25)
    edit_button = tk.Button(root, text="Edit", command=lambda: display_edit_menu())
    edit_button.place(x=275, y=25)
   


def run_gui():
    display_main_menu()
    root.mainloop()


