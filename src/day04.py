import hashlib

def mine(prefix, n):
    i = 0
    while not hashlib.md5(f'{prefix}{i}'.encode()).hexdigest().startswith('0' * n):
        i += 1
    return i

with open('resources/day04.txt', 'r') as f:
    raw = f.read().strip()
    print(f'Part 1: {mine(raw, 5)}')
    print(f'Part 2: {mine(raw, 6)}')
