# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
#     *Пример:*
#
#     - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 5.1, 10.01]
lst2 = []
for i in range(len(lst)):
    lst[i] = lst[i] - int(lst[i])
    lst2.append(lst[i])
max = lst2[0]
min = lst[0]
for i in range(1,len(lst2)):
    if lst2[i] > max:
        max = lst2[i]
    if lst2[i] < min:
        min = lst2[i]
print(round(max-min,2))

