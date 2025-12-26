import numpy as np


def part1():
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
    ranges, numbers = [], []
    with open("input.txt") as f:
        ranges, numbers = f.read().split("\n\n")
        ranges = [list(map(int, r.split("-"))) for r in ranges.splitlines()]
        numbers = list(map(int, numbers.splitlines()))
        ranges.sort()

        last = None

        for low, high in ranges:
            if last is None:
                last = (low, high)
                continue
            if last[1] < low:
                res += last[1] - last[0] + 1
                last = (low, high)
                continue
            last = (last[0], max(last[1], high))
        res += last[1] - last[0] + 1
    print(res)
    assert res == 14


# part1()
part2()
