import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    result = 'ON'
    for _ in range(N):
        M, r = M // 2, M % 2
        if not r:
            result = 'OFF'
            break

    print('#{} {}'.format(tc, result))
