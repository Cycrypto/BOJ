n, k = map(int, input().split())
s = list(map(int, input().split()))
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i-1] + s[i-1]

left, right = 0, k
result = -float('inf')
while left <= n - k:
    result = max(result, p[right] - p[left])
    left += 1
    right += 1
print(result)