import numpy as np


def part1():
    # ranges
    # if empty line = no more ranges
    # check if number in range
    # count how many
    res = 0
    ranges, numbers = [], []
    with open("input.txt") as f:
        ranges, numbers = f.read().split("\n\n")
        ranges = [list(map(int, r.split("-"))) for r in ranges.splitlines()]
        numbers = list(map(int, numbers.splitlines()))

        for n in numbers:
            for low, high in ranges:
                if low > n:
                    continue
                if high < n:
                    continue
                res += 1
                break
    print(res)
    # assert res == 3


def part2():
    res = 0
    with open("test_input.txt") as f:
        pass
    assert res == 0
    print(res)


part1()
# part2()
