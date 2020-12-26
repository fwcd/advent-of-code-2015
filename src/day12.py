import json

def total(elem, ignored=None):
    t = type(elem)
    if t is dict:
        return sum(total(v, ignored) for _, v in elem.items()) if not ignored or ignored not in elem.values() else 0
    elif t is list:
        return sum(total(v, ignored) for v in elem)
    elif t is int:
        return elem
    else:
        return 0

def main():
    with open('resources/day12.json', 'r') as f:
        elem = json.loads(f.read().strip())
        print(f'Part 1: {total(elem)}')
        print(f"Part 2: {total(elem, ignored='red')}")

if __name__ == "__main__":
    main()
