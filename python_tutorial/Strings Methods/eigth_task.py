import string

stop_value = True

while stop_value:
    s = input("Write two-words string here: ")
    spaces_count = [index for index, char in enumerate(s) if char == " "]

    has_puntuation = any(sym in string.punctuation for sym in s)

    if len(spaces_count) != 1 or has_puntuation:
        #s = input("Oops, you've written more than two words, try again\n")
        print("\nOops, you've written more than two words or " \
               "your string contains special symbols, try again\n")
        continue 
    space_idx = spaces_count[0]
    first_word = s[:space_idx]
    second_word = s[space_idx+1:]
    print(second_word.title(), first_word.lower())
    stop_value = False

            
            


        

