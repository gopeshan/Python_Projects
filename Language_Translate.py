from googletrans import Translator

class LanguageTranslator:
    def __init__(self):
        self.translator = Translator()
        self.languages = {
            "en": "English",
            "es": "Spanish",
            "zh": "Chinese",
            "hi": "Hindi",
            "ar": "Arabic",
            "fr": "French",
            "ru": "Russian",
            "ja": "Japanese",
            "de": "German",
            "ko": "Korean",
            "pt": "Portuguese",
            "it": "Italian",
            "tr": "Turkish",
            "nl": "Dutch",
            "vi": "Vietnamese"
        }
        
    def display_language_options(self):
        print("Code : Language")
        for code, language in self.languages.items():
            print(f"{code} => {language}")
        print()

    def get_user_language(self):
        while True:
            user_code = input(
                "Please input the desired language code. To see the language code list, enter 'options':\n")

            if user_code == "options":
                self.display_language_options()
            elif user_code in self.languages:
                print(f"You have selected {self.languages[user_code]}")
                return user_code
            else:
                print("It's not a valid language code!")
