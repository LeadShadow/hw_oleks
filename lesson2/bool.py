# and (І)
# A  B
# 1  1 -> True
# 1  0 -> False
# 0  1 -> False
# 0  0 -> False

print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or (або)
# A   B
# 1   1 -> True
# 1   0 -> True
# 0   1 -> True
# 0   0 -> False

print(True or True)
print(True or False)
print(False or True)
print(False or False)


# not (не)
# A  not A
# 1    0
# 0    1

a = not 2 < 0  # True
print(a)
