n = int(input("Введите число:"))
sum = 0
while(n > 0):
    rez = n % 10
    sum = sum + rez
    n = n//10
print("Сумма цифр равна:", sum)