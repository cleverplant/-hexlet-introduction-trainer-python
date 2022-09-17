string = 'furehjkli'
print(string[:4])

print('... \\\  ...')\

def reverse_string(string):
    i = len(string) - 1
    revers = ''

    while i >= 0:
        current_char = string[i]
        revers = revers + current_char
        i = i - 1
    return revers
print(reverse_string('Game Of Thrones')) # 'senorhT fO emaG'
print(reverse_string('')) # ''

def join_numbers_from_range(start, end):
    i = 0
    result = ''
    while i < end: # <= сцука. здесь надо было не <=, а просто <
        char = start[i]
        result = result + (char)
        i = i + 1
    return result

print(join_numbers_from_range('kjglkjhlkjlkjh', 1))  # '1'
print(join_numbers_from_range('kjglkjhlkjlkjh', 3))  # '23'
print(join_numbers_from_range('kjglkjhlkjlkjh', 5))  # '5678910'

def my_substr(string, long):
    index = 0
    revers = ''
    while index < long: # все таки, главное - это условие 
        current_char = string[index]
        revers = revers + current_char
        index = index + 1
    return revers 

string = 'If I look back I am lost'
print(my_substr(string, 1)) # => 'I' 
print(my_substr(string, 7)) # => 'If I lo'       


def my_substr(string, length):
    result_string = ''
    index = 0
    while index < length:
        result_string = result_string + string[index]
        index = index + 1

    return result_string
string = 'If I look back I am lost'
print(my_substr(string, 1)) # => 'I' 
print(my_substr(string, 7)) # => 'If I lo'       








