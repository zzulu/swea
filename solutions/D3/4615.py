"""
4615. 재미있는 오셀로 게임
"""

T = int(input())
for tc in range(1, T+1):
    N, M = (int(n) for n in input().split())
    
    # 판 초기화
    board = [ [ 0 for _ in range(N+2) ] for _ in range(N+2) ]
    board[N//2][N//2], board[N//2][N//2+1] = 2, 1
    board[N//2+1][N//2], board[N//2+1][N//2+1] = 1, 2

    for _ in range(M):
        x, y, stone = (int(n) for n in input().split())
        board[y][x] = stone
    
        delta = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)] # 8 방향

        for xd, yd in delta:
            step_x, step_y = xd, yd
            while board[y+yd][x+xd]: # 돌이 없거나 가장자리까지
                if board[y+yd][x+xd] == stone: # 같은 돌이 있는지 찾음
                    xd, yd = step_x, step_y # 거리 초기화
                    while board[y+yd][x+xd] != stone: # 해당 위치까지 (같은 돌이 있는지 확인 되었으므로)
                        board[y+yd][x+xd] = stone # 돌 교체
                        xd += step_x
                        yd += step_y
                    break
                xd += step_x
                yd += step_y

    # 돌 갯수 세기
    b, w = 0, 0
    for line in board:
        for cell in line:
            if cell == 1:
                b += 1
            elif cell == 2:
                w += 1

    print('#{} {} {}'.format(tc, b, w))
