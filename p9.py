data = open("input/p9", "rb").read().decode()

import time

start = time.time()

nums = [int(x.strip()) for x in data.split('\n') if x and x.strip()]

def find_sum(target, interval):
    for i in range(len(interval)-1):
        for j in range(i+1, len(interval)):
            if interval[i] + interval[j] == target:
                return True
    return False

def find_sum_multiple(target, interval):
    for count in range(2, len(interval)):
        for i in range(len(interval) - count + 1):
            if sum(interval[i:i+count]) == target:
                return (True, i, count)
    return (False, None, None)

for i in range(25, len(nums)):
    if not find_sum(nums[i], nums[i-25:i]):
        invalid_num = nums[i]
        print(f"part 1: found the number {nums[i]} at position {i}")
        found, pos, length = find_sum_multiple(invalid_num, nums[:i])
        if found:
            print(f"part 2: found the interval at {pos} of length {length}: {' + '.join(map(str,nums[pos:pos+length]))} = {invalid_num}")
            in_order = sorted(nums[pos:pos+length])
            print(f"part 2: {in_order[0]} (min) + {in_order[-1]} (max) = {in_order[0] + in_order[-1]}")
        break

end = time.time()

print(f"total duration: {end-start:6.5f}")