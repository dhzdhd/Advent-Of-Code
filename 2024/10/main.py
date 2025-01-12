import re
from functools import reduce

# Part 1
with open("2024/10/input.txt") as f:
    matrix = []

    for line in f.readlines():
        buf = []
        for num in list(line.strip()):
            buf.append(int(num))
        matrix.append(buf)

    acc = 0

    def do_something(root):
        global acc
        if matrix[root[0]][root[1]] == 9:
            acc += 1

    def get_neighbors(root):
        neighbors = []

        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        for direction in directions:
            i = root[0] + direction[0]
            j = root[1] + direction[1]

            if i < 0 or i >= len(matrix[0]) or j < 0 or j >= len(matrix):
                continue
            if matrix[i][j] - matrix[root[0]][root[1]] != 1:
                continue
            neighbors.append((i, j))

        return neighbors

    def dfs(root, visited):
        if root in visited:
            return

        do_something(root)

        visited.add(root)

        for neighbor in get_neighbors(root):
            dfs(neighbor, visited)

    roots = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                roots.append((i, j))

    for root in roots:
        visited = set()
        dfs(root, visited)
    print(acc)
