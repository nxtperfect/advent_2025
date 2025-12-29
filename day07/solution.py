def part1():
    def find(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    # when hitting . continue
    # if '^' go to left and right continue
    # count number of splits
    res = 0
    with open("input.txt") as f:
        # if 'S' in line, save it's column index
        # add to 'beams' list
        # next line find '^'
        # if on the index in beams, remove that index
        # and add -1 and +1 of that index to list
        # add +1 to res
        lines = f.readlines()
        beams = set()
        for line in lines:
            line = line.strip()
            startPos = line.find("S")
            # print("But here")
            if startPos != -1:
                beams.add(startPos)
                continue
            # print("Here")
            if find(line, "^"):
                poses = find(line, "^")
                # print(f"Found '^' at {poses}")
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
    # assert res == 21


def part2():
    res = 0
    with open("input.txt") as f:
        pass
    print(res)
    # assert res == 3263827


part1()
# part2()
