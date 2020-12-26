with open('resources/day01.txt', 'r') as f:
    floor = 0
    basement = None
    for (i, r) in enumerate(f.read()):
        floor += 1 if r == '(' else -1 if r == ')' else 0
        if basement == None and floor == -1:
            basement = i + 1
    print(f'Part 1: {floor}, Part 2: {basement}')
