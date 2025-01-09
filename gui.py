import tkinter as tk

def run_gui(write_file_func, edit_file_func, read_file_func):
    # Create the main window
    root = tk.Tk()
    root.title("Language Evolution Simulator")

    # Set the default size of the window
    root.geometry("400x300")  # Width x Height

    # Create a label with a welcome message
    label = tk.Label(root, text="Welcome to the Language Evolution Simulator!")
    label.pack(pady=5)  # Add some vertical padding

    # Create a frame to hold the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)  # Add some vertical padding for the button frame

    # Create buttons for New, Edit, and Open
    new_button = tk.Button(button_frame, text="New", command=lambda: (write_file_func(), root.quit()))
    new_button.pack(side=tk.LEFT, padx=10)  # Pack the button to the left with padding

    edit_button = tk.Button(button_frame, text="Edit", command=lambda: (edit_file_func(), root.quit()))
    edit_button.pack(side=tk.LEFT, padx=10)  # Pack the button to the left with padding

    open_button = tk.Button(button_frame, text="Open", command=lambda: (read_file_func(), root.quit()))
    open_button.pack(side=tk.LEFT, padx=10)  # Pack the button to the left with padding

    # Start the Tkinter event loop
    root.mainloop()
