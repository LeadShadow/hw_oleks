name = input("Яке твоє ім'я?: ")
print(f'Hello, {name}')


nice = False
state = 'nice' if nice else 'not nice'
print(state)

data = None
message = data or 'Не було повернено даних'
print(message)