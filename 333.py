print(' ... ... ...\n')

def is_arguments_for_substr_correct(string, char, length):
    result_string = ''
    index = 0
    while index < length:
        result_string = (result_string + string[index]) # <= это мы извлекли строку начиная с index до length => (index < length) 
                                                        #    на длину извлекаемой строки --- length
        long_string = len(string) # <= считаем всю строку                                               
        trim_substring = result_string[char:] # <= извлекаем подстроку начиная с индекса char                                            
        number_char = len(trim_substring) # <= считаем обрезанную подстроку
        sum_trim_char = number_char + char
        index = index + 1
    return result_string # yesss

string = 'Sansa Stark'
print(is_arguments_for_substr_correct(string, 2, -3))   # => False
print(is_arguments_for_substr_correct(string, -1, 3))   # => False
print(is_arguments_for_substr_correct(string, 4, 100))  # => False
print(is_arguments_for_substr_correct(string, 10, 10))  # => False
print(is_arguments_for_substr_correct(string, 11, 1))   # => False
print(is_arguments_for_substr_correct(string, 3, 3))    # => True
print(is_arguments_for_substr_correct(string, 0, 5))    # => True