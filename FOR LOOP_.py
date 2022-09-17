# FOR LOOP
# ЦИКЛ FOR

'''Реализуйте функцию filter_string(), принимающую на вход строку и символ, 
и возвращающую новую строку, в которой удален переданный символ во всех его позициях.'''

def filter_string(text, char):
    index = 0
    result = ''
    while index < len(text):
        current_char = text[index]
        if current_char != char:
            result = f'{result}{current_char}'
        index += 1
    return result
text = 'If I look back I am lost'
filter_string(text, 'I')  # 'f  look back  am lost'
filter_string(text, 'o')  # 'If I lk back I am lst'

'''
Задание
В одном из предыдущих уроков мы уже написали функцию filter_string(). 
Напомним, она принимает на вход строку и символ и возвращает новую строку, 
в которой удалён переданный символ во всех его позициях. 
На этот раз реализуйте эту функцию с помощью цикла for. 
Дополнительное условие: регистр исключаемого символа не имеет значения.'''


print('===  Решение учителя:  ===')

text = 'If I look forward I win'

def filter_string(text, char):
    result = ''
    for current_char in text:
        if current_char.upper() != char.upper():
            result += current_char
    return result

print(filter_string(text, 'i'))  # 'f  look forward  wn'
print(filter_string(text, 'O'))  # 'If I lk frward I win'
















