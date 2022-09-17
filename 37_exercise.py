# Conditions inside the loop body
# Условия внутри тела цикла

print('=== Функция из теории ===') 

def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index] == char:
            # Считаем только подходящие символы
            count = count + 1
        # Счётчик увеличивается в любом случае
        index = index + 1
    return count
print(count_chars('Fear cuts deeper than swords.', 'e')) # 4
# Если вы ничего не нашли, то результат — 0 совпадений
print(count_chars('Sansa', 'y')) # 0


'''Задание
Функция из теории учитывает регистр букв. 
То есть A и a с её точки зрения разные символы. 
Реализуйте вариант этой же функции, так чтобы регистр букв был не важен:'''

#  count_chars('HexlEt', 'e')  # 2
#  count_chars('HexlEt', 'E')  # 2

#  lower(): переводит строку в нижний регистр
#  upper(): переводит строку в вехний регистр

print(" === Решение учителя 1 ===: ")

def count_chars(string, char):
    index = 0 # инициализируем счетчик
    count = 0 # count увеличивается только в том случае, 
              # когда текущий рассматриваемый символ совпадает с ожидаемым
    while index < len(string):
        if string[index].upper() == char.upper():
            count = count + 1 # Считаем только подходящие символы
        index = index + 1 # Счётчик увеличивается в любом случае
    return count

print(count_chars('HexlEt', 'e'))    
print(count_chars('HexlEt', 'E')) 

'''_____________________________________
Реализуйте функцию is_contains_char(), которая проверят, содержит ли строка указанную букву. 
Регистр букв не важен. 
Функция принимает два параметра:

- Строка
- Буква для поиска

И возвращает результат проверки – булево значение.'''

# is_contains_char()
# print(is_contains_char('Hexlet', 'H'))  # => True
# print(is_contains_char('Hexlet', 'h'))  # => True
# print(is_contains_char('Awesomeness', 'd'))  # => False
# ==========================================================================================
print(''' === Решение учителя 2 ===: 
 v1 =======================''')

def is_contains_char(string, char): # Функция принимает два параметра: (Строка, Буква для поиска)
    index = 0 # инициализируем счетчик
    count = 0 # count увеличивается только в том случае, 
              # когда текущий рассматриваемый символ совпадает с ожидаемым
    while index < len(string):
        if string[index].upper() == char.upper(): # upper(): переводит строку в вехний регистр
            count = count + 1 # Считаем только подходящие символы
            return True
        index = index + 1 # Счётчик увеличивается в любом случае
    return False # и возвращает результат проверки – булево значение

print(is_contains_char('Hexlet', 'H'))  # => True
print(is_contains_char('Hexlet', 'h'))  # => True
print(is_contains_char('Awesomeness', 'd'))  # => False

print(" v2 =======================")
def is_contains_char(string, char): # Функция принимает два параметра: (Строка, Буква для поиска)
    index = 0 # инициализируем счетчик
    count = 0 # count увеличивается только в том случае, 
              # когда текущий рассматриваемый символ совпадает с ожидаемым
    while index < len(string):
        if string[index].upper() == char.upper(): # upper(): переводит строку в вехний регистр
            count = count + 1 # Считаем только подходящие символы
        index = index + 1 # Счётчик увеличивается в любом случае
    return bool(count) # и возвращает результат проверки – булево значение

print(is_contains_char('Hexlet', 'H'))  # => True
print(is_contains_char('Hexlet', 'h'))  # => True
print(is_contains_char('Awesomeness', 'd'))  # => False

print(" ===========================")