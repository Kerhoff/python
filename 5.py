"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
   В список должны войти четные числа от 100 до 1000 (включая границы).
   Необходимо получить результат вычисления произведения всех элементов списка.
   Подсказка: использовать функцию reduce().
"""

even_numbers: list = [digit for digit in range(100, 1001) if digit % 2 == 0]


def multiply(numbers_list):
    multiply_result = 1
    for number in numbers_list:
        multiply_result = multiply_result * number

    return multiply_result


print(multiply(even_numbers))
