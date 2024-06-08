"""
You are a student and you are trying to organize your subjects and grades using Python.
Let’s explore what we’ve learned about lists to organize your subjects and scores.
"""

last_semester_gradebook = [["politics", 80], [
    "latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below:


# Create a list called subjects and fill it with the classes you are taking:
# "physics"
# "calculus"
# "poetry"
# "history"

subjects = ['physics', 'calculus', 'poetry', 'history']


# Create a list called grades and fill it with your scores:
# 98
# 97
# 85
# 88

grades = [98, 97, 85, 88]


# Manually(without any methods) create a two-dimensional list to combine subjects and grades. Use the table below as a reference to associated values.

# Name	Test Score
# "physics"	98
# "calculus"	97
# "poetry"	85
# "history"	88

# Assign the value into a variable called gradebook.

gradebook = [['physics', 98], ['calculus', 97],
             ['poetry', 85], ['history', 88]]
print(gradebook)

# Your grade for your computer science class just came in ! You got a perfect score, 100!
# Use the .append() method to add a list with the values of "computer science" and an associated grade value of 100 to our two-dimensional list of gradebook.
gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])

# Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class .
# Access the index of the grade for your visual arts class and modify it to be 5 points greater.

gradebook[-1][-1] += 5
print(gradebook)

# You decided to switch from a numerical grade value to a Pass/Fail option for your poetry class .
# Find the grade value in your gradebook for your poetry class and use the .remove() method to delete it.
gradebook[2].remove(85)
print(gradebook)
gradebook[2].append('Pass')
print(gradebook)

# You also have your grades from last semester, stored in last_semester_gradebook.
# Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook using + to have one complete grade book.
# Print full_gradebook to see our completed list.
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
