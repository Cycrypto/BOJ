import sys
input = sys.stdin.readline

s = input().strip()
bomb = input().strip()
bl = len(bomb)

st = []
last = bomb[-1]

for ch in s:
    st.append(ch)
    if ch == last and len(st) >= bl:
        if ''.join(st[-bl:]) == bomb:
            del st[-bl:]

print(''.join(st) if st else "FRULA")