str1 = input()
str2 = input()
dp = [[0 for _ in range(len(str2) + 1)] for __ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max(sum(dp, [])))

stream = ''
i, j = len(dp) - 1, len(dp[0]) - 1
while dp[i][j] != 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1

    elif dp[i][j] == dp[i][j - 1]:
        j -= 1

    else:
        i, j = i - 1, j - 1
        stream += str1[i]

print(stream[::-1])