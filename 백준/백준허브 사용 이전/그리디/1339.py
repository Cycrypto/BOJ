import operator
from string import ascii_uppercase
number = {i: 0 for i in ascii_uppercase}
start = 9
result = 0

op = []
for i in range(int(input())):
    op.append(input())

for j in list(map(list, op)):
    j.reverse()
    for idx, k in enumerate(j):
        number[k] += (10 ** idx)

for u in sorted(number.items(), key=operator.itemgetter(1), reverse=True):
    if u[1] == 0:
        break

    result += u[1] * start
    start -= 1
print(result)