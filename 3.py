# 3. Реализовать функцию my_func(),
#    которая принимает три позиционных аргумента,
#    и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    args: list = [a, b, c]
    args.sort()
    return args[1] + args[2]


print(f"Sum of two max args of (1, 5, 2): {my_func(1, 5, 2)}")
print(f"Sum of two max args of (5, 1, 2): {my_func(5, 1, 2)}")
