with open('resources/day02.txt', 'r') as f:
    area = 0
    ribbon = 0
    for line in f.readlines():
        [l, w, h] = map(int, line.strip().split('x'))
        areas = [l * w, w * h, h * l]
        perimeters = map(lambda x: 2 * x, [l + w, w + h, h + l])
        area += sum(map(lambda x: 2 * x, areas)) + min(areas)
        ribbon += min(perimeters) + l * w * h
    print(f'Part 1: {area}')
    print(f'Part 2: {ribbon}')
