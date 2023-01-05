# x + y -> + -> оператор, x, y -> операнди
x = 10
y = 20
# + - * / // % **
# x, y

print(x + y)  # 30
print(x - y)  # -10
print(x * y)  # 200
print(y / x)  # 2.0
print(y // x)  # 2
print(y % x)  # 0
print(x ** 2)  # 100


c = 8 ** 2 + 4 * (2 + 2)  # 80
print(c)
# -> коментар


# None -> пустий тип
# Числа -> int, float -> int(1, 13, 15, 142, 3121, 543534, 63542), float(3.2, 5.4, 8.9, 10.1534)
# Рядки -> string(str) -> 'HELLO WORLD'
# Boolean -> логічний тип True or False
# x = 10, y = 20
print(x < y)  # True
print(x > y)  # False
print(x <= y)  # True
print(x >= y)  # False
print(x == y)  # False
print(x != y)  # True


print(3.14)
s = 'Hello, World!'
print(s)

s1 = 'Hello'
s2 = 'World!'
joined_string = s1 + ' ' + s2
print(joined_string)
new_string = 'didn\'t'
new_string = "didn't"
# -> \' -> апостроф

name = 'Oleksiy'
hello_string = f"Hello, {name}"
print(hello_string)
hello_string = 'Hello, name'
print(hello_string)
a = True
b = False
age = 18
adult = age >= 18  # -> True
age = 15
adult2 = age >= 18  # -> False

print('Hello world!')


a = input('Рядок запрошення: ')
print(a)


age = input('Введіть свій вік: ')
age = int(age)
print(type(age))
