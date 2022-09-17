# Conditional constructions
# Условные конструкции

'''
Условные конструкции позволяют изменить поведение программы в зависимости от проверяемых условий. 
Благодаря им у нас появляется возможность писать сложные программы, ведущие себя по разному, 
в зависимости от ситуации.

if
Напишем, для примера, функцию, которая определяет тип переданного предложения. 
Для начала она будет отличать обычные предложения от вопросительных.'''

def get_type_of_sentence(sentence):
  last_char = sentence[-1]
  if last_char == '?':
      return 'question'
  return 'normal'

print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question
# ======================================================================================================
''' if
if - конструкция языка, управляющая порядком выполнения инструкций. 
После слова if ей передается выражение-предикат, завершающееся двоеточием. 
После этого описывается блок кода. Этот блок кода будет выполнен, только если предикат — истина.

Если предикат — ложь, то блок кода пропускается, и функция продолжает свое выполнение дальше. 
В нашем случае следующая строчка кода — return 'normal' — заставит функцию вернуть строку и завершиться.

Как видите, return может находиться где угодно в функции. В том числе внутри блока кода с условием.'''
# ======================================================================================================
''' else
Попробуем изменить функцию из предыдущего примера так, чтобы она возвращала не просто тип предложения, 
а целую строку Sentence is normal или Sentence is question.'''

def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    else:
        sentence_type = 'normal'

    return "Sentence is " + sentence_type

print(get_type_of_sentence('Hodor'))   # => 'Sentence is normal'
print(get_type_of_sentence('Hodor?'))  # => 'Sentence is question'

'''
Мы добавили else и новый блок. Этот блок выполнится, только если условие в if — ложь. 
Также в блок else можно вкладывать другие условия if. "Else" переводится «иначе», «в ином случае».

Существует два способа оформления конструкции if-else. 
С помощью отрицания можно изменить порядок блоков:'''

def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char != '?':
        sentence_type = 'normal'
    else:
        sentence_type = 'question'

    return "Sentence is " + sentence_type

'''
Какой способ предпочтительнее? Человеческому мозгу проще мыслить прямолинейно, 
а не через отрицание. Старайтесь выбирать проверку, которая не содержит отрицаний, 
и подстраивайте содержимое блоков под неё.'''    

'''Конструкция else + if = elif
Функция get_type_of_sentence() из предыдущего урока различает только вопросительные 
и обычные предложения. 
Давайте попробуем добавить поддержку восклицательных предложений:'''

def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'

    if last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type

print(get_type_of_sentence('Who?'))  # => 'Sentence is normal'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'

'''
Мы добавили еще одну проверку ("exclamation" переводится «восклицание»). 
Технически функция работает, но вопросительные предложения трактует неверно, 
да и с точки зрения семантики есть проблемы.

Проверка на наличие восклицательного знака происходит в любом случае, 
даже если уже был обнаружен вопросительный знак.
Ветка else описана именно для второго условия, но не для первого 
(именно поэтому вопросительное предложение становится "normal").
Для исправления ситуации воспользуемся ещё одной возможностью условной конструкции:'''

def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type

print(get_type_of_sentence('Who?'))  # => 'Sentence is question'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'

'''
Теперь все условия выстроены в единую конструкцию. 
elif — это «если не выполнено предыдущее условие, но выполнено текущее». 
Получается такая схема:

если последняя буква ?, то 'question'
иначе, если последняя буква !, то 'exclamation'
иначе 'normal'
Выполнится только один из блоков кода, относящихся ко всей конструкции if.'''

'''Тернарный оператор
Посмотрите на определение функции, которая возвращает модуль переданного числа:'''

def abs(number):
    if number >= 0:
        return number
    return -number

'''
Можно ли записать более лаконично?
Что-то вроде return ОТВЕТ В ЗАВИСИМОСТИ ОТ УСЛОВИЯ? 
Для этого справа от return должно быть выражение, но if — это инструкция, а не выражение. 
В Python существует конструкция, которая по своему действию аналогична конструкции if-else, 
но при этом является выражением. Она называется тернарный оператор. Тернарный оператор 
— единственный в своем роде оператор, требующий три операнда:'''    

def abs(number):
    return number if number >= 0 else -number

'''
Общий паттерн выглядит так: <expression on true> if <predicate> else <expression on false>.
Давайте перепишем начальный вариант get_type_of_sentence() аналогично.'''

'''Было:'''   

def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':
        return 'question'
    return 'normal'

'''Стало:'''    

def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    return 'question' if last_char == '?' else 'normal'

print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question

'''
Если вы помните, в чём сила выражений, то, вероятно, уже догадались, 
что тернарный оператор можно вкладывать в тернарный оператор. 
Не делайте этого :) Такой код тяжело и читать и отлаживать, это очень плохая практика.'''












