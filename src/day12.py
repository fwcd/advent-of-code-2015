import json

def total(elem):
    t = type(elem)
    if t is dict:
        return sum(total(v) for _, v in elem.items())
    elif t is list:
        return sum(map(total, elem))
    elif t is int:
        return elem
    else:
        return 0

def main():
    with open('resources/day12.json', 'r') as f:
        elem = json.loads(f.read().strip())
        print(f'Part 1: {total(elem)}')

if __name__ == "__main__":
    main()
