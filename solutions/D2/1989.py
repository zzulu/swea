"""
1989. 초심자의 회문 검사
"""

for t in range(int(input())):
    w = input().strip(); print(f'#{t+1} {1 if w==w[::-1] else 0}')
