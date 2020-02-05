"""
2005. 파스칼의 삼각형
"""

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    print('#{}'.format(test_case))

    prev_line = [0, 1, 0]
    print(''.join([str(n) for n in prev_line[1:-1]]))
    for length in range(2, N+1):
        curr_line = [0] + [ prev_line[i] + prev_line[i+1] for i in range(length) ] + [0]
        print(' '.join([str(n) for n in curr_line[1:-1]]))
        prev_line = curr_line
