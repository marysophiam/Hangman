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


def load_words():

    with open("hangman_words.txt", mode = "r") as word_list:
        word_list = word_list.readlines()
        word_list = [word.strip() for word in word_list]
        
    return word_list


def get_random_word(word_list):

    random_word = random.choice(word_list).upper()
    return random_word


def print_ufo_pics(ufo_pics, miss_counter):

    index = miss_counter
    print ufo_pics[index]


def have_player_guess_letter(already_guessed):

    guess = raw_input("Guess a letter: ").upper(); print ""

    while True:

        if guess.isdigit():
            guess = raw_input("Please enter a LETTER: ").upper(); print ""
        elif len(guess) != 1:
            guess = raw_input("Please enter a single letter: ").upper(); print ""
        elif guess in already_guessed:
            guess = raw_input ("You've already guessed that letter, please choose another: ").upper(); print ""
        else:
            break

    return guess


def replace_blanks_with_correct_letter(current_output, guess, game_word):

    for index, letter in enumerate(game_word):
        if letter == guess:
            current_output[index] = letter


def record_guessed_letters(already_guessed, letter):

    already_guessed.update([letter])


def display_guessed_letters(already_guessed, current_output):
    
    if (len(already_guessed) > 0) and ("_" in current_output):
            print "Letters you've guessed: " + ", ".join(sorted(already_guessed))


def missed_guess_counter(letter, game_word, miss_counter):

    if letter not in game_word:
        miss_counter += 1
    
    return miss_counter


def check_if_game_over(game_over, current_output, miss_counter):

    if "_" not in current_output:
        game_over = True
    elif miss_counter == len(ufo_pics) - 1:
        game_over = True
    else:
        game_over = False

    return game_over


def display_outcome(current_output, miss_counter, game_word):

    if "_" not in current_output:
        print win_pic; print ""
        print "   " + "".join(current_output); print ""
        print "The word was " + game_word.upper() + ": Congratulations, you've won! You're safe here on Earth."; print ""
    else:
        print ufo_pics[-1]; print " \n "
        print "   " + "".join(current_output); print ""
        print "The word was " + game_word.upper() + ": Too bad, you lose--You've been abducted by aliens!"; print ""


def play_again():

    again = raw_input("Do you want to play again? Y/N: ").upper()

    while True:
        if again == "Y":
            return True
        elif again == "N":
            return False
        else:
            again = raw_input("Not a valid choice, please enter Y/N: ").upper()


def main():

    print "\nWelcome to the game of ALIEN ABDUCTION!\n"
    print "Guess the word before the UFO beams you up!"

    word_list = load_words()
    game_word = get_random_word(word_list)
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
        record_guessed_letters(already_guessed, letter)
        miss_counter = missed_guess_counter(letter, game_word, miss_counter)
        game_over = check_if_game_over(game_over, current_output, miss_counter)

        if game_over == True:
            display_outcome(current_output, miss_counter, game_word)
            if play_again():
                game_word = get_random_word(word_list)
                current_output = len(game_word) * ["_"]
                already_guessed = set()
                miss_counter = 0
                game_over = False
            else:
                break

if __name__ == "__main__":
    main()
