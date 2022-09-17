'''
# Выведите на экран две строки: Do you want to eat, ? и Yes, I'm hungry, mom.
# Вместо <name> должна использоваться переменная stark. 
# При формировании итоговой строки используйте интерполяцию. 
# Вывод должен получиться таким:
# Do you want to eat, Arya?
# Yes, I'm hungry, mom.
'''

stark = 'Arya'

# BEGIN (write your solution here)
text = f'''Do you want to eat, {stark}?
Yes, I'm hungry, mom.'''
print(text)
# END