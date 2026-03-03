import sys
input = sys.stdin.readline

n = int(input())

a, b, c = map(int, input().split())
prev_max = [a, b, c]
prev_min = [a, b, c]

for _ in range(n - 1):
    a, b, c = map(int, input().split())

    cur_max0 = a + max(prev_max[0], prev_max[1])
    cur_max1 = b + max(prev_max[0], prev_max[1], prev_max[2])
    cur_max2 = c + max(prev_max[1], prev_max[2])

    cur_min0 = a + min(prev_min[0], prev_min[1])
    cur_min1 = b + min(prev_min[0], prev_min[1], prev_min[2])
    cur_min2 = c + min(prev_min[1], prev_min[2])

    prev_max = [cur_max0, cur_max1, cur_max2]
    prev_min = [cur_min0, cur_min1, cur_min2]

print(max(prev_max), min(prev_min))