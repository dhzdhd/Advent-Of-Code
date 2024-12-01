import itertools as it
import functools as ft
import math
from functools import reduce
from itertools import (
    combinations,
    combinations_with_replacement,
    permutations,
    product,
    pairwise,
    repeat,
)
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Model:
    data: str
    group: int | None
    arrangements: int


def in_range(springs, i):
    return 0 < i < len(springs)


with open("2023/12/input.txt") as f:
    raw = f.readlines()

    for i in raw[-1:]:
        partition = i.split(" ")
        groups = list(map(int, partition[1].removesuffix("\n").split(",")))
        springs = partition[0]
        # springs = list(filter(lambda x: x != "", re.split("\.+", partition[0])))
        print(springs, groups)

        buf = []
        counter = 0
        i = 0
        while i < len(springs):
            if springs[i] == "#":
                num = groups[counter]
                counter += 1
                buf.append(Model(data=springs[i : i + num], group=num, arrangements=1))

                i += num
            elif in_range(springs, i) and springs[i] == "." and springs[i - 1] != ".":
                i += 1
            elif springs[i] == "?":
                ...
            i += 1
        print(buf)
