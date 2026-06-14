
import string

words = input("Type your sentence here (with space between them): ")

count_words = 1

for word in words:
    if (word == " "):
        count_words += 1

print(count_words)

