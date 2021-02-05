"""
5431. 민석이의 과제 체크하기
"""

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    submitted = list(map(int, input().split()))

    result = []
    for n in range(1, N+1):
        if n not in submitted:
            result.append(str(n))

    print('#{} {}'.format(tc, ' '.join(result)))
