"""
5356. 의석이의 세로로 말해요
"""

T = int(input())

for tc in range(1, T+1):
    words = [input() for _ in range(5)]
    result = ''
    for x in range(15):
        vertical = ''
        for y in range(5):
            vertical += words[y][x:x+1]
        if not vertical:
            break
        result += vertical
    print('#{} {}'.format(tc, result))
