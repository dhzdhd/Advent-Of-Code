from functools import reduce
import heapq as hq


# Part 1
with open("2024/1/input.txt") as f:
    ctr = 0
    arr1 = []
    arr2 = []

    for raw in f.readlines():
        a, b = raw.split("   ")

        hq.heappush(arr1, int(a))
        hq.heappush(arr2, int(b))

        ctr += 1

    acc = 0
    for i in range(ctr):
        a = hq.heappop(arr1)
        b = hq.heappop(arr2)

        acc += abs(a - b)

    print(acc)

# Part 2
with open("2024/1/input.txt") as f:
    d = {}
    acc = 0

    for raw in f.readlines():
        a, b = raw.split("   ")

        arr1.append(int(a))
        arr2.append(int(b))

    for num in arr1:
        if num not in d:
            d[num] = arr2.count(num)

        acc += d[num] * num

    print(acc)
