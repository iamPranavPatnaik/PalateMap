import requests
import os
import json
from dotenv import load_dotenv
import requests
import json
load_dotenv()

class OCRMenu:
    def __init__(self, api_key=None):
        # Load CSV file
        api_key = os.getenv("OCR_API_KEY")
        self.api_key = api_key

    def ocr_space_file(self, filename, overlay=False, language='eng'):
        """ OCR.space API request with local file.
        :param filename: Your file path & name.
        :param overlay: Is OCR.space overlay required in your response. Defaults to False.
        :param language: Language code to be used in OCR. Defaults to 'eng'.
        :return: Result in JSON format.
        """
        payload = {
            'isOverlayRequired': overlay,
            'apikey': self.api_key,
            'language': language,
        }
        with open(filename, 'rb') as f:
            r = requests.post('https://api.ocr.space/parse/image', files={filename: f}, data=payload)
        return r.content.decode()

    def parse_menu_file(self, filename):
        """ Parse the menu file and return the parsed text.
        :param filename: Your file path & name.
        :return: Parsed text from the image.
        """
        response = self.ocr_space_file(filename, language='eng')
        response_json = json.loads(response)
        return response_json["ParsedResults"][0]["ParsedText"]

if __name__ == "__main__":
    ocr = OCRMenu(api_key=os.getenv("OCR_API_KEY"))
    menu_text = ocr.parse_menu_file(filename=r"C:\Users\prana\Downloads\menuexample.png")
    print(menu_text)
