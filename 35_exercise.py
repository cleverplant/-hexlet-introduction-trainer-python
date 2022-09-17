# Data aggregation
# Агрегация данных

'''Числа'''
#  Задание
#  Реализуйте функцию multiply_numbers_from_range(), 
#  которая перемножает числа в указанном диапазоне включая границы диапазона. 
#  Пример вызова:

# multiply_numbers_from_range(1, 5)  # 1 * 2 * 3 * 4 * 5 = 120
# multiply_numbers_from_range(2, 3)  # 2 * 3 = 6
# multiply_numbers_from_range(6, 6)  # 6

#  Решение учителя:
def multiply_numbers_from_range(start, finish):
    i = start
    result = 1
    while i <= finish:
        result = result * i
        i = i + 1
    return result
print(multiply_numbers_from_range(1, 5))  # 1 * 2 * 3 * 4 * 5 = 120
print(multiply_numbers_from_range(2, 3))  # 2 * 3 = 6
print(multiply_numbers_from_range(6, 6))  # 6


'''Строки'''
#  Задание
#  Реализуйте функцию join_numbers_from_range(), которая объединяет все числа из диапазона в строку:

#  join_numbers_from_range(1, 1)   # '1'
#  join_numbers_from_range(2, 3)   # '23'
#  join_numbers_from_range(5, 10)  # '5678910'

#  Решение учителя:
def join_numbers_from_range(start, end):
    i = start
    result = ''
    while i <= end:
        result = result + str(i)
        i = i + 1
    return result

'''========================================================================='''    
'''
Вопрос: 1 из 3. Правильных ответов: 0
Какой нейтральный элемент у операции умножения?'''
#  0
#  "" (пустая строка)
#  Эта операция не имеет нейтрального элемента
'''1''' 
'''========================================================================='''  
'''
Вопрос: 2 из 3. Правильных ответов: 1
Функция multiply_numbers_from_range() перемножает числа указанного диапазона. 
Дополните недостающие места в коде:'''

def multiply_numbers_from_range(start, finish):
    i = start
    multiply = 1

    while i <= finish:
        multiply *= i  # => multiply *= x  => multiply =  multiply * x

        i += 1
    return multiply

print(multiply_numbers_from_range(3, 5))  # 60 => 3 * 4 * 5 = 60

print('===  v 1  ==============================================================')

def multiply_numbers_from_range(start, finish):
    i = start
    result = 1
    while i <= finish:
        result = result * i
        i = i + 1
    return result
print(multiply_numbers_from_range(1, 5))  # 1 * 2 * 3 * 4 * 5 = 120
print(multiply_numbers_from_range(2, 3))  # 2 * 3 = 6
print(multiply_numbers_from_range(6, 6))  # 6
print(multiply_numbers_from_range(3, 5))  # 60 => 3 * 4 * 5 = 60

print('===   v 2  ==============================================================')

'''Вопрос: 3 из 3. Правильных ответов: 2
Какие типы данных можно собирать (агрегировать) в цикле?
(нужно выбрать все корректные ответы)

   строки
   числа'''
#  цикл не предназначен для агрегации данных

#  src/solution.py
'''
Реализуйте функцию join_numbers_from_range(), которая объединяет все числа из диапазона в строку:

join_numbers_from_range(1, 1)  # '1'
join_numbers_from_range(2, 3)  # '23'
join_numbers_from_range(5, 10)  # '5678910'
'''
def join_numbers_from_range(start, end):
    i = start
    result = ''
    while i <= end:
        result = result + str(i)
        i = i + 1
    return result
print(join_numbers_from_range(1, 1))  # '1'
print(join_numbers_from_range(2, 3))  # '23'
print(join_numbers_from_range(5, 10))  # '5678910'








'''==========================================================================================='''



