with open('resources/day03.txt', 'r') as f:
    x = 0
    y = 0
    visited = set()
    def deliver():
        visited.add(f'{x},{y}')
    for c in f.read():
        deliver()
        x += 1 if c == '>' else -1 if c == '<' else 0
        y += 1 if c == 'v' else -1 if c == '^' else 0
    deliver()
    print(f'Part 1: {len(visited)}')
