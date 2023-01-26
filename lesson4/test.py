def say_hello():
    print('Привіт, світ!')
    print('Привіт, світ!')
    print('Привіт, світ!')
    print('Привіт, світ!')
    print('Привіт, світ!')
    print('Привіт, світ!')
    print('Привіт, світ!')
    print('Привіт, світ!')
    print('Привіт, світ!')
    print('Привіт, світ!')
    print('Привіт, світ!')
    print('Привіт, світ!')


say_hello()


def plus(a, b):
    c = a + b  # 3 + 4 -> 7
    return c


result = plus(3, 4)
print(result)



x = 50

def func():
    x = 2
    print('Заміна глобального х на', x)


func()
print('x все ще', x)


x = 50

def func1():
    global x
    print('x ==', x)
    x = 2
    print('Заміна глобального х на', x)


func1()
print('Значення х ==', x)


def func2(a, b=5, c=10):
    print('a ==', a, 'b ==', b, 'c ==', c)


func2(3)
func2(25, b=24, c=29)
func2(a=25, c=29)