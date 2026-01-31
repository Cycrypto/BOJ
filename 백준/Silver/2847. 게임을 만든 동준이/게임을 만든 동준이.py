import sys
input = sys.stdin.readline

n = int(input())
stage = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n - 2, -1, -1):
    if stage[i] >= stage[i + 1]:
        new_score = stage[i + 1] - 1
        cnt += stage[i] - new_score
        stage[i] = new_score

print(cnt)