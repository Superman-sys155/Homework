from random import *

lists1 = []

for i in range(1,101):
    lists1.append(randint(1,101))


lists2 = []

for i in range(1,101):
    lists2.append(randint(1,101))


lists3 = []

for i in range(1,101):
    lists3.append(randint(1,101))



final_list = [lists1]


for i in lists1:
    if i not in final_list:
        final_list.append(i)


for i in lists2:
    if i not in final_list:
        final_list.append(i)


for i in lists3:
    if i not in final_list:
        final_list.append(i)


print(final_list)