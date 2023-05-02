import sys
input = sys.stdin.readline
# print = sys.stdout.write

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

    print(len(set(n_list) & set(m_list)))