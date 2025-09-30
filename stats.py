def number_of_words(text):
    count = 0
    for words in text.split():
        count += 1
    return count
