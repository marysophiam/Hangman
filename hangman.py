import random


def select_word():

    word_list = ['apple', 'berry', 'cherry', 'arkansas', 'mississippi', 'hawaii', 'serendipity']

    game_word = random.choice(word_list)
    return game_word



def replace_blanks_with_correct_letters():
    # Replace blanks with correct letter(s) as they are guessed

    game_ongoing = True    # probably need a better variable name

    game_word = 'arkansas'    # obviously, this will change...this is just a test word for the sake of simplicity/debugging right now

    currently_guessed_word = '_' * len(game_word)    # still want to come up with a better variable name

    # These variables will probably live elsewhere in the program down the road, in display_guessed_letters()
    correct_letters = ''
    # missed_letters = ''    # don't need this right now, but probably will later

    while game_ongoing:

        guess = raw_input("Guess a letter: ")

        if guess in game_word:
            correct_letters += guess

        # if guess not in game_word:
            # missed_letters += guess    # see above comment re. this variable

        for i in range(len(game_word)):
            if game_word[i] in correct_letters:
                currently_guessed_word = currently_guessed_word[:i] + game_word[i] + currently_guessed_word[i + 1:]

        print 'Current word status: ', currently_guessed_word
        # return currently_guessed_word

        if '_' not in currently_guessed_word:
            game_ongoing = False
            break

replace_blanks_with_correct_letters()


# def display_game_board():
    # Gallows pictures, blank spaces, guessed letters (correct/incorrect)



# def display_guessed_letters():
    # correct & incorrect


# def have_player_guess_letter():


# with the replace_blanks_with_correct_letters() function as currently written, it may not be necessary for this to be a separate function
# def is_letter_in_word():
    # True/False


