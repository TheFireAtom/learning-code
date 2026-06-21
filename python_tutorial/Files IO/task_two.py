import os

marker = True
filename = input("Write filename (without .txt): ")
print("Start typing your strings: ")
while marker:
    user_input = input("String: ")
    if user_input == "exit" or user_input == "":
        marker = False
        print("Exiting program")
        exit()
    else:
        with open(f"Files IO/{filename}.txt", "a") as file:
            file.write(f"{user_input}\n")
            print("Line was written")
