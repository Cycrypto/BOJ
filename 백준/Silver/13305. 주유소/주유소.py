n = int(input())
dist = [0] + list(map(int, input().split()))
cost = list(map(int, input().split()))

current_cost = 987654321
result = 0

for i in range(n-1):
    if cost[i] < current_cost:
        current_cost = cost[i]

    result += (current_cost * dist[i+1])

print(result)