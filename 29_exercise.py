# Environment
# Окружение

'''
Вопрос: 1 из 3. Правильных ответов: 0
Выполнится ли такой код?'''

from traceback import print_stack


one = 1
 
def print_one():
    print(one)
 
print_one()

'''Да. На экран будет выведено число 1, так как внутри функции мы можем использовать переменные, 
   которые определены за её пределами'''
#  Нет. Интерпретатор выдаст ошибку, так как переменная определена за пределами функции
#  Не сработает. Переменные должны именоваться капслоком, тогда они будут видны в теле функции.
'''============================================================================================'''
'''
Вопрос: 2 из 3. Правильных ответов: 1
Что будет выведено на экран?'''

men_count = 10
women_count = 15
 
def get_people_count():
    men_count = 5
    women_count = 5
 
    print(men_count + women_count) # <==== 1 
print('v1')    
#   10
#   25
''' Ничего. Чтобы что-то вывелось на экран, функцию нужно вызвать'''
men_count = 10
women_count = 15
 
def get_people_count():
    men_count = 5
    women_count = 5
get_people_count() 
print(men_count + women_count) # <==== 25
print('v2')   
'''======================================================================================'''

men_count = 10
women_count = 15
 
def get_people_count():
    men_count = 5
    women_count = 5
    print(men_count + women_count) # <==== 20    
get_people_count() 
print('v3')   
'''======================================================================================='''

'''Вопрос: 3 из 3. Правильных ответов: 2
Что будет выведено на экран?'''

men_count = 10
women_count = 15
 
def get_people_count():
    men_count = 5
    print(men_count + women_count)
get_people_count()
print('v4')
#  10
#  5
#  Ничего. Интерпретатор выдаст ошибку NameError
'''20'''
#  25

'''==============================================================================================='''
#  src/solution.py
'''
Это задание не связано напрямую с уроком, это просто еще одно полезное упражнение по работе с функциями.
Напишите функцию get_age_difference(), которая принимает два года рождения и возвращает строку с разницей 
в возрасте в виде The age difference is 11. Пример работы функции:

actual = get_age_difference(2001, 2018)
print(actual)  # => The age difference is 17
'''
# Мое решение
def get_age_difference(x,y):
    return 'The age difference is ' + str(abs(y - x)) # <===== забыл поставить абсолютное значение в str(y - x)
actual = get_age_difference(2001, 2012)
print(actual)

#  Решение учителя
def get_age_difference(year_one, year_two):
    difference = abs(year_one - year_two)
    return f"The age difference is {difference}"
actual = get_age_difference(2001, 2012)
print(actual)
'''==============================================================================='''





