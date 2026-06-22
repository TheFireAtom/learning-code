filename = input("Write full filepath: ")
N = int(input("Write maximum number of lines that you want to have: "))

with open(f"{filename}", "r") as file:
    for i in range(N):
        line = file.readline()
        print(line.strip())
        with open(f"{i}.txt", "w") as f:
            f.write()
            print(content)
    

            
    