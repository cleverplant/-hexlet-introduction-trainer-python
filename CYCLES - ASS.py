# Python: Цикл While
print('... 1 ...\n')

def print_hello(n):
    counter = 0
    while counter < n:
        print('Hello!')
        counter = counter + 1
print_hello(3)
print('... 2 ...\n')

def print_numbers(last_number):
    i = 1
    while i <= last_number:
        print(i)
        i = i + 1
    print('finished!')

print_numbers(4)
print('... ... ... ... ...\n')

def print_numbers(number):
    i = number
    while i  > number: # <= условие
        print('i') 
        i = i - 1
    print('finished!')
print_numbers(5)
 

# Модифицируйте функцию print_numbers() так, чтобы она выводила числа в обратном порядке. 
# Для этого нужно идти от верхней границы к нижней. 
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# То есть счётчик должен быть инициализирован максимальным значением, 
# а в теле цикла его нужно уменьшать до нижней границы.

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



















































