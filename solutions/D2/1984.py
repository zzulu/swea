"""
1984. 중간 평균값 구하기
"""

for t in range(int(input())):
    l = [int(n) for n in input().split()]
    l.remove(max(l))
    l.remove(min(l))
    print(f'#{t+1} {round(sum(l)/len(l))}')
    