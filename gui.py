import tkinter as tk
from tkinter import messagebox

# Function to display a message with the entered value
def display_value():
    user_input = entry.get()
    messagebox.showinfo("Entered Value", f"You entered: {user_input}")

# Create the main window
root = tk.Tk()
root.title("PalateMap")

# Set the window size
root.geometry("400x200")

# Add a label for the entry box
label = tk.Label(root, text="Enter your preference:")
label.pack(pady=10)

# Add an entry box
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Add a button to submit the entry
submit_button = tk.Button(root, text="Submit", command=display_value)
submit_button.pack(pady=10)

# Run the application
root.mainloop()
