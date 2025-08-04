def get_book_text(path):
    try:
        with open(path, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{path}' not found."
    except Exception as e:
        return f"Error: {str(e)}"

def count_words(text):
    return len(text.split()) if isinstance(text, str) else 0

def count_characters(text):
    if not isinstance(text, str):
        return {}
    char_count = {}
    for char in text:
        char_lower = char.lower()
        char_count[char_lower] = char_count.get(char_lower, 0) + 1
    return char_count

def sort_characters(char_counts):
    if not isinstance(char_counts, dict):
        return []
    sorted_list = [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list