import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    p = [0] * (len(s) + 1)
    for k in range(1, len(s) + 1):
        p[k] = p[k - 1] + s[k - 1]

    for _ in range(m):
        i, j = map(int, input().split())
        print(p[j] - p[i - 1])
