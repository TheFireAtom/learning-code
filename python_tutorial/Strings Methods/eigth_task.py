import string

s = input("Write your sentence here: ")

sspace_pos = []

for index, char in enumerate(s):
    if char == " ":
        sspace_pos.append(index)

sspace_pos = sspace_pos[-1]

print(s[sspace_pos+1:])
