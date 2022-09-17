# For Loop
# Цикл For

print('===  Вопрос: 1 из 3.  ===')
'''
Выберите верные утверждения
(нужно выбрать все корректные ответы)'''

# цикл while не может быть бесконечным
# в цикле for обязательно должны присутствовать все три элемента: счетчик, условие, изменение счетчика
'''
# цикл while может быть бесконечным
# цикл for перебирает все элементы объекта
# В цикле for нет счётчика и условия остановки цикла'''


print('===  Вопрос: 2 из 3.  ===')
'''
Функция sum() принимает ряд чисел (строку) и возвращает их сумму (сумму символов в строке). 
Добавьте недостающие части кода:'''

print('===  это правильное решение:  ===')
def sum(numbers):
    result = 0
    for num in numbers:
        result += int(num)

    return result

print(sum("12345"))  # 15

print('===  это НЕ правильное решение:  ===')
def sum(numbers):
    result = 0
    for num in numbers:  # for проходит по каждому символу в строке numbers, 
                         # num - переменная, в которую записывается текущий символ  
        result += 3                 # result = result + 3  # при прохождении каждого символа в строке прибавлем к нему 3
    return result            # и возвращаем результат

print(sum("12345"))

print('===  Задание:  ===')
#  src/solution.py

'''
Реализуйте функцию filter_string(). 
Она принимает на вход строку и символ и возвращает новую строку, 
в которой удалён переданный символ во всех его позициях. 
Если строка не содержит указанный символ, то она возвращается без изменений.

Итоговая строка также не должна содержать концевые пробелы:
Дополнительное условие: регистр исключаемого символа не имеет значения.'''

# text = 'If I look forward I win'
# filter_string(text, 'i')  # 'f  look forward  wn'
# filter_string(text, 'O')  # 'If I lk frward I win

text = 'If I look forward I win'
def filter_string(text, char):
    result = ''
    for current_char in text:
        if current_char != char:
            result += current_char
    return result.strip()

print(filter_string(text, 'i'))  # 'f  look forward  wn'
print(filter_string(text, 'O'))  # 'If I lk frward I win'

'''
Задание
В одном из предыдущих уроков мы уже написали функцию filter_string(). 
Напомним, она принимает на вход строку и символ и возвращает новую строку, 
в которой удалён переданный символ во всех его позициях. 
На этот раз реализуйте эту функцию с помощью цикла for. 
Дополнительное условие: регистр исключаемого символа не имеет значения.

Пример вызова:
'''
# text = 'If I look forward I win'
# filter_string(text, 'i')  # 'f  look forward  wn'
# filter_string(text, 'O')  # 'If I lk frward I win'

print('===  Решение учителя:  ===')

text = 'If I look forward I win'

def filter_string(text, char):
    result = ''
    for current_char in text:
        if current_char.upper() != char.upper():
            result += current_char
    return result

print(filter_string(text, 'i'))  # 'f  look forward  wn'
print(filter_string(text, 'O'))  # 'If I lk frward I win'


print('=== ======== ===')

def filter_string(text, char):
    index = 0
    result = ''
    while index < len(text):
        current_char = text[index]
        if current_char != char:
            result = f'{result}{current_char}'
        index += 1
    return result
text = 'If I look back I am lost'
filter_string(text, 'I')  # 'f  look back  am lost'
filter_string(text, 'o')  # 'If I lk back I am lst'


