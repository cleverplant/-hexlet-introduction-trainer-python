# Return from Cycles
# Возврат из циклов

def is_contains_char(string, char):
    index = 0
    while index < len(string):
        if string[index] == char:
            return True
        index += 1
    return False
print(is_contains_char('Hexlet', 'H'))  # => True
print(is_contains_char('Hexlet', 'h'))  # => False
print(is_contains_char('Awesomeness', 'm'))  # => True
print(is_contains_char('Awesomeness', 'd'))  # => False








