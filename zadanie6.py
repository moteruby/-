#Задание6
numbers = (1, 3, 9, 0, 7, 8, 0)
zero_count = 0
for num in numbers:
    if num == 0:
        zero_count += 1
print("Количество нулевых элементов: " + str(zero_count))