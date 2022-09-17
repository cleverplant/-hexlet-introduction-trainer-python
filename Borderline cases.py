# Borderline cases
# Пограничные случаи

'''Реализуйте функцию-предикат is_arguments_for_substr_correct(), 
которая принимает три аргумента:

- строку; --- string
- индекс, с которого начинать извлечение; --- char
- длину извлекаемой подстроки. --- length

Функция возвращает False, если хотя бы одно из условий истинно:

1 - Отрицательная длина извлекаемой подстроки.( -trim_substring ) 
2 - Отрицательный заданный индекс. ( -char )
3 - Заданный индекс выходит за границу всей строки.   ( char > long_string    result_string ) 
4 - Длина подстроки в сумме с заданным индексом выходит за границу всей строки. sum_trim_char > result_string ---
                                                                                ( sum_trim_char = number_char + char ) 
5 - В ином случае функция возвращает True.

Не забывайте, что индексы начинаются с 0, 
поэтому индекс последнего элемента — это «длина строки минус 1».
'''
print(' ... ... ...\n')
'''
def is_arguments_for_substr_correct(string, end, length):
    result_string = ''
    index = 0
    while index < length:
        result_string = (result_string + string[index]) # <= это мы извлекли строку начиная с index до length => (index < length) 
                                                        #    на длину извлекаемой строки --- length
        long_string = len(string) # <= считаем всю строку                                               
        trim_substring = result_string[end:] # <= извлекаем подстроку начиная с индекса char                                            
        number_char = len(trim_substring) # <= считаем обрезанную подстроку
        sum_trim_char = number_char + end

        if trim_substring[0] == '-' : # Отрицательная длина извлекаемой подстроки.( -trim_substring ) 
            return bool(0)
        elif (str(end))[0] == '-' : # Отрицательный заданный индекс. ( -char )
            return bool(0)  
        elif end > long_string:  # Заданный индекс выходит за границу всей строки.   ( char > long_string    result_string )     
            return bool(0)
        elif sum_trim_char > long_string: # Длина подстроки в сумме с заданным индексом выходит за границу всей строки. sum_trim_char > long_string
            return bool(0)
        else: 
             return bool(1)                                                                  
    index = index + 1
'''   

def is_arguments_for_substr_correct(string, index, length):
    if index < 0:
        return False
    elif length < 0:
        return False
    elif index > len(string) - 1:
        return False
    elif index + length > len(string):
        return False
    return True




string = '-Sansa Stark'
print(is_arguments_for_substr_correct(string, 2, -3))   # => False
print(is_arguments_for_substr_correct(string, -1, 3))   # => False
print(is_arguments_for_substr_correct(string, 4, 100))  # => False
print(is_arguments_for_substr_correct(string, 10, 10))  # => False
print(is_arguments_for_substr_correct(string, 11, 1))   # => False
print(is_arguments_for_substr_correct(string, 3, 3))    # => True
print(is_arguments_for_substr_correct(string, 0, 5))    # => True

print(is_arguments_for_substr_correct(string, -1, 0))
print(is_arguments_for_substr_correct(string, 0, -1))
print(is_arguments_for_substr_correct(string, + 1, 0))
print(is_arguments_for_substr_correct(string, -2, 5))
print(is_arguments_for_substr_correct(string, -4, 1))
print(is_arguments_for_substr_correct(string, 3, 3))
print(is_arguments_for_substr_correct(string, 0, 3))
print(is_arguments_for_substr_correct(string, 0, 1))
print(is_arguments_for_substr_correct(string, 0, 0)) 




