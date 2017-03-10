import random


ufo_pics = ['''
     ___
 ___/...\\___
/   '---'   \\
'--_______--'
     / \\
    /   \\
    /\\0/\\
    / | \\
    // \\\\''', '''
     ___
 ___/...\\___
/   '---'   \\
'--_______--'
     / \\
    /   \\
    /\\0/\\
    / | \\
    //  \\''', '''
     ___
 ___/...\\___
/   '---'   \\
'--_______--'
     / \\
    /   \\
    /\\0/\\
    / | \\
    /   \\''','''
     ___
 ___/...\\___
/   '---'   \\
'--_______--'
     / \\
    /   \\
    / 0/\\
    / | \\
    /   \\''','''
     ___
 ___/...\\___
/   '---'   \\
'--_______--'
     / \\
    /   \\
    / 0 \\
    / | \\
    /   \\''','''
     ___
 ___/...\\___
/   '---'   \\
'--_______--'
     / \\
    /   \\
    / 0 \\
    /   \\
    /   \\''', '''
     ___
 ___/...\\___
/   '---'   \\
'--_______--'
     / \\
    / ~ \\
    / ~ \\
    / ~ \\
    / ~ \\'''
]


win_pic = '''
                                   .''.       
       .''.      .        *''*    :_\\/_:     . 
      :_\\/_:   _\\(/_  .:.*_\\/_*   : /\\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\\/_:'.:::.    ' *''*    * '.\\'/.' _\\(/_'.':'.'
 : /\\ : :::::     *_\\/_*     -= o =-  /)\\    '  *
  '..'  ':::'     * /\\ *     .'/.\\'.   '
      *            *..*         :
        *
        *'''


# Sample list--good for testing
# For finished game, import .txt file(s) for word choice
word_list = ["apple", "berry", "cherry", "arkansas", "mississippi", "hawaii", "serendipity", "insomnia"]

def get_random_word():

    random_word = random.choice(word_list).upper()
    return random_word


def print_ufo_pics(ufo_pics, miss_counter):

    index = miss_counter
    print ufo_pics[index]


def have_player_guess_letter(already_guessed):

    guess = raw_input("Guess a letter: ").upper()

    while True:

        if len(guess) != 1:
            guess = raw_input("Please enter a single letter: ").upper()
        elif guess in already_guessed:
            guess = raw_input ("You've already guessed that letter, please choose another: ").upper()
        elif not guess.isalpha():
            guess = raw_input("Please enter a LETTER: ").upper()
        else:
            break

    return guess


# ***THIS IS A VARIANT OF THE ABOVE FUNCTION***

# def have_guess_letter(already_guessed):

#     valid_guess = False
#     guess = raw_input("Guess a letter: ")

#     while not valid_guess:

#         if len(guess) != 1:
#             guess = raw_input("Please enter a single letter: ").upper()
#         elif guess in already_guessed:
#             guess = raw_input ("You've already guessed that letter, please choose another: ").upper()
#         elif not guess.isalpha():
#             guess = raw_input("Please enter a LETTER: ").upper()
#         else:
#             valid_guess = True

#     return guess


def replace_blanks_with_correct_letter(current_output, guess, game_word):

    for index, letter in enumerate(game_word):
        if letter == guess:
            current_output[index] = letter


def display_guessed_letters(already_guessed, current_output):
    
    if (len(already_guessed) > 0) and ("_" in current_output):
            print "Letters you've guessed: " + ", ".join(sorted(already_guessed))


def missed_guess_counter(letter, game_word, miss_counter):

    if letter not in game_word:
        miss_counter += 1
    
    return miss_counter


def determine_and_display_outcome(current_output, game_word, miss_counter, game_over):

    if "_" not in current_output:
        game_over = True
        print win_pic; print ""
        print "   " + "".join(current_output); print ""
        print "The word was " + game_word.upper() + ": Congratulations, you've won! You're safe here on Earth."; print ""

    elif miss_counter == len(ufo_pics) - 1:
        game_over = True
        print ufo_pics[6]; print " \n "
        print "   " + "".join(current_output); print ""
        print "The word was " + game_word.upper() + ": Too bad, you lose--You've been abducted by aliens!"; print ""

    # Not really necessary for game to function properly, should it be included?
    # else:
    #     game_over = False
        
    return game_over


def play_again():

    again = raw_input("Do you want to play again? Y/N: ").upper()

    if again == "Y":
        return True
    elif again == "N":
        return False
    else:
        again = raw_input("Not a valid choice, please enter Y/N: ").upper()


def main():

    print "\nWelcome to the game of ALIEN ABDUCTION!\n"
    print "Guess the word before the UFO beams you up!"

    game_word = get_random_word()
    current_output = len(game_word) * ["_"]
    already_guessed = set()
    miss_counter = 0
    game_over = False

    while True:

        print_ufo_pics(ufo_pics, miss_counter); print " \n "
        print "   " + "".join(current_output); print ''
        display_guessed_letters(already_guessed, current_output); print ""
        letter = have_player_guess_letter(already_guessed)
        replace_blanks_with_correct_letter(current_output, letter, game_word)
        already_guessed.update([letter])
        miss_counter = missed_guess_counter(letter, game_word, miss_counter)
        game_over = determine_and_display_outcome(current_output, game_word, miss_counter, game_over)

        if game_over == True:
            if play_again():
                game_word = get_random_word()
                current_output = len(game_word) * ["_"]
                already_guessed = set()
                miss_counter = 0
                game_over = False
            else:
                break


if __name__ == "__main__":
    main()
