import re
import functools

def score(values):
    if not values:
        return 0
    return functools.reduce(lambda x, y: x * y, [max(0, v) for k, v in values.items() if k != 'calories'])

def cookies(total, ingreds):
    if len(ingreds) == 1:
        yield {prop: total * value for prop, value in next(iter(ingreds.values())).items()}
        return

    for ingred, props in dict(ingreds).items():
        for i in range(total):
            del ingreds[ingred]
            for cookie in cookies(total - i, ingreds):
                for prop, value in props.items():
                    cookie[prop] = cookie.get(prop, 0) + (i * value)
                yield cookie
            ingreds[ingred] = props

def main():
    with open('resources/day15.txt', 'r') as f:
        ingreds = dict()
        for line in f.readlines():
            l = line.strip()
            if l:
                [name, raw_props] = [s.strip() for s in l.split(':')]
                props = dict()
                for prop, value in re.findall(r'(\w+)\s+(-?\d+)', raw_props):
                    props[prop] = int(value)
                ingreds[name] = props
        print(f'Part 1: {max(score(c) for c in cookies(100, ingreds))}')
        print(f"Part 2: {max(score(c) for c in cookies(100, ingreds) if c['calories'] == 500)}")

if __name__ == "__main__":
    main()
