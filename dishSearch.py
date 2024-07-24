import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

import requests


class DishSearcher:
    def __init__(self, csvFilePath=None):
        # Load CSV file
        csvFilePath = os.getenv("RECIPE_DATASET_PATH")
        self.csvFilePath = csvFilePath
    
    def extract_top_ingredients(self, data):
        # Extract the ingredients from the top recipe
        if data['hits']:
            top_recipe = data['hits'][0]['recipe']
            if 'ingredientLines' in top_recipe:
                return top_recipe['ingredientLines']
        return []

    # Returns ingredients
    def returnIngredients(self, query):
        r = requests.get('https://api.edamam.com/api/recipes/v2?type=public&q=' + query + '&app_id=f1431fdd&app_key=26d9a654405a30b4a18ddb36216b1046')

        # Parse the JSON response
        parsed = r.json()
        top_ingredients = self.extract_top_ingredients(parsed)
        return top_ingredients

    # Returns recipe instructions
    def returnRecipe(self, dishTitle):
        # Read CSV
        df = pd.read_csv(self.csvFilePath)
        ingredients = df[df['Title'] == dishTitle][['Instructions']]
        return ingredients.values.tolist()
