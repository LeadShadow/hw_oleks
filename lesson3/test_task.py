while True:
    number = int(input('number == '))
    while True:
        print(number)
        number = number - 1
        if number < 0:
            break
    user_exit = input('Введіть exit щоб вийти: ')  # 'exit'
    if user_exit == 'exit':
        break
