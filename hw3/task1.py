# пам'ятаєш ми робили завдання levels.py в модулі lesson2
# тобі потрібно написати схоже завдання використовуючи цикл while, підказки до завдання дам

x = int(input('X: '))
y = int(input('Y: '))

while x == 0 :
    print("X can't be equal to zero")
    x = int(input('X: '))

result = y / x
print(result)