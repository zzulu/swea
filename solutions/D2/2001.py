"""
2001. 파리 퇴치
"""

for t in range(1,int(input())+1):
    N, M = map(int, input().split())
    flies = []
    for i in range(N):
        flies.append(list(map(int, input().split())))

    died = []
    for v in range(N-M+1):
        for h in range(N-M+1):
            s = 0
            for m in range(M):
                s += sum(flies[v+m][h:h+M])
            died.append(s)

    print(f'#{t} {max(died)}')
