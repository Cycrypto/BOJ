plusArr = []
minusArr = []
result = 0

for i in range(int(input())):
    k = int(input())
    if k == 1:
        result += 1

    elif k > 1:
        plusArr.append(k)

    else:
        minusArr.append(k)

plusArr.sort()
minusArr.sort(reverse=True)

while len(plusArr) > 1:
    result += plusArr.pop() * plusArr.pop()
if len(plusArr) != 0:
    result += plusArr.pop()

while len(minusArr) > 1:
    result += minusArr.pop() * minusArr.pop()

if len(minusArr) != 0:
    result += minusArr.pop()

print(result)