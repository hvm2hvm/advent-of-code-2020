"""
    Challenge URL: https://adventofcode.com/2020/day/5/answer

    The ids are basically 10 digit binary numbers in little endian format

    For part 1, I convert all ids to integer numbers and keep track of the largest id

    For part 2, I map all ids into a 1024 long list
    Each entry is True/False depending on whether that id was found (seat taken)
    Once the list is built, I go through it to find the right id (the one that is missing but has existing ids in front and behind)

    At the end I print out a layout of the entire plane, showing the empty seats at the front and back and the missing seat (the one we're looking for)
"""

data = open("input/p5", "rb").read().decode()

ids = [x.strip() for x in data.split("\n") if x and x.strip()]

conv_table = {
    'F': 0,
    'B': 1,
    'L': 0,
    'R': 1,
}

max_id = 0

id_exists = [False] * 1024

for id in ids:
    num_id = sum((conv_table[d] * 2**(len(id) - p - 1)
                  for p, d in enumerate(id)))

    if num_id > max_id:
        max_id = num_id

    id_exists[num_id] = True

found_id = None

for i in range(1, len(id_exists) - 1):
    if id_exists[i-1] and not id_exists[i] and id_exists[i+1]:
        found_id = i
        break

print(f"Max id: {max_id}")

print(f"Found id: {'none' if found_id is None else found_id}")

print("\nPlane layout:")
for row_index in range(128):
    row = id_exists[row_index * 8:(row_index + 1) * 8]
    row = map(lambda seat: "#" if seat else "_", row)
    print(''.join(row))
