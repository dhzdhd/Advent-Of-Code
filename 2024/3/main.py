import re
from functools import reduce

# Part 1
with open("2024/3/input.txt") as f:
    raw = f.read()

    regex = re.compile(r"mul\((\d{1,3})\,(\d{1,3})\)")
    matches = regex.findall(raw)

    acc = reduce(
        lambda acc, t: acc + t[0] * t[1],
        map(lambda t: (int(t[0]), int(t[1])), matches),
        0,
    )
    print(acc)

# Part 2
with open("2024/3/input.txt") as f:
    raw = f.read()
    parts = raw.split("do()")

    raw = ""
    for part in parts:
        subparts = part.split("don't()")
        raw += subparts[0]

    regex = re.compile(r"mul\((\d{1,3})\,(\d{1,3})\)")
    matches = regex.findall(raw)

    acc = reduce(
        lambda acc, t: acc + t[0] * t[1],
        map(lambda t: (int(t[0]), int(t[1])), matches),
        0,
    )
    print(acc)
