def p1():
    res = 0
    ranges = []
    with open("input.txt") as f:
        ranges = [list(map(int, item.split("-"))) for item in f.readline().split(",")]
    numbers = sum((list(range(a, b + 1)) for a, b in ranges), [])

    for num in numbers:
        s = str(num)
        if len(s) % 2:
            continue
        half = len(s) // 2
        if s[:half] == s[half:]:
            res += num
    print(res)


def p2():
    res = 0
    ranges = []
    with open("input.txt") as f:
        ranges = [list(map(int, item.split("-"))) for item in f.readline().split(",")]
    numbers = sum((list(range(a, b + 1)) for a, b in ranges), [])

    for num in numbers:
        s = str(num)
        for n in range(2, len(s) + 1):
            if len(s) % n:
                continue
            split = len(s) // n
            if s[:split] * n == s:
                res += num
                break
    # assert res == 4174379265
    print(res)


# p1()
p2()
