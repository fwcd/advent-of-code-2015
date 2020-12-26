with open('resources/day02.txt', 'r') as f:
    total = 0
    for line in f.readlines():
        [l, w, h] = map(int, line.strip().split('x'))
        sides = [l * w, w * h, h * l]
        total += sum(map(lambda x: 2 * x, sides)) + min(sides)
    print(f'Part 1: {total}')
