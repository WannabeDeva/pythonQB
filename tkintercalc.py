import tkinter as tk
from math import *

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to insert character in entry field
def insert_character(character):
    entry.insert(tk.END, character)

# Create a Tkinter window
window = tk.Tk()
window.title("Scientific Calculator")

# Entry field to display expression and result
entry = tk.Entry(window, font=('Arial', 14), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for numerical and mathematical operations
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('(', ')', 'sin', 'cos'),
    ('tan', 'log', 'sqrt', 'clear')
]

# Function to handle button click
def button_click(symbol):
    if symbol == '=':
        evaluate_expression()
    elif symbol == 'clear':
        entry.delete(0, tk.END)
    else:
        insert_character(symbol)

# Create buttons
for i, row in enumerate(buttons):
    for j, symbol in enumerate(row):
        btn = tk.Button(window, text=symbol, font=('Arial', 12), padx=10, pady=10, 
                        command=lambda symbol=symbol: button_click(symbol))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

# Run the Tkinter event loop
window.mainloop()
