with open('resources/day08.txt', 'r') as f:
    part1 = 0
    part2 = 0
    for line in f.readlines():
        l = line.strip()
        if l:
            part1 += len(l) - len(eval(l))
            part2 += len(l.__repr__().replace('"', '\\"')) - len(l)
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
