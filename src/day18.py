def step(grid):
    new = [[cell for cell in row] for row in grid]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            nbs = [grid[y + dy][x + dx] for dy in range(-1, 2) for dx in range(-1, 2) if (dy != 0 or dx != 0) and y + dy >= 0 and y + dy < len(grid) and x + dx >= 0 and x + dx < len(grid[y + dy])]
            ons = len([nb for nb in nbs if nb == '#'])
            if grid[y][x] == '#':
                new[y][x] = '#' if ons in [2, 3] else '.'
            else:
                new[y][x] = '#' if ons == 3 else '.'
    return new

def main():
    with open('resources/day18.txt', 'r') as f:
        grid = [l.strip() for l in f.readlines() if l.strip()]
        for i in range(100):
            grid = step(grid)
        print(f"Part 1: {len([cell for row in grid for cell in row if cell == '#'])}")

if __name__ == "__main__":
    main()
