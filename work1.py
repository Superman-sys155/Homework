final = {}
answer = input('Введитк строку ')

for i in answer:
    try:
        if i in final:
            final[i] = final[i] + 1
        else:
            final[i] = 1
    except:
        continue

print(final)