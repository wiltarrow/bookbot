def number_of_words(text):
    count = 0
    for words in text.split():
        count += 1
    return count

def number_of_char(text):
    chars = {}
    for i in text.lower():
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars