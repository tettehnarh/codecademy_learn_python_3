"""
Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
The function should sum the elements of the list until the sum is greater than 9000.
When this happens, the function should return the sum.
If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements.
If the list is empty, the function should return 0.
For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.
"""
# Write your function here


def over_nine_thousand(lst):
    lst_sum = 0

    if len(lst) == 0:
        return 0
    elif sum(lst) < 9000:
        return sum(lst)
    elif lst_sum < 9000:
        for item in lst:
            lst_sum += item
            if lst_sum > 9000:
                return lst_sum
    else:
        return lst_sum


# Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))


# solution 2
# def over_nine_thousand(lst):
#   sum = 0
#   for number in lst:
#     sum += number
#     if (sum > 9000):
#       break
#   return sum
