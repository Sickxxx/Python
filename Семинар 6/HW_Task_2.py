import random as r
# Звдание 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
k = int(input("Введите степень k: "))
a = [r.randint(-5, 2) for i in range(k + 1)]
for i in range(len(a)):
    a[i] = "{:+}".format(a[i]) + str(f"*x^{k - i}")
for i in a:
    if "+0*x^" in i:
        a.remove(i)
print(''.join(a))
