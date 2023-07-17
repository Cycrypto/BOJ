MOD = 1000000007
def solve(ans):
    n = int(input())
    if n == 0:
        return 1
    if n % 3 != 0:
        return 0
    
    return ans[n // 3]


if __name__ == "__main__":
    ans = [1, 3, 13]
    for i in range(3, 10000, 1):
        k = (((5 * ans[i-1]) % MOD) + MOD - ((3 * ans[i-2]) % MOD) + ans[i-3])% MOD
        ans.append(k)
    
    for i in range(int(input())):
        print(solve(ans))