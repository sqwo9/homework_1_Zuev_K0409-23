list1 = []
l1 = [list1.append(i) for i in input('Введите первый список через пробелы - ').split(' ')]
list2 = []
l2 = [list2.append(i) for i in input('Введите второй список через пробелы - ').split(' ')]
list = list1 + list2
list.sort()

print(list)
