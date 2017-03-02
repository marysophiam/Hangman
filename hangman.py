import random

# For finished game, import .txt file(s) for word choice
word_list = ['apple', 'berry', 'cherry', 'arkansas', 'mississippi', 'hawaii', 'serendipity', 'insomnia']    # sample list--good for testing

def get_random_word():

    random_word = random.choice(word_list)
    return random_word


def have_player_guess_letter():

    player_guess = raw_input('Guess a letter: ')
    return player_guess


def replace_blanks_with_correct_letter(current_output, guess, game_word):

    for (index, letter) in enumerate(game_word):
        if letter == guess:
            current_output[index] = letter
    print ''.join(current_output)


def main():

    game_word = get_random_word()
    current_output = len(game_word) * ['_']

    while True:

        replace_blanks_with_correct_letter(current_output, have_player_guess_letter(), game_word)


if __name__ == "__main__":
    main()
