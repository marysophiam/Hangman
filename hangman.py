import random


title_pic = '''
    ___    __    ___________   __     ___    ____  ____  __  ______________________  _   __
   /   |  / /   /  _/ ____/ | / /    /   |  / __ )/ __ \/ / / / ____/_  __/  _/ __ \/ | / /
  / /| | / /    / // __/ /  |/ /    / /| | / __  / / / / / / / /     / /  / // / / /  |/ / 
 / ___ |/ /____/ // /___/ /|  /    / ___ |/ /_/ / /_/ / /_/ / /___  / / _/ // /_/ / /|  /  
/_/  |_/_____/___/_____/_/ |_/    /_/  |_/_____/_____/\____/\____/ /_/ /___/\____/_/ |_/


                  #################################################
                  #                                               #
                  #    Welcome to the game of ALIEN ABDUCTION!    #
                  #                                               #
                  #  Guess the word before the UFO beams you up!  #
                  #                                               #
                  #################################################
'''


ufo_pics = ['''
      ___
 ____/...\\____
/    '---'    \\
'--_________--'
      / \\
     /   \\
    / \\0/ \\
   /   |   \\
  /   / \\   \\''', '''
      ___
 ____/...\\____
/    '---'    \\
'--_________--'
      / \\
     /   \\
    / \\0/ \\
   /   |   \\
  /     \\   \\''','''
      ___
 ____/...\\____
/    '---'    \\
'--_________--'
      / \\
     /   \\
    / \\0/ \\
   /   |   \\
  /         \\''','''
      ___
 ____/...\\____
/    '---'    \\
'--_________--'
      / \\
     /   \\
    /  0/ \\
   /   |   \\
  /         \\''','''
      ___
 ____/...\\____
/    '---'    \\
'--_________--'
      / \\
     /   \\
    /  0  \\
   /   |   \\
  /         \\''','''
      ___
 ____/...\\____
/    '---'    \\
'--_________--'
      / \\
     /   \\
    /  0  \\
   /       \\
  /         \\''','''
      ___
 ____/...\\____
/    '---'    \\
'--_________--'
      / \\
     / ~ \\
    /  ~  \\
   /   ~   \\
  /    ~    \\''']


win_pic = '''

      .       .    )        .           .
   .       *             .         .
               .                      .
   .       .                   .
                                *        .
      .   '               .              .
              _.---._   .            .     *
    *       .'       '.
        _.-~===========~-._
       (___________________)       .   *
  __  .'     \_______/   .'  ______        __
    |              .'  .'   |      |      |  |
    |             '         |      |      |  |
    |                       |      |   ___|  |_
  __|_______________________|__..--~~~~        ~--.
                    /|\\
                   /   \\
                  /  |  \\
                 /       \\
   \|/          /    |    \\
               /           \\
              /      |      \\
             /       -------------------------------------------------
            /        |  YOU WIN!!! (You watch the UFO fly away as    |
           /         |                                               |
          /    __    |  you remain safely here on Earth....for now!) |  
         /    /  \   -------------------------------------------------
        /    (\__/)  |            \\
       /     _\__/_                \\
      /     /      \ |              \\
     /     / /   / /                 \\
           \ |   \_\                  \\
            \|____\_)                  \    \|/
             |    \\
             | |\  \\
             | |/  /
             |_/__/
            (__[__)'''


lose_pic = '''
              .-""""-.
             /        \\
            /_        _\\
           // \      / \\\\
           |\__\    /__/|
            \    ||    /
             \        /
              \  __  /  \  /     ------------------------------------------
                |  |     /\\      |           Oh no, YOU LOSE!             |
                |  |    O  O     |                                        |
                ----    //       |  ALIEN ABDUCTION & EXPERIMENTATION!!!  |
               (    )  //        ------------------------------------------
              (\\\\     //
             (  \\\\    )
             (   \\\\   )   /\\\\
   ___[\______/^^^^^^^\__/) o-)__
  |\__[=======______//________)__\\
  \|_______________//____________|
      |||      || //||     |||
      |||      || @.||     |||
       ||      \/  .\/      ||'''



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

    guess = raw_input(" Guess a letter: ").upper()

    while True:
        if not guess.isdigit() and not guess.isalpha():
            print ""
            guess = raw_input(" Please enter a LETTER (you're being tricky!): ").upper()
        elif guess.isdigit():
            print ""
            guess = raw_input(" Please enter a LETTER: ").upper()
        elif len(guess) != 1:
            print ""
            guess = raw_input(" Please enter a single letter: ").upper()
        elif guess in already_guessed:
            print ""
            guess = raw_input (" You've already guessed that letter, please choose another: ").upper()
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
            print " Letters you've guessed: " + ", ".join(sorted(already_guessed))


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
        print ""; print " " + " ".join(current_output).strip(); print ""
        print " The word was " + game_word.upper() + ": CONGRATULATIONS, YOU'VE WON!"
        print win_pic; print " \n \n "
    else:
        print ufo_pics[-1]; print " \n "
        print " " + " ".join(current_output).strip(); print ""
        print " The word was " + game_word.upper() + ": Oh no, you lose--You've been abducted by aliens!"; print ""
        print lose_pic; print " \n \n "


def play_again():

    again = raw_input(" Do you want to play again? Y/N: ").upper()

    while True:
        if again == "Y":
            return True
        elif again == "N":
            return False
        else:
            print ""
            again = raw_input(" Not a valid choice, please enter Y/N: ").upper()


def play_game():

  word_list = load_words()
  game_word = get_random_word(word_list)
  current_output = len(game_word) * ["_"]
  already_guessed = set()
  miss_counter = 0
  game_over = False

  while not game_over:
    print_ufo_pics(ufo_pics, miss_counter); print " \n "
    print " " + " ".join(current_output).strip(); print ''
    display_guessed_letters(already_guessed, current_output); print ""
    letter = have_player_guess_letter(already_guessed)
    replace_blanks_with_correct_letter(current_output, letter, game_word)
    record_guessed_letters(already_guessed, letter)
    miss_counter = missed_guess_counter(letter, game_word, miss_counter)
    game_over = check_if_game_over(game_over, current_output, miss_counter)
    
  display_outcome(current_output, miss_counter, game_word)


def main():

    print title_pic

    while True:
      play_game()
      if not play_again():
        break


if __name__ == "__main__":
    main()


# Next steps:
# -- Move ASCII pictures to external file and import
# -- Flaskify using Oxford Dictionary API to import random word choices
#    (eventually add feature to choose Easy/Intermediate/Difficult words)
