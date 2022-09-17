

from os import times


print('---22---------------------------------------------------')
info = "We couldn't verify your mother's maiden name."
intro = "Here is important information about your account security."

first_name = 'Joffrey'
greeting = 'Hello'

print(greeting + ','  + ' ' + first_name + '!')
print(intro)
print(info)
print('\n')

print(greeting + ", " + first_name + "!")
print(intro + "\n" + info)

print('---23---------------------------------------------------')

king = "Rooms in King Balon's Castle:"
# Комнаты в замке короля Балкона:

# BEGIN (write your solution here)
count_king = 6
count_palace = 17
print(king + '\n' + str(count_king * count_palace))
# END

print('---24---------------------------------------------------')

first_name = 'Joffrey'
greeting = 'Hello'

print(f'{greeting}, {first_name}! - "Hexlet!" - Hexlet! ')

stark = 'Arya'
# BEGIN (write your solution here)
print(f'Do you want to eat, {stark}?')
# END
print('---25--------------------------------------------------')
magic = '\nyou'
print(magic[1]) # => y

name = 'Na\nharis'

# BEGIN (write your solution here)
print(name)
print(name[-1])
print(name[7])
# END
print('---26--------------------------------------------------')

value = '12-08-2034'

print(value[6]) # => 2
print(value[9]) # => 4
print(value[6] + value[9]) #  => 24
print(value[6:10]) # => 2034

print('---27--------------------------------------------------')
# переворот строки:

value = 'Hexlet'
# Пропускаем обе границы
print(value[::-1]) # 'telxeH'

# BEGIN (write your solution here)
print(value[-4:5]) # => xle
print(value[2:5])  # => xle
# END
print('---28--------------------------------------------------')

a = 'A'
b = 'B'

# Слева добавился f
text = f'''{a} и {b}
сидели на трубе
'''
print(text)

print('---29--------------------------------------------------')
string = '-0.304 '
print(float(string))

print('---30--------------------------------------------------')

print(int('7') - (-8 - -2))

print('---31--------------------------------------------------')
# Bам даны три переменные с фамилиями разных людей. 
# Составьте и выведите на экран слово из символов в таком порядке:
'''
Третий символ из первой строки
Второй символ из второй строки
Четвертый символ из третьей строки
Пятый символ из второй строки
Третий символ из второй строки'''

# Попробуйте использовать интерполяцию: 
# внутри фигурных скобок можно помещать не только целые переменные, 
# но и отдельные символы с помощью квадратных скобок.

one = 'Naharis'
two = 'Mormont'
three = 'Sand'

# BEGIN (write your solution here)
print(f'{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}')
# END

print('---32--------------------------------------------------')
value = 2.9

# BEGIN (write your solution here)
print(f'{int(value)} times')
# END

# BEGIN
int_value = int(value)
str_value = str(int_value)
print(str_value + ' times')
# END

print('---33--------------------------------------------------')
print()
company1 = 'Apple'
company2 = 'Samsung'

# BEGIN (write your solution here)
print(len(company1) + len(company2))
# END
print('---34--------------------------------------------------')
print()

print('модуль числа - это абсолютное значение. количественный показатель. сумма чисел не учитывая знаков')
print(pow(2,3))
print(pow(2,3,5))

number = 255

# BEGIN (write your solution here)
print(hex(number))
# END
print('---35--------------------------------------------------')
print()

print(round(10.25, 0))
print(round(10.1234, 2))

number = 10.1234

print(round(number, 2))

print('---36--------------------------------------------------')
print()

name = 'python'
print(len(name) - 1) # 5

print('---37--------------------------------------------------')
print()

# Задание
# Выведите на экран первую и последнюю буквы предложения, 
# записанного в переменную text, в следующем формате:
# First: N
# Last: t

# Постарайтесь создать только одну переменную, 
# в которую сразу запишется нужный текст перед печатью на экран. 
# В этом уроке мы отрабатываем умение собирать составное выражение.

text = 'Never forget what you are, for surely the world will not'

# count_text = len(text)                         # это общее количество символов - 56
# first_letter = len(text) - (len(text) - 1) - 1 # это первый символ в строке 
                                               # { -1 в конце выражения, потому что индекс в строках считают 0}
                                               # first_letter = count_text - two_letter
# last_letter = len(text) - 1                    # это последний символ в строке - 55

print('First: ' + text[(len(text) - (len(text) - 1))-1])
print('Last: ' + text[len(text) - 1])

print("---  или РЕШЕНИЕ УЧИТЕЛЯ  ---")

text = 'Never forget what you are, for surely the world will not'

# BEGIN
result = f'First: {text[0]}\nLast: {text[-1]}'
print(result)
# END

print('---38--------------------------------------------------')
print()
print(min(3, 10, 22, -3, 0))

print('---39--------------------------------------------------')
print()
  
# Задание 
# Функция random() возвращает случайное число от 0 до 1 с большим количеством знаков после запятой.
# Реализуйте код, который выводит на экран случайное целое число в диапазоне от 0 до 10. 
# Для этой задачи вам понадобится функция random() и функция round(), которая округляет переданное ей значение

from random import random


# random_number = random() * 10
# round_number = round(random_number) 
# print(round_number)

print(round(random() * 10))

print('---41--------------------------------------------------')
print()

name = 'Python'

# Возвращает индекс первого вхождения буквы в строку
name.find('t') # 2
# Переводит в нижний регистр
name.lower() # 'python'
print(name.replace('on', 'off')) 
print(name.replace('on', 'off')) # 'Pythoff'

print(len.__doc__)

print('---42--------------------------------------------------')
print()

name = 'Tirion'
print(name.upper()) # => TIRION
print(name) # => ?

# Задание
# Данные, вводимые пользователями, часто содержат лишние пробельные символы в конце или начале строки. 
# Обычно их вырезают с помощью метода .strip(), например, было: ' hello\n ', стало: 'hello'.
# Обновите переменную first_name, записав в неё то же самое значение, но обработанное методом .strip(). 
# Распечатайте то, что получилось, на экран.

first_name = '  Grigor   \n'

# BEGIN (write your solution here)
first_name = first_name.strip()
print(first_name)
# END()

print(first_name.strip()) # <= а вот так нельзя было, потому что в задании сказано  - обновить переменную first_name,
                              #  записав в неё то же самое значение, но обработанное методом .strip(). 

print('---43--------------------------------------------------')
print()

# Задание
# Найдите символы N и , (запятая) внутри текста в переменной text. 
# Выведите на экран их индексы. Ожидаемый тестами вывод:

# Index Of N: 0
# Index Of ,: 25
# Ваша задача найти эти индексы в строке с помощью метода .find() и вставить в print(), 
# не используя промежуточные переменные. 
# Для разбиения вывода на две строки, вам может понадобится \n.

text = 'Never forget what you are, for surely the world will not'

# BEGIN (write your solution here)
print('Index Of N: ' + str(text.find("N")) + '\n' + 'Index Of ,: ' + str(text.find(",")))
# END

# BEGIN
print(f"Index Of N: {text.find('N')}\nIndex Of ,: {text.find(',')}")
# END

print('---44--------------------------------------------------')
print()

name = 'Tirion';
print(name.replace('Ti', 'Ki').lower()) # => ?

# Чему равен результат такого вызова?
print(name[1:5].upper().find('I'))
print(name.find('i',2))

# Задание
# С помощью слайсов, получите часть предложения, записанного в переменную text, 
# c 5 по 15 символы включительно. Полученную подстроку обработайте методом .strip() 
# и выведите на экран длину итоговой подстроки. 
# Выполните эти операции подряд в цепочке без создания промежуточных переменных.

text = 'When \t\n you play a \t\n game of thrones you win or you die.'

# BEGIN (write your solution here)
print(text[5:15].strip())

print(len(text[5:15].strip()))
# END

print('---45--------------------------------------------------')
print()

def show_greeting():
    # Внутри тела отступ 4 пробела
    text = 'Hello, Hexlet!'
    print(text)
# Вызов функции
show_greeting() # => 'Hello, Hexlet!'

text = 'Hello, Slava!'
def show_greeting():
    # Внутри тела отступ 4 пробела
    text 
    print(text)
# Вызов функции
show_greeting() # => 'Hello, Hexlet!'

# Задание
# Реализуйте функцию с именем print_motto(), которая выведет на экран фразу Winter is coming.

# print_motto() # => Winter is coming
# В задачах, в которых нужно реализовать функцию, эту функцию вызывать не нужно. 
# Вызывать функцию будут автоматизированные тесты, которые проверяют его работоспособность. 
# Пример с вызовом выше показан только для того, чтобы вы понимали, как ваша функция будет использоваться.

def print_motto():
    print('Winter is coming')
print_motto()

print('---46--------------------------------------------------')
print()
print('---v1-------------------------------------------')
def greeting_with_return_and_printing():
    print('Я появлюсь в консоли')
    return 'Hello, Hexlet!'
# И напечатает текст на экран и вернет значение
print(greeting_with_return_and_printing())

print('---v2-------------------------------------------')

def greeting_with_return_and_printing():
    print('Я появлюсь в консоли')
    return print('Hello, Hexlet!')
# И напечатает текст на экран и вернет значение
greeting_with_return_and_printing()

print('---v3----------------------------------------------')

def greeting_with_return_and_printing():
    print('Я появлюсь в консоли')
    print('Hello, Hexlet!')
    return 
# И напечатает текст на экран и вернет значение
greeting_with_return_and_printing()

print('---v4----------------------------------------------')
print()
# Определение
def run():
    return 50 # Любой код после return не выполняется:
    return 10
# Что будет выведено на экран?
print(run()) # => 50

# Любой код после return не выполняется:
print('---w--------------------------------')
def greeting_with_code_after_return():
    return 'Hello, Hexlet!'
    print('Я никогда не выполнюсь')

# Задание 
# Реализуйте функцию say_hurray_three_times(), 
# которая возвращает строку 'hurray! hurray! hurray!'.

print('----e------------------------------')

def say_hurray_three_times():
    return ('hurray!' * 3)
hurray = say_hurray_three_times()
print(hurray) # => hurray! hurray! hurray!

print('----r------------------------------')

def say_hurray_three_times():
    return ('hurray! hurray! hurray!')
hurray = say_hurray_three_times()
print(hurray) # => hurray! hurray! hurray!

print('---d-----------------------------')

# BEGIN
def say_hurray_three_times():
    word = 'hurray!'
    return f'{word} {word} {word}'
hurray = say_hurray_three_times()
print(hurray) # => hurray! hurray! hurray!    
# END

print('---47----------------------------------------------')
print()

# text = 'Winter is coming'
# text.strip()
# print(text.strip())

# Задание
# Допишите функцию truncate(), 
# которая обрезает переданную строку до указанного количества символов, 
# добавляет в конце троеточие и возвращает получившуюся строку. 
# Подобная логика часто используется на сайтах, чтобы отобразить длинный текст в сокращенном виде.
# Функция принимает два параметра:
# Строка, которую нужно обрезать
# Число символов, которые нужно оставить

print('.................................................')

text = 'Winter is coming'

def truncate(text, length):
    string = text[0:length]
    return string + '...'
print(truncate(text, 5))

print('.................................................')

def truncate(text, length):
    # BEGIN
    result = f"{text[0:length]}..."
    return result
    # END
print(truncate(text, 5))

print('---48----------------------------------------------')
print()

def my_print(text='nothing'):
  print(text)

my_print() # => nothing
my_print('Hexlet') # => Hexlet

print('--sensey---------------------------------------')

def get_hidden_card(card_number, stars_count=4):
    visible_digits_line = card_number[-4:]
    return f"{'*' * stars_count}{visible_digits_line}"
print(get_hidden_card('1234567891234567',8))

print('--yaia-------------------------------------------')

def get_hidden_card(card_number, asterisks = 4):
    return '*' * (asterisks)  + card_number[12:16]
print(get_hidden_card('1234567891234567',2))

  
card_number = '1234567891238765'
asterisks = 4
print(('*' * asterisks) + card_number[12:16])

print('---49----------------------------------------------')
print()

# Реализуйте функцию trim_and_repeat(), которая принимает три параметра: 
# строку, 
# offset — число символов, на которое нужно обрезать строку слева 
# repetitions — количество раз, сколько ее нужно повторить, и возращает получившуюся строку.

# Число символов для среза по умолчанию равно 0, а повторений — 1.

print('.................................................................')
value = 'Hexlet'
value[3:] # 'let'
value[:3] # 'Hex'

text = 'python'
offset = 2
print(text[offset:])

def trim_and_repeat(text, offset = 0, repetitions = 1):
        return text[offset:] * repetitions

print(trim_and_repeat(text, offset=3, repetitions=2)) # => honhon
print(trim_and_repeat(text, repetitions=3)) # => pythonpythonpython
print(trim_and_repeat(text)) # => python

print('---50----------------------------------------------')
print()

def is_pensioner(age):
    return age >= 60

print(is_pensioner(23))
print(is_pensioner(70))
print(is_pensioner(60))
print(is_pensioner(59))
print(is_pensioner(75)) # True
print(is_pensioner(18)) # False

def is_mister(string):
    return string == 'Mister'

print('---51----------------------------------------------')
print()

def is_international_phone(number): 
    number[0] == '+'
    return

print('---52----------------------------------------------')
print()

def is_good_apartment(area, street):
    return area >= 100 or (area >= 80 and street == 'Main Street')

print(is_good_apartment(91, 'Queens Street'))  # => False
print(is_good_apartment(78, 'Queens Street'))  # => False
print(is_good_apartment(70, 'Main Street'))    # => False

print(is_good_apartment(120, 'Queens Street')) # => True
print(is_good_apartment(120, 'Main Street'))   # => True
print(is_good_apartment(80, 'Main Street'))    # => True

# Реализуйте метод is_leap_year(), который определяет является ли год високосным или нет. 
# Год будет високосным, если он кратен 400 (то есть делится без остатка)
# или он одновременно кратен 4 и не кратен 100. 
# Как видите, в определении уже заложена вся необходимая логика, осталось только переложить её на код:
print('....is_leap_year........................................................')

def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

print(is_leap_year(2018)) # false
print(is_leap_year(2017)) # false
print(is_leap_year(2016)) # true
print(is_leap_year(2000))
print(is_leap_year(1900))
'''
# Кратность можно проверять так:
print('...multiplicity.........................................................')
# % - возвращает остаток от деления левого операнда на правый
# number = 478
# Проверяем что number кратен 10
print(number % 10 == 0)

# Проверяем что number не кратен 10
print(number % 10 != 0)
'''
print('....is_palindrome....................')

def outer_func():
    def inner_func():
        print("Hello, World!")
    inner_func()
outer_func()

print('.вызовите функцию is_palindrome() внутри is_not_palindrome() и примените отрицание.')

# Реализуйте функцию is_not_palindrome(), которая проверяет что слово НЕ является палиндромом:
# Для этого, вызовите функцию is_palindrome() внутри is_not_palindrome() и примените отрицание.

print(' ... Ваше решение: ......')
'''___________________________________________________________'''
def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def is_not_palindrome(word):
    return word.lower() != word[::-1].lower()
'''____________________________________________________________'''

print(' ... Решение учителя: ......')

def is_palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]
print('')
def is_not_palindrome(word):
    return not is_palindrome(word)
'''_____________________________________________________________'''
print('')
print(' ТЫ ЛАШАРА - ТЫ СМУХЛЕВАЛ ! ! ! ЖУЛИК...')
print('')

print(is_not_palindrome('wow'))
print(is_not_palindrome('hexlet'))
print(is_not_palindrome('asdffdsa'))
print(is_not_palindrome('Wow'))
print(is_not_palindrome('CodeBasics'))

print('...55......................................................')
print('')
print('... Ваше решение ...')
def string_or_not(is_string):
    return (not isinstance(is_string, str)) and 'no' or 'yes'

print(string_or_not('Hexlet')) # 'yes'
print(string_or_not(10)) # 'no'
print(string_or_not('')) # 'yes'
print(string_or_not(False)) # 'no'

print('')
print('... Решение учителя ...')

def string_or_not(value):
    return isinstance(value, str) and 'yes' or 'no'

print(string_or_not('Hexlet')) # 'yes'
print(string_or_not(10)) # 'no'
print(string_or_not('')) # 'yes'
print(string_or_not(False)) # 'no'

print('')
print('...56...Условная конструкция (if).............................')
print('')

def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':
        return 'question'
    return 'normal'

print(get_type_of_sentence('Hodor'))  # => normal
print(get_type_of_sentence('Hodor?')) # => question

def guess_number(number):
    if number == 42:
       return 'You win!'
    return 'Try again!'   

print(guess_number(42)) # You win!
print(guess_number(61)) # Try again!

print('...57...Условная конструкция (   else   ).............................')
print('')

def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    else:
        sentence_type = 'normal'

    return "Sentence is " + sentence_type

print(get_type_of_sentence('Hodor'))   # => 'Sentence is normal'
print(get_type_of_sentence('Hodor?'))  # => 'Sentence is question'

print('')

def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    else:
        if last_char == '!':
            sentence_type = 'exclamation'
        else:
            sentence_type = 'normal'

    return "Sentence is " + sentence_type

print(get_type_of_sentence('Hodor'))   # => 'Sentence is normal'
print(get_type_of_sentence('Hodor?'))  # => 'Sentence is question'
print(get_type_of_sentence('Hodor!'))  # => 'Sentence is exclamation'

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# Реализуйте функцию normalize_url(), которая выполняет нормализацию данных. 
# Она принимает адрес сайта и возвращает его с https:// в начале.

# Функция принимает адреса в виде АДРЕС или http://АДРЕС, но всегда возвращает адрес в виде https://АДРЕС. 
# На вход функции также может поступить адрес в уже нормализованном виде https://АДРЕС, 
# в этом случае ничего менять не надо. 

print('... v1 ...\n')

adress = 'https://ya.ru'
print(adress)

adress = 'http://ai.fi'
print('https://' + adress[7:])

adress = 'google.com'
print('https://' + adress)

print('... v2 ...\n')

print(len('https://')) # => 8

def normalize_url(url):
    https = 'https://'
    if url[:8] == https:
        return url
    elif url[:7] == 'http://':
        return https + url[7:]
    else:
        return https + url

print(normalize_url('https://ya.ru'))  # => 'https://ya.ru'
print(normalize_url('http://ai.fi'))   # => 'https://ai.fi'
print(normalize_url('google.com'))     # => 'https://google.com'

print('>>  Решение учителя: 1  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def normalize_url(url):
    https = 'https://'
    if url[:8] == https:
        return url
    elif url[:7] == 'http://':
        return https + url[7:]
    else:
        return https + url

print(normalize_url('https://ya.ru'))  # => 'https://ya.ru'
print(normalize_url('http://ai.fi'))   # => 'https://ai.fi'
print(normalize_url('google.com'))     # => 'https://google.com'

print('>>  Решение учителя: 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def normalize_url(url):
    prefix = 'https://'
    if url[:8] == prefix:
        return url
    else:
        if url[:7] == 'http://':
            return prefix + url[7:]
        else:
            return prefix + url

print(normalize_url('https://ya.ru'))  # => 'https://ya.ru'
print(normalize_url('http://ai.fi'))   # => 'https://ai.fi'
print(normalize_url('google.com'))     # => 'https://google.com'

print('...59...Конструкция else + if = elif.............................')
print('')
print('... v1 ...')

def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    else:
        if last_char == '!':
           sentence_type = 'exclamation'
        else:
           sentence_type = 'normal'

    return 'Sentence is ' + sentence_type
print(get_type_of_sentence('Who?'))  # => 'Sentence is normal'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'
print('')
print('... v2 ...')

def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':             # <= elif  — это «если не выполнено предыдущее условие, но выполнено текущее»
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'
    return 'Sentence is ' + sentence_type
print(get_type_of_sentence('Who?'))  # => 'Sentence is question'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'
print('')
print('... family_name   ...')

# На электронной карте Вестероса, которую реализовал Сэм, союзники Старков отображены зелёным кружком, 
# враги — красным, а нейтральные семьи — серым.

# Напишите для Сэма функцию who_is_this_house_to_starks(), 
# которая принимает на вход фамилию семьи и возвращает одно из трёх значений: 'friend', 'enemy', 'neutral'.

# Правила определения:

# -Друзья ('friend'): 'Karstark', 'Tully'
# -Враги ('enemy'): 'Lannister', 'Frey'
# -Любые другие семьи считаются нейтральными ('neutral')
# -Примеры вызова:

print('''... КОНСТРУКЦИЮ ИЛИ НЕ ПОЛУЧИЛОСЬ ПРИМЕНИТЬ, 
ПОТОМУЧТО Я ПИСАЛ:
( house_name == 'Karstark or 'Tully'), 
А НАДО БЫЛО ПРИМЕНЯТЬ КОНСТРУКЦИЮ:
( house_name == 'Karstark') or (house_name == 'Tully')   ...''')
print('\n')
print('... ВАШЕ РЕШЕНИЕ ... ')

def who_is_this_house_to_starks(family_name):

    if family_name == ('Karstark'):
        return 'friend'
    elif family_name == ('Tully'):
        return  'friend'
    elif family_name == ('Lannister'):
        return  'enemy'
    elif family_name == ('Frey'):
        return  'enemy'        
    else:
        return 'neutral'
    
print('.............test..............')
print(who_is_this_house_to_starks('Tully')) # 'friend'
print(who_is_this_house_to_starks('Karstark')) # 'friend'
print(who_is_this_house_to_starks('Lannister')) # 'enemy'
print(who_is_this_house_to_starks('Martell')) # 'neutral'
print(who_is_this_house_to_starks('undefined')) # 'neutral'

print('... РЕШЕНИЕ УЧИТЕЛЯ ... ')

def who_is_this_house_to_starks(house_name):
    if house_name == 'Karstark' or house_name == 'Tully':
        return 'friend'
    elif house_name == 'Lannister' or house_name == 'Frey':
        return 'enemy'
    return 'neutral'

print('.............test..............')
print(who_is_this_house_to_starks('Tully')) # 'friend'
print(who_is_this_house_to_starks('Karstark')) # 'friend'
print(who_is_this_house_to_starks('Lannister')) # 'enemy'
print(who_is_this_house_to_starks('Martell')) # 'neutral'
print(who_is_this_house_to_starks('undefined')) # 'neutral'

print('...59...Тернарный оператор.............................')
print('')

# Было:

def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':
        return 'question'
    return 'normal'

print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question

# Стало:

def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    return 'question' if last_char == '?' else 'normal'

print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question

def flip_flop(string):
    if string == 'flip':
        return 'flop'
    return 'flip'

print(flip_flop('flip'))  # => 'flop'
print(flip_flop('flop'))  # => 'flip'

def flip_flop(string):
    return 'flop' if string == 'flip' else 'flip'

print(flip_flop('flip'))  # => 'flop'
print(flip_flop('flop'))  # => 'flip'

print('...60...Цикл While.............................')
print('')

def print_hello(n):
    counter = 0
    while counter < n:
        counter = counter + 1
        print('Holla!')
print_hello(4)

def print_numbers(last_number):
    i = 1
    while i <= last_number: # <= условие
        print(i)
      # print('Hello!')
        i = i + 1
    print('\n   finished!')
print_numbers(3)

print('..._______________________ ...')

# Инициализируется i
i = 1

# Предикат возвращает true, поэтому выполняется тело цикла
# while 1 <= 3:
# print(1)
# i = 1 + 1

# Закончилось тело цикла, поэтому происходит возврат в начало
# while 2 <= 3:
# print(2)
# i = 2 + 1

# Закончилось тело цикла, поэтому происходит возврат в начало
# while 3 <= 3:
# print(3)
# i = 3 + 1

# Предикат возвращает false, поэтому выполнение переходит за цикл
# while 4 <= 3:

# print('finished!');
# На этом этапе i равен 4, но он нам уже не нужен
# функция завершается
print('...\n_______________________ ...')

def print_numbers(last_number):
    i = 1
    while i <= last_number: # <= условие
        print(i)
        i = i + 1
    print('finished!')
print_numbers(3)

print('...\n_____Ваше решение:__________________ ...')

def print_numbers(last_number):
    i = 0
    
    while i < last_number: # <= условие
        print(last_number - i) 
        i = i + 1
    print('finished!')
print_numbers(4)

print('...\n______Решение учителя:_________________ ...')

def print_numbers(last_number):
    i = last_number
    while i > 0:
        print(i)
        i = i - 1
    print('finished!')
print_numbers(4)



