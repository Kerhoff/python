# 4. Пользователь вводит целое положительное число.
#    Найдите самую большую цифру в числе.
#    Для решения используйте цикл while и арифметические операции.

number: int = int(input("Number: "))
digits: list = []

# Create list of digits
while number > 0:
    digits.append(number % 10)
    number = number // 10

# Find max digits - max value in list
# max_digit = max(digits)
max_digit = digits[0]
for digit in digits:
    if digit > max_digit:
        max_digit = digit

print(digits)
print(f"Max digit: {max_digit}")
