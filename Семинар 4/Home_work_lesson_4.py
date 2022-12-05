# Задание 1. Вычислить число ПИ c заданной точностью d
# import math
#
# d = int(input("Введите количество знаков после запятой: "))
# pi = str(math.pi)
# for i in range(d+2):
#     print(pi[i], end="")

# Задание 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# n = int(input("Введите число N: "))
# def multiplier(n):
#     arr=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             arr.append(i)
#     return arr
# print(f"Все простые множители числа {n}: {multiplier(n)}")

# Задание 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random as r


# a = [r.randint(1, 10) for i in range(r.randint(5,10))]
# print(a)
# print("Последовательность из неповторяющихся элементов:")
# new_a = [i for i in a if a.count(i) == 1]
# print(new_a)

# Звдание 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k(до 6 степени).*
# k = int(input("Введите степень k: "))
def polynomial(k, a = []):
    b = ""
    if len(a) == 0:
        a = []
        for i in range(k + 1):
            a.append(r.randint(-100, 100))
    if a[0] != 0:
        b = str(f"{a[0]}*x^{k} ")  # Если первый элемент не 0, то начинаем запись многочлена с
        ind = 1  # коэф * х ^(степень к)
    else:
        ind = 0
        while a[ind] == 0:
            ind += 1
            b = str(
                f"{a[ind]}*x^{k - ind} ")  # если первый элемент 0, то запись многочлена начинается со второго коэф * х ^ (степень к)
        ind += 1
    for i in range(ind, len(a) - 1):  # продолжение записи многочлена в зависимости от знака коэфициента
        if a[i] > 0:
            b += str(f"+ {a[i]}*x^{k - i} ")
        elif a[i] < 0:
            b += str(f"{a[i]}*x^{k - i} ")
        else:
            continue
    if a[len(a) - 1] > 0:
        b += str(f"+ {a[len(a) - 1]} = 0")  # в конце формулы дописываем + "последний коэффициент" = 0
    elif a[len(a) - 1] < 0:
        b += str(f"{a[len(a) - 1]} = 0")
    else:
        b += " = 0"
    return b


# with open("file1.txt", 'w') as file1:
#     file1.write(polynomial(k))
# with open("file1.txt", 'r') as file1:
#     print(file1.readline())

# Задание 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.*
with open("file1.txt", 'w') as file1:
    file1.write(polynomial(r.randint(2, 6)))
with open("file2.txt", 'w') as file2:
    file2.write(polynomial(r.randint(2, 6))) # запись многочленов в файлы
file1 = open("file1.txt", 'r')
file2 = open("file2.txt", 'r')
value = [str(i) for i in file1.readline().split(" ")]
value2 = [str(i) for i in file2.readline().split(" ")]
print(value) # читаем файлы и выводим многочлены
print(value2)
def dellandsep(a): # удаляем ненужные символы
    size = len(a)
    i = 0
    while i < size:
        if a[i] == "+" or a[i] == "=" or a[i] == "0":
            del a[i]
            size -= 1
            i -= 1
        i += 1
    arr = []
    for i in a:
        arr.append(i.split("*x^"))
    return arr
if len(dellandsep(value)) > len(dellandsep(value2)):
    arr1 = dellandsep(value)
    arr2 = dellandsep(value2)
else:
    arr1 = dellandsep(value2)
    arr2 = dellandsep(value)
ind = 0
ind2 = 0
for i in arr1: # ниже мы будем сравнивать части многорчленов, для того чтобы правильно сложить коэффициенты
    if len(i) == 2:
        if i[1] == arr2[ind][1]:
            arr1[ind2][0] = int(arr1[ind2][0]) + int(arr2[ind][0])
            ind += 1
        ind2 += 1
    elif len(arr1[ind2]) == len(arr2[ind]):
        arr1[ind2][0] = int(arr1[ind2][0]) + int(arr2[ind][0])
arr3=[]
for i in arr1:
    arr3.append(int(i[0]))
print(polynomial(len(arr3)-1, arr3))
with open("finalfile.txt", 'w') as file3:
    file3.write(polynomial(len(arr3)-1, arr3)) # записываем итоговую сумму многочленов в новый файл