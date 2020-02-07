"""
1211. Ladder2
"""

for _ in range(10):
    tc = input()

    radder = [[int(n) for n in input().split()] for _ in range(100)]

    startings = [i for i, v in enumerate(radder[0]) if v] # [0, 3, 12, 18, ...]

    shortest, result = 0, 0
    for index, starting in enumerate(startings): 
        x, y, distance = startings[index], 0, 0
        while y < 100:
            if not x == 99 and radder[y][x+1]:
                distance += startings[index+1] - startings[index]
                index += 1

            if not x == 0 and radder[y][x-1]:
                distance += startings[index] - startings[index-1]
                index -= 1

            x = startings[index]
            y += 1
        
        if not shortest or shortest > distance:
            shortest = distance
            result = starting

    print('#{} {}'.format(tc, result))
