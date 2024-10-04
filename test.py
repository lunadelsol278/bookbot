
with open('books/frankenstein.txt') as f:
    file_contents = f.read()
low_chars = file_contents.lower()
char_dict = {}
for char in low_chars:
    char_dict[char] = 0
for i in low_chars:
    char_dict[i] += 1
print(char_dict)


