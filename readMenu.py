from openai import OpenAI
from ocrMenu import OCRMenu
import os
from dotenv import load_dotenv
load_dotenv()

class ReadMenu:
    def __init__(self):
        # Initialize the OpenAI client and DishSearcher here
        self.ocr = OCRMenu(api_key=os.getenv("OCR_API_KEY"))
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def parseMenu(self, menu_file):
        ocr = OCRMenu(api_key=os.getenv("OCR_API_KEY"))
        menu_text = ocr.parse_menu_file(menu_file)
        completion = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are GPT-4-Turbo, a highly advanced 3D modeling assistant. 
                    Your primary function is to parse through menus, output only titles of dishes
                    Ignore all other text, only focus on the dishes. No other text in the output please.
                    Output should be comma separated, titles of dishes.
                    """
                },
                {
                    "role": "user",
                    "content": menu_text
                }
            ]
        )
        
        response = completion.choices[0].message.content
        return response

if __name__ == "__main__":
    menuEvaluator = ReadMenu()
    menuEvaluator.parseMenu("C:/Users/prana/Downloads/menuexample.png")

