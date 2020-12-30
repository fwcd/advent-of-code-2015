def combinations(remaining):
    if len(remaining) == 0:
        return [[]]
    else:
        n = remaining[0]
        combs = []
        for comb in combinations(remaining[1:]):
            combs.append(comb)
            combs.append([n] + comb)
        return combs

def main():
    with open('resources/day17.txt', 'r') as f:
        goal = 150
        ns = [int(l.strip()) for l in f.readlines() if l.strip()]
        cs = combinations(ns)
        print(f'Part 1: {len([c for c in cs if sum(c) == goal])}')

        mn = min(len(c) for c in cs if sum(c) == goal)
        print(f'Part 2: {len([c for c in cs if sum(c) == goal and len(c) == mn])}')

if __name__ == "__main__":
    main()
