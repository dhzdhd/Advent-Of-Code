from itertools import pairwise
from functools import reduce


def isAP(l: list[int]) -> bool:
    init = l[1] - l[0]
    return bool(
        reduce(
            lambda state, x: init == (x[1] - x[0]) if state else state,
            pairwise(l),
            True,
        )
    )


with open("2023/9/input.txt") as f:
    raw = f.readlines()

    l = list(map(lambda x: list(map(int, x.split())), raw))

    res = 0

    for i in l:
        temp_sum = 0
        buf = i

        while True:
            buf = list(map(lambda x: x[1] - x[0], pairwise(buf)))
            if isAP(buf):
                temp_sum += buf[-1] + (buf[1] - buf[0])
                res += i[-1] + temp_sum
                break
            temp_sum += buf[-1]

            print(list(buf))
    print(res)

    res = 0

    for i in l:
        temp_sum = 0
        buf = i[::-1]

        while True:
            buf = list(map(lambda x: x[1] - x[0], pairwise(buf)))
            if isAP(buf):
                temp_sum += buf[-1] + (buf[1] - buf[0])
                res += i[0] + temp_sum
                break
            temp_sum += buf[-1]

            print(list(buf))
    print(res)
