import hashlib

def mine(prefix):
    i = 0
    while not hashlib.md5(f'{prefix}{i}'.encode()).hexdigest().startswith('0' * 5):
        i += 1
    return i

with open('resources/day04.txt', 'r') as f:
    print(f'Part 1: {mine(f.read().strip())}')
