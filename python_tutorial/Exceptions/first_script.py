import os

result = 0.0
lines = ["10.3", "20.4", "anc", "152.2"]
filename = "data.txt"

if not os.path.exists("Exceptions/data.txt"):
    with open("Exceptions/data.txt", "w") as f:
        for line in lines:
            f.write(line + "\n")
    print("New file was created")

try:
    with open("Exceptions/data.txt", "r", encoding="utf-8") as f:
        for value in f:
            stripped = value.strip()
            try:
                float_value = float(stripped)
                result += float_value
                print("Ok: ", value)
            except ValueError:
                print("Wrong value.")
except FileNotFoundError:
    print("Something went wrong, file was not created... \n Mayber file exist already?")
            
print(f"Overall result: {result}")