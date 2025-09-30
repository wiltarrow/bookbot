from stats import number_of_words

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    return contents

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = number_of_words(text)
    print(f"Found {num_words} total words")

main()