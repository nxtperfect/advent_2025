def p1():
    num = 50
    res = 0
    with open("input.txt") as f:
        for line in f:
            prefix, suffix = line[0], line[1:]
            if prefix == "L":
                num -= int(suffix)
            else:
                num += int(suffix)
            while num > 99:
                num -= 100
                print(num)
            while num < 0:
                num += 100
                print(num)
            if num == 0:
                res += 1
    print(res)


def p2():
    # get nearest distance in the prefix dir to zero
    # then get the modulo of that distance
    # by the amount we move
    # and add that to res
    num = 50
    res = 0
    dials = [
        int(line.strip().replace("L", "-").replace("R", ""))
        for line in open("input.txt")
    ]
    for turn in dials:
        if turn < 0:
            div, mod = divmod(turn, -100)
            res += div
            if num != 0 and num + mod <= 0:
                res += 1
        else:
            div, mod = divmod(turn, 100)
            res += div
            if num + mod >= 100:
                res += 1
        num = (num + turn) % 100
    print(f"{res}")


p2()
