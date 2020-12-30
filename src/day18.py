def is_corner(x, y, width, height):
    return (x, y) in [(0, 0), (0, height - 1), (width - 1, 0), (width - 1, height - 1)]

def step(grid, part2=False):
    new = [[cell for cell in row] for row in grid]
    height = len(grid)
    width = len(grid[0])
    for y in range(height):
        for x in range(width):
            nbs = [
                grid[y + dy][x + dx] == '#' or (part2 and is_corner(x + dx, y + dy, width, height))
                for dy in range(-1, 2)
                for dx in range(-1, 2)
                if (dy != 0 or dx != 0) and y + dy >= 0
                                        and y + dy < len(grid)
                                        and x + dx >= 0
                                        and x + dx < len(grid[y + dy])
            ]
            ons = len([nb for nb in nbs if nb])
            on = grid[y][x] == '#'
            new_on = (on and ons in [2, 3]) or (not on and ons == 3) or (part2 and is_corner(x, y, width, height))
            new[y][x] = '#' if new_on else '.'
    return new

def simulate(grid, n=100, part2=False):
    new = grid
    for i in range(n):
        new = step(new, part2)
    return new

def total_ons(grid):
    return len([cell for row in grid for cell in row if cell == '#'])

def main():
    with open('resources/day18.txt', 'r') as f:
        grid = [l.strip() for l in f.readlines() if l.strip()]
        print(f"Part 1: {total_ons(simulate(grid, part2=False))}")
        print(f"Part 2: {total_ons(simulate(grid, part2=True))}")

if __name__ == "__main__":
    main()
