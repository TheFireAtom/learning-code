user_input = input("Write your line: ")
with open("Files IO/data.txt", "w", encoding="utf-8") as file:
    file.write(user_input)
    file.close()



