def is_monotonic(nums):
    return all(x < y for x, y in zip(nums, nums[1:])) or all(x > y for x, y in zip(nums, nums[1:]))

def max_gap(nums):
    return max(abs(x - y) for x, y in zip(nums, nums[1:]))

def passes_with_one_removal(nums):
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i+1:]
        if is_monotonic(new_nums) and max_gap(new_nums) <= 3:
            return True
    return False

count = 0
with open('input_data/day_2.txt') as file:
    for line in file:
        nums = list(map(int, line.strip().split()))
        if (is_monotonic(nums) and max_gap(nums) <= 3) or passes_with_one_removal(nums):
            count += 1

print(count)