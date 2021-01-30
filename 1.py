# 1. Реализовать функцию, принимающую два числа
#    (позиционные аргументы) и выполняющую их деление.
#    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(numerator: float, denominator: float) -> float:
    if denominator == 0:
        return 0
    return numerator / denominator


numerator: float = float(input("Numerator: "))
denominator: float = float(input("Denominator: "))

print(division(numerator, denominator))
