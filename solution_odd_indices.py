"""
Create a function named odd_indices() that has one parameter named my_list.
The function should create a new empty list and add every element from my_list that has an odd index.
The function should then return this new list.
For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].
"""
# Write your function here


def odd_indices(my_list):
    new_list = []
    index_count = 0
    for num in my_list:
        if index_count % 2 != 0:
            new_list.append(num)
        index_count += 1
    return new_list


# Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
