def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counter = get_char_counter(text)
    sorted_chars = sorted(char_counter.items(), reverse=True, key=lambda item: item[1])
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for letter, ccount in sorted_chars:
        if not letter.isalpha():
            continue
        print(f"The '{letter}' character was found {ccount} times")
    print("--- End report---")



def get_char_counter(text):
    low_chars = text.lower()
    char_dict = {}
    for char in low_chars:
        char_dict[char] = 0
    for i in low_chars:
        char_dict[i] += 1
    return char_dict

def sort_on(char_counter):
    return char_counter["ccount"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
