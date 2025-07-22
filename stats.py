import string

def get_word_count(filepath):
    with open(filepath, 'r') as file:
        contents = file.read()
        words = contents.split()
        return len(words)

def get_character_count(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in string.ascii_lowercase or char in "æâêëô":  # only count these letters
            char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts

def sort_on(item):
    return item["num"]

