# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
#     *Пример:*
#
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


n = int(input('Введите длину ряда: '))

f1 = 0
f2 = 1

lst = [0, 1]

while len(lst) <= n:
 lst.append(lst[-2] + lst[-1])
print(lst)

lst2 = []

for i in range(1, len(lst)):
    lst[i] = lst[i] * -1
    lst2.append(lst[i])

lst2.reverse()
print(lst2)

numbers = lst2 + lst

print(numbers)
