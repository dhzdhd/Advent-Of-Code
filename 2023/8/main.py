from math import lcm


def parse(input):
    raw_pair = input.split("= ")[1]
    tup = tuple(raw_pair[1:-2].split(", "))

    return input.split(" ")[0], tup


with open("2023/8/input.txt") as f:
    raw = f.readlines()

    instructions = list(raw[0].removesuffix("\n"))
    rules = {i: j for i, j in map(parse, raw[2:])}

    current = "AAA"
    steps = 0
    while current != "ZZZ":
        for inst in instructions:
            match inst:
                case "L":
                    current = rules[current][0]
                case "R":
                    current = rules[current][1]
            steps += 1
            if current == "ZZZ":
                break

    print(steps)

    current = list(filter(lambda i: i[-1] == "A", rules.keys()))
    steps = [0 for _ in range(len(current))]
    print(list(current))

    for i in range(len(current)):
        while current[i][-1] != "Z":
            for inst in instructions:
                match inst:
                    case "L":
                        current[i] = rules[current[i]][0]
                    case "R":
                        current[i] = rules[current[i]][1]
                steps[i] += 1
                if current[i][-1] == "Z":
                    break

    print(lcm(*steps))
