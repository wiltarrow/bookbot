def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    return contents

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()