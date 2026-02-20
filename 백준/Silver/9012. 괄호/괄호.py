for _ in range(int(input())):
    stack = []
    for ch in input().strip():
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                print("NO")
                break
            stack.pop()
    else:
        print("YES" if not stack else "NO")