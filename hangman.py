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


if __name__ == "__main__":
    main()