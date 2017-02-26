import random

game_word = 'arkansas'    # just a test word for now; good b/c of multiples

# ---------------------------------------------------------------------------

# This works the way I want it to, but the problem is that the guess is still
# coming from inside the function, not from the have_player_guess_letter
# function.

def replace_blanks_with_correct_letters():

    current_output = len(game_word) * ['_']

    while True:

        guess = raw_input('Guess a letter: ')

        for index, letter in enumerate(game_word):
            if letter == guess:
                current_output[index] = letter
        print ''.join(current_output)


replace_blanks_with_correct_letters()


# ---------------------------------------------------------------------------

# In this version, the user is prompted for a guess by passing a returned
# value in from the have_player_guess_letter function in the main() function
# (therefore avoiding having the guess come from inside the function).
# It works, but the problem is that each time a new letter is guessed, the
# current_output variable is reset to all '_'s instead of the value
# being permanently changed. When I messed around with putting while True:
# inside this function, I ended up in an endless loop after the first guess
# was made.

def have_player_guess_letter():

    player_guess = raw_input('Guess a letter: ')
    return player_guess


def replace_blanks_with_correct_letters(guess):

    current_output = len(game_word) * ['_']

    for (index, letter) in enumerate(game_word):
        if letter == guess:
            current_output[index] = letter
    print ''.join(current_output)
    return current_output


def main():

    while True:

        replace_blanks_with_correct_letters(have_player_guess_letter())


main()
