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

    def parse_menu_file(self, menu_file):
        url = "https://api.ocr.space/parse/image"
        headers = {"apikey": self.api_key}  # Replace with your actual API key

        with open(menu_file, 'rb') as file:
            response = requests.post(url, headers=headers, files={'file': file})
        
        response_json = response.json()
        
        # Check for 'ParsedResults' in the response
        if 'ParsedResults' in response_json:
            parsed_results = response_json['ParsedResults']
            if parsed_results:
                return parsed_results[0].get("ParsedText", "No text found")
            else:
                return "No parsed results found"
        else:
            return "OCR response does not contain 'ParsedResults' key"


if __name__ == "__main__":
    ocr = OCRMenu(api_key=os.getenv("OCR_API_KEY"))
    menu_text = ocr.parse_menu_file(filename=r"C:\Users\prana\Downloads\menuexample.png")
    print(menu_text)
