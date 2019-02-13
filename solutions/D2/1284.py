"""
1284. 수도 요금 경쟁
"""
for t in range(int(input())):
    P, Q, R, S, W = map(int, input().split())
    a = P*W; b = Q+S*(W-R) if W > R else Q
    print(f'#{1} {b if a > b else a}')
