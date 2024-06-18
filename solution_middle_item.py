"""
Create a function called middle_element that has one parameter named my_list.
If there are an odd number of elements in my_list, the function should return the middle element.
If there are an even number of elements, the function should return the average of the middle two elements.
"""

# Write your function here


def middle_element(my_list):
    if len(my_list) % 2 != 0:
        middle_item = int((len(my_list)/2))
        return my_list[middle_item]
    else:
        middle_item_a = my_list[int(len(my_list)/2)]
        middle_item_b = my_list[int(len(my_list)/2) - 1]
        return int((middle_item_a + middle_item_b)/2)


# Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
