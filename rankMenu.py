# Given 8-dimensional vectors and a user vector, rank which ones are closest based on distance and output a list of dishes
import math
from readMenu import ReadMenu
from evaluateMenu import MenuEvaluator 

class RankMenu:
    def findDistance(self, userVector, menuVector):
        difference_list = list()
        for i in range(len(userVector)):
            difference = (userVector[i] - menuVector[i])**2
            difference_list.append(difference)
        
        # Find distance
        distance = math.sqrt(sum(difference_list))
        print(menuVector)
        return distance

    def rankMenu(self, userVector, menuDict):
        dishDistance = {}
        for dish, dishVector in menuDict.items():
            distance = self.findDistance(userVector, dishVector)
            dishDistance[dish] = distance

        rankedMenu = sorted(dishDistance.items(), key=lambda item: item[1])
        rankedDishes = [dish for dish, distance in rankedMenu]
        return rankedMenu

if __name__ == "__main__":
    eval_menu = MenuEvaluator()
    dish_dict = eval_menu.evaluate_menu(r"C:\Users\prana\Downloads\menuexample.png") # List of all dish vectors

    # user_menu = dish_dict.keys()
    # dish_vectors = dish_dict.values()
    
    menuRanker = RankMenu()
    user_vector = [3, 4, 6, 2, 8, 9]
    desert_vector = [8,2,8,0,10,3]

    menuRanker.rankMenu(desert_vector, dish_dict)
    menuRanker.rankMenu(user_vector, dish_dict)
