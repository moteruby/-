#Задание 3
new_list = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,90,0]
list_of_unique_elements = []
sum = 0
for element in new_list:
    if new_list.count(element) == 1:
        list_of_unique_elements.append(element)
print(list_of_unique_elements)
first_zero = new_list.index(0)
last_zero = len(new_list) - new_list[::-1].index(0)
for i in range(first_zero + 1, last_zero):
    sum += new_list[i]
print(sum)