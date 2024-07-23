import pandas as pd

class DishSearcher:
    def __init__(self, csvFilePath):
        # Load CSV file
        csvFilePath = r"C:\Users\prana\Downloads\foodrecipes.csv"
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
