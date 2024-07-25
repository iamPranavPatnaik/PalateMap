from openai import OpenAI
from dishSearch import DishSearcher
import os
from dotenv import load_dotenv
load_dotenv()

class FlavorEvaluator:
    def __init__(self):
        # Initialize the OpenAI client and DishSearcher here
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.searcher = DishSearcher(os.getenv("RECIPE_DATASET_PATH"))

    def evaluateFlavor(self, ingredients):
        completion = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are GPT-4-Turbo, a highly advanced flavor profiling assistant. 
                    Your primary function is to evaluate flavor profiles. 
                    For the categories grains, vegetables, dairy, meat, spiciness, sweetness rate this dish from 0-10 based on the ingredients. 
                    Ask the question: how much of these ingredients is, for example, "grain-dominated"? Or "dairy dominated"?
                    Rate the relevancy of each food category 0-10.
                    If aboslutely hidden from the recipe, put a 0. 
                    If it is absolutely the most dominant part of the dish, put a 10.
                    This will be a spectrum, so we recommend you rate these dishes fairly from 0-10, and not choose merely the ends out of easiness (0 or 10).
                    Be sensitive about the number, don't merely put 10 and call it a day.
                    If ingredients are unclear, make an educated guess and leave it as that. For instance, if your final scores are "0, 0, 0, 0, 0, 0" please leave a guess based on educated resources. Thank you.
                    IMPORTANT: NEVER leave a final score with primarily "0s." (ex: 0, 0, 0, 0, 0, 0). All dishes have some sort of variety, 0s merely decrease the proficiency of our program. Thank you. 
                    Format the answer as just 6 numbers, the score for each category, no other text,
                    """
                },
                {
                    "role": "user",
                    "content": "Ingredients: " + str(ingredients)
                }
            ]
        )
        
        response = completion.choices[0].message.content
        response_list = [int(x) for x in response.split(",")]
        return response_list
