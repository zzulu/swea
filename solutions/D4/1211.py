"""
1211. Ladder2
"""

for _ in range(10):
    tc = input()

    radder = [[int(n) for n in input().split()] for _ in range(100)]

    start_indices = [i for i, v in enumerate(radder[0]) if v] # [0, 3, 12, 18, ...]

    shortest, result = 0, 0
    for index, starting in enumerate(start_indices): 
        x, distance = start_indices[index], 0
        for y in range(100):
            if not x == 99 and radder[y][x+1]:
                distance += start_indices[index+1] - start_indices[index]
                index += 1

            if not x == 0 and radder[y][x-1]:
                distance += start_indices[index] - start_indices[index-1]
                index -= 1

            x = start_indices[index]
        
        if not shortest or shortest > distance:
            shortest = distance
            result = starting

    print('#{} {}'.format(tc, result))
