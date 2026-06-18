a = int(input("Write your number: "))

cnt = 0

while a != 0:
    cnt += a % 10
    a = a // 10

print(cnt)
