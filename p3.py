data = open("input/p3", "rb").read().decode()

pattern = [x.strip() for x in data.split("\n") if x and x.strip()]

def trees_by_slope(dx, dy):
    trees = 0
    x_pos = 0
    y_pos = 0

    while y_pos < len(pattern):
        line = pattern[y_pos]
        trees += 1 if line[x_pos % len(line)] == '#' else 0

        x_pos += dx
        y_pos += dy

    return trees

slopes = [
    trees_by_slope(1, 1),
    trees_by_slope(3, 1),
    trees_by_slope(5, 1),
    trees_by_slope(7, 1),
    trees_by_slope(1, 2),
]

def product(l):
    r = 1
    for e in l:
        r *= e
    return r

print(f"Results: { ', '.join(map(str, slopes)) }; multiplied: {product(slopes)}")
