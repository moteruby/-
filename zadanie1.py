# Вариант: 9
#Задание 1
import random
a = random.randint(0,1000)
print("Угадайте число")
print("Правильное число:", a)
i = 1
while True:
    b = input("Введите целое число: ")
    while not b.isdigit():
        b = input("Неправильный ввод. Введите целое число: ")
        continue
    b = int(b)
    if b > a:
        print("Ваше число больше загаданного.")
        i += 1
        continue
    if b < a:
        print("Ваше число меньше загаданного.")
        i += 1
        continue
    if b == a:
        break;
print("Вы угадали число с", i,"-ой попытки.")