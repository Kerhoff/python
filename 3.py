# 3. Узнайте у пользователя число n.
#    Найдите сумму чисел n + nn + nnn.
#    Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n: int = int(input("Enter number from 0 to 9: "))
sum_of_n: int = n + (n * 10 + n) + (n * 100 + n * 10 + n)

print(f"n + nn + nnn = {sum}")
