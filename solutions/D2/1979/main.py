"""
1979. 어디에 단어가 들어갈 수 있을까
"""

import sys
sys.stdin = open('input.txt', 'r')


def each_axis(n, puzzle):
    return puzzle, [[puzzle[j][i] for j in range(n)] for i in range(n)]


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [[n for n in input().split()] for _ in range(N)]
    result = 0
    for board in each_axis(N, puzzle):
        for line in board:
            result += ''.join(line).split('0').count('1'*K)
    print('#{} {}'.format(tc, result))
