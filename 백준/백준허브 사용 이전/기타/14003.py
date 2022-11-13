import sys

read = sys.stdin.readline
n = read()
arr = list(map(int, read().split()))


def bi_search(num):
    l = 0
    h = len(solve)
    ret = float("inf")

    while l <= h:
        mid = (l + h) // 2
        if solve[mid] >= num:
            if ret > mid:
                ret = mid
            h = mid - 1

        else:
            l = mid + 1

    return ret

solve = [arr[0]]
for i in range(1, len(arr)):
    if solve[-1] >= arr[i]:  # LIS 마지막 값보다 들어온 arr 값이 더 작은 경우
        solve[bi_search(arr[i])] = arr[i]

    else:
        solve.append(arr[i])

print(len(solve))
print(*solve)

####################################################################################### 정답 코드 #######################################################################################
import bisect as bs

n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
# 문제의 조건에 음수가 포함되므로 최저를 0이 아닌 -무한대로 설정해준다.
cp = [-float('inf')]

for i in range(1, n + 1):
    if nums[i] > cp[-1]:
        cp.append(nums[i])
        dp[i] = len(cp) - 1
    else:
        dp[i] = bs.bisect_left(cp, nums[i])
        cp[dp[i]] = nums[i]
print(len(cp) - 1)

# 역추적
max_idx, ans = max(dp) + 1, []
for i in range(n, 0, -1):
    if dp[i] == max_idx - 1:
        ans.append(nums[i])
        max_idx = dp[i]
print(*ans[::-1])
