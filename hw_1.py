n = int(input("Введите число: "))
sum = 0
for i in range(2, n+1):
    suc = True
    for j in range(2, i):
        if i % j == 0:
            suc = False
    if suc:
        sum += i
print(sum)