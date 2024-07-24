from gui import GUI
from evaluateFlavor import FlavorEvaluator
from dishSearch import DishSearcher
from tkinter import messagebox

class Main:
    def __init__(self):
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

def startPalateMap():
    main = Main() 
    main.gui.run()  # Run the GUI loop

startPalateMap()
