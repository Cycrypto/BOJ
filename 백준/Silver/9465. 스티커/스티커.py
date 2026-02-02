import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    s0 = list(map(int, input().split()))
    s1 = list(map(int, input().split()))

    if n == 1:
        print(max(s0[0], s1[0]))
        continue

    prev2_0 = s0[0]
    prev2_1 = s1[0]

    prev1_0 = s0[1] + prev2_1
    prev1_1 = s1[1] + prev2_0

    for j in range(2, n):
        cur0 = s0[j] + max(prev1_1, prev2_1)
        cur1 = s1[j] + max(prev1_0, prev2_0)

        prev2_0, prev2_1 = prev1_0, prev1_1
        prev1_0, prev1_1 = cur0, cur1

    print(max(prev1_0, prev1_1))
