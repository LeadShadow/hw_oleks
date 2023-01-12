name = 'Sasha'
age = 14
has_driver_license = True
# if name -> True
# age -> True
# if name and age >= 18 and has_driver_license -> True and True and True
if name and age >= 18 and has_driver_license:
    print(f'User can rent a car')
else:
    print("User can't rent a car")
