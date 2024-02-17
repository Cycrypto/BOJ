n = int(input())
deck = sorted(list(map(int, input().split())), reverse=True)
diff = [abs(deck[i] - deck[i-1]) for i in range(1, n)]

maxx = deck[0]
result = 0
for i in deck[1:]:
    result += (maxx+i)

print(result)