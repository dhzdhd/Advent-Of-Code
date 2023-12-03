import functools as ft
import itertools as it

with open("2023/3/input.txt") as f:
    raw: list[str] = list(map(lambda x: x.replace("\n", ""), f.readlines()))
    width = len(raw[0])
    height = len(raw)

    # full = ""
    # for i in raw:
    #     full += i
    # print(set(full))

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
                print(num)
                res += int(num)
                flag = False
                num = ""
            j += 1
    print(res)
