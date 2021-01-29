# 2. Пользователь вводит время в секундах.
#    Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#    Используйте форматирование строк.

num_of_seconds: int = int(input("Please, enter number of seconds: "))

hours: int = num_of_seconds // 3600
minutes: int = (num_of_seconds - hours * 3600) // 60
seconds: int = num_of_seconds - hours * 3600 - minutes * 60

print(f"Time: {hours}:{minutes}:{seconds}.")
