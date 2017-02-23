import random


def select_word():
    # For finished game, import .txt file(s) for word choices

    word_list = ['apple', 'berry', 'cherry', 'arkansas', 'mississippi', 'hawaii', 'serendipity']    # sample list--good for testing

    game_word = random.choice(word_list)
    return game_word



def replace_blanks_with_correct_letters():
    # Replace blanks with correct letter(s) as they are guessed

    game_ongoing = True    # probably need a better variable name

    game_word = 'arkansas'    # obviously, this will change...this is just a test word for the sake of simplicity/debugging right now

    currently_guessed_word = '_' * len(game_word)    # still want to come up with a better variable name

    while game_ongoing:

        guess = raw_input("Guess a letter: ")    # will be incorporated into have_player_guess_letter() function later

        for i in range(len(game_word)):
            if game_word[i] == guess:
                currently_guessed_word = currently_guessed_word[:i] + guess + currently_guessed_word[i + 1:]

        print 'Current word status: ', currently_guessed_word    # wording of print statement to be changed, just testing right now
        # return currently_guessed_word

        if '_' not in currently_guessed_word:
            game_ongoing = False
            break

replace_blanks_with_correct_letters()


# def display_game_board():
    # gallows pictures, blank spaces, guessed letters (correct/incorrect)


# def display_guessed_letters():
    # correct & incorrect


# def have_player_guess_letter():
    # Incorporate guess = raw_input("Guess a letter: ") into this function


# def is_letter_in_word():
    # True/False

    # Is this function necessary anymore? (probably not)


