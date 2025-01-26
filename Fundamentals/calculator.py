# Write a Python program that implements a basic calculator using GUI libraries like Tkinter or PyQt.

import tkinter as tk
from tkinter import messagebox

def evaluate_expression():
    try:
        result = eval(entry.get())  # Evaluate the math expression entered in the input field.
        result_label.config(text=f"Result: {result}")  # Display the result in the label.
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")  # Show error if the expression is invalid.


root = tk.Tk()  # Create the main window.
root.title("Basic Calculator")  # Set the title of the window.
root.geometry("300x200")  # Set the size of the window (300x200 pixels).


entry = tk.Entry(root, width=20, font=("Arial", 14))  # Create an input field for user input.
entry.pack(pady=10)  # Add padding around the input field.


# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=evaluate_expression, font=("Arial", 12))
calculate_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
