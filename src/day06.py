import re

with open('resources/day06.txt', 'r') as f:
    grid = set()
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
                    if on:
                        grid.add(i)
                    elif toggle:
                        if i in grid:
                            grid.remove(i)
                        else:
                            grid.add(i)
                    else:
                        grid.discard(i)
    print(f'Part 1: {len(grid)}')
