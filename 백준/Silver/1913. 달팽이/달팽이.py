import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    target = int(input().strip())

    a = [[0] * n for _ in range(n)]

    r, c = 0, 0
    v = n * n

    tr = tc = -1

    a[r][c] = v
    if v == target:
        tr, tc = r, c

    for _ in range(n - 1):
        r += 1
        v -= 1
        a[r][c] = v
        if v == target:
            tr, tc = r, c

    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    d = 0
    
    for k in range(n - 1, 0, -1):
        for _ in range(2):
            for _ in range(k):
                r += dr[d]
                c += dc[d]
                v -= 1
                a[r][c] = v
                if v == target:
                    tr, tc = r, c
            d = (d + 1) & 3

    out_lines = []
    for row in a:
        out_lines.append(" ".join(map(str, row)))
    out_lines.append(f"{tr + 1} {tc + 1}")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
