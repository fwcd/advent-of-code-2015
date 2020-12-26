import functools
import re

with open('resources/day07.txt', 'r') as f:
    circuit = dict()

    @functools.lru_cache
    def wire(x):
        try:
            return int(x)
        except:
            return circuit[x]()

    for x, op, y, dest in re.findall(r'([0-9a-z]+)?\s*([A-Z]+)?\s*(\S+)?\s+->\s+(\w+)\n', f.read()):
        print(f'x: {x}, op: {op}, y: {y}, dest: {dest}')
        if op == 'AND':
            circuit[dest] = lambda x=x, y=y: wire(x) & wire(y)
        elif op == 'OR':
            circuit[dest] = lambda x=x, y=y: wire(x) | wire(y)
        elif op == 'LSHIFT':
            circuit[dest] = lambda x=x, y=y: wire(x) << wire(y)
        elif op == 'RSHIFT':
            circuit[dest] = lambda x=x, y=y: wire(x) >> wire(y)
        elif op == 'NOT':
            circuit[dest] = lambda y=y: ~wire(y)
        else:
            circuit[dest] = lambda x=x: wire(x)

    print(f"Part 1: {circuit['a']()}")
