from collections import defaultdict, deque

gear = defaultdict(deque)
score = [1, 2, 4, 8]
lt, rt = 6, 2

for i in range(1, 5):
    for e in map(int, input().strip()):
        gear[i].append(e)


def turn_left(g, r=0):
    left_contact = gear[g][lt]
    right_contact = gear[g][rt]

    if r != +1 and g - 1 > 0:
        if left_contact != gear[g - 1][rt]:
            turn_right(g - 1, -1)

    if r != -1 and g + 1 <= 4:
        if right_contact != gear[g + 1][lt]:
            turn_right(g + 1, +1)

    tmp = gear[g].popleft()
    gear[g].append(tmp)


def turn_right(g, r=0):
    left_contact = gear[g][lt]
    right_contact = gear[g][rt]

    if r != +1 and g - 1 > 0:
        if left_contact != gear[g - 1][rt]:
            turn_left(g - 1, -1)

    if r != -1 and g + 1 <= 4:
        if right_contact != gear[g + 1][lt]:
            turn_left(g + 1, +1)

    tmp = gear[g].pop()
    gear[g].appendleft(tmp)


for _ in range(int(input())):
    o, h = map(int, input().split())
    if h == -1:
        turn_left(o, 0)
    else:
        turn_right(o, 0)

ans = 0
for i in range(1, 5):
    if gear[i][0] == 1:
        ans += score[i - 1]
print(ans)
