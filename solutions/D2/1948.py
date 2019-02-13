"""
1948. 날짜 계산기
"""

c = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for t in range(int(input())):
    m1, d1, m2, d2 = map(int, input().split())
    print(f'#{t+1} {sum(c[m] for m in range(m1, m2))-(d1-d2)+1}')
