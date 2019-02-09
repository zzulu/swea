"""
1954. 달팽이 숫자
"""

def fill(n, c, x, y):
    for i in range(2):
        base = diag(n, c+i)
        r[x][y] = base
        for a in range(1, n-(c+i)+1):
            if (c+i) % 2:
                r[x][y-a] = base-a
                r[x+a][y] = base+a
            else:
                r[x][y+a] = base-a
                r[x-a][y] = base+a
        x, y = y, x

def diag(n, c):
    return (2*c-1)*n-(c*(c-1))

import math
for t in range(int(input())):
    n = int(input()); c = 1
    r = [[0]*n for i in range(n)]

    for i in range(math.ceil(n/2)):
        fill(n, c, i, n-1-i)
        c += 2

    print(f'#{t+1}')
    for row in r:
        for col in row:
            print(col, end=' ')
        print()
