import math


def part1():
    res = 0
    with open("input.txt") as f:
        lines = f.read().strip().split("\n")
        numbers = []
        symbols = []
        # print(lines)
        for l in lines:
            if "*" not in l and "+" not in l:
                temp = list(map(int, l.strip().split()))
                numbers.append(temp)
                continue
            symbols = l.strip().split()
        sortedNums = []
        for i in range(len(numbers[0])):
            temp = []
            for j in range(len(numbers)):
                temp.append(numbers[j][i])
            sortedNums.append(temp)
        # print(numbers)
        # print(sortedNums)
        # print(symbols)
        for i in range(len(symbols)):
            if symbols[i] == "*":
                res += math.prod(sortedNums[i])
                continue
            res += sum(sortedNums[i])
    print(res)
    # assert res == 4277556


def part2():
    pass


part1()
# part2()
