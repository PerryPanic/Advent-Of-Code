import math as m,re

# Open and create list
board = list(open('2023/day3input.txt'))
# find position of every non digit or full stop
chars = {(r, c): [] for r in range(140) for c in range(140) if board[r][c] not in '0123456789.'}

# enumerate rows
for r, row in enumerate(board):
    # find series of digits in row. n is match obj. Contains span and string
    for n in re.finditer(r'\d+', row):
        # print(n)
        # get edge of the digits as a set of coordinates row +-1, column from start-1 to end +1
        edge = {(r, c) for r in (r-1, r, r+1)
                    for c in range(n.start()-1, n.end()+1)}        
        # find intersect of edge set and char keys, and append n (the integer) as dict value    
        for o in edge & chars.keys():
            chars[o].append(int(n.group()))
        
print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))