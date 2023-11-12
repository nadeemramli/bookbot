def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    printing = printing_out(chars_dict)

    print (f"{num_words} words found in the document")

    for wording in printing:
        printing_it = print (f"The '{wording[0]}' character was found {wording[1]} times")
        
    print ("---End report---")

def get_book_text(path):
    with open(path) as reading:
        return reading.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def printing_out(chars_dict):
    list_transformation = list(chars_dict.items())
    list_transformation.sort()

    clean_list = []

    for word in list_transformation:
        if word[0].isalpha() == True:
            clean_list.append(word)
    
    return clean_list


main()