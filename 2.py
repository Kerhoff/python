# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#    имя, фамилия, год рождения, город проживания, email, телефон.
#    Функция должна принимать параметры как именованные аргументы.
#    Реализовать вывод данных о пользователе одной строкой.

def person(name, surname, year, city, email, phone):
    print(f"{name} {surname} was born in {year} lives in {city} has {email} email and phone {phone}.")


print(person(name="John", surname="Travolta", city="New York", year="1954", email="email@gmail.com", phone="+11234567890"))
