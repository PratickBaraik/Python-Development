def filter_and_square(nums):
    squared_even = [x ** 2 for x in nums if x % 2 ==0]
    return sorted(squared_even)

nums = [5, 2, 8, 3, 1, 4]
print(filter_and_square(nums))