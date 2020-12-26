def look_and_say(n):
    last = None
    count = 1
    result = ''
    def say():
        nonlocal result
        nonlocal last
        if last:
            result += f'{count}{last}'
    for digit in map(int, str(n)):
        if digit == last:
            count += 1
        else:
            say()
            count = 1
        last = digit
    say()
    return int(result)

n = 1113122113

for i in range(40):
    n = look_and_say(n)

print(f'Part 1: {len(str(n))}')
