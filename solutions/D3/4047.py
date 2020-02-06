"""
4047. 영준이의 카드 카운팅
"""

T = int(input())

for test_case in range(1, T+1):
    cards = input()
    hand = {'S':[], 'D':[], 'H':[], 'C':[]}
    for n in range(len(cards)//3):
        shape = cards[n*3]
        number = cards[n*3+1:n*3+3]
        if number not in hand[shape]:
            hand[shape] += [number]
        else:
            print('#{} ERROR'.format(test_case))
            break
    else:
        result = [13-len(n) for n in hand.values()]
        print('#{} {} {} {} {}'.format(test_case, *result))
