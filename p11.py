data = open("input/p11", "rb").read().decode()

NO_SEAT = 0
EMPTY_SEAT = 1
FULL_SEAT = 2

mapping = {
    '.': NO_SEAT,
    'L': EMPTY_SEAT,
    '#': FULL_SEAT,

    NO_SEAT: ".",
    EMPTY_SEAT: "L",
    FULL_SEAT: "#",
}

matrix = [ [mapping[s] for s in row] for row in data.split('\n') if row and row.strip()]
max_rows = len(matrix)
max_cols = len(matrix[0])

neighbour_deltas = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def full_neighbours(r, c):
    result = 0
    for dr, dc in neighbour_deltas:
        rr = r + dr
        cc = c + dc
        if rr < 0 or cc < 0 or rr >= max_rows or cc >= max_cols:
            continue
        if matrix[rr][cc] == FULL_SEAT:
            result += 1

    return result

def print_matrix():
    for row in matrix:
        for place in row:
            print(mapping[place], end='')
        print()
    print()

while True:
    changes = []

    for ri, row in enumerate(matrix):
        for ci, place in enumerate(row):
            neighbours = full_neighbours(ri, ci)
            if place == EMPTY_SEAT and neighbours == 0:
                changes.append((ri, ci, FULL_SEAT))
            elif place == FULL_SEAT and neighbours >= 4:
                changes.append((ri, ci, EMPTY_SEAT))

    if len(changes) == 0:
        break

    for ri, ci, new_val in changes:
        matrix[ri][ci] = new_val

occupied = 0

for row in matrix:
    for place in row:
        if place == FULL_SEAT:
            occupied += 1

print(f"Part 1: {occupied}")