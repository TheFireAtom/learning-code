from random import randint

first_list = []
second_list = []
final_list = []

for _ in range(4):
    first_list.append(randint(1, 5))
for _ in range(4):
    second_list.append(randint(3, 7))
# for _ in range(len(first_list) + len(second_list)): 

print(first_list)
print(second_list)

final_list = first_list.copy()

for num in second_list:
    if num not in final_list:
        final_list.append(num)

print(final_list)

