# Task1
# a = int(input("Введите первое число "))
# b = int(input("Введите второе число "))
# if (b == a**2):
#     print(f'Число {b} является квадратом {a}')
# elif (a == b**2):
#     print(f'Число {b} является квадратом {a}')
# else:
#     print('Числа не являются квадратами друг друга')
# Task2
# nums = [int(i) for i in input().split()]
# max = nums[0]
# for i in range(1,len(nums)):
#     if (nums[i] > max):
#         max = nums[i]
# print(max)
# Task3
# a = int(input('Введите число N '))
# if (a > 0):
#     for i in range(-a, a + 1):
#         print(i, end=" ")
# else:
#     for i in range(-a, a - 1, -1):
#         print(i, end=" ")
# Task4
# a = float(input("Введите число "))
# print(int(a * 10 % 10))
# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# Task5
a = int(input("Введите число "))
print((a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and (a % 30 != 0))
