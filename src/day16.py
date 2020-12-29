import re

def parse_props(raw):
    return {k: v for [k, v] in re.findall(r'(\w+): (\d+)', raw)}

def main():
    with open('resources/day16-given.txt', 'r') as f:
        given = parse_props(f.read())

    with open('resources/day16.txt', 'r') as f:
        for i, raw_props in re.findall(r'Sue (\d+): (.+)', f.read()):
            props = parse_props(raw_props)
            if all(props[k] == given[k] for k in props.keys() if k in given.keys()):
                print(f'Part 1: {i}')

if __name__ == "__main__":
    main()