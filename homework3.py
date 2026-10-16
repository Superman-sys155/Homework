text = input('Введите строчку ')
sum = 0


for i in text:
    try:
        sum += int(i)

    except:
        continue

print(sum)