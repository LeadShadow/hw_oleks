# Давайте вернемся к задаче из пункта 8 про расчет площади. Ширина и высота заданы в строковом
# виде. Необходимо, как и раньше, рассчитать площадь, но требуется строковый тип преобразовать в
# численный (float) при расчете площади area. Не забудьте также добавить в переменную show строку
# со следующим шаблоном: 'With width <значение ширины> and length <значение длины> of the room,
# its area is equal to <значение площади>'.
# int(), float(), str(), bool()
length = "2.75"
width = "1.75"
area = float(length) * float(width)
print(area)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print(show)
