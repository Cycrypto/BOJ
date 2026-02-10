def solution(name):
    n = len(name)
    updown = 0
    for c in name:
        updown += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
        
    move = n - 1

    for i in range(n):
        j = i + 1
        while j < n and name[j] == 'A':
            j += 1

        move = min(move, 2 * i + (n - j), i + 2 * (n - j))

    return updown + move
