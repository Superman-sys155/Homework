answer = input('Введите строчку ')

final = answer.split()
final_1 = final[-1::-1]
sp = ''
for i in final_1:
    sp += i
print(sp)