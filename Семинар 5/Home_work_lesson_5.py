def Task1():
    # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
    text = "Герой посетил Зимбабве и впал в самозабвение"
    text_arr = [i for i in text.split()]
    symb = "абв"
    text2 = " ".join([i for i in text_arr if symb not in i])
    print(text2)
def Task2():
    # Создайте программу для игры с конфетами человек против человека.
    # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
    # Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
    # Все конфеты оппонента достаются сделавшему последний ход.
    # Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
    # a) Добавьте игру против бота
    # b) Подумайте как наделить бота ""интеллектом""
    import random
    def human(candy, player):
        while candy != 0:
            player = not player
            print(f"Ход Игрока №{player + 1}")
            i = int(input("Сколько конфет забираем? "))
            while i > step:
                print(f"Вы ввели недопустимое значение, можно забрать максимум {step} конфет!")
                i = int(input("Сколько конфет забираем? "))
            if candy - i < 0:
                print(f"Можно забрать максимум {candy} конфет!!!")
                i = int(input("Сколько конфет забираем? "))
            candy -= i
            print(f"На столе осталось {candy} конфет")
        print(f'Победил Игрок №{player + 1}! Поздравляю!')

    def bot(candy, player, diff):
        i = random.randint(1, step)
        while candy != 0:
            player = not player
            if player == 0:
                print(f"Ход Игрока №{player + 1}")
                i = int(input("Сколько конфет забираем? "))
                while i > step:
                    print(f"Вы ввели недопустимое значение, можно забрать максимум {step} конфет!")
                    i = int(input("Сколько конфет забираем? "))
                if candy - i < 0:
                    print(f"Можно забрать максимум {candy} конфет(у\ы)!!!")
                    i = int(input("Сколько конфет забираем? "))
            else:
                print(f"Ход Бота")
                if diff == 1:
                    if candy < step:
                        i = random.randint(1, candy)
                    elif candy < step + (step // 2):
                        res = candy - (step + 1)
                        i = res
                    else:
                        i = random.randint(1, step)
                else:
                    if candy == step + 1:
                        i = random.randint(1, step)
                    elif candy < step:
                        i = candy
                    elif candy < step * 2:
                        i = candy - (step + 1)
                    else:
                        i = i = random.randint(1, step)
                print(f'Бот забрал {i} конфет(у\ы)')
            candy -= i
            print(f"На столе осталось {candy} конфет(ы)")

        if not player:
            print(f'Победил Игрок №{player + 1}! Поздравляю!')
        else:
            print(f'Победил Бот!!!')

    candy = 200
    step = 28
    ask = int(input("Кто будет играть?(1 - человек vs человек, 2 - человек vs бот): "))
    if ask == 2:
        diff = int(input("Введите сложность бота(1 - Легкий, 2 - Сложный):"))
    a = int(input(f"Кидаем монетку! Игрок №1, выбери сторону монеты(1 - орел, 2 - решка!): "))
    b = random.randint(1, 2)
    print('Выпадает Орел!' if b == 1 else 'Выпадает Решка!')
    player = (1 if a == b else 0)
    if ask == 1:
        human(candy, player)
    else:
        bot(candy, player, diff)
def Task3():
    field = [int(i) for i in range(1, 10)]
    def f(m=""):
        count = 0
        for i in field:
            if i == "X":
                print("\033[31m X", end=f"\033[0m |")
            elif i == "O":
                print(f"\033[32m O", end="\033[0m |")
            else:
                print(f"\033[0m {i}", end="\033[0m |")
            count += 1
            if count == 3:
                print("\n------------")
                count = 0
    def win(field):
        if field.count("X") + field.count("O") == len(field):
            print("Ничья!")
            return True
        for i in range(0,len(field), 3):
            if field[i] == field[i+1] == field[i+2]:
                print(f"Победили {symb}")
                return True
        for i in range(3):
            if field[i] == field[i+3] == field[i+6]:
                print(f"Победили {symb}")
                return True
        for i in range(0, 3, 2):
            if field[i] == field[i+3] == field[i+6]:
                print(f"Победили {symb}")
                return True
        if field[0] == field[4] == field[8]:
            print(f"Победили {symb}")
            return True
        elif field[0] == field[4] == field[8]:
            print(f"Победили {symb}")
            return True




    print("Играем в крестики нолики! Выбирай поля для хода!")
    f()
    count = True
    draw = 0
    while not win(field):
        if count:
            symb = "X"
        else:
            symb = "O"
        move = int(input(f"Выбери позицию для хода {symb}: "))
        field[move - 1] = symb
        # print(100 * '\n')
        f()
        count = not count
    # print(f"Победили {symb}") if draw == 0 else "Ничья!")
def Task4():
    #Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
    def compression():
        text = [i for i in input("Введите символы для сжатия: ")]
        text2 = []
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i-1]:
                count+=1
            else:
                text2.append(str(count))
                text2.append(text[i-1])
                count = 1
        text2.append(str(count))
        text2.append(text[i])
        print("".join(text2))
    def decompression():
        text = [i for i in input("Введите символы для востановления: ")]
        count = ""
        for i in text:
            if i.isdigit():
                count += i
                continue
            else:
                print(i * int(count), end = "")
                count = ""
    compression()
    decompression()
Task1()
Task2()
Task3()
Task4()
