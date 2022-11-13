from collections import deque
dq = deque()
i = 0
inp = list(map(int, input().split()))
strs = input()

for i in range (len(strs)):
    while (inp[1] != 0 and len(dq) != 0 and strs[i] > dq[-1]):
        dq.pop();
        inp[1] -=1


    dq.append(strs[i])

for j in range(len(dq) - inp[1]):
    print(dq[j], end='')
