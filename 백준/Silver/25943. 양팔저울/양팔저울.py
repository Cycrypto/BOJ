k = int(input())
stone = list(map(int, input().split()))
left, right = [stone[0]], [stone[1]]
for i in  stone[2:]:
    if sum(left) == sum(right):
        left.append(i)
    else:
        if sum(left) > sum(right):
            right.append(i)
        else:
            left.append(i)

between = abs(sum(left) - sum(right))
weight = [100, 50, 20, 10, 5, 2, 1]
w = 0
cnt = 0
while between:
    if weight[w] <= between:
        between -= weight[w]
        cnt += 1
    else:
        w += 1
print(cnt)