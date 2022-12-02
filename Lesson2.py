# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

# x = input('Введите число: ')
# res = 0

# for i in x:
#     if i.isdigit():
#         res += int(i)
# print(res)

# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# x = int(input('Введите число: '))
# factorial = 1
# numbers = []

# for i in range(1, x + 1):
#     factorial *= i
#     numbers.append(factorial)
# # print(numbers)
# print(*numbers, sep=', ')

# 3.Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6:
#     [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
#     Сумма чисел = 14.0717

# n = int(input('Введите число N: '))
# my_list = []
# mysum = 0

# for i in range(1, n+1):
#     res = round((1 + 1/i)**i, 4)
#     my_list.append(res)
#     # mysum += res

# print(my_list)
# # print(mysum)
# print(sum(my_list))

# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
#Позиции хранятся в списке positions - создайте этот список (например: positions = [1, 3, 6]).

# from random import randint

# def fill_list(n):
#     fill_list = []
#     for i in range(n):
#         fill_list.append(randint(-n, n))
#     return fill_list


# n = int(input('Введите число N: '))
# my_list = fill_list(n)
# print(my_list)
# multy = 1
# positions = [1, 3, 6]

# for i in positions:
#     if i <= len(my_list):
#         multy *= my_list[i-1]

# print(multy)


# 5 Реализовать алгоритм перемешивания списка.
import random


def fill_list(n):
    fill_list = []
    for i in range(n):
        fill_list.append(random.randint(-n, n))
    return fill_list

new_list = fill_list(int(input('Введите число N: ')))
print(new_list)

# random.shuffle(new_list)
# print(new_list)

for i in range(len(new_list-1), -1, -1):
    j = random.randint(0, i)
    new_list[i], new_list[j] = new_list[j], new_list[i]
    
print(new_list)