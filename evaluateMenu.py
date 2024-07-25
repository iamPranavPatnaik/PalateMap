from evaluateFlavor import FlavorEvaluator
from readMenu import ReadMenu
import os
from dotenv import load_dotenv
load_dotenv()

class MenuEvaluator:
    def __init__(self):
        pass

    def evaluate_menu(self, menu):
        dish_vectors = []
        readMenu = ReadMenu()
        user_menu = readMenu.parseMenu(menu)
        evalFlavor = FlavorEvaluator()
        for dish in user_menu:
            dish_vector = evalFlavor.evaluateFlavor(dish)
            dish_vectors.append(dish_vector)

        return dish_vectors

if __name__ == "__main__":
    menu_eval = MenuEvaluator()
    menu_eval.evaluate_menu("C:/Users/prana/Downloads/menuexample.png")

