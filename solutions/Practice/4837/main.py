"""
4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합
"""

def subset(n, k, num):
    if n == 0 and k == 0:
        return 1

    count = 0
    while num > 0:
        if n-1 < 0 and k-num < 0:
            break;
        count += subset(n-1, k-num, num-1)
        num -= 1
    return count


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    count = subset(N, K, min(K, 12))
    print('#{} {}'.format(tc, count))
