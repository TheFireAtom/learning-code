age = int(input("Введите возраст сотрудника: "))
exp = int(input("Введите стаж сотрудника: "))

minimal_age = 20
minimal_exp = 3

if age >= minimal_age and exp >= 3:
    print("Вы нам подходите")
else:
    print("К сожалению, вы нам не подходите")