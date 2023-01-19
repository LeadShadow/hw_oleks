x = int(input('Input x: '))
y = int(input('Input y: '))

# 1 -> (2, 3)
# 2 -> (-3, 2)
# 3 -> (-2, -3)
# 4 -> (1, -2)
if x >= 0:
    if y >= 0:
        print('Перша чверть')
    else:
        print('Четверта чверть')
else:
    if y >= 0:
        print('Друга чверть')
    else:
        print('Третя чверть')
