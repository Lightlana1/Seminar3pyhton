# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
#     *Пример:*
#
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

from random import randint
lst = [randint(-10, 10) for i in range(5)]
print(lst)
result = 0
a = 0
b = len(lst) - 1
for i in range(len(lst)):
    while a <= b:
        result = lst[a]*lst[b]
        a = a + 1
        b = b - 1
        print(result, end=',')