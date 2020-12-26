VOWELS = {'a', 'e', 'i', 'o', 'u'}

def three_vowels(s):
    return sum(s.count(v) for v in VOWELS) >= 3

def pair(s):
    for (c, d) in zip(s, s[1:]):
        if c == d:
            return True
    return False

def nice1(s):
    return three_vowels(s) and pair(s) and not any(p in s for p in ['ab', 'cd', 'pq', 'xy'])

def pair_twice(s):
    for (i, (c, d)) in enumerate(zip(s, s[1:])):
        for (j, (e, f)) in enumerate(zip(s, s[1:])):
            if abs(i - j) >= 2 and c == e and d == f:
                return True
    return False

def hole(s):
    for (c, d) in zip(s, s[2:]):
        if c == d:
            return True
    return False

def nice2(s):
    return pair_twice(s) and hole(s)

with open('resources/day05.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]
    part1 = len([l for l in lines if nice1(l)])
    part2 = len([l for l in lines if nice2(l)])
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
