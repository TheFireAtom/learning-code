from random import randint

randlist = []

for _ in range(10):
    randlist.append(randint(1, 10))

def sumlist(randlist):
    totalsum = 0
    for num in randlist:
        totalsum += num
    return totalsum

print(randlist)
print(sumlist(randlist))

