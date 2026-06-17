import string

punctuation_set = set(string.punctuation)

s = input("Enter string here: ")

# locations = [index for index, char in enumerate(s) if char in punctuation_set]

first_word = ""

for char in s:
    if char == " " or char in punctuation_set:
        break

    first_word += char

print(first_word)


        