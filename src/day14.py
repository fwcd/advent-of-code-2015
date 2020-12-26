import re

def reindeer(speed, fly_time, rest_time, s):
    resting = False
    kms = 0
    j = 0
    for i in range(s):
        kms += 0 if resting else speed
        if (resting and j >= rest_time - 1) or (not resting and j >= fly_time - 1):
            resting = not resting
            j = 0
        else:
            j += 1
    return kms

def main():
    with open('resources/day14.txt', 'r') as f:
        kms = 0
        for name, speed, fly_time, rest_time in re.findall(r'(\w+)\s+can fly\s+(\d+)\s+km/s for\s+(\d+)\s+seconds, but then must rest for\s+(\d+)\s+seconds\.', f.read()):
            kms = max(kms, reindeer(int(speed), int(fly_time), int(rest_time), 2503))
        print(f'Part 1: {kms}')

if __name__ == "__main__":
    main()
