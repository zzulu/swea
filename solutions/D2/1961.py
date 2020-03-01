"""
1961. 숫자 배열 회전
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = [ list(map(int, input().split())) for _ in range(N) ]

    print('#{}'.format(tc))
    for y in range(N):
        # 90도
        for x in range(N):
            print(numbers[N-1-x][y], end='')
        print(end=' ')
        # 180도
        for x in range(N):
            print(numbers[N-1-y][N-1-x], end='')
        print(end=' ')
        # 270도
        for x in range(N):
            print(numbers[x][N-1-y], end='')
        print()
