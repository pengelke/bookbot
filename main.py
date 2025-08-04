import os
import sys

# Add current directory to sys.path to ensure module import
sys.path.append(os.getcwd())

try:
    from stats import get_book_text, count_words, count_characters, sort_characters
    print(f"Successfully imported from stats.py in {os.getcwd()}")
except ImportError as e:
    print(f"Error: Could not import from stats.py - {str(e)}. Ensure stats.py exists and is named correctly.")
    exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    
    if isinstance(book_text, str) and "Error" in book_text:
        print(book_text)
    else:
        num_words = count_words(book_text)
        char_counts = count_characters(book_text)
        sorted_chars = sort_characters(char_counts)
        
        print("---------- BOOKBOT ----------")
        print(f"Analyzing book found at {book_path} ...")
        print("---------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("---------- Character Count ----------")
        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")
        print("---------- END ----------")

if __name__ == "__main__":
    main()