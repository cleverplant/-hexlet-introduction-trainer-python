#  src/solution.py
'''
   Задание нужно читать внимательно = 
   сказано получить - print(result) 
   а не             - print(f'{result} {result} {result}')
'''

def say_hurray_three_times():
    return 'hurray!'
result = say_hurray_three_times()
print(f'{result} {result} {result}')  # => 'hurray! hurray! hurray!'
# =============================================================================
# BEGIN
def say_hurray_three_times():
    word = 'hurray!'
    return f'{word} {word} {word}'
 
result = say_hurray_three_times()
print(result)  # => 'hurray! hurray! hurray!'
# END
# =============================================================================
# BEGIN
def say_hurray_three_times():
        return 'hurray! ''hurray! '
 
result = say_hurray_three_times()
print(result)  # => 'hurray! hurray! hurray!'
# END
# =============================================================================
'''Реализуйте функцию say_hurray_three_times(), которая возвращает строку 
hurray! hurray! hurray!'''

# result = say_hurray_three_times()
# print(result)  # => 'hurray! hurray! hurray!'

