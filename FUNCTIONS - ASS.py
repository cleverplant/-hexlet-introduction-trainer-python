
print('...ПЕРЕДЕЛКА... ')
def who_is_this_house_to_starks(family_name):

    if family_name == ('Tully'):
        string = 'friend'
    else:
        string = 'neutral'
    return string
print(who_is_this_house_to_starks('Tully')) # 'friend'

print('...ИСХОДНЫЙ КОД...')
def who_is_this_house_to_starks(family_name):

    if family_name == ('Tully'):
        return 'friend'
    else:
        return 'neutral'
print(who_is_this_house_to_starks('Tully')) # 'friend'

print('\n')
print('...ПОЛНЫЙ ИСХОДНЫЙ КОД...')

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
    
print(who_is_this_house_to_starks('Tully')) # 'friend'
print(who_is_this_house_to_starks('Karstark')) # 'friend'
print(who_is_this_house_to_starks('Lannister')) # 'enemy'
print(who_is_this_house_to_starks('Martell')) # 'neutral'
print(who_is_this_house_to_starks('undefined')) # 'neutral'

print('...ПЕРЕДЕЛКА ПОЛНОГО ИСХОДНОГО КОДА...')

def who_is_this_house_to_starks(family_name):
    string = 'neutral'
    if family_name == ('Karstark'):
        string = 'friend'
    elif family_name == ('Tully'):
        string = 'friend'
    elif family_name == ('Lannister'):
        string = 'enemy'
    elif family_name == ('Frey'):
        string = 'enemy'        
    else:
        string = 'neutral'
    return string 

print(who_is_this_house_to_starks('Tully')) # 'friend'
print(who_is_this_house_to_starks('Karstark')) # 'friend'
print(who_is_this_house_to_starks('Lannister')) # 'enemy'
print(who_is_this_house_to_starks('Martell')) # 'neutral'
print(who_is_this_house_to_starks('undefined')) # 'neutral'








