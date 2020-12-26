import re

with open('resources/day06.txt', 'r') as f:
    grid1 = set()
    grid2 = [[0 for i in range(1000)] for j in range(1000)]
    for l in f.readlines():
        match = re.search(r'(toggle|turn (?:on|off))\s+(\d+),(\d+)\s+through\s+(\d+),(\d+)', l.strip())
        if match:
            x1, y1 = (int(match[2]), int(match[3]))
            x2, y2 = (int(match[4]), int(match[5]))
            toggle = match[1] == 'toggle'
            on = not toggle and match[1].endswith('on')
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    i = y * 1000 + x
                    if on or (toggle and not i in grid1):
                        grid1.add(i)
                    else:
                        grid1.discard(i)
                    grid2[y][x] = max(0, grid2[y][x] + (2 if toggle else 1 if on else -1))
    print(f'Part 1: {len(grid1)}')
    print(f'Part 2: {sum(sum(row) for row in grid2)}')
