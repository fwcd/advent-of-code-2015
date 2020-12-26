def look_and_say(s):
    last = None
    count = 1
    result = ''
    def say():
        nonlocal result
        nonlocal last
        if last:
            result += f'{count}{last}'
    for c in s:
        if c == last:
            count += 1
        else:
            say()
            count = 1
        last = c
    say()
    return result

def iterate(f, n, x):
    y = x
    for i in range(n):
        y = f(y)
    return y

n = '1113122113'

part1 = iterate(look_and_say, 40, n)
print(f'Part 1: {len(str(part1))}')

part2 = iterate(look_and_say, 10, part1)
print(f'Part 1: {len(str(part2))}')
