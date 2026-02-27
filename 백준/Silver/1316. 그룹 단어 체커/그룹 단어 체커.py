def solve(check):
    s = set()
    k = check[0]

    s.add(k)

    for i in range(1, len(check)):
        if check[i] not in s:
            k = check[i]
            s.add(k)

        elif check[i] != k:
            return False
    return True


if __name__ == "__main__":
    cnt = 0
    for _ in range(int(input())):
        check = input()
        cnt = (cnt + 1) if solve(check) else cnt
    print(cnt)