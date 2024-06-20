"""
Create a function named max_num() that takes a list of numbers named nums as a parameter.
The function should return the largest number in nums
"""
# Write your function here


def max_num(nums):
    max_number = nums[0]
    for num in nums:
        if num > max_number:
            max_number = num
    return max_number


# Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
