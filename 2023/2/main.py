import functools as ft


limit = (12, 13, 14)  # RGB

with open("2023/2/input.txt") as f:
    raw = f.readlines()
    res = 0

    for s in raw:
        abc = s.split(": ")
        id_ = int(abc[0].split()[-1])

        red = 0
        green = 0
        blue = 0
        flag = True
        for cubes in abc[1].split("; "):
            for cube in cubes.split(", "):
                match cube.split()[1]:
                    case "red":
                        red += int(cube.split()[0])
                    case "green":
                        green += int(cube.split()[0])
                    case "blue":
                        blue += int(cube.split()[0])

            if any([red > 12, green > 13, blue > 14]):
                flag = False
            else:
                red = 0
                green = 0
                blue = 0

        if flag:
            res += id_

    print(res)

    res = []
    for s in raw:
        abc = s.split(": ")
        id_ = int(abc[0].split()[-1])

        red = []
        green = []
        blue = []
        flag = True
        for cubes in abc[1].split("; "):
            for cube in cubes.split(", "):
                match cube.split()[1]:
                    case "red":
                        red.append(int(cube.split()[0]))
                    case "green":
                        green.append(int(cube.split()[0]))
                    case "blue":
                        blue.append(int(cube.split()[0]))

        res.append(max(red) * max(green) * max(blue))

    print(sum(res))
