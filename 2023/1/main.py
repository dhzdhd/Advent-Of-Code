import functools as ft


with open("2023/1/input.txt") as f:
    raw = f.readlines()

    # Part 1
    digits = map(lambda x: "".join(i for i in x if i.isdigit()), raw)
    res = ft.reduce(lambda st, x: st + int(x[0] + x[-1]), digits, 0)

    ## One liner
    res = __import__("functools").reduce(
        lambda st, x: st + int(x[0] + x[-1]),
        map(
            lambda x: "".join(i for i in x if i.isdigit()),
            open("2023/1/input.txt").readlines(),
        ),
        0,
    )

    # Part 2
    num_d = list(
        enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
            start=1,
        )
    )

    raw = map(
        lambda s: ft.reduce(
            lambda st, num: st.replace(num[1], f"{num[1][0]}{str(num[0])}{num[1][-1]}")
            if num[1] in st
            else st,
            num_d,
            s,
        ),
        raw,
    )
    digits = map(lambda x: "".join(i for i in x if i.isdigit()), raw)
    res = ft.reduce(lambda st, x: st + int(x[0] + x[-1]), digits, 0)
    print(res)
