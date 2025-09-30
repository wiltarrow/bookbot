def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    return contents

def number_of_words(text):
    count = 0
    for words in text.split():
        count += 1
    return count

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = number_of_words(text)
    print(f"Found {num_words} total words")

main()