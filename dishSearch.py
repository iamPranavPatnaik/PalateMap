import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

class DishSearcher:
    def __init__(self, csvFilePath=None):
        # Load CSV file
        csvFilePath = os.getenv("RECIPE_DATASET_PATH")
        self.csvFilePath = csvFilePath

    # Returns ingredients
    def returnIngredients(self, dishTitle):
        # Read CSV
        df = pd.read_csv(self.csvFilePath)
        ingredients = df[df['Title'] == dishTitle][['Ingredients']]
        return ingredients.values.tolist()

    # Returns recipe instructions
    def returnRecipe(self, dishTitle):
        # Read CSV
        df = pd.read_csv(self.csvFilePath)
        ingredients = df[df['Title'] == dishTitle][['Instructions']]
        return ingredients.values.tolist()
