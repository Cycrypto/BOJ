def generateGrid(grid, n):
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    grid.reverse()

def main():
    for i in range(int(input())):
        n, _ = map(int, input().split())
        grid = []
        result = 0

        generateGrid(grid, n)
        # grid 생성
        for i in list(zip(*grid)):
            for idx, j in enumerate(i):
                if j:
                    result += (idx - sum(i[:idx]))
        print(result)


main()