import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password are correct
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create a Tkinter window
window = tk.Tk()
window.title("Login Form")

# Username label and entry
username_label = tk.Label(window, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password label and entry
password_label = tk.Label(window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Login button
login_button = tk.Button(window, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
