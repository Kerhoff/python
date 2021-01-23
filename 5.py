# 5. Запросите у пользователя значения выручки и издержек фирмы.
#    Определите, с каким финансовым результатом работает фирма
#    (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#    Выведите соответствующее сообщение.
#    Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
#    Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# Get data from user
proceeds: float = float(input("Enter proceeds, please: "))
costs: float = float(input("Enter costs, please: "))
# Get result
result: float = proceeds - costs
# Output
if result > 0:
    print("You have profit :)")
    profitability = result / proceeds
    print(f"Your profitability is {profitability}.")

    num_of_staff: int = int(input("Enter number of staff, please: "))
    print(f"Profit per employee: {result / num_of_staff}")
else:
    print("You have damages :(")
