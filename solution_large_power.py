"""
Create a function named large_power() that takes two parameters named base and exponent.
If base raised to the exponent is greater than 5000, return True, otherwise return False
"""

# Write your large_power function here:


def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False


# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False
