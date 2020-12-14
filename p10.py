"""
    Challenge URL: https://adventofcode.com/2020/day/10

    Part 1: sort, get differences between entries, count the 1's and 3's and multiply the counts

    Part 2: each section of 1s can have multiple setups (up to 2 1s can be taken away)

"""

data = open("input/p10", "rb").read().decode()

jolts = map(int, [x.strip() for x in data.split('\n') if x and x.strip()])

jolts = sorted(jolts)
jolts.insert(0, 0) # add the extra one from the charging port (0)
jolts.append(jolts[-1] + 3) # add the extra one from the builtin device
diffs = [jolts[i] - jolts[i-1] for i in range(1, len(jolts))]
count_1 = diffs.count(1)
count_3 = diffs.count(3)
print(f"""Part 1
Count of 1s: {count_1}
Count of 3s: {count_3}
Product: {count_1 * count_3}\n""")

print("Part 2")
range_sizes = []
csize = 0
for d in diffs:
    if d == 1:
        csize += 1
    elif d == 3 and csize > 0:
        range_sizes.append(csize)
        csize = 0
if csize > 0:
    range_sizes.append(csize)
print(f"ranges = {range_sizes}")
setups = [n*(n-1) // 2 + 1 if n > 1 else 1 for n in range_sizes]
print(f"setups = {setups}")
total = 1
for num in setups:
    total *= num

print(f"Different setups: {total}")
