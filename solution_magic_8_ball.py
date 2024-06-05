"""
The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.

Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

Magic 8-Ball, should I do this project?

We’ll be using the following 9 possible answers for our Magic 8-Ball:

Yes - definitely
It is decidedly so
Without a doubt
Reply hazy, try again
Ask again later
Better not tell you now
My sources say no
Outlook not so good
Very doubtful
The output of the program will have the following format:

[Name] asks: [Question]
Magic 8-Ball’s answer: [Answer]

For example:

Joe asks: Is this real life?
Magic 8-Ball's answer: Better not tell you now

Let’s get started!

"""

import random  # Module to generate a random number from a range.

# Declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.
name = "Leslie"

# Declare a variable question, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.
question = "Will I win the lottery"

# Assign the answer of the Magic 8-ball to a variable
answer = ""
# Variable to store random number in range 1 - 9
random_number = random.randint(1, 9)
# print(random_number)

if name and random_number == 1:
    answer += "Yes - definitely"
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")
    # print("Yes - definitely")
elif name and random_number == 2:
    answer += "It is decidedly so"
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")
    # print("It is decidedly so")
elif name and random_number == 3:
    answer += "Without a doubt"
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")
    # print("Without a doubt")
elif name and random_number == 4:
    answer += "Reply hazy, try again"
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")
    # print("Reply hazy, try again")
elif name and random_number == 5:
    answer += "Ask again later"
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")
    # print("Ask again later")
elif name and random_number == 6:
    answer += "Better not tell you now"
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")
    # print("Better not tell you now")
elif name and random_number == 7:
    answer += "My sources say no"
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")
    # print("My sources say no")
elif name and random_number == 8:
    answer += "Outlook not so good"
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")
    # print("Outlook not so good")
elif name and random_number == 9:
    answer += "Very doubtful"
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")
    # print("Very doubtful")
elif not (name):
    answer += "Outlook not so good"
    print(f"Question: {question}")
    print(f"Magic 8-Ball's answer: {answer}")

else:
    print("Error")
