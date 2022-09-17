# returning values
# возврат значений

'''============================================================================
Функции, которые мы определяли в предыдущих уроках, заканчивали свою работу тем, 
что печатали на экран какие-то данные:'''
def greeting():
    print('Hello, Hexlet!')
'''
Пользы от таких функций не очень много, так как результатом их работы невозможно 
воспользоваться внутри программы. Рассмотрим это на примере. 
Возьмем задачу обработки электронной почты. 
Когда пользователь регистрируется на каком-то сайте, 
то он может ввести email любым способом:'''

# => Добавив случайно пробелы в начале или в конце _support@hexlet.io__
# => Использовав буквы в разном регистре SUPPORT@hexlet.io
'''
Если мы сохраним его в таком виде в базу данных, то пользователь, 
скорее всего, не сможет войти на сайт, так как будет вбивать адрес 
без пробелов и используя другой регистр символов. 
Чтобы этого не произошло, email нужно подготовить к записи в базу, 
привести его к нижнему регистру и обрезать пробельные символы по краям строки. 
Вся задача решается в пару строчек:'''    

def save_email():
    # В реальности email приходит из формы
    email = '  SuppORT@hexlet.IO'
    # обрезаем пробельные символы
    trimmed_email = email.strip()
    prepared_email = trimmed_email.lower()
    print(prepared_email)
    # здесь будет запись в базу данных
save_email()

'''
Этот код стал возможен только благодаря возврату значения. 
Методы strip() и lower() ничего не печатают на экран (в консоль), 
они возвращают результат своей работы и поэтому мы можем записать его в переменные.
Если бы они вместо этого печатали на экран, мы бы не могли присвоить результат их 
работы переменной. 
Как мы не можем сделать с определенной выше функцией greeting():'''

def greeting():
    print('Hello, Hexlet!')
message = greeting()
print(message) # => None
'''
изменим функцию greeting() таким образом, чтобы она начала возвращать данные, 
вместо их печати. Для этого нам понадобится выполнить возврат 
вместо печати на экран:'''

def greeting():
    return 'Hello, Hexlet!' # => None
greeting()
'''
return – особая инструкция, которая берёт выражение, записанное справа, 
и отдаёт его наружу, тому коду, который вызвал метод. 
Как только Python натыкается на return, выполнение функции на этом завершается.'''

def greeting():
    return 'Hello, Hexlet!' # => None
greeting()
# Теперь мы можем использовать результат работы функции
message = greeting()
print(message) # => Hello, Hexlet!
# И даже выполнить какие-то действия над результатом
print(message.upper()) # => HELLO, HEXLET!

'''Любой код после return не выполняется:'''

def greeting_with_code_after_return():
    return 'Hello, Hexlet!'
    #print('Я никогда не выполнюсь')
greeting_with_code_after_return()    

'''
Даже если функция возвращает данные, это не ограничивает её в том, 
что она печатает. Кроме возврата данных мы можем и печатать:'''

def greeting_with_return_and_printing():
    print('Я появлюсь в консоли')
    return 'Hello, Hexlet!'
# И напечатает текст на экран и вернет значение
message = greeting_with_return_and_printing()

'''
Возвращать можно не только конкретное значение. Так как return работает 
с выражениями, то справа от него может появиться почти все что угодно. 
Здесь нужно руководствоваться принципами читаемости кода:'''

def greeting():
    message = 'Hello, Hexlet!'
    return message
'''
Здесь мы не возвращаем переменную, возвращается всегда значение, 
которое находится в этой переменной. Ниже пример с вычислениями:'''

def double_five():
    # или return 5 + 5
    result = 5 + 5
    return result
'''
Вопрос на самопроверку. Что вернет вызов, 
определенной ниже, функции run()?'''

# Определение
def run():
    return 5
    return 10
# Что будет выведено на экран?
print(run()) # => 5



