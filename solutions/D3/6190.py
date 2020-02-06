"""
6190. 정곤이의 단조 증가하는 수
"""

def check(n):
    n, r = n//10, n%10
    while n:
        if n%10 > r:
            return False
        n, r = n//10, n%10
    return True

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = [int(n) for n in input().split()]
    result = -1
    for index, i in enumerate(numbers):
        for j in numbers[index+1:]:
            if i*j > result:
                if check(i*j):
                    result = i*j
    
    print('#{} {}'.format(tc, result))
