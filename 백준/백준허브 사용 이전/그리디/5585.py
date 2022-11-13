N = 1000 - int(input())
cnt = 0

while (N != 0):
    if (N // 500 != 0):
        cnt = cnt + (N//500)
        N = N - (500 * (N//500))

    elif (N // 100 != 0):
        cnt = cnt + (N//100)
        N = N - (100 * (N//100))

    elif (N // 50 != 0):
        cnt = cnt + (N//50)
        N = N - (50 * (N//50))

    elif (N //10 != 0):
        cnt = cnt + (N//10)
        N = N - (10 * (N//10))

    elif (N // 5 != 0):
        cnt = cnt + (N//5)
        N = N - (5 * (N//5))

    else:
        cnt = cnt + N
        N = 0

print(cnt)
    
