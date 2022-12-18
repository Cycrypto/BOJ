import operator
from string import ascii_uppercase
number = {i: 0 for i in ascii_uppercase}
start = 9
result = 0

op = [input() for i in range(int(input()))]

for j in op:
    for idx, k in enumerate(j):
        number[k] += (10 ** (len(j) - idx - 1))

for u, v in sorted(number.items(), key=operator.itemgetter(1), reverse=True):
    if v == 0:
        break
    result += v * start
    start -= 1
print(result)
