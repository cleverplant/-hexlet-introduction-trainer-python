'''
В коде подключена функция random(). 
Она возвращает случайное число от 0 до 1 с большим количеством знаков после запятой. 
Но в реальных задачах бывает нужно получать случайные целые числа в заданном диапазоне.

Реализуйте код, который печатает на экран случайное число в диапазоне 
от 1 до 10 включительно. Для этого вам понадобятся операции умножения, сложения, 
а также преобразование типов. random() возвращает float, а нам нужен int.

Попробуйте решить это задание в одну строку.

Подсказка
random() возвращает число в диапазоне [0, 1). 
Такая запись обозначает, что 0 включается в диапазон, а 1 – нет.'''

'''================================================================================'''
# Синтаксис импортов будет изучаться позже на Хекслете
from random import random
# Функция, возвращающая случайное число
# print(random() * 1) # 0.09856613113197676
# print(random() * 10)  # 0.8839904367241888

# src/solution.py

# BEGIN (write your solution here)
print(int((random() * 1 + random() * 10) + 1))
# Решение учителя
print(int(random() * 10) + 1)
# END
