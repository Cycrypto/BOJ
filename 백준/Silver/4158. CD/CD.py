import sys
input = sys.stdin.readline
print = sys.stdout.write
def bi_search(lst, start, end, target): # start와 end는 인덱스
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return 1
        elif lst[mid] < target:
            start  = mid + 1
        else:

            end = mid - 1
    return 0

while True:
    n, m = map(int, input().split())
    n_list = []
    m_list = []
    if n == 0 and m == 0:
        break

    for _ in range(n):
        n_list.append(int(input()))

    for _ in range(m):
        m_list.append(int(input()))

    result = 0
    for x in n_list:
        start, end = 0, len(m_list)
        result += bi_search(m_list, start, end, x)
    print(str(result)+"\n")