#Задание 2
string = input("Введите строку: ")
while not string:
    string = input("Вы не ввели строку!Введите строку: ")
else:
    words = string.split()
    even_count = 0
    odd_count = 0
    for word in words:
        if len(word) % 2 == 0:
            even_count += 1
        else:
            odd_count +=1
print("Количество слов четной длины:", even_count)
print("Количество слов нечетной длины:", odd_count)