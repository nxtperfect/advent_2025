import numpy as np


def part1():
    # ranges
    # if empty line = no more ranges
    # check if number in range
    # count how many
    res = 0
    ranges = np.array([[]])
    temp = []
    with open("test_input.txt") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() == "":
                continue
            if "-" not in line:
                ranges = np.asarray(temp)
                num = int(line.strip())
                print("Lookup")
                starts = np.asarray([x[0] for x in ranges])
                stops = np.asarray([x[1] for x in ranges])
                print(list(zip(starts, stops)))
                print(np.any(((2 >= a) and (2 <= b)) for a, b in zip(starts, stops)))
                if np.any(
                    (num == a and num == (b + 1))
                    for a, b in [(x[0], x[1]) for x in ranges]
                ):
                    # if np.where(ranges == num):
                    # print(np.where(ranges == num))
                    res += 1
                    print(f"Found {num} in {ranges}")
                continue
            low, high = line.split("-")
            low, high = int(low), int(high)
            print("Adding ranges")
            temp.append((low, high))
    print(res)
    assert res == 3


def part2():
    res = 0
    with open("test_input.txt") as f:
        pass
    assert res == 0
    print(res)


part1()
# part2()
