import os


def get_luganda_norm():
    # Reads luganda normalization txt and convert to dictionary
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, "resources", "lug_norm.txt")
    norm_dict = {}
    with open(file_path, 'r', encoding='utf-8') as lug_file:
        for line in lug_file:
            line = line.strip()
            if not line:
                continue
            if ':' in line:
                key, value = line.split(':', 1)
                norm_dict[key.strip().lower()] = value.strip().lower()
    return norm_dict


def normalize_text(text, language):    
    # Replace local language terms with standard categories.
    if language == 'luganda':
        words = text.lower().split()
        normalized_words = [get_luganda_norm().get(word, word) for word in words]    
        return " ".join(normalized_words)
    else:
        return text