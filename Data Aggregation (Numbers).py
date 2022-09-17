# Data Aggregation (Numbers)
# Агрегирование данных (Цифры)

def sum_numbers_from_range(start, finish):
    # Технически можно менять start
    # Но входные аргументы нужно оставлять в исходном значении
    # Это сделает код проще для анализа
    i = start
    sum = 0  # Инициализация суммы
    while i <= finish:  # Двигаемся до конца диапазона
        sum = sum + i   # Считаем сумму для каждого числа
        i = i + 1       # Переходим к следующему числу в диапазоне
    # Возвращаем получившийся результат
    return sum

print(sum_numbers_from_range(1, 10))      # 1
print(sum_numbers_from_range(10, 100))  # 100

# Реализуйте функцию multiply_numbers_from_range(), 
# которая перемножает числа в указанном диапазоне включая границы диапазона. 
# Пример вызова:

def multiply_numbers_from_range(start, finish):
    i = start
    multiplication = 1
    while i <= finish:
        multiplication = multiplication * i
        i = i + 1
    return multiplication

print(multiply_numbers_from_range(1, 5))  # 1 * 2 * 3 * 4 * 5 = 120
print(multiply_numbers_from_range(2, 3))  # 2 * 3 = 6
print(multiply_numbers_from_range(6, 6))  # 6












