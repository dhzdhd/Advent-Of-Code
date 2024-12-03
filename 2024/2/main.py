from itertools import pairwise

# Part 1
with open("2024/2/input.txt") as f:
    reports = f.readlines()
    count = 0

    for report in reports:
        report = list(map(int, report.split(" ")))
        flag = True
        pairs = pairwise(report)
        if report[0] < report[1]:
            for i, j in pairs:
                if i >= j or j - i > 3:
                    flag = False
                    continue
        elif report[0] == report[1]:
            continue
        else:
            for i, j in pairs:
                if i <= j or i - j > 3:
                    flag = False
                    continue

        if flag:
            count += 1

    print(count)

# Part 2
# TODO:
with open("2024/2/input.txt") as f:
    reports = f.readlines()
    count = 0

    for report in reports:
        report = list(map(int, report.split(" ")))
        flag = 0
        pairs = pairwise(report)

        if report[0] > report[1]:
            report = report[::-1]

        i = 0
        j = 1
        while j < len(report):
            if report[i] >= report[j] or report[j] - report[i] > 3:
                if flag == 0:
                    j += 1
                    flag += 1
                else:
                    flag += 1
                    break
            else:
                if flag == 1:
                    j += 1
                    i += 2
                else:
                    j += 1
                    i += 1

        if flag <= 1:
            count += 1

    print(count)
