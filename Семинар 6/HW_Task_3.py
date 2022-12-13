import math

# # Задание 1. Вычислить число ПИ c заданной точностью d
print(*list(str(math.pi)[i] for i in range(int(input("Введите количество знаков после запятой: ")) + 2)))
