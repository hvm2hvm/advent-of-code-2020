"""
    Challenge URL: https://adventofcode.com/2020/day/7

"""


data = open("input/p7", "rb").read().decode()

lines = [x.strip() for x in data.split("\n") if x and x.strip()]

contained_in = {}

contains = {}

for line in lines:
    outer_color, inner_bags = line.rstrip(".").split(" bags contain ")
    inner_bags = [x.split(" bag")[0].split(" ", 1)
             for x in inner_bags.split(", ")]

    contains.setdefault(outer_color, {})

    for count, inner_color in inner_bags:
        contained_in.setdefault(inner_color, set())
        contained_in[inner_color].add(outer_color)

        if count != "no":
            contains[outer_color][inner_color] = int(count)

all_containers = set()

to_check = {'shiny gold'}

while len(to_check) > 0:
    next_check = set()
    for bag in to_check:
        if bag in contained_in:
            all_containers.update(contained_in[bag])
            next_check.update(contained_in[bag])
    to_check = next_check

print(f"the shiny gold bag can be found in {len(all_containers)} other bags\n")

to_check = contains['shiny gold'].items()

count_all = 0

while len(to_check) > 0:
    new_check = []
    for bag, bag_count in to_check:
        count_all += bag_count
        print(f"checking {bag_count:5} {bag:15} bags {count_all:9} (total)")
        for inner, inner_count in contains[bag].items():
            # count_all += bag_count * inner_count
            new_check.append((inner, inner_count * bag_count))
            print(f"  contains {inner_count:2}x{bag_count:5}={inner_count*bag_count:5} {inner:15} bags")

    to_check = new_check

print(f"\nbags inside the shiny gold bag: {count_all}")
