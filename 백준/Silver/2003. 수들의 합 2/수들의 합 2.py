n, m = map(int, input().split())
s = list(map(int, input().split()))
p = [0] * (n + 1)

# for i in range(1, n + 1):
#     p[i] = p[i - 1] + s[i - 1]
#
left, right = 0, 0
current_sum = 0
answer = 0

while True:
    if current_sum > m:
        current_sum -= s[left]
        left += 1

    elif current_sum < m:
        if right == n:
            break
        current_sum += s[right]
        right += 1

    else:
        answer += 1
        left += 1
        right = left
        current_sum = 0
print(answer)