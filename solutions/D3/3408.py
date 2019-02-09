"""
3408. 세가지 합 구하기
"""
# def three(n):
#     return int(n*(n+1)/2), n**2, n*(n+1)

for t in range(int(input())):
    n = int(input()); a = n*(n+1)//2; e = a*2; o = e-n
    print(f'#{t+1} {a} {o} {e}')
