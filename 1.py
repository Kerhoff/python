"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
   В расчете необходимо использовать формулу:
   (выработка в часах * ставка в час) + премия.
   Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, hours, wage_per_hour, bonus = argv

hours = int(hours)
wage_per_hour = float(wage_per_hour)
bonus = float(bonus)

salary = (hours * wage_per_hour) + bonus
print(f"Your salary is: {salary}")
