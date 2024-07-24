import requests

class IngredientExtract:
    def extract_top_ingredients(data):
        # Extract the ingredients from the top recipe
        if data['hits']:
            top_recipe = data['hits'][0]['recipe']
            if 'ingredientLines' in top_recipe:
                return top_recipe['ingredientLines']
        return []
