"""
1976. 시각 덧셈
"""
for t in range(int(input())):
    h1, m1, h2, m2 = map(int, input().split())
    M, m = (m1 + m2) // 60, (m1 + m2) % 60
    h = (h1 + h2) % 12 + M
    print(f'#{t+1} {h or 12} {m}')
    # print(f'#{t+1} {((h1+h2)%12)+(m1+m2)//60 or 12} {(m1+m2)%60}')
