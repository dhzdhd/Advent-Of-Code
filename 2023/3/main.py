import functools as ft
import itertools as it
from dataclasses import dataclass


@dataclass(frozen=True)
class Gear:
    value: str
    pos: (int, int)


with open("2023/3/input.txt") as f:
    raw: list[str] = list(map(lambda x: x.replace("\n", ""), f.readlines()))
    width = len(raw[0])
    height = len(raw)

    j = 0
    res = 0
    for i in range(height):
        j = 0
        while j < width:
            num = ""
            flag = False

            # Absolutely horrid code, need to refactor
            while raw[i][j].isdigit() and raw[i][j] != ".":
                if i > 0:
                    if not raw[i - 1][j].isdigit() and raw[i - 1][j] != ".":
                        flag = True
                if i < height - 1:
                    if not raw[i + 1][j].isdigit() and raw[i + 1][j] != ".":
                        flag = True
                if j > 0:
                    if not raw[i][j - 1].isdigit() and raw[i][j - 1] != ".":
                        flag = True
                if j < width - 1:
                    if not raw[i][j + 1].isdigit() and raw[i][j + 1] != ".":
                        flag = True
                if i > 0 and j > 0:
                    if not raw[i - 1][j - 1].isdigit() and raw[i - 1][j - 1] != ".":
                        flag = True
                if i > 0 and j < width - 1:
                    if not raw[i - 1][j + 1].isdigit() and raw[i - 1][j + 1] != ".":
                        flag = True
                if i < height - 1 and j > 0:
                    if not raw[i + 1][j - 1].isdigit() and raw[i + 1][j - 1] != ".":
                        flag = True
                if i < height - 1 and j < width - 1:
                    if not raw[i + 1][j + 1].isdigit() and raw[i + 1][j + 1] != ".":
                        flag = True
                num += raw[i][j]

                if j == width - 1:
                    break
                j += 1

            if flag:
                res += int(num)
                flag = False
                num = ""
            j += 1
    # print(res)

    objs: [Gear] = []
    for i in range(height):
        j = 0
        while j < width:
            buffer = ""

            if raw[i][j] == "*":
                buffer += raw[i][j]
            else:
                while raw[i][j].isdigit() and raw[i][j] != ".":
                    buffer += raw[i][j]

                    if j == width - 1:
                        break
                    j += 1

            if buffer != "":
                objs.append(Gear(buffer, (j, i)))
            j += 1

    stars = list(filter(lambda x: x.value == "*", objs))
    gears = list(filter(lambda x: x.value != "*", objs))

    res = 0
    for i in stars:
        couple = []
        pos = i.pos

        for j in gears:
            if j.pos[1] - 1 <= pos[1] <= j.pos[1] + 1:
                start = j.pos[0] - len(j.value)
                end = j.pos[0]

                if start - 1 <= pos[0] <= start + 1 or end - 1 <= pos[0] <= end + 1:
                    couple.append(j)

                # checks for top and bottom just fine but not on same line
                # if (j.pos[0] - len(j.value) - 1) <= pos[0] <= (j.pos[0] + 1):
                #     couple.append(j)
                # elif j.pos[1] == pos[1] and j.pos[0] <= pos[0] <= j.pos[0]:
                #     couple.append(j)
        if len(couple) == 2:
            res += int(couple[0].value) * int(couple[1].value)
            print(couple)

    # for i in objs:
    #     print(i)

    print(res)
