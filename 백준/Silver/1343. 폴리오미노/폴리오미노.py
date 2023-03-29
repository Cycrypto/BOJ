board = input().replace('XXXX', 'AAAA').replace('XX', 'BB')
print(board if 'X' not in board else -1)