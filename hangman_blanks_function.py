# Version worked out w/ a student from the Tu/Th class during code brunch
# on 2/27 (Swati).
# current_output now resides in main() function; value will now be saved
# because the variable is in the global scope.

import random

game_word = "arkansas"

def have_player_guess_letter():

    player_guess = raw_input("Guess a letter: ")
    return player_guess


def replace_blanks_with_correct_letter(current_output, guess):

    for (index, letter) in enumerate(game_word):
        if letter == guess:
            current_output[index] = letter
    print "".join(current_output)


def main():

    current_output = len(game_word) * ["_"]

    while True:

        replace_blanks_with_correct_letter(current_output, have_player_guess_letter())

main()

# The new challenge is to pass in a game_word from a function choosing that word
# (get_random_word). Having issues with that right now...working on it!