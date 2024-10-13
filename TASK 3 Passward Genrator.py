import random #random library
import string #string library
import tkinter as tk #using tkinter interface
from tkinter import messagebox 

# Function to generate a password
def generate_password():
    try:
        length = int(length_entry.get())  # Get the password length from user input
        if length < 4:
            messagebox.showwarning("Input Error", "Password length should be at least 4.")
            return

        # Define the character set
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number for password length.")

# Function to clear the password
def clear_password():
    password_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)

# Set up the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("900x500")

# Label and entry for password length
tk.Label(window, text="Enter the desired password length:").pack(pady=10)
length_entry = tk.Entry(window, width=20)
length_entry.pack(pady=5)

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", width=20, command=generate_password)
generate_button.pack(pady=10)

# Entry to display the generated password
password_entry = tk.Entry(window, width=50, font=('Arial', 12))
password_entry.pack(pady=5)

# Button to clear the password
clear_button = tk.Button(window, text="Clear", width=20, command=clear_password)
clear_button.pack(pady=10)

# Start the main event loop
window.mainloop()
