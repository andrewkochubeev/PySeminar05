# Напишите программу, которая
# на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def power(x, y):
    if y == 0:
        return 1
    if y > 0:
        return x * power(x, y - 1)
    if y < 0:
        return 1 / power(x, -y)
a = int(input("Введите число А: "))
b = int(input("Введите степень B: "))
result = power(a, b)
print(result)
