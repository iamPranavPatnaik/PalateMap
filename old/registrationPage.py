# registerPage.py
import tkinter as tk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate('palatemapfirebase.json')
firebase_admin.initialize_app(cred)

class RegistrationPage:

    def __init__(self, on_register_success):
        self.root = tk.Tk()
        self.root.title("Register")
        self.on_register_success = on_register_success

        # Styling (fill out later)
        self.root.geometry("300x250")
        self.root.configure(bg="#f0f0f0")

        # Label and inputs for email and password (and confirming it)
        self.email_label = tk.Label(self.root, text="Email:")
        self.email_entry = tk.Entry(self.root)
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_entry = tk.Entry(self.root, show="*")
        self.confirm_password_label = tk.Label(self.root, text="Confirm Password:")
        self.confirm_password_entry = tk.Entry(self.root, show="*")
        self.register_button = tk.Button(self.root, text="Register", command=self.register)

        # Laying them on the screen (I love tkinter)
        self.email_label.pack(pady=5)
        self.email_entry.pack(pady=5)
        self.password_label.pack(pady=5)
        self.password_entry.pack(pady=5)
        self.confirm_password_label.pack(pady=5)
        self.confirm_password_entry.pack(pady=5)
        self.register_button.pack(pady=10)

    def register(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        if not email or not password:
            messagebox.showerror("Input Error", "Email and password are required.")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        try:
            user = auth.create_user(email=email, password=password)
            messagebox.showinfo("Success", "Registration successful! Please log in.")
            self.on_register_success()
        except firebase_admin.auth.EmailAlreadyExistsError:
            messagebox.showerror("Registration Error", "Email already in use.")
        except ValueError as ve:
            messagebox.showerror("Input Error", f"Invalid input: {str(ve)}")
        except Exception as e:
            messagebox.showerror("Registration Error", f"An error occurred: {str(e)}")

    def run(self):
        self.root.mainloop()
