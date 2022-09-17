# Conditional constructions
# Условные конструкции

'''Вопрос: 1 из 4. Правильных ответов: 0
Дан код:'''

'''
if a > 100:
    something
elif a == 95:
    something_different
elif a == 90:
    something_different_yet
else:
    something_else
'''    
# Что будет, если ни одно условие из блоков if и elif не будет истинным?

''' будет выполнена инструкция something_else'''
#   компьютер зависнет
#   будет выполнена инструкция something_different_yet
'''================================================================================================'''

from ast import Return


def get_type_of_sentence(a):
    var = a 
    if a > 100:
      var = 'something'
    elif a == 95:
       var = 'something_different'
    elif a == 90:
       var = 'something_different_yet'
    else:
     var = 'something_else'
    return 'Resultat => ' + var 
print('v1 ' + get_type_of_sentence(101))      
print('v2 ' + get_type_of_sentence(95))     
print('v3 ' + get_type_of_sentence(90))     
print('v4 ' + get_type_of_sentence(80))     

'''================================================================================================='''

'''Вопрос: 2 из 4. Правильных ответов: 1
Проанализируйте следующий код (см. «Тернарный оператор» в тексте урока):

num = 6
result = num + 1 if num % 2 != 0 else 1 - num
print(result)
Что будет выведено на экран?

'''
#  Интерпретатор выведет ошибку
'''-5'''
#  7
#  16
#  True
#  17

num = 6
result = num + 1 if num % 2 != 0 else 1 - num
print(result)

'''============================================================================================'''

'''Вопрос: 3 из 4. Правильных ответов: 2
Дан код:

if temperature > 10:
    return temperature
elif temperature < 10:
    return 0
Изменится ли функциональность, если поменять местами условия таким образом:

if temperature < 10:
    return 0
elif temperature > 10:
    return temperature
    '''
def get_type_of_sentence(temperature):
    if temperature > 10:
        return 0
    elif temperature < 10:
        return temperature
print(get_type_of_sentence(150))
print(get_type_of_sentence(7))
#  ================================================================================================
def get_type_of_sentence(temperature):
    if temperature < 10:
        return temperature
    elif temperature > 10:
        return 0
print(get_type_of_sentence(150))
print(get_type_of_sentence(7))

'''================================================================================================'''
'''Вопрос: 4 из 4. Правильных ответов: 3
Дан код:

if temperature > 10:
    return temperature
elif temperature < 10:
    return 0
Изменится ли функциональность, если изменить elif на else?
'''
#  Да
#  Нет

def get_type_of_sentence(temperature):
    if temperature > 10:
        return temperature
    elif temperature < 10:
        return 0
print(get_type_of_sentence(150))
print(get_type_of_sentence(7))
print("Изменится ли функциональность, если изменить elif на else?")
#  =====================================================================================
def get_type_of_sentence(temperature):
    if temperature > 10:
        return temperature
      # else  temperature < 10:
# => вообще не работает - "Expected expression - Ожидаемое выражение" else  temperature < 10:
        return 0
print(get_type_of_sentence(150))
print(get_type_of_sentence(7))
'''================================================================================================'''
#  src/solution.py
'''
Реализуйте функцию normalize_url(), которая выполняет так называемую нормализацию данных. 
Она принимает адрес сайта и возвращает его с https:// в начале.

Функция принимает адреса в виде:

АДРЕС
http://АДРЕС
https://АДРЕС (уже нормализованный)
и всегда возвращает адрес в виде https://АДРЕС.'''

#  normalize_url('https://ya.ru')  # 'https://ya.ru'
#  normalize_url('google.com')     # 'https://google.com'
#  normalize_url('http://ai.fi')   # 'https://ai.fi'

'''Подсказка
Можно сравнить первые 7 символов адреса со строкой http://. 
Для этого потребуется получить кусок строки или отбросить ненужный. 
Мы рассматривали способ получения части строки её начала:
'''
# Берём 2 символа от начала
#print('Python'[:2])  # 'Py'
 
# Отбрасываем первые 2 символа
# print('Python'[2:])  # 'thon'

'''================================================================================================'''

#  РЕШЕНИЕ УЧИТЕЛЯ






def normalize_url(url):
    https = 'https://'
    if url[:8] == https:
        return url
    elif url[:7] == 'http://':
        return https + url[7:]
    else:
        return https + url

print(normalize_url('https://ya.ru'))  # 'https://ya.ru'
print(normalize_url('google.com'))     # 'https://google.com'
print(normalize_url('http://ai.fi'))   # 'https://ai.fi'

