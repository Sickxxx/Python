# Задание №1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
num = int(input("Введите число: "))
if (num == 6 or num == 7):
    print("Выходной день")
else:
    print("Не выходной день")
print("_________________________________")
# Задание №2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(f'При x = {x}, y = {y}, z = {z} значение выражения {not (x or y or z) == (not x) and (not y) and (not z)}')
print("_________________________________")
# Задание №3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
x = int(input("Введите координату X: "))
y = int(input("Введите координату Y: "))
if (x > 0 and y > 0):
    print("Точка находится в 1ой четверти")
elif (x < 0 and y > 0):
    print("Точка находится во 2ой четверти")
elif (x < 0 and y < 0):
    print("Точка находится в 3ей четверти")
else:
    print("Точка находится в 4ой четверти")
print("_________________________________")
# Задание №4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
quarter = int(input('Введите номер четверти: '))
if (quarter == 1):
    print("Х[0;+∞],Y[0;+∞]")
elif (quarter == 2):
    print("Х[-∞;0],Y[0;+∞]")
elif (quarter == 3):
    print("Х[-∞;0],Y[-∞;0]")
elif (quarter == 4):
    print("Х[0;+∞],Y[-∞;0]")
else:
    print("Число не соответствует номеру четверти")
print("_________________________________")
# Задание №5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
print("Введите координаты точки A: ")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
print("Введите координаты точки B: ")
x2 = int(input("x2: "))
y2 = int(input("y2: "))
print(f"Заданы точки: A({x1},{y1}), B({x2},{y2})")
print(f"Расстояние между точками A и B: {round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5,3) }")
print("_________________________________")
