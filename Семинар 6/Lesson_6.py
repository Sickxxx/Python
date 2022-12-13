# реализовать калькулятор
str = input('Введите выражение: ').split()
def calc(args):
    while len(args) != 1:
        while "*" in args or "/" in args:
            try:
                prod_index = args.index("*")
            except:
                prod_index = 100
            try:
                div_index = args.index("/")
            except:
                div_index = 100

            if prod_index < div_index:
                args[prod_index - 1] = int(args[prod_index - 1]) * int(args[prod_index + 1])
                args.pop(prod_index + 1)
                args.pop(prod_index)
            else:
                args[div_index - 1] = int(args[div_index - 1]) / int(args[div_index + 1])
                args.pop(div_index + 1)
                args.pop(div_index)
        while "+" in args or "-" in args:
            try:
                sum_index = args.index("+")
            except:
                sum_index = 100
            try:
                minus_index = args.index("-")
            except:
                minus_index = 100

            if sum_index < minus_index:
                args[sum_index - 1] = int(args[sum_index - 1]) + int(args[sum_index + 1])
                args.pop(sum_index + 1)
                args.pop(sum_index)
            else:
                args[minus_index - 1] = int(args[minus_index - 1]) - int(args[minus_index + 1])
                args.pop(minus_index + 1)
                args.pop(minus_index)
    print(args[0])
calc(str)
