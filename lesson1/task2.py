# При заполнении анкеты на сайте нам необходимо через функцию input присвоить
# соответствующим переменным значения:

# name - ваше имя, тип строка
# email - ваша электронная почта, тип строка
# age - ваш возраст, тип число int
# height - ваш рост, тип число float
# is_active - хотите ли вы получать уведомления от сайта, тип булевый

name = input("Your name? ")
email = input('Input your email: ')
age = int(input('Input your age: '))
height = float(input('Input your height: '))
is_active = bool(input('Dou you want receive message from our site? '))

