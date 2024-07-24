from gui import GUI
from evaluateFlavor import FlavorEvaluator
from dishSearch import DishSearcher
from tkinter import messagebox
from loginPage import LoginPage
from registrationPage import RegistrationPage

class Main:
    def __init__(self, user_id):
        self.user_id = user_id
        self.searcher = DishSearcher()
        # Pass the submitDish method as a callback
        self.gui = GUI(self.submitDish)
        self.evaluator = FlavorEvaluator()

    def submitDish(self):
        userDish = self.gui.get_dish()
        if userDish:
            print(userDish)
            ingredients = self.searcher.returnIngredients(userDish)
            evaluation_result = self.evaluator.evaluateFlavor(ingredients)
            messagebox.showinfo("Flavor Evaluation Result", evaluation_result)
        else:
            messagebox.showwarning("Input Error", "Please enter a dish name.")

def startPalateMap(user_id):
    main = Main(user_id) 
    main.gui.run()  # Run the GUI loop

def onLoginSuccess(user_id):
    # Destroy login window and start the main application
    login_page.root.destroy()
    startPalateMap(user_id)

def showRegistrationPage():
    def on_register_success():
        register_page.root.destroy()
        startLoginPage()

    register_page = RegistrationPage(on_register_success)
    register_page.run()

def startLoginPage():
    global login_page
    login_page = LoginPage(onLoginSuccess, showRegistrationPage)
    login_page.run()

if __name__ == "__main__":
    startLoginPage() # Basically just call it when its started