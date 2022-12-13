# реализовать калькулятор
str = [i for i in input('Введите выражение: ').split()]


def action(str):
    if "(" in str:
        tmp = action_2(str[(str.index("(")) + 1:str.index(")")]) # запоминаем результат действия в скобках
        del str[str.index("("):str.index(")")] # удалаем из массива все что в скобках
        str[str.index(")")] = tmp # вставляем вместо последней скобки результат вычислений выше
    return str


def action_2(str):
    symb = ["*", "/", "+", "-"]
    for i in symb:
        while i in str:
            for j in range(len(str)): # выполняем фунцию, пока в нашем массиве есть знаки арифм. действий
                if str[j] == i:
                    if i == "*":
                        str[j] = int(str[j - 1]) * int(str[j + 1]) # проделываем вычисление согласно знаку и меняем их на сам знак
                    elif i == "/":
                        str[j] = int(str[j - 1]) / int(str[j + 1])
                    elif i == "+":
                        str[j] = int(str[j - 1]) + int(str[j + 1])
                    elif i == "-":
                        str[j] = int(str[j - 1]) - int(str[j + 1])
                    del str[j + 1] # удаляем символ до и после знака
                    del str[j - 1]
                    break # проделываем все заного сначала списка, чтобы не поехала нумерация
    return (str[0])

action(str)
print(action_2(str))
