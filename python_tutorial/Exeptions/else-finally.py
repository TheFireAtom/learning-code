f = None
try:
    f = open("Exeptions\data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File is read: ", content)
finally:
    if f:
        f.close()