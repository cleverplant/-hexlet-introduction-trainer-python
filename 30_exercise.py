# Logic
# Логика

'''
Вопрос: 1 из 3. Правильных ответов: 0
Что будет выведено на экран?'''

print(5 <= 5)

'''================================================================================================'''
#  src/solution.py

'''
Реализуйте функцию has_upper_case(), которая определяет, содержит ли строка заглавные буквы. 
Функция должна вернуть булево значение:

has_upper_case("")  # False
has_upper_case("python")  # False
has_upper_case("Hexlet")  # True

Подсказка
Воспользуйтесь методом из стандартной библиотеки, которая приводит строку к нижнему регистру. 
Чем отличается такая строка от исходной?'''

def has_upper_case(has_upper):
    return has_upper != has_upper.lower()

print(has_upper_case(""))  # False
print(has_upper_case("python"))  # False
print(has_upper_case("Hexlet"))  # True

#  Решение учителя

def has_upper_case(text):
    return text != text.lower()

print(has_upper_case(""))  # False
print(has_upper_case("python"))  # False
print(has_upper_case("Hexlet"))  # True



