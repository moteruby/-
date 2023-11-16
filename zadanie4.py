#Задание4
new_string = "8761239540"
dict = {}
for char in new_string:
    if char.isdigit():
        num = int(char)
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
print(dict)