# Задание № 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = input("Введите вещественное число: ")
number = int(number.replace('.', ''))
sum = 0
while (number != 0):
    sum = sum + number % 10
    number = number // 10
print(f"Сумма цифр в числе: {sum}")

# Задание № 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('Введите число: '))
lst = list()
for i in range(n):
    lst.append(i + 1)
for i in range(1,n):
    lst[i] = lst[i-1]*lst[i]
print(lst)


# Задание № 3. Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
n = int(input('Введите число: '))
dict={}
sum = 0
for i in range(1, n + 1):
    dict[i] = round((1 + (1 / i)) ** i,2)
    sum = dict[i] + sum
print(dict)
print(f"Сумма всех значений словаря: {sum}")

# Задание № 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
a = int(input('Введите число: '))
lst = list()
if (a > 0):
    for i in range(-a, a + 1):
        lst.append(i)
else:
    for i in range(-a, a - 1, -1):
        lst.append(i)
print(f"Список чисел от {-a} до {a}:")
print(lst)
product = 1
path = 'file.txt'
data = open(path, 'r')
for i in data:
    product = product * lst[int(i)]
data.close()
print(f"Произведение элементов списка на позициях из файла file1.txt: {product}")


# Задание № 5. Реализуйте алгоритм генерации случайного числа.(Не используя библиотеки связанные с рандомом) (Доп задача, не влияющая на оценку )
import time
num = time.time()
print(int(num%10*100))
