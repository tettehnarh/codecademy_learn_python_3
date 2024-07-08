letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
          3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Using a list comprehension and zip, create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.
letter_to_points = {letter: point for letter, point in zip(letters, points)}
# Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
letter_to_points[" "] = 0

print(letter_to_points)

# We want to create a function that will take in a word and return how many points that word is worth.


def score_word(word):
    point_total = 0
    for letter in word:
        if letter in letter_to_points.keys():
            point_total += letter_to_points[letter]
        else:
            point_total += 0
    return point_total


# Let's test this function by using the word "BROWNIE"
brownie_points = score_word("BROWNIE")
print(brownie_points)

# Create a dictionary called player_to_words that maps players to a list of the words they have played.
player_to_words = {"player1": ['BLUE', 'TENNIS', 'EXIT'],
                   "wordNerd": ['EARTH', 'EYES', 'MACHINE'], "Lexi Con": ['ERASER', 'BELLY', 'HUSKY'], "Prof Reader": ['ZAP', 'COMA', 'PERIOD']}

# Create an empty dictionary called player_to_points.
player_to_points = {}

# Iterate through the items in player_to_words. Call each player player and each list of words words.


def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
            player_to_points[player] = player_points

# print(player_to_points)

# Let's test update_point_totals()


def play_word(player, word):
    player_to_words[player].append(word)


# Let's test
play_word("player1", "TEST")
update_point_totals()

print(player_to_words)
print(player_to_points)
