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
