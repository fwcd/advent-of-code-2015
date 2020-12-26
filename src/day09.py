import re

def best_from(start, f, d, locs):
    if len(locs) == 0:
        return 0
    else:
        total = None
        for loc in set(locs):
            if (start, loc) in d:
                locs.remove(loc)
                dist = d[(start, loc)] + best_from(loc, f, d, locs)
                if total == None:
                    total = dist
                else:
                    total = f(total, dist)
                locs.add(loc)
        return total

def best(f, d, locs):
    return f(best_from(loc, f, d, locs.difference({loc})) for loc in locs)

with open('resources/day09.txt', 'r') as f:
    d = dict()
    locs = set()

    for src, dest, dist in re.findall(r'(\w+)\s+to\s+(\w+)\s+=\s+(\d+)', f.read()):
        d[(src, dest)] = int(dist)
        d[(dest, src)] = int(dist)
        locs.add(src)
        locs.add(dest)
    
    print(f'Part 1: {best(min, d, locs)}')
    print(f'Part 2: {best(max, d, locs)}')
