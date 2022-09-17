# Решение учителя:

# BEGIN
from unittest import result

def say_hurray_three_times():
    word = 'hurray!'
    return f'{word} {word} {word}'
# END

'''====================================================================='''

def save_email():
    # В реальности email приходит из формы
    email = '  SuppORT@hexlet.IO'
    # обрезаем пробельные символы
    trimmed_email = email.strip()
    prepared_email = trimmed_email.lower()
    print(prepared_email)
    # здесь будет запись в базу данных
save_email()
#  or
def save_email():
    # В реальности email приходит из формы
    email = '  SuppORT@hexlet.IO'
    # обрезаем пробельные символы
    trimmed_email = email.strip().lower() #  <====================
    print(trimmed_email)
    # здесь будет запись в базу данных
save_email()
#  ===============================================================

def greeting():
    return 'Hello, Hexlet!' # => None
greeting()
# Теперь мы можем использовать результат работы функции
message = greeting()
print(message) # => Hello, Hexlet!
# И даже выполнить какие-то действия над результатом
print(message.upper()) # => HELLO, HEXLET!
'''================================================================='''

def greeting_with_code_after_return():
    return 'Hello, Hexlet!'
    print('Я никогда не выполнюсь')
greeting_with_code_after_return()    
# ===================================================================
def greeting_with_code_after_return():
    return 'Hello, Hexlet!'
greeting_with_code_after_return()    
print('Я никогда не выполнюсь')
# ====================================================================

def greeting():
    return 'Hellooouoooooo, HexleeeEeet!' # => None
print(greeting())

# Вопрос: 1 из 3. Правильных ответов: 0
'''Что происходит, когда интерпретатор при выполнении кода 
   встречает оператор return?'''

#  На экран выводится значение и функция продолжает выполняться дальше
'''Функция возвращает значение и её выполнение на этом заканчивается'''
#  На экран ничего не выводится, но функция продолжает выполняться и 
#  после возврата значения

# Вопрос: 2 из 3. Правильных ответов: 1
'''Что вернёт функция, код которой приведён ниже:'''

def multiply(num1, num2):
    num1 * num2

'''Так как внутри функции не используется оператор return, 
   она неявно вернёт значение None'''
#  Результат умножения num1 на num2
#  Так как внутри функции не используется оператор return, она вернёт значение 0

# Вопрос: 3 из 3. Правильных ответов: 2
'''Что будет выведено на экран?'''

def multiply(num1, num2):
    num1 * num2
 
result = multiply(2, 2)
print(result)  # ?

#  Результат функции, которая ничего не возвращает, невозможно вывести на экран
'''На экран будет выведено значение None'''
#  Будет выведен результат умножения — число 4

'''=========================================================================='''
#  src/solution.py

'''Реализуйте функцию say_hurray_three_times(), которая возвращает строку 
hurray! hurray! hurray!'''

result = say_hurray_three_times()
print(result)  # => 'hurray! hurray! hurray!'

'''Вам не нужно вызывать свою функцию. Только определите её.'''
# Решение учителя:
# BEGIN
from unittest import result

def say_hurray_three_times():
    word = 'hurray!'
    return f'{word} {word} {word} {word}'
# END


