"""
6782. 현주가 좋아하는 제곱근 놀이
"""

for t in range(int(input())):
    n, c = float(input()), 0
    while n != 2:
        n = n**(1/2) if (n**(1/2)).is_integer() else n + 1
        c += 1
    print(f'#{t+1} {c}')