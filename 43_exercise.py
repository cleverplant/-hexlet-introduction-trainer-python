# random module
# Модуль random

print('src/solution.py')
'''
Реализуйте функцию choice_from_range(), 
которая принимает строку-набор и выбирает случайный символ по индексу 
из ограниченного диапазона.

Аргументы функции:
- строка-набор
- начальный индекс диапазона
- конечный индекс диапазона
'''
text = "abcdef"
# choice_from_range(text, 3, 5)  # d
# choice_from_range(text, 3, 5)  # f
# choice_from_range(text, 3, 5)  # e

print('решение учителя')

import random

# BEGIN (write your solution here)
def choice_from_range(text, begin, end):
    return text[random.randint(begin, end)]

print(choice_from_range(text, 3, 5))  # d
print(choice_from_range(text, 3, 5))  # f
print(choice_from_range(text, 3, 5))  # e


# END


