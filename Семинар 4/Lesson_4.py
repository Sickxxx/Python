# #Задайте строку из набора чисел. Напишите программу, которая покажет
# # большее и меньшее число. В качестве символа-разделителя используйте пробел.
# n = input("Введите число").split()
# for i in range(len(n)):
#     n[i] = int(n[i])
# print(min(n), max(n))

# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами
# str = "3x^2 + 4x + 1 = 0"
# main_str = str.split(" = ")[0]
# a, b, c = main_str.split(" + ")
# a = int(a[:a.index("x")])
# b = int(b[:b.index("x")])
# c = int(c)
# d = b * b - 4 * a * c
# if d < 0:
#     print("Нет Корней")
# elif d == 0:
#     print(f"x = {-b / (2 * a)}")
# else:
#     print(f"x1 = {-b + (d ** 0.5) / (2 * a)} \n x2 = {-b - (d ** 0.5) / (2 * a)}")

# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
n1 = int(input("1"))
n2 = int(input("2"))


def nok(n1, n2):
    if n1 > n2:
        greater = n1
    else:
        greater = n2
    while (True):
        if ((greater % n1 == 0) and (greater % n2 == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


def nod(n1, n2):
    if n1 > n2:
        smaller = n2
    else:
        smaller = n1
    for i in range(1, smaller + 1):
        if ((n1 % i == 0) and (n2%i == 0)):
            res = i
    return res

print(nok(n1, n2), nod(n1, n2))