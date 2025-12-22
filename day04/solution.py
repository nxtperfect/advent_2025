def part1():
    res = 0
    grid = []
    with open("input.txt") as f:
        grid = f.readlines()
        grid: list[list[str]] = [[y for y in x.strip()] for x in grid]

        for r, line in enumerate(grid):
            for c, roll in enumerate(line):
                if roll == ".":
                    continue
                neighbours = 0
                for rx in range(-1, 2):  # -1, 0, 1
                    for cx in range(-1, 2):  # -1, 0, 1
                        if (rx, cx) == (0, 0):
                            continue
                        if (r + rx not in range(len(grid))) or (
                            c + cx not in range(len(grid[0]))
                        ):
                            continue
                        if grid[r + rx][c + cx] != "@":
                            continue
                        neighbours += 1
                if neighbours >= 4:
                    continue
                res += 1
    print(res)


def part2():
    res = 0
    grid = []
    with open("input.txt") as f:
        grid = f.readlines()
        grid = [[y for y in x.strip()] for x in grid]

        while True:
            isRemovedThisRun = False
            for r, line in enumerate(grid):
                for c, roll in enumerate(line):
                    if roll == ".":
                        continue
                    neighbours = 0
                    for rx in range(-1, 2):  # -1, 0, 1
                        for cx in range(-1, 2):  # -1, 0, 1
                            if (rx, cx) == (0, 0):
                                continue
                            if (r + rx not in range(len(grid))) or (
                                c + cx not in range(len(grid[0]))
                            ):
                                continue
                            if grid[r + rx][c + cx] != "@":
                                continue
                            neighbours += 1
                    if neighbours >= 4:
                        continue
                    res += 1
                    grid[r][c] = "."
                    isRemovedThisRun = True
            if not isRemovedThisRun:
                break
    print(res)


# part1()
part2()
