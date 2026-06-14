# first, second, third = input("Enter three words: ").split()

words_list = []
word_max = 0
string_max = ""

while True:
    user_input = input("Enter your words or sentences (when you're done, type 'quit'): ")

    if user_input.lower() == "quit":
        break
    
    new_words = user_input.split()

    words_list.extend(new_words)

for word in words_list:
    temp_var = len(word)
    if temp_var > word_max:
        word_max = temp_var
        string_max = word

print(words_list)
print(word_max)
print(string_max)


