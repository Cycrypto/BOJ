n = int(input())
A = list(map(int, input().split()))

count = 0
start = 0

for end in range(n):
    if end > 0 and A[end] <= A[end - 1]:
        start = end
    count += end - start + 1

print(count)


