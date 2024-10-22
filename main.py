import tkinter as tk
from tkinter import messagebox
import string
import random

# Function to generate the password
def generate_password():
    length = length_var.get()
    if length == 0:
        messagebox.showwarning("Input Error", "Please select a password length!")
        return
    
    characters = ""
    
    if letters_var.get():
        if uppercase_var.get():
            characters += string.ascii_uppercase
        if lowercase_var.get():
            characters += string.ascii_lowercase
    if digits_var.get():
        characters += string.digits
    if special_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Input Error", "Please select at least one character type!")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=password)

# Function to copy the password to clipboard
def copy_to_clipboard():
    password = result_label.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Copy Error", "No password to copy!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

# Frame for inputs
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=20)

# Length of password
tk.Label(frame, text="Password Length:").grid(row=0, column=0, padx=5, pady=5)
length_var = tk.IntVar(value=8)
length_spinbox = tk.Spinbox(frame, from_=4, to_=32, textvariable=length_var)
length_spinbox.grid(row=0, column=1, padx=5, pady=5)

# Include letters
letters_var = tk.BooleanVar(value=True)
tk.Checkbutton(frame, text="Include Letters", variable=letters_var).grid(row=1, column=0, padx=5, pady=5)

# Uppercase letters
uppercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(frame, text="Uppercase", variable=uppercase_var).grid(row=1, column=1, padx=5, pady=5)

# Lowercase letters
lowercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(frame, text="Lowercase", variable=lowercase_var).grid(row=2, column=1, padx=5, pady=5)

# Include digits
digits_var = tk.BooleanVar(value=True)
tk.Checkbutton(frame, text="Include Digits", variable=digits_var).grid(row=2, column=0, padx=5, pady=5)

# Include special characters
special_var = tk.BooleanVar(value=False)
tk.Checkbutton(frame, text="Include Special Characters", variable=special_var).grid(row=3, column=0, padx=5, pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
result_label.pack(pady=10)

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

root.mainloop()
