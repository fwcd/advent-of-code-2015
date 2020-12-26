with open('resources/day03.txt', 'r') as f:
    x, y, sx, sy, rx, ry = (0, 0, 0, 0, 0, 0)
    pt1_visited = set()
    pt2_visited = set()
    def deliver():
        pt1_visited.add(f'{x},{y}')
        pt2_visited.add(f'{sx},{sy}')
        pt2_visited.add(f'{rx},{ry}')
    for (i, c) in enumerate(f.read()):
        deliver()
        dx, dy = (0, 0)
        dx = 1 if c == '>' else -1 if c == '<' else 0
        dy = 1 if c == 'v' else -1 if c == '^' else 0
        x += dx
        y += dy
        if i % 2 == 0:
            sx += dx
            sy += dy
        else:
            rx += dx
            ry += dy
    deliver()
    print(f'Part 1: {len(pt1_visited)}')
    print(f'Part 2: {len(pt2_visited)}')
