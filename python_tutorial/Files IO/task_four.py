filepath = input("Write full filepath (without name of the file): ")
filename = input("Write full filename (with extension): ")

with open(f"{filepath}{filename}", "r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        print(f"{i} {lines[i].rstrip()}")