with open('resources/day01.txt', 'r') as f:
    i = 0
    for r in f.read():
        i += 1 if r == '(' else -1 if r == ')' else 0
    print(f'Part 1: {i}')
