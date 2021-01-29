#  2. Для списка реализовать обмен значений соседних элементов,
#     т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#     При нечетном количестве элементов последний сохранить на своем месте.
#     Для заполнения списка элементов необходимо использовать функцию input().

list_length: int = int(input("Enter list length: "))
my_list: list = []

for i in range(0, list_length):
    list_element: str = input(f"Enter {i} element of List: ")
    my_list.append(list_element)

print(my_list)

i = 0
while i < len(my_list) // 2:
    start: int = i * 2
    (my_list[start], my_list[start + 1]) = (my_list[start + 1], my_list[start])
    i += 1
print(my_list)