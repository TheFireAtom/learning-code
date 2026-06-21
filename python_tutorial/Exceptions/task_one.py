# First try:

# def is_float(num):
#     try:
#         float_num = float(num)
#         return float_num
#     except ValueError:
#         return "This is not a float"
# try:
#     with open("Exceptions/data.txt", "r") as file:
#         summ = 0
#         for line in file:
#             print(is_float(line.strip()))
# except FileNotFoundError:
#     print("File not found")

# Second try:

def try_float(num):
    try:
        return float(num)
    except ValueError:
        return None
    
def sum_nubers_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            total = 0.0    
            for line in file:
                num = try_float(line.strip())
                if num is not None:
                    total += num
                else:
                    print(f"Warning: line {num} is not float!")
        return total
    except FileNotFoundError:
        print(f"File {filename} is not found!")
        return None

result = sum_nubers_from_file("Exceptions/data.txt")
if result is not None:
    print(f"Sum is {result}")



