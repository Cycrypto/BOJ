import sys
input = sys.stdin.readline

def solve(op, l):
    le, r = 0, len(l)
    rev_flag = False

    for o in op:
        if o == 'R':
            rev_flag = not rev_flag
        else:
            if le >= r:
                return None, None
            if not rev_flag:
                le += 1
            else:
                r -= 1

    return l[le:r], rev_flag


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        op = input().strip()
        n = int(input())
        arr = input().strip()

        if arr == "[]":
            l = []
        else:
            l = list(map(int, arr[1:-1].split(',')))

        result, flag = solve(op, l)
        if result is None:
            print("error")
        else:
            if flag:
                result = result[::-1]
            print("[" + ",".join(map(str, result)) + "]")