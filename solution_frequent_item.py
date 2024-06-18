"""
Create a function named more_frequent_item that has three parameters named my_list, item1, and item2.
Return either item1 or item2 depending on which item appears more often in my_list.
If the two items appear the same number of times, return item1.
"""
# Write your function here


def more_frequent_item(my_list, item1, item2):
    if my_list.count(item1) >= my_list.count(item2):
        return item1
    else:
        return item2


# Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
