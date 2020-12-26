from itertools import islice
import re

def reindeer(speed, fly_time, rest_time):
    resting = False
    kms = 0
    j = 0
    while True:
        kms += 0 if resting else speed
        if (resting and j >= rest_time - 1) or (not resting and j >= fly_time - 1):
            resting = not resting
            j = 0
        else:
            j += 1
        yield kms

def main():
    with open('resources/day14.txt', 'r') as f:
        reindeers = [(n, int(s), int(f), int(r)) for n, s, f, r in re.findall(r'(\w+)\s+can fly\s+(\d+)\s+km/s for\s+(\d+)\s+seconds, but then must rest for\s+(\d+)\s+seconds\.', f.read())]
        print(reindeers)

        part1 = max(next(islice(reindeer(s, f, r), 2503, None)) for _, s, f, r in reindeers)
        print(f'Part 1: {part1}')

        scores = dict()
        part2_rds = [reindeer(s, f, r) for _, s, f, r in reindeers]
        for j in range(2503):
            max_kms = 0
            max_is = set()
            for (i, rd) in enumerate(part2_rds):
                kms = next(rd)
                if kms > max_kms:
                    max_kms = kms
                    max_is = {i}
                elif kms == max_kms:
                    max_is.add(i)
            for i in max_is:
                scores[i] = scores.get(i, 0) + 1
        print(f'Part 2: {max(scores.values())}')

if __name__ == "__main__":
    main()
