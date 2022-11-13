iters = int(input())
arr = []

for i in range(iters):
    arr.append(tuple(map(int, input().split())))


c = sorted(arr, key = lambda arr : (arr[0], arr[1]))

for i in c:
    print(i[0],i[1])

