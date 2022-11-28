# c:\python310\
# vscode pycharm

# python
#  - homework_1
#  - homework_2
#
# master/main
# homework_1
# PEP 8
# x = 5
#
# if 5 < x < 9:
#     print(x)
# else:
#     print('x не входит в диапазон')

# 7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
# ⋁ - ИЛИ, ⋀ - И
# 8 Сообщить в какой четверти координатной плоскости или на какой
# оси находится точка с координатами Х и У.
# 9 Указав номер четверти прямоугольной системы координат, показать
# допустимые значения координат для точек этой четверти.
# 10 Найти расстояние между двумя точками пространства.

# № 7
# for x in (0, 1):
#     for y in (0, 1):
#         for z in (0, 1):
#             left = not(x or y or z)
#             right = not x and not y and not z
#             # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
#             print(f'x = {x}, y = {y}, {z = }')
#             print(left == right)

# x = float(input('Введите координату Х: '))
# y = float(input('Введите координату У: '))
# if x > 0 and y > 0:
#     print('1 четверть')
# elif x < 0 and y > 0:
#     print('2 четверть')
# elif x < 0 and y < 0:
#     print('3 четверть')
# elif x > 0 and y < 0:
#     print('4 четверть')
# elif x == 0 and y == 0:
#     print('точка лежит в начале координат')
# elif x == 0 and y != 0:
#     print('точка лежит на оси X')
# else:
#     print('точка лежит на оси Y')

# a = input('Введите номер четверти: ')
# if a == '1':
#     print('x > 0, y > 0')
# import math
ax = float(input('Введите координату x точки А: '))
ay = float(input('Введите координату y точки А: '))
bx = float(input('Введите координату x точки Б: '))
by = float(input('Введите координату y точки Б: '))
l = ((ax - bx)**2 + (ay - by)**2)**0.5
# l = math.sqrt((ax - bx)**2 + (ay - by)**2)
print(round(l, 3))
