def remove_occurrence(nums, val):
    result = []
    for x in nums:
        if x != val:
            result.append(x)
    return result

nums = [3, 2, 2, 3, 4, 2]
val = 3
print(remove_occurrence(nums, val))