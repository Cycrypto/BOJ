import sys

input = sys.stdin.readline

if __name__ == "__main__":
    da= []
    for _ in range(int(input())):
        a, b, c, d = input().split()
        da.append([a] + list(map(int, [b, c, d])))
    da.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
    for n in da:
        print(n[0])