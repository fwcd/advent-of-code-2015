with open('resources/day08.txt', 'r') as f:
    part1 = 0
    for line in f.readlines():
        l = line.strip()
        if l:
            part1 += len(l) - len(eval(l))
    print(f'Part 1: {part1}')
