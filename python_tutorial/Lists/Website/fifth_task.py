from random import randint

bubble_list = []

for _ in range(10):
    bubble_list.append(randint(1, 10))

print(bubble_list)

def bubble(arg_list):
    for arg in range(len(arg_list)-1):

        if arg_list[arg] > arg_list[arg+1]:
            temp_arg = arg_list[arg]
            arg_list[arg] = arg_list[arg+1] 
            arg_list[arg+1] = temp_arg
    return arg_list

print(bubble(bubble_list))