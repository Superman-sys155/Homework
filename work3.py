final = {}
answer = input('Введитe строку ')

for i in answer:
    try:
        if i in final:
            pass
        else:
            final[i] = 1
    except:
        continue

final1 = ''

for i in final.keys():
    if i != ' ':
        final1 = final1 + i
    else:
        pass

print(final1)