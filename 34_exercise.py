#  #  Цикл while
print('========================================================================')
def print_hello(n):
  counter = 0
  while counter < n:
    print('Hello!')
#   print('Holla!')
    counter = counter + 1

print_hello(2)
print('========================================================================')
# => Hello!
# => Hello!

def print_numbers(last_number):
  
  i = 1
  while i <= last_number:
      print(i)
      i = i + 1
  print('finished!')

print_numbers(3)
print('========================================================================')
# => 1
# => 2
# => 3
# => finished!
'''===================================================================================='''
#  Решение учителя:
def print_numbers(last_number):
    i = last_number
    while i > 0:
        print(i)
        i = i - 1
    print('finished!')
'''====================================================================================='''
'''Вопрос: 1 из 5. Правильных ответов: 0
Возможно ли, чтобы код внутри цикла while ни разу не выполнился?'''

'''
Возможно. Проверка условия выполняется до выполнения, 
и если условие ложное, то код из тела цикла выполняться не будет'''
#  Нет, невозможно. Код в цикле выполняется как минимум один раз
'''====================================================================================='''
'''Вопрос: 2 из 5. Правильных ответов: 1
Возможны ли бесконечные циклы?'''

'''Да, если условие всегда остаётся истинным'''
# Нет, условие всегда меняется, так что в какой-то момент оно обязательно станет ложным
'''====================================================================================='''
'''Вопрос: 3 из 5. Правильных ответов: 2
Выберите верное утверждение:
(нужно выбрать все корректные ответы)'''


''' Циклы полезны, когда нужно повторять какие-то действия, 
    и количество таких повторений заранее неизвестно# '''
#  Если в коде есть бесконечный цикл, то интерпертатор автоматически остановит его
''' Нельзя определить цикл с пустым телом. Интерпретатор выдаст ошибку IndentationError'''
'''====================================================================================='''
'''Вопрос: 4 из 5. Правильных ответов: 3
Запишите начальное значение a, чтобы после выполнения кода a было равно 0?

a = 

a -= 8 - a   →  a = a - 8 - a'''
'''========================================================================================'''
'''
Вопрос: 5 из 5. Правильных ответов: 3
Что будет выведено на экран?'''

a = 5
a -= 4  #  →  a = a - 4 => a = 5 - 4 => a = 1
a += 1  #  →  a = a + 1 => a = 1 + 1 => a = 2
print(a)
print('========================================================================')

'''2'''
#  4
#  1
#  5

#  a = a + 1 → a += 1
#  a = a - 1 → a -= 1
#  a = a * 2 → a *= 2
#  a = a / 1 → a /= 1
'''
Вопрос: 4 из 5. Правильных ответов: 4
Запишите начальное значение a, чтобы после выполнения кода a было равно 0?'''

a = 4
a -= 8 - a   #  →  a = (a - 8) - a => a = 
print(a)

''' ни хрена не поял - как вычеслить математически ???'''
'''==========================================================================='''
#  src/solution.py
'''
Модифицируйте функцию print_numbers() так, чтобы она выводила числа в обратном порядке. 
Для этого нужно идти от верхней границы к нижней. 
То есть счётчик должен быть инициализирован максимальным значением, 
а в теле цикла его нужно уменьшать.'''

#  print_numbers(4)
# => 4
# => 3
# => 2
# => 1
# => finished!
print('========================================================================') 
#   Решение учителя:
def print_numbers(last_number):
    i = last_number
    while i > 0: # <============ !!!!!!!!!!!!!!!!!!!
        print(i)
        i = i - 1
    print('finished!')
print_numbers(4)

print('========================================================================')

def print_numbers(last_number):
  i = 1 # <====================== !!!!!!!!!!!!!!!!!!!
  while i <= last_number:
      print(i)
      i = i + 1
  print('finished!')
print_numbers(4)

print('''... ... ... ... ...''')

