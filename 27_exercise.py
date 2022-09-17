'''после обязательного параметра идет необязательный'''
# ====================================================================
'''Вопрос: 2 из 3. Правильных ответов: 2'''
#  Какие определения функции записаны верно?
#  (нужно выбрать все корректные ответы)

'''def pow(x, base):'''
'''def pow(x, base=2):'''
'''def pow(x=2, base=2):'''
#  def pow(x=2, base): <===== так и не понял почему............
# ===================================================================== 

#  Решение учителя:

def get_hidden_card(card_number, stars_count=4):
    visible_digits_line = card_number[-4:]
    return f"{'*' * stars_count}{visible_digits_line}"
# ===================================================================

def get_hidden_card(card_number, stars_count=4):
    number_digital = card_number[-4:]
    return f"{'*' * stars_count}{number_digital}"

