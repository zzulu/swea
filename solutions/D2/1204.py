"""
1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
"""

for t in range(int(input())):
    n, r = int(input()), {}
    for s in input().split():
        r[s] = r[s] + 1 if r.get(s) is not None else 1
    print(f'#{n} {max(sorted(r.items(),reverse=True), key=lambda x: x[1])[0]}')
