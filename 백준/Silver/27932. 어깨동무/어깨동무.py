n, k = map(int, input().split())

if n == 1:
    print("0")
    exit()

heights = list(map(int, input().split()))
score = [0] * n

for i in range(1, n-1):
    score[i] = max(abs(heights[i] - heights[i-1]), abs(heights[i] - heights[i+1]))

score[0] = abs(heights[1] - heights[0])
score[n-1] = abs(heights[n-2] - heights[n-1])

score.sort()
print(0 if n == k else score[n-k-1])