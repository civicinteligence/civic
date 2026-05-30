#  Language Detection Module
# Detects if text is English, Luganda, or Other
import re

class LanguageDetector:
    
    def __init__(self):
        self.luganda_words = [
            'amazzi', 'mazzi',           # water
            'webale',                    # thank you
            'ssebo', 'nyabo',            # sir, madam
            'kale', 'kati',              # okay, now
            'nnyo', 'ddala',             # very, truly
            'bubi',                      # bad
            'kizibu',                    # problem
            'kawempe', 'nakawa',         # places in Kampala
            'enguudo',                   # roads
            'ensimbi',                   # money
            'awaka',                     # home
            'omuntu', 'abantu',          # person, people
            'budde',                     # time
            'kabisa',                    # completely
            'kutata',                    # trouble
            'kosa',                      # wrong
            'kasasiro',                  # garbage
            'matope',                    # mud
            'mayembe',                   # potholes
            'akawuka',                   # disease
            'kansi',                     # cholera
            'kayoola',                   # bus/taxi
            'ola', 'oli', 'mutya',       # greetings
            'lwaki',                     # why
            'kiki',                      # what
            'ani',                       # who
        ]
        
        self.english_words = [
            'the', 'and', 'for', 'are', 'but', 'not', 'you',
            'have', 'this', 'that', 'from', 'they', 'will',
            'what', 'there', 'please', 'help', 'water',
            'road', 'health', 'garbage', 'problem', 'issue',
            'urgent', 'emergency', 'broken', 'fix', 'repair'
        ]
    
    def detect(self, text):
        '''
        Detect language of input text
        
        Returns:
            language: 'English', 'Luganda', or 'Other'
        '''
        if not text or len(text.strip()) == 0:
            return "Other"
        
        text_lower = text.lower()
        
        luganda_count = 0
        for word in self.luganda_words:
            if word in text_lower:
                luganda_count += 1
        
        english_count = 0
        for word in self.english_words:
            if word in text_lower:
                english_count += 1
        
        # Decision logic
        if luganda_count > english_count and luganda_count >= 1:
            return "Luganda"
        elif english_count > luganda_count and english_count >= 1:
            return "English"
        elif luganda_count >= 1 and english_count >= 1:
            # Mixed
            return "Luganda" if luganda_count >= english_count else "English"
        else:
            return "Other"

# FUNCTION FOR OTHER TEAMS TO USE
def detect_language(text):
    detector = LanguageDetector()
    return detector.detect(text)

# USER INTERACTION
if __name__ == "__main__":
    print("LANGUAGE DETECTION MODULE")
    
    detector = LanguageDetector()
    
    print("\nEnter text to detect language (or 'quit' to exit)")
    
    while True:
        user_text = input("\nEnter text: ")
        
        if user_text.lower() == 'quit':
            print("\nend")
            break
        
        # Detect language
        result = detector.detect(user_text)
        
        # Show result
        if result == "English":
            print(f"\n{result}")
        elif result == "Luganda":
            print(f"\n{result}")
        else:
            print(f"\n{result}")
