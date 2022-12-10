# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

x = int(input('Введите число: '))


def factorial(a):
    factorial = 1
    for i in range(1, a + 1):
        factorial *= i
    return factorial


li = [i for i in range (1, x+1)]
res = list(map(lambda i: factorial(i), li))

print(res)