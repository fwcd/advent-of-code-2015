import re

def apply(rules, start):
    molecules = set()
    for [lhs, rhs] in rules:
        for i in range(len(start) - len(lhs) + 1):
            if start[i:(i + len(lhs))] == lhs:
                new = start[:i] + rhs + start[(i + len(lhs)):]
                molecules.add(new)
    return molecules

def main():
    with open('resources/day19.txt', 'r') as f:
        [first, start] = [p.strip() for p in f.read().split('\n\n') if p.strip()]
        rules = re.findall(r'(\w+) => (\w+)', first)
        print(f'Part 1: {len(apply(rules, start))}')
        molecules = {'e'}
        i = 0
        while start not in molecules:
            new_molecules = set()
            for mol in list(molecules):
                for new in apply(rules, mol):
                    new_molecules.add(new)
            molecules = new_molecules
            i += 1
            print(f'>> {i} ({len(molecules)} total)')
        print(f'Part 2: {i}')

if __name__ == "__main__":
    main()
