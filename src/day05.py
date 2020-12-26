VOWELS = {'a', 'e', 'i', 'o', 'u'}

def three_vowels(s):
    return sum(s.count(v) for v in VOWELS) >= 3

def pair(s):
    for (c, d) in zip(s, s[1:]):
        if c == d:
            return True
    return False

def nice(s):
    return three_vowels(s) and pair(s) and not any(p in s for p in ['ab', 'cd', 'pq', 'xy'])

with open('resources/day05.txt', 'r') as f:
    nices = len([l for l in f.readlines() if nice(l)])
    print(f'Part 1: {nices}')
