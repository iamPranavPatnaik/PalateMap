# Given 8-dimensional vectors and a user vector, rank which ones are closest based on distance and output a list of dishes
import math
from readMenu import ReadMenu
from evaluateMenu import MenuEvaluator 

class RankMenu:
    def __init__(self):
        pass

    def findDistance(self, userVector, menuVector):
        difference_list = list()
        print(type(menuVector))
        # Find component difference
        for i in range(len(userVector)):
            difference = userVector[i] - menuVector[i]
            difference_list.append(difference)
        
        # Find distance
        sum = 0
        for j in difference_list:
            sum += j**2
        
        distance = math.sqrt(sum) 
        return distance

    def rankMenu(self, userVector, menuDict):
        dishDistance = {}
        for dish, dishVector in menuDict.items():
            distance = self.findDistance(userVector, dishVector)
            dishDistance[dish] = distance

        rankedMenu = sorted(dishDistance)
        return rankedMenu

if __name__ == "__main__":
    eval_menu = MenuEvaluator()
    dish_dict = eval_menu.evaluate_menu(r"C:\Users\prana\Downloads\menuexample.png") # List of all dish vectors

    # user_menu = dish_dict.keys()
    # dish_vectors = dish_dict.values()
    
    menuRanker = RankMenu()
    user_vector = [3, 4, 6, 2, 8, 9]
    menuRanker.rankMenu(user_vector, dish_dict)
