import math as m,re
board = list(open('2023/day3inputtest.txt'))
chars = {(r, c): [] for r in range(10) for c in range(10) if board[r][c] not in '0123456789.'}

print(board)
print(chars)