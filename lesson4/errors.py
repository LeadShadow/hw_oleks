value = '1'
try:
    value = int(value)
    print(value)
except ValueError:
    print(f'value {value} is not a number')
finally:
    print('This will be printed anyway')


age = input('How old are you?: ')
try:
    age = int(age)
    if age >= 18:
        print('Ти вже повнолітній')
    else:
        print('Ти ще не повнолітній')
except ValueError:
    print(f'{age} is not a number')