text = input('Введите строку ')
final = ''
for i in text:
    if i == i.upper() and i != ' ':
        final += i

print(final)