from itertools import islice

def to_num(s):
    n = 0
    factor = 1
    for i in range(len(s)):
        n += (ord(s[-(i + 1)]) - ord('a')) * factor
        factor *= 26
    return n

def digits(n):
    while n != 0:
        yield n % 26
        n = n // 26

def from_num(n):
    s = ''
    for d in digits(n):
        s = chr(d + ord('a')) + s
    return s or 'a'

def increasing_seq(n):
    for (c, d, e) in zip(digits(n), islice(digits(n), 1, None), islice(digits(n), 2, None)):
        if e == d - 1 and d == c - 1:
            return True
    return False

def pairs(n):
    for (i, (c, d)) in enumerate(zip(digits(n), islice(digits(n), 1, None))):
        for (j, (e, f)) in enumerate(zip(digits(n), islice(digits(n), 1, None))):
            if abs(i - j) >= 2 and c == d and e == f and c != e:
                return True
    return False

def valid(n):
    return increasing_seq(n) and pairs(n) and not any(c in digits(n) for c in 'iol')

def next_valids(n):
    while True:
        while not valid(n):
            n += 1
        yield n
        n += 1

def main():
    with open('resources/day11.txt', 'r') as f:
        n = to_num(f.read().strip())
        pws = next_valids(n)
        print(f'Part 1: {from_num(next(pws))}')
        print(f'Part 2: {from_num(next(pws))}')

if __name__ == "__main__":
    main()
