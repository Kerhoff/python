# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
#    Вывести каждое слово с новой строки.
#    Строки необходимо пронумеровать.
#    Если в слово длинное, выводить только первые 10 букв в слове.

# Get string
string: str = input("Enter your phrase: ")

# Split string to words by space
words: list = string.split()

# Print first 10 letter of each word on new line
for word in words:
    print(word[:9])
