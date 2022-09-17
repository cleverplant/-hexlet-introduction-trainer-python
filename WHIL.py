print('..Ваше решение:....')

def print_numbers(last_number):
    i = 0
    number = last_number
    while i < last_number: # <= привязка к last_number, как в примере - сбило с толку, а надо было i > 0
        print(number) 
        number = number - 1
        i = i + 1
    print('finished!')
print_numbers(4)

print('..Решение учителя:....')

def print_numbers(last_number):
    i = last_number
    while i > 0:
        print(i)
        i = i - 1
    print('finished!')
print_numbers(4)
'''
print('... ПРИМЕР .......')

def print_numbers(last_number):
  i = 1
  while i <= last_number:
      print(i)
      i = i + 1
print_numbers(4)
'''
