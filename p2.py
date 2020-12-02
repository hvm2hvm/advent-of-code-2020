"""
    Challenge URL: https://adventofcode.com/2020/day/2
"""

data = open("input/p2", "rb").read().decode()

entries = [x.strip() for x in data.split('\n') if x and x.strip()]

count = 0

count_2 = 0

for entry in entries:
    # line format: 6-7 z: dqzzzjbzz
    #
    policy, password = entry.split(": ")
    interval, letter = policy.split(" ")
    num_min, num_max = map(int, interval.split('-'))

    count += 1 if num_min <= password.count(letter) <= num_max else 0

    pos_1 = password[num_min-1] == letter
    pos_2 = password[num_max-1] == letter

    count_2 += 1 if pos_1 ^ pos_2 else 0

print(count)

print(count_2)
