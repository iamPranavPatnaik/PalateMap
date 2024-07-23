from gui import GUI
from evalFlavor import FlavorEvaluator
from dishSearch import DishSearcher
from tkinter import messagebox

class Main:
    def __init__(self):
        self.searcher = DishSearcher()
        self.evaluator = FlavorEvaluator()
        self.gui = GUI()

    def submitDish(self):
        userDish = self.gui.return_dish()
        if userDish:
            evaluator = FlavorEvaluator(userDish)
            recipe = self.searcher.returnRecipe(userDish)
            ingredients = self.searcher.returnIngredients(userDish)
            evaluation_result = evaluator.evaluateFlavor(recipe, ingredients)
            messagebox.showinfo("Flavor Evaluation Result", evaluation_result)
        else:
            messagebox.showwarning("Input Error", "Please enter a dish name.")

def startPalateMap():
    gui = GUI()
    gui.run()

startPalateMap()