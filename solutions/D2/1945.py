"""
1945. 간단한 소인수분해
"""

for t in range(int(input())):
    n = int(input()); r = []
    for i in [2, 3, 5, 7, 11]:
        q = n; c = 0
        while not q % i:
            q //= i; c += 1
        r.append(str(c))
    print(f'#{t+1} {" ".join(r)}')
