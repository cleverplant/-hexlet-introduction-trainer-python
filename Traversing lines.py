# Traversing lines
# Обход строк

def print_name_by_symbol(name):
    i = 0
    # Такая проверка будет выполняться до конца строки
    # включая последний символ. Его индекс `length - 1`.
    while i < len(name):
        # Обращаемся к символу по индексу
        print(name[i])
        i = i + 1

name = 'Arya'
print_name_by_symbol(name)
# => 'A'
# => 'r'
# => 'y'
# => 'a'
print('---- 77777 -----\n')

# Самое главное в этом коде, поставить правильное условие в while. 
# Это можно сделать сразу двумя способами: i < len(name) или i <= len(name) - 1. 
# Оба способа приводят к одному результату.

# Реализуйте функцию print_reversed_word_by_symbol(), 
# которая печатает переданное слово посимвольно, 
# как в примере из теории, но делает это в обратном порядке.

def print_name_by_symbol(name):
    i = len(name)
    
    while i < len(name):
        print(name[i])
        i = i - 1
name = 'Arya'
print_name_by_symbol(name)



'''
def print_numbers(number):
    i = number
    while i  > number: # <= условие
        print('i') 
        i = i - 1
print_numbers(5)
'''


