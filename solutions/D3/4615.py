"""
4615. 재미있는 오셀로 게임
"""

T = int(input())

for tc in range(1, T+1):
    N, M = (int(n) for n in input().split())
    
    # 판 초기화
    board = [[0 for _ in range(N+2)] for _ in range(N+2)]
    board[(N//2)][(N//2):(N//2)+2] = [2, 1]
    board[(N//2)+1][(N//2):(N//2)+2] = [1, 2]

    for _ in range(M):
        x, y, stone = (int(n) for n in input().split())
        board[y][x] = stone
    
        delta = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)] # 8 방향

        for xd, yd in delta:
            dx, dy = xd, yd
            while board[y+yd][x+xd]: # 돌이 없거나 가장자리까지
                if board[y+yd][x+xd] == stone: # 같은 돌이 있는지 찾음
                    xd, yd = dx, dy # 같은 돌이 있는 위치 기록
                    while board[y+yd][x+xd] != stone: # 해당 위치까지
                        board[y+yd][x+xd] = stone # 돌 교체
                        xd += dx
                        yd += dy
                    break
                xd += dx
                yd += dy

    # 돌 갯수 세기
    b, w = 0, 0
    for line in board:
        for cell in line:
            if cell == 1:
                b += 1
            elif cell == 2:
                w += 1

    print('#{} {} {}'.format(tc, b, w))
