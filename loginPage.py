import tkinter as tk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials, auth

class LoginPage:

    def __init__(self, on_login_success, on_register):
        self.root = tk.Tk()
        self.root.title("Login")
        self.on_login_success = on_login_success
        self.on_register = on_register

        # Quick lil styling (add more)
        self.root.geometry('300x200')
        self.root.configure(bg="#f0f0f0")

        # Label and inputs for email and password
        self.email_label = tk.Label(self.root, text="Email:")
        self.email_entry = tk.Entry(self.root)
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_entry = tk.Entry(self.root, show="*")
        self.login_button = tk.Button(self.root, text="Login", command=self.authenticate)
        self.register_button = tk.Button(self.root, text="Register", command=self.register)

        # Needed to make sure elements show up?!
        self.email_label.pack()
        self.email_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()
        self.register_button.pack()

    # Function to authenticate login
    def authenticate(self):
        email = self.email_entry.get()
        try:
            if not email:
                raise ValueError("Email is required.")
            
            user = auth.get_user_by_email(email)
            self.on_login_success(user.uid)
        
        except ValueError as ve:
            # Handle specific errors, such as missing email or invalid format
            messagebox.showerror("Input Error", f"Invalid input: {str(ve)}")
        
        except firebase_admin._auth_utils.UserNotFoundError:
            # Handle the case where the user is not found
            messagebox.showerror("Login Error", "No user record found for the provided email.")
        
        except Exception as e:
            # Handle any other exceptions that may occur
            messagebox.showerror("Login Error", f"An error occurred: {str(e)}")

    def register(self):
        self.root.destroy()
        self.on_register()

    def run(self):
        self.root.mainloop()
