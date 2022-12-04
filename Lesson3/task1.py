# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


def fill_list(n):
    fill_list = []
    for i in range(n):
        fill_list.append(randint(1, n))
    return fill_list


n = int(input('Введите число N: '))
my_list = fill_list(n)
print(my_list)

summ = 0
for i in range(len(my_list)):
    if i % 2 != 0:
        summ += my_list[i]
        
print(summ)