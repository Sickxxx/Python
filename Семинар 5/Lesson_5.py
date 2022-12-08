def Task1():
    # В файле находятся N натуральных чисел, записанных, через пробел
    # Среди них не хватает одного числа, чтобы выполнить условие A[i] - 1 = A[i - 1]. Найти это число
    import random
    list1 = [i for i in range(11)]
    del list1[random.randint(0, 10)]
    print(list1)
    print(*[i for i in range(1, len(list1)) if list1[i] - 1 != list1[i - 1]])


def Task2():
    # Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
    # [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 5] или [1, 4, 6, 7] и т.д.
    list1 = [1, 5, 2, 3, 4, 6, 1, 7]
    list2 = []
    a = []
    for i in range(len(list1)):
        a = []
        for j in range(i, len(list1)):
            if list1[j] == list1[i] + 1:
                a.append(list1[i])
                i = j
        if len(a) > 0:
            a.append(list1[i])
            list2.append(a)
    print(list2)


Task2()
