def part1():
    def find(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    res = 0
    with open("input.txt") as f:
        lines = f.readlines()
        beams = set()
        for line in lines:
            line = line.strip()
            startPos = line.find("S")
            # print("But here")
            if startPos != -1:
                beams.add(startPos)
                continue
            if find(line, "^"):
                poses = find(line, "^")
                for p in poses:
                    if p not in beams:
                        continue
                    if p - 1 >= 0:
                        beams.add(p - 1)
                    if p + 1 < len(line):
                        beams.add(p + 1)
                    res += 1
                    beams.remove(p)
    print(res)


from functools import cache


def part2():
    res = 0
    with open("input.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

        S = [
            (r, c)
            for r, row in enumerate(grid)
            for c, char in enumerate(row)
            if char == "S"
        ][0]

        @cache
        def solve(r, c):
            if r >= len(grid):
                return 1

            if grid[r][c] == "." or grid[r][c] == "S":
                return solve(r + 1, c)
            return solve(r, c - 1) + solve(r, c + 1)

        res = solve(*S)
    print(res)
    # assert res == 40


# part1()
part2()
