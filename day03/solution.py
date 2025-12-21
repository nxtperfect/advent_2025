def part1():
    res = 0
    with open("input.txt", "r") as file:
        for line in file.readlines():
            bank = list(map(int, line.strip()))
            tens = max(bank[:-1])
            ones = max(bank[bank.index(tens) + 1 :])
            res += tens * 10 + ones
    print(res)


def part2():
    res = 0
    with open("input.txt", "r") as file:
        for line in file.readlines():
            bank = list(map(int, line.strip()))
            jolts = 0
            for index in range(11):
                digit = max(bank[: index - 11])
                bank = bank[bank.index(digit) + 1 :]
                jolts = (jolts * 10) + digit
            jolts = (jolts * 10) + max(bank)
            res += jolts
    print(res)


# part1()
part2()
