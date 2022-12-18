from fractions import Fraction


def view_data(data, act):
    if act == "*":
        print(f'Умножение = {data}')
    elif act == "/":
        print(f'Деление = {data}')
    elif act == "+":
        print(f'Сложение = {data}')
    else:
        print(f'Вычитание = {data}')


def get_value_complex(x):
    num = input(f'Введите {x}-ое число = ')
    if "j" in num:
        num = complex(num)
    else:
        num = num.split(",")
        num = complex(int(num[0]), int(num[1]))
    print(num)
    return num


def get_value_fraction(x):
    num = input(f'Введите {x}-ое число = ')
    if "/" in num:
        num = num.split("/")
        num = Fraction(int(num[0]), int(num[1]))
    else:
        num = Fraction(num)
    print(num)
    return num
