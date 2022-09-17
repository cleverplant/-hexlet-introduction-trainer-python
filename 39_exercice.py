# Debugging
# Отладка

'''========================================================================
Вопрос: 1 из 10.
Какие шаги нужно выполнить при анализе ошибки?
(нужно выбрать все корректные ответы)'''

#  Сразу просить помощи
#  Менять код методом тыка
'''Найти в трейсбэке файл и строчку в нем, на которой произошла ошибка'''
'''Перевести сообщение об ошибке'''

'''========================================================================
Вопрос: 2 из 10. 
SyntaxError означает, что в программе произошла…'''

'''Ошибка, возникающая из-за неверного синтаксиса, например, забытой скобки или точки с запятой'''
#  Логическая ошибка; программа работает, но выдает неверный результат
#  Ошибка деления на ноль

'''Вопрос: 3 из 10.======================================================== 
Как правильно искать ошибку в коде?'''

'''
  Нужно отслеживать изменения переменных и результаты выполнения операций до тех пор, 
  пока не будет найдено место, которое ведёт себя не так, как ожидалось'''
# Нужно менять код случайным образом до тех пор, пока он не заработает
# Нужно долго на него смотреть, пока в голову не придёт решение'''

'''Вопрос: 4 из 10.=========================================================
Возможно ли допустить в одной строке кода разные виды ошибок?'''


'''Да! Программирование — это здорово!'''
#  Нет! Одна строка — одна ошибка, максимум.

'''Вопрос: 5 из 10.========================================================= 
Рассмотрите такой код:'''

# def func()
#     a = 120.333
#     return 10 * a

'''Eсть ли тут ошибки? Если да, то какого типа?'''
#  Ошибок нет
'''SyntaxError на строке 1'''
#  NameError на строке 3

'''Вопрос: 6 из 10.========================================================== 
Рассмотрите такой код (переменная b не определена глобально):'''

def func():
    a = 120.333
#   return 10 * a * b

'''Есть ли тут ошибки? Если да, то какого типа?'''
#  Ошибок нет
'''NameError ("name 'b' is not defined") на строке 3'''
#  SyntaxError на строке 1

'''Вопрос: 7 из 10.===================================================== 
Проанализируйте код функции, вычисляющей квадрат суммы двух чисел:'''

def square_of_sum(a, b):
    return (a - b) ** 2
'''Есть ли тут ошибки? Если да, то какого типа?'''

'''В коде логическая ошибка (неверный алгоритм расчёта)'''
#  NameError ("name 'b' is not defined") на строке 2
#  Ошибок нет
#  SyntaxError на строке 1'''

'''Вопрос: 8 из 10.======================================================= 
Проанализируйте код функции, вычисляющей квадрат суммы двух чисел:'''

def square_of_sum(a, b):
    return (a ** 2) + (2 * a * b) + (b ** 2)

#  Есть ли тут ошибки? Если да, то какого типа?
#  В коде логическая ошибка (неверный алгоритм расчёта)
#  NameError ("name 'b' is not defined") на строке 2
#  SyntaxError на строке 1
'''Ошибок нет'''

'''Вопрос: 9 из 10.======================================================================== 
Что нужно делать в любой непонятной ситуации?'''

#  Медитировать
'''Выводить значения на экран'''
#  Гадать

'''Вопрос: 10 из 10.======================================================================== 
Как поступить, если мы хотим вывести значения на экран только в определённых ситуациях?'''

#  Распечатывать всё и искать в выводе то, что нас интересует
'''Добавить условие, в которое обернуть вызов печати на экран'''
#  Пытаться догадаться, чему будут равны значения в этих ситуациях

'''============================================================================'''

'''
Палиндром — слово или текст, одинаково читающиеся в обоих направлениях. Примеры:

- "я",
- "радар",
- "асса",
- "ишак ищет у тещи каши"'''

print('src/solution.py')
#  src/solution.py
'''
Реализуйте функцию is_palindrome(), которая принимает на вход слово, 
определяет является ли оно палиндромом и возвращает логическое значение.'''

# from solution import is_palindrome
# is_palindrome('')  # True пустая строка тоже считается палиндромом
# is_palindrome('radar') # True
# is_palindrome('a') # True
# is_palindrome('abs') # False
# is_palindrome('ишак ищет у тещи каши') # True

print('''ЗАДАНИЕ 
v1
''')

def is_palindrome(text):
    revers = text
    return revers == text[::-1]
print(is_palindrome(''))
print(is_palindrome('radar'))
print(is_palindrome('a'))
print(is_palindrome('abs'))
print(is_palindrome('ишак ищет у тещи каши'))
# Alternative solution
# def is_palindrome(string):
# return string == string[::-1]
print('# Alternative solution')
# =================================================
print('''ЗАДАНИЕ 
v2
''')

def is_palindrome(string):
    pointer1 = 0
    pointer2 = len(string) - 1
    while pointer2 - pointer1 > 0:
        if string[pointer1] != string[pointer2]:
            return False
        pointer1 += 1
        pointer2 -= 1
    return True
print(is_palindrome(''))
print(is_palindrome('radar'))
print(is_palindrome('a'))
print(is_palindrome('abs'))
print(is_palindrome('ишак ищет у тещи каши'))    

print('============================================')

print('Задание 1')

'''Задание
Реализуйте функцию is_palindrome(), которая определяет, является ли слово палиндромом или нет.
Палиндром - это слово, которое читается одинаково в обоих направлениях. 
Слова в функцию могут быть переданы в любом регистре, 
поэтому сначала нужно привести слово к нижнему регистру:'''
#  word.lower().

#  is_palindrome('шалаш') # true
#  is_palindrome('хекслет') # false
#  is_palindrome('Довод') # true
#  is_palindrome('Функция') # false

def is_palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]

print(is_palindrome('шалаш'))  
print(is_palindrome('хекслет'))
print(is_palindrome('Довод'))
print(is_palindrome('Функция'))

print('Задание 2')
'''Реализуйте функцию is_not_palindrome(), которая проверяет что слово НЕ является палиндромом:'''

#  is_not_palindrome('шалаш') # false
#  is_not_palindrome('Ага') # false
#  is_not_palindrome('хекслет') # true
#  Для этого, вызовите функцию is_palindrome() внутри is_not_palindrome() и примените отрицание.

def is_not_palindrome(word):
    return not is_palindrome(word)
print(is_not_palindrome('шалаш'))  
print(is_not_palindrome('Ага'))
print(is_not_palindrome('хекслет'))

print('Задание ===========================')









