for _ in range(int(input())):
    heading = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    exc = list(input().strip())
    result = [0, 0]
    ptr = 0

    mx, my = 0, 0
    mix, miy = 0, 0
    for e in exc:
        if e == 'L':
            ptr = (ptr - 1) % 4
        elif e == 'R':
            ptr = (ptr + 1) % 4
        elif e == 'F':
            result[0] += heading[ptr][0]
            result[1] += heading[ptr][1]
        else:
            result[0] -= heading[ptr][0]
            result[1] -= heading[ptr][1]

        mx = max(mx, result[0])
        my = max(my, result[1])
        mix = min(mix, result[0])
        miy = min(miy, result[1])

    print((mx - mix) * (my-miy))