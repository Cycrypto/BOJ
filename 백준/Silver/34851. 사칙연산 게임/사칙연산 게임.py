import sys
input = sys.stdin.readline

MOD = 1_000_000_007

n = int(input())
nums = list(map(int, input().split()))

ans = nums[0] % MOD

r = 0 if nums[0] == 0 else (1 if nums[0] == 1 else 2)

for x in nums[1:]:
    if r < 2:
        ans = (ans + x) % MOD

        if r == 0:
            if x == 0:
                r = 0
            elif x == 1:
                r = 1
            else:
                r = 2
        else:
            if x == 0:
                r = 1
            else:
                r = 2
    else:
        if x <= 1:
            ans = (ans + x) % MOD
        else:
            ans = (ans * (x % MOD)) % MOD

print(ans)
