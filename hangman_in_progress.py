import random

def get_random_word(word_list):
    # For finished game, import .txt file(s) for word choice

    random_word = random.choice(word_list)
    return random_word


# This is GOOD
def have_player_guess_letter():

    player_guess = raw_input('Guess a letter: ')
    return player_guess


# This is GOOD
def replace_blanks_with_correct_letter(current_output, guess):

    for (index, letter) in enumerate(game_word):
        if letter == guess:
            current_output[index] = letter
    print ''.join(current_output)


def main():

    word_list = ['apple', 'berry', 'cherry', 'arkansas', 'mississippi', 'hawaii', 'serendipity', 'insomnia']    # sample list--good for testing

    # Herein lies the problem...
    game_word = get_random_word(word_list)

    # This is GOOD
    current_output = len(game_word) * ['_']

    while True:

        # This is GOOD
        replace_blanks_with_correct_letter(current_output, have_player_guess_letter())


if __name__ == "__main__":
    main()