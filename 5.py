# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
#    При нажатии Enter должна выводиться сумма чисел.
#    Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
#    Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
#    Но если вместо числа вводится специальный символ, выполнение программы завершается.
#    Если специальный символ введен после нескольких чисел,
#    то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

summary: int = 0
stop_symbol_is_in_string: bool = False


def search_stop_symbol(s="", stop_symbol="/") -> tuple:
    result = s.find(stop_symbol)
    if result >= 0:
        return True, result

    return False, None


def get_numbers_from_string(numbers_string, crop):
    if crop[0]:
        s = numbers_string[:crop[1]]
    else:
        s = numbers_string

    return s.split()


while not stop_symbol_is_in_string:
    user_string: str = input("Enter numbers: ")
    search_result: tuple = search_stop_symbol(user_string)
    stop_symbol_is_in_string = search_result[0]
    numbers: list = get_numbers_from_string(user_string , search_result)
    for number in numbers:
        summary += int(number)
    print(summary)
