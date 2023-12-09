# dest start, source start, range length

from dataclasses import dataclass


@dataclass(frozen=True)
class Mapping:
    start: range
    dest: int


with open("2023/5/input.txt") as f:
    raw = f.read().split("\n\n")

    seeds, maps = raw[0].split("seeds: ")[1].split(" "), raw[1:]
    mappings: [[Mapping]] = []

    for mapping in maps[:-1]:
        ranges = mapping.split("\n")[1:]

        buffer = []
        for r in ranges:
            dest, src, length = map(int, r.split(" "))

            buffer.append(Mapping(start=range(src, src + length), dest=dest))
        mappings.append(buffer)

    res = []
    for seed in list(map(int, seeds)):
        temp = seed
        for category in mappings:
            mapping = list(filter(lambda x: temp in x.start, category))
            if len(mapping) == 0:
                continue

            mapping = mapping[0]
            temp = mapping.dest + mapping.start.index(temp)
        res.append(temp)

    print(min(res))
