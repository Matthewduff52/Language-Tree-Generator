import tkinter as tk
from binary_tree import *
from tree_generator import *

root = tk.Tk() #The root is the main menu of the GUI, so anytime you do a button, textbox, label, etc... you want to put root into its paremeters.
user_input = "" #Global variable for user input into textboxes
god = Node(1)  # This is just an easy way to keep track of the root node

def read_user_input(textbox):
    user_input = textbox.get("1.0", tk.END).strip() #This grabs the user input from the textbox
    read_file(user_input, god) #*IMPORTANT* you will need to type "close" into the console to continue to the next steps in the GUI menu.
    output = display(god) #This should be your display_chart list from your display function in binary tree.
    
    #KEEP IN MIND: I changed your display function to return the display_chart, thats why this should work.

    for element in output: #This aims to output the display chart into the menu identical to your console output.
        user_label = tk.Label(root, text=element) #This is how you output text to the GUI menu.
        user_label.pack(pady=2) #This just defines how much verticle room should be between each output line
        
    #if you can help trouble shoot being able to display this that would be awesome! 
    #Thanks!
        
    
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
