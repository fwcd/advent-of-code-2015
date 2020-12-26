import re

def find_solution_from(first, current, d, people):
    if len(people) == 0:
        return d[(first, current)] + d[(current, first)]
    else:
        lowest = 0
        for p in people:
            people.remove(p)
            lowest = max(lowest, d[(current, p)] + d[(p, current)] + find_solution_from(first, p, d, people))
            people.add(p)
        return lowest

def find_solution(d, people):
    return max(find_solution_from(c, c, d, people.difference({c})) for c in people)

def main():
    d = dict()
    people = set()
    with open('resources/day13.txt', 'r') as f:
        for left, raw_sign, raw_delta, right in re.findall(r'(\w+)\s+would\s+(\w+)\s+(\d+)\s+happiness units by sitting next to\s+(\w+)\.', f.read()):
            sign = 1 if raw_sign == 'gain' else -1
            delta = sign * int(raw_delta)
            d[(left, right)] = delta
            people.add(left)
            people.add(right)
    print(f'Part 1: {find_solution(d, people)}')

if __name__ == "__main__":
    main()
