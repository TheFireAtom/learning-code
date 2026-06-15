s1 = input("Введите вашу фамилию: ")
s2 = input("Введите ваше имя: ")
s3 = input("Введите ваше отчество: ")

sout = f"{s1.title()} {s2[0].title()}. {s3[0].title()}."
print(sout)