"""
1986. 지그재그 숫자
"""

for t in range(int(input())):
    print(f'#{t+1} {sum(n if n % 2 else -n for n in range(1,int(input())+1))}')