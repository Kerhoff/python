# 1. Поработайте с переменными, создайте несколько, выведите на экран,
#    запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

# Work with variables and data types
# String
country: str = "Russia"
city: str = "Moscow"
# Integer
year: int = 2021
# Boolean
not_false: bool = True
not_true: bool = False
# Float
figure_skating_max_score: float = 6.0

# User input example
intro: str = "Hello! Let's play in my games :)"
print(intro)

name: str = input("Enter your name: ")
surname: str = input("Add please your surname: ")
age: int = int(input("Enter your age: "))

person: dict = {"name": name, "surname": surname, "birth_year": year - age}
print(f"Hello, {person['surname']} {person['name']}! You are in {city}, {country}. "
      f"Year of you birth is {person['birth_year']}.")
