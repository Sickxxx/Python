# Задание 1. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
size = int(input('Введите длину списка: '))
array = [random.randint(1, 10) for i in range(size)]
print(array)
for i in range((size + 1) // 2):
    print(array[i] * array[size - 1], end=" ")
    size -= 1

# Задание 2. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

size = int(input('Введите длину списка: '))
array = [round(random.uniform(1, 10), 2) for i in range(size)]
print(array)
min = max = array[0] - int(array[0])
for i in range(len(array)):
    if (array[i] - int(array[i]) < min):
        min = array[i] - int(array[i])
    if (array[i] - int(array[i]) > max):
        max = array[i] - int(array[i])
print(f"Разница между {round(max, 2)} и {round(min, 2)} = {round((max - min), 2)}")

# Задание 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#Первый вариант решения
number = int(input("Введите число: "))
print(f"Число {number} в двоичной системе = {bin(number)}")
# Второй вариант решения
number = int(input("Введите число: "))
number_bin = ""
while number > 0:
    number_bin = str(number % 2) + number_bin
    number = int(number // 2)
print(number_bin)

# Задание 4. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
n = int(input('Введите число: '))
array = [1, 1]
for i in range(2, n):
    array.append(array[i - 1] + array[i - 2])
array2 = array[::-1]
if (n % 2 == 0):
    k = -1
else:
    k = 1
for i in range(n):
    array2[i] = array2[i] * k
    k = -k
array2.append(0)
print(array2 + array)
