try:
    number = int(input("Type value: "))
    print(10 / number)
except ValueError:
    print("This is not a number!")
except ZeroDivisionError:
    print("You can't divide by zero!")