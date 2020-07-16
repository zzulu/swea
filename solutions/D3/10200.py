"""
10200. 구독자 전쟁
"""

T = int(input())
for tc in range(1, T+1):
    N, P, T = list(map(int, input().split()))

    max_n = T if P > T else P
    min_n = P + T - N if P + T > N else 0

    print('#{} {} {}'.format(tc, max_n, min_n))
