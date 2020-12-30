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

if __name__ == "__main__":
    main()
