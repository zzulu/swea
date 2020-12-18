"""
4047. 영준이의 카드 카운팅
"""

import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())

# for test_case in range(1, T+1):
#     cards = input()
#     hand = {'S':[], 'D':[], 'H':[], 'C':[]}
#     for n in range(len(cards)//3):
#         shape = cards[n*3]
#         number = cards[n*3+1:n*3+3]
#         if number not in hand[shape]:
#             hand[shape] += [number]
#         else:
#             print('#{} ERROR'.format(test_case))
#             break
#     else:
#         result = [13-len(n) for n in hand.values()]
#         print('#{} {} {} {} {}'.format(test_case, *result))

T = int(input())

for tc in range(1, T+1):
    cards = input()
    card_count = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    check_list = []

    for _ in range(0, len(cards), 3):
        if cards[:3] not in check_list:
            check_list.append(cards[:3])
            card_count[check_list[-1][0]] -= 1
            cards = cards[3:]
        else:
            print('#{} {}'.format(tc, 'ERROR'))
            break
    else:
        print('#{} {} {} {} {}'.format(tc, *card_count.values()))
