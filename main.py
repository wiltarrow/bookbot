from stats import number_of_words
from stats import number_of_char
from stats import sort_chars
import sys

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = number_of_words(text)
    char_list = number_of_char(text)
    sorted_list = sort_chars(char_list)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for pair in sorted_list:
        if pair["char"].isalpha():
            c = pair["char"]
            n = pair["num"]
            print(f"{c}: {n}")

main()