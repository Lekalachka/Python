# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


def fill_list(n):
    fill_list = []
    for i in range(n):
        fill_list.append(randint(1, n))
    return fill_list


n = int(input('Введите число N: '))
my_list = fill_list(n)
my_list2 = []

for i in range(n):
    while i < len(my_list)/2 and n > len(my_list)/2:
        n = n - 1
        a = my_list[i] * my_list[n]
        my_list2.append(a)
        i += 1

print(my_list)
print(my_list2)