import functools
import re

def parse_circuit(raw):
    circuit = dict()

    @functools.lru_cache
    def wire(x):
        try:
            return int(x)
        except:
            return circuit[x]()

    for x, op, y, dest in re.findall(r'([0-9a-z]+)?\s*([A-Z]+)?\s*(\S+)?\s+->\s+(\w+)\n', raw):
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
    
    return circuit

with open('resources/day07.txt', 'r') as f:
    raw = f.read()
    circuit1 = parse_circuit(raw)
    part1 = circuit1['a']()
    print(f"Part 1: {part1}")

    circuit2 = parse_circuit(raw)
    circuit2['b'] = lambda: part1
    part2 = circuit2['a']()
    print(f"Part 2: {part2}")
