from itertools import product
from functools import reduce

with open("2020/1/input.txt") as f:
    raw = list(map(int, f.readlines()))

    cartprod = product(raw, repeat=2)

    ans = reduce(
        lambda st, t: st + t[0] * t[1]
        if t[0] + t[1] == 2020 and t[0] != t[1]
        else st + 0,
        cartprod,
        0,
    )

    print(ans)
