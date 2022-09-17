# modules
# модули

'''
Вопрос: 1 из 6.
Как следует назвать файл модуля, содержащего математические константы?

  math_constants.py'''
# MathConstants.py
# mathconstatns.py
# mathConstants.py'''

'''
Вопрос: 2 из 6. 
Пусть у нас имеется модуль utils, в котором определена функция без аргументов с именем make_stuff. 
Модуль импортирован с помощью строчки:
import utils
Как следует вызывать функцию make_stuff ниже по коду?

  utils.make_stuff()'''
# make_stuff()

'''
Вопрос: 3 из 6. 
Пусть у нас имеется модуль app.py, в котором определена функция с именем run.
Выберите корректный вариант импорта самого модуля:

  import app'''
# import app.py
# from app import run'''

'''
Вопрос: 4 из 6. 
Пусть у нас имеется модуль helpers, в котором определена функция без аргументов с именем do_good. 
Функция импортирована с помощью строчки:
from helpers import do_good
Как следует вызывать функцию do_good ниже по коду?

  do_good()'''
# helpers.do_good()

'''
Вопрос: 5 из 6. 
Пусть у нас имеется модуль helpers.py, в котором определены две функции: start и finish.

Выберите корректный вариант импорта указанных функций:
(нужно выбрать все корректные ответы)

  from helpers import start, finish
  from helpers import finish, start'''
# from helpers import run, finish

'''
Вопрос: 6 из 6. 
Пусть у нас имеется модуль functions.py, в котором определены две функции: start и finish.
Выберите синтаксически корректный вариант импорта упомянутых функций:
(нужно выбрать все корректные ответы)


from functions import start
from functions import finish

from functions import finish, start

from functions import start, finish'''

# from functions.py import start, finish

# from functions.py import start
# from functions.py import finish

print('src/solution.py')

'''
Реализуйте функцию count_vowels(), 
которая принимает строку, считает и возвращает количество гласных букв в ней.

Для проверки, является ли буква гласной, 
импортируйте и используйте функцию is_vowel() из модуля symbols.py.'''

# is_vowel('a')  # True
# is_vowel('n')  # False
 
# count_vowels('One')  # 2
# count_vowels('London is the capital of Great Britain')  # 13

print('решение 1')

from symbols_40 import is_vowel

def count_vowels(text):
    result = 0
    for char in text:
        if is_vowel(char):
            result += 1
    return result

print(is_vowel('a')) # True
print(is_vowel('n')) # False

print(count_vowels('One')) # 2
print(count_vowels('London is the capital of Great Britain')) # 13

print('решение пользователей 1')
'-----------------------------------------------------------------'
from symbols_40 import is_vowel
def count_vowels(string):
    counter = 0
    for char in string:
        char = char.lower()
        if is_vowel(char):
            counter += 1
    return counter
'-----------------------------------------------------------------'
from symbols_40 import is_vowel
def count_vowels(string):
    vowel=0
    i=0
    while i<=len(string)-1:
        if is_vowel(string[i].lower())==True:
            vowel=vowel+1
            i=i+1
        return vowel

from symbols_40 import is_vowel
'-----------------------------------------------------------------'
def count_vowels(s):
    return sum(is_vowel(c) for c in s)

import symbols_40
'------------------------------------------------------------------'
def count_vowels(text):
    counts = 0
    for char in text:
        if symbols_40.is_vowel(char) == True:
            counts += 1
    return counts    
'---------------------------------------------------------------------'    

from symbols_40 import is_vowel

def count_vowels(text):
    res = 0
    for amount_char in text.lower():
      if amount_char in ("у", "е", "ы", "а", "о", "э", "я", "и", "ю", "a", "e", "i", "u", "y", "o"):
        res += 1
    return res
'----------------------------------------------------------------------'

def count_vowels(txt):
  return sum([1 for x in txt.lower() if x in 'aeiouаоэеиыуёюя'])
'----------------------------------------------------------------------'  
from symbols_40 import is_vowel

