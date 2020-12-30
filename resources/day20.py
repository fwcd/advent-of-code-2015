import sys

def house(n):
    total = n
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            total += i
    return 10 * total

def main():
    with open('resources/day20.txt', 'r') as f:
        n = int(f.read().strip())
        part1 = 0
        while house(part1) < n:
            part1 += 1
            if part1 % 1000 == 0:
                sys.stdout.write(f'\r{part1}: {house(part1)}')
        print()
        print(f'Part 1: {part1}')

if __name__ == '__main__':
    main()
