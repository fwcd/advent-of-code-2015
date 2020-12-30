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
        ns = [int(l.strip()) for l in f.readlines() if l.strip()]
        print(f'Part 1: {len([c for c in combinations(ns) if sum(c) == 150])}')

if __name__ == "__main__":
    main()
