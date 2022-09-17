# Data Aggregation (Rows)
# Агрегация данных (Строки)
print(' ---  uuu ---\n')

def print_name_by_symbol(name):
    i = 0
    # Такая проверка будет выполняться до конца строки
    # включая последний символ. Его индекс `length - 1`.
    while i < len(name):
        # Обращаемся к символу по индексу
        print(name[i])
        i = i + 1

name = 'Arya'
print_name_by_symbol(name)
# => 'A'
# => 'r'
# => 'y'
# => 'a'
print(' ---  rrr ---\n')

def print_name_by_symbol(name):
    i = len(name) - 1
    while i >= 0:
        print(name[i])
        i = i - 1

name = 'Arya'
print_name_by_symbol(name)
# => 'a'
# => 'y'
# => 'r'
# => 'A'
print(' ---  www ---\n')
def print_numbers(last_number):
    i = last_number
    while i > 0:
        print(i)
        i = i - 1
    print('finished!')
print_numbers(4)
# 4
# 3
# 2
# 1

print('========================символы исходной строки в обратном порядке===================')
# функция len(_______) Считает количество символов в строке

def reverse_string(string):
    index = len(string) - 1 # <— записываем в новую переменную индекс последнего символа строки 
                               # (напомним, что индексы начинаются с нуля)
                               # мое мнение: инициализируем последний символ в строке                               
    reversed_string = '' # <— инициализируем строку, куда будем записывать результат

    while index >= 0: # <— условие: повторяем тело цикла, пока текущий индекс не дошёл до 0, 
                      #               то есть до первого символа.

        current_char = string[index] # <= — берём из строки символ по текущему индексу
        reversed_string = reversed_string + current_char # <— записываем в строку-результат новое значение: 
                                                         #    текущая строка-результат + новый символ.
        # То же самое через интерполяцию
        # reversed_string = f'{reversed_string}{current_char}'
        index = index - 1 # <— обновляем счётчик 

    return reversed_string # 

print(reverse_string('Game Of Thrones'))  # 'senorhT fO emaG'
# Проверка нейтрального элемента
reverse_string('')  # ''

print('============================================================================')

