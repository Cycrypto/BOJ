plant = int(input())
lst = list(map(sum, zip(sorted(list(map(int, input().split())), reverse=True), [i for i in range (1, plant + 1)])))
print(max(lst) + 1)
