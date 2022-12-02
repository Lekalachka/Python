# # Реализуйте алгоритм задания случайных чисел без использования встроенного генератора
# # псевдослучайных чисел.
# import time
# print(time.time())
# print(time.time_ns())
# num = time.time_ns() % 1000 // 100
# print(num)
# numb = time.time_ns() % 1000 // 100
# print(numb)

# 2 Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке
# строк некое число.
# my_list = input("Введите числа через пробел: ").split()
# f_num = input("Введите искомое число: ")
# for i in my_list:
#     # print(i)
#     if  f_num in i:
#         print("Присутствует")
#         break


# input_list = input("Введите числа через запятую: ").split(',')
# print(input_list)
# # x = input_list.split()
# # print(x)

# Напишите программу, которая определит позицию второго вхождения строки в списке либо
# сообщит, что её нет.

my_list = input("Введите числа через пробел: ").split()
f_num = input("Введите искомое число: ")
def find_second(my_list, f_num):
    count = 0
    for i in range(len(my_list)):
        # print(i)
        if  f_num in my_list[i]:
            count+=1
            if count == 2:
                return i
            else:
                return -1
         
print(find_second(my_list, f_num))
