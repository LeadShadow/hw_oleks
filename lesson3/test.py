# apple

fruit = 'apple'
for char in fruit:
    print(char)


a = 1
while a <= 5:
    print(a)
    a = a + 1


a = 0
while True:
    print(a)
    if a >= 20:
        break
    a += 1


while True:
    user_input1 = int(input('Введіть перше число: '))
    user_input2 = int(input('Введіть друге число: '))
    print(user_input2 + user_input1)
    user_exit = input('Введіть exit щоб вийти: ')  # 'exit'
    if user_exit == 'exit':
        break

