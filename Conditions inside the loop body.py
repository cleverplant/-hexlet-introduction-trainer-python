# Conditions inside the loop body
#  Условия внутри тела цикла

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

# Функция из теории учитывает регистр букв. 
# То есть A и a с её точки зрения разные символы. 
# Реализуйте вариант этой же функции, так чтобы регистр букв был не важен:
print('... Ваше решение:/n')

def count_chars(string, char):
    index = 0
    count = 0
    string = string.upper()
    char = char.upper()
    while index < len(string):
        if string[index] == char:
            # Считаем только подходящие символы
            count = count + 1
        # Счётчик увеличивается в любом случае
        index = index + 1
    return count
print(count_chars('HexlEt', 'e'))  # 2  
print(count_chars('HexlEt', 'E'))  # 2

print('... Решение учителя:/n')

def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index].upper() == char.upper():
            count = count + 1
        index = index + 1
    return count
print(count_chars('HexlEt', 'e'))  # 2  
print(count_chars('HexlEt', 'E'))  # 2


