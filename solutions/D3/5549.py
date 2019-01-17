"""
5549. 홀수일까 짝수일까
"""

for t in range(int(input())):
    r = 'Odd' if int(input()) % 2 else 'Even'
    print(f'#{t+1} {r}')
    
