import random

# For finished game, import .txt file(s) for word choice
word_list = ["apple", "berry", "cherry", "arkansas", "mississippi", "hawaii", "serendipity", "insomnia"]    # sample list--good for testing

gallows_pics = []

def get_random_word():

    random_word = random.choice(word_list).upper()
    return random_word


def have_player_guess_letter(already_guessed):

    player_guess = raw_input("Guess a letter: ").upper()

    while True:

        if len(player_guess) != 1:
            player_guess = raw_input("Please enter a single letter: ").upper()
        elif player_guess in already_guessed:
            player_guess = raw_input ("You've already guessed that letter, please choose another: ").upper()
        elif not player_guess.isalpha():
            player_guess = raw_input("Please enter a LETTER: ").upper()
        else:
            break

    return player_guess


# ***THIS IS ANOTHER VERSION OF THE ABOVE FUNCTION***
# def have_player_guess_letter(already_guessed):

#     valid_guess = False
#     player_guess = raw_input("Guess a letter: ")

#     while not valid_guess:

#         if len(player_guess) != 1:
#             player_guess = raw_input("Please enter a single letter: ").upper()
#         elif player_guess in already_guessed:
#             player_guess = raw_input ("You've already guessed that letter, please choose another: ").upper()
#         elif not player_guess.isalpha():
#             player_guess = raw_input("Please enter a LETTER: ").upper()
#         else:
#             valid_guess = True

#     return player_guess


def replace_blanks_with_correct_letter(current_output, guess, game_word):

    for index, letter in enumerate(game_word):
        if letter == guess:
            current_output[index] = letter


# Use dictionary--keys are letters, values are True/False
def record_and_display_guessed_letters(already_guessed, current_output):
    
    if (len(already_guessed) > 0) and ("_" in current_output):
            print "Letters you've guessed: " + ", ".join(sorted(already_guessed))


# IN PROGRESS
def check_if_player_has_won():

    found_all_letters = True

    if "_" in current_output:
        found_all_letters = False
        # do something here

    if found_all_letters:
        print "Congratulations, you've won!"
        game_is_over = True
        # do something here


# IN PROGRESS
def missed_letter_counter():

    if player_guess not in game_word():
        miss_counter += 1
    return miss_counter


# IN PROGRESS -- 2 separate functions or just 1?
def determine_if_won_or_lost():

    # do something here to determine if game is won

    if miss_counter == len(gallows_pics): # final intention; for testing purposes, set a number
        print "You lose!"


# IN PROGRESS
def ask_if_play_again():

    again = raw_input("Do you want to play again? Y/N: ").upper()

    if again == "Y":
        return True
    elif again == "N":
        return False
    else:
        again = raw_input("Not a valid choice, please enter Y/N: ").upper()


def main():

    game_word = get_random_word()
    current_output = len(game_word) * ["_"]
    already_guessed = set()
    # game_is_over = False

    while True:

        letter = have_player_guess_letter(already_guessed)
        replace_blanks_with_correct_letter(current_output, letter, game_word)
        already_guessed.update([letter])
        print ''.join(current_output)
        record_and_display_guessed_letters(already_guessed, current_output)
        if "_" not in current_output:
            print "Congratulations, you've won!"
            break


if __name__ == "__main__":
    main()
