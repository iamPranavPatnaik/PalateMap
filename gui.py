import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self, submit_callback):
        self.root = tk.Tk()
        self.root.title("PalateMap")
        self.root.geometry("400x200")
        self.user_input = None

        # Set the callback function
        self.submit_callback = submit_callback

        label = tk.Label(self.root, text="Enter your preference:")
        label.pack(pady=10)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        submit_button = tk.Button(self.root, text="Submit", command=self.return_dish)
        submit_button.pack(pady=10)

    def return_dish(self):
        self.user_input = self.entry.get()
        if self.submit_callback:
            self.submit_callback()  # Call the callback function

    def get_dish(self):
        return self.user_input

    def run(self):
        self.root.mainloop()
