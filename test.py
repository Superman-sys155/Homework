
a = input('Введите число ')
sum = 0

while True:
    try:
        sum += int(a)
        a = input('Введите число ')
    except:
        break

print(sum)