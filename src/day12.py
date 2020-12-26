import json

def part2_total(elem):
    t = type(elem)
    if t is dict:
        return sum(part2_total(v) for k, v in elem.items()) if 'red' not in elem.values() else 0
    elif t is list:
        return sum(map(part2_total, elem))
    elif t is int:
        return elem
    else:
        return 0

def part1_total(elem):
    t = type(elem)
    if t is dict:
        return sum(part1_total(v) for _, v in elem.items())
    elif t is list:
        return sum(map(part1_total, elem))
    elif t is int:
        return elem
    else:
        return 0

def main():
    with open('resources/day12.json', 'r') as f:
        elem = json.loads(f.read().strip())
        print(f'Part 1: {part1_total(elem)}')
        print(f'Part 2: {part2_total(elem)}')

if __name__ == "__main__":
    main()
