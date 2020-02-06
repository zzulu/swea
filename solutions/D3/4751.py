"""
4751. 다솔이의 다이아몬드 장식
"""

T = int(input())

for tc in range(1, T+1):
    word = input()
    length = len(word)
    print('..' + '...'.join('#'*length) + '..')
    print('.#' + '#.#'.join('.'*length) + '#.')
    print('#.' + '.#.'.join(word) + '.#')
    print('.#' + '#.#'.join('.'*length) + '#.')
    print('..' + '...'.join('#'*length) + '..')
