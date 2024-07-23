from openai import OpenAI
from dishSearch import DishSearcher

class FlavorEvaluator:
    def __init__(self):
        # Initialize the OpenAI client and DishSearcher here
        self.client = OpenAI()
        self.searcher = DishSearcher("C:/Users/prana/Downloads/foodrecipes.csv")

    def evaluateFlavor(self, ingredients, recipe):
        completion = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are GPT-4-Turbo, a highly advanced 3D modeling assistant. 
                    Your primary function is to evaluate flavor profiles. 
                    For the categories grains, vegetables, dairy, meat, spiciness, rate this dish from 0-10 based on the ingredients and recipe. 
                    Format the answer as just 5 numbers, the score for each category, no other text,
                    """
                },
                {
                    "role": "user",
                    "content": "Ingredients: " + str(ingredients) + "\nRecipe:\n" + str(recipe)
                }
            ]
        )
        
        response = completion.choices[0].message.content
        return response
