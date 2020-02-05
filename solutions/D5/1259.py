"""
1259. [S/W 문제해결 응용] 7일차 - 금속막대 
"""

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    P = [n for n in input().split()]

    pipes = [[P[i], P[i+1]] for i in range(0, N*2, 2)]
    
    connected = pipes.pop()
    while pipes:
        for i in range(len(pipes)): # index 찾아서 pop 하는 것보다 그냥 index로 돌리는게 나을거 같아서!
            if pipes[i][0] == connected[-1]:
                connected = connected + pipes.pop(i)
                break
            if pipes[i][-1] == connected[0]:
                connected = pipes.pop(i) + connected
                break
        # print(pipes)


    result = ' '.join(connected)
    print('#{} {}'.format(test_case, result))