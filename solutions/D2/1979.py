def each_axis(n, p):
    return p, [[p[j][i] for j in range(n)] for i in range(n)]
            
for t in range(int(input())):
    n, k = map(int, input().split())
    p = [[x for x in input().split()] for _ in range(n)]
    print(f"#{t+1} {sum(''.join(l).split('0').count('1'*k) for b in each_axis(n, p) for l in b)}")