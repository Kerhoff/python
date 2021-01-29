# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
#    Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#    Напишите решения через list и через dict.

# Get month number
month_number: int = int(input("Month number:"))
while ((month_number < 1) or (month_number > 12)):
    month_number = int(input("Please enter number from 1 to 12: "))

#while (month_number < 0) or (month_number > 12):
#    month_number: int = int(input("Enter number from 1 to 12 please")


# 1st Solution via List
seasons_list: list = ["Зима", "Зима", 
                      "Весна", "Весна", "Весна",
                      "Лето", "Лето", "Лето",
                      "Осень", "Осень", "Осень",
                      "Зима"]

print(seasons_list[month_number - 1])

# 2nd Solution via lists
winter_months: list = [12, 1, 2]
spring_months: list = [3, 4, 5]
summer_months: list = [6, 7, 8]
fall_months: list = [9, 10, 11]

if month_number in winter_months:
    print("Зима")
elif month_number in spring_months:
    print("Весна")
elif month_number in summer_months:
    print("Лето")
elif month_number in fall_months:
    print("Осень")

# 1st Solution via Dictionary
seasons: dict = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
for season, months in seasons.items():
    if month_number in months:
        print(season)

# 2st Solution via Dictionary
months: dict = {12: "Зима", 1: "Зима", 2: "Зима", 
                3: "Весна", 4: "Весна", 5: "Весна",
                6: "Лето", 7: "Лето", 8: "Лето",
                9: "Осень",10: "Осень", 11: "Осень"}
print(months[month_number])