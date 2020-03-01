"""
1974. 스도쿠 검증
"""

T = int(input())
for tc in range(1, T+1):
    numbers = [ list(map(int, input().split())) for _ in range(9) ]

    # 합 이용
    result = 1
    for y in range(9):
        x_sum, y_sum = 0, 0
        for x in range(9):
            x_sum += numbers[y][x]
            y_sum += numbers[x][y]

        if x_sum != 45 or y_sum != 45:
            result = 0
            break

    for y in range(3):
        for x in range(3):
            block_sum = 0
            for dy in range(3):
                for dx in range(3):
                    block_sum += numbers[3*y+dy][3*x+dx]

            if block_sum != 45:
                result = 0
                break

        if not result:
            break

    print('#{} {}'.format(tc, result))
