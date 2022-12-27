string = list(input())
bomb_str = input()
end = bomb_str[-1]
stack = []

for c in string:
    stack.append(c)
    if c == end and ''.join(stack[-len(bomb_str):]) == bomb_str:
        del stack[-len(bomb_str):]

print(''.join(stack) if len(stack) else "FRULA")