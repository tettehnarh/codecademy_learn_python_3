"""
Create a function named in_range() that has three parameters named num, lower, and upper.
The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.
"""

# Write your in_range function here:


def in_range(num, lower, upper):
    if num >= lower:
        return True
    elif num <= upper:
        return False


# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False
