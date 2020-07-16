"""
1206. [S/W 문제해결 기본] 1일차 - View
"""

for tc in range(1, 11):
    h = int(input())
    b = list(map(int, input().split()))

    count = 0
    for i in range(2, h-2):
        if b[i]-b[i-2] > 0 and b[i]-b[i-1] > 0 and b[i]-b[i+1] > 0 and b[i]-b[i+2] > 0:
            count += b[i] - max(b[i-2], b[i-1], b[i+1], b[i+2])

    print('#{} {}'.format(tc, count))

