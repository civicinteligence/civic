from langdetect import detect
from .text_cleaner import clean_text
import re
import os


#luganda
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "resources", "luganda.txt")
luganda = open(file_path, "r")
luganda_words = clean_text(luganda.read()).split()


def detect_language(text):
    text = text.lower()
    try:
        language = detect(text)
        if language == "en":
            return "english"
        for word in luganda_words:
            if word in text:
                return "luganda"
        return "unknown"
    except:
        return "unknown"