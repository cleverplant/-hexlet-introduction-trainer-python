'''======================================================================================='''
#  data types
#  типы данных
'''======================================================================================='''

'''Бывают разные способы представлять данные в программах. 
Есть строки — наборы символов в кавычках вроде "Hello, World!". 
Есть целые числа — например, 7, -198, 0. 
Это две разные категории информации — два разных типа данных. 
Операция умножения имеет смысл для категории «целые числа». 
Но не имеет смысла для категории «строки»: 
умножать слово «мама» на слово «блокнот» — бессмыслица.

Тип данных определяет, что можно делать с элементами конкретного множества информации.
Язык программирования распознает типы. 
Поэтому Python не позволит нам умножать строку на строку («умножать текст на текст»). 
Но позволит умножать целое число на другое целое число. 
Наличие типов и таких ограничений в языке защищает программы от случайных ошибок.

В отличие от строк, числа оборачивать в кавычки не нужно. 
Чтобы напечатать число 5, достаточно написать:'''

print(5)  # => 5
print('5')  # => 5

'''Обратите внимание, что число 5 и строка '5' — совершенно разные вещи, 
хотя вывод у print() для этих данных идентичный. 
Целые числа (1, 34, -19 и т.д.) и рациональные числа (1.3, 1.0, -14.324 и т.д.)
— это два отдельных типа данных. 
Такое разделение связано с особенностями устройства компьютеров. 
Есть и другие типы, с ними мы познакомимся позже.
Вот еще один пример, но уже с рациональным числом:'''

print(10.234)  # => 10.234

'''Типы данных «строка», «целое число» и «рациональное число» — это примитивные типы, 
они встроены в сам язык Python. В язык встроены также и некоторые составные типы данных, 
но пока мы будем работать только с примитивными. 
Программисты также могут создавать собственные типы данных.

(По-английски строки в программировании называются "strings", 
а строчки текстовых файлов называются "lines". 
Например, в примере кода выше есть строчка (line), и нет никаких строк (strings).
В русском иногда может быть путаница, поэтому во всех уроках мы будем говорить строка 
для обозначения типа данных «строка», и строчка для обозначения строчек кода (lines) 
в файлах).'''
 
'''Сильная типизация
Нам известно про два разных типа данных: числа и строки. 
Мы, например, могли складывать числа, потому что операция сложения
— это операция для типа «числа». 
А что, если применить эту операцию не к двум числам, а к числу и строке?'''

# print(1 + '7')  # TypeError: unsupported operand type(s)...

'''Python не разрешит сложить число 1 и строку '7', 
потому что это значения разных типов. 
Нужно сначала либо сделать строку числом, 
либо число строкой (как это сделать, мы поговорим позже). 
Такое педантичное отношение к совместимости типов называется 
строгой типизацией или сильной типизацией. 
Python - язык со строгой типизацией.

Не все языки так делают. 
Скажем, PHP, это язык со слабой типизацией. 
Он знает о существовании разных типов (числа, строки и др.), 
но относится к их использованию не очень строго, 
пытаясь преобразовывать информацию, когда это кажется разумным. 
Тоже самое относится к JavaScript:''' 

'''// Как тебе такое, Илон Маск?
// Число 1 + Строка 7 = Строка 17
1 + '7'; // '17'
'''
'''Автоматическое неявное преобразование типов с одной стороны и правда кажется удобным. 
Но на практике это свойство языка создает множество ошибок и проблем, 
которые трудно найти. Код может иногда работать, а иногда не работать 
— в зависимости от того, «повезло» ли в конкретном случае с автоматическим преобразованием.
Программист это заметит не сразу.'''

'''======================================================================================='''

# Неизменяемость примитивных типов
'''======================================================================================='''

'''Что произойдет, если попытаться изменить символ в строке?'''

# first_name = 'Alexander'
# first_name[0] = 'B'
# Ошибка: TypeError: 'str' object does not support item assignment

'''
Такое происходит из-за неизменяемости примитивных типов в Python 
— язык не дает никакой физической возможности поменять строку. 
Неизменяемость примитивных типов важна по многим причинам, 
ключевая — производительность. Но что делать, если нам действительно нужно её изменить? 
Для этого и существуют переменные:''' 

first_name = 'Alexander'
first_name = 'Blexander'
print(first_name)  # => Blexander

'''Есть большая разница между 
изменением значения переменной и изменением самого значения. 
Примитивные типы в Python поменять нельзя 
(а вот составные можно, подробнее о них будет дальше), 
а заменить значение переменной — без проблем.'''

'''======================================================================================='''

# Явное преобразование типов
'''======================================================================================='''

'''В программировании регулярно встречаются задачи, 
когда один тип данных нужно преобразовать в другой. 
Простейший пример – работа с формами на сайтах. 
Данные формы всегда приходят в текстовом виде, даже если значение число. 
Вот как его можно преобразовать:'''

# str станет int
number = int('345')
print(number)  # => 345

'''Технически int() это функция, в которую передается значение, 
которое нужно преобразовать. Функции мы еще не проходили, 
но общую концепцию можно увидеть и сейчас. 
Функция ведет себя подобно арифметическим операциям, 
но делает какие-то особые действия. Вот еще несколько примеров:'''

value = '0'
# Внутри скобок можно указывать переменную
converted_value = int(value)
print(converted_value)  # => 0

# Или конкретное значение
converted_value2 = int('10')
print(converted_value2)  # => 10

converted_value3 = int(False)
print(converted_value3)  # => 0

converted_value4 = int(True)
print(converted_value4)  # => 1

# Если преобразуется число с плавающей точкой
# то отбрасывается вся дробная часть
converted_value5 = int(3.5)
print(converted_value5)  # => 3

'''Точно так же можно преобразовать данные в строки str() 
и число с плавающей точкой float():'''

value = str(10)
print(value)  # '10'

value2 = str(True)
print(value2)  # 'True'

value3 = float(5)
print(value3)  # 5.0

'''Некоторые преобразования Python выполняет автоматически. 
Например в операциях, где встречается одновременно целое число и число с плавающей точкой. 
Python автоматически все приводит к float (числа с плавающей точкой).'''

'''========================================================================================='''

# Числа с плавающей точкой
'''========================================================================================='''

'''В математике существуют разные виды чисел, например, натуральные 
- это целые числа от одного и больше, или рациональные - это числа с точкой, 
например 0.5. С точки зрения устройства компьютеров, между этими видами чисел - пропасть. 
Попробуйте ответить на простой вопрос, сколько будет 0.2 + 0.1? А теперь посмотрим, 
что на это скажет Python:'''

print(0.2 + 0.1) # 0.30000000000000004

'''Операция сложения двух рациональных чисел внезапно привела к неточному вычислению 
результата. Тот же самый результат выдадут и другие языки программирования. 
Такое поведение обуславливается ограничениями вычислительных мощностей. 
Объём памяти, в отличие от чисел, конечен 
(бесконечное количество чисел требует бесконечного количества памяти для своего хранения).'''

'''Рациональные числа не выстроены в непрерывную цепочку, 
между 0.1 и 0.2 бесконечное множество чисел. 
Соответственно возникает серьезная проблема, а как хранить рациональные числа? 
Это интересный вопрос сам по себе. 
В интернете множество статей, посвященных организации памяти в таких случаях. 
Более того, существует стандарт, в котором описано, как это делать правильно, 
и подавляющее число языков на него опирается.'''

'''Для нас, как для разработчиков, важно понимать, что операции с плавающими числами неточны 
(эту точность можно регулировать), а значит при решении задач, связанных с подобными числами, 
необходимо прибегать к специальным трюкам, которые позволяют добиться необходимой точности.'''




