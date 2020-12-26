import re

def shortest_from(start, d, locs):
    if len(locs) == 0:
        return 0
    else:
        total = 10000000000
        for loc in set(locs):
            if (start, loc) in d:
                locs.remove(loc)
                total = min(total, d[(start, loc)] + shortest_from(loc, d, locs))
                locs.add(loc)
        return total

def shortest(d, locs):
    return min(shortest_from(loc, d, locs.difference({loc})) for loc in locs)

with open('resources/day09.txt', 'r') as f:
    d = dict()
    locs = set()

    for src, dest, dist in re.findall(r'(\w+)\s+to\s+(\w+)\s+=\s+(\d+)', f.read()):
        d[(src, dest)] = int(dist)
        d[(dest, src)] = int(dist)
        locs.add(src)
        locs.add(dest)
    
    part1 = shortest(d, locs)
    print(f'Part 1: {part1}')
