  
SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
MAX_WRONG_GUESSES = 7
SNOWMAN_MAX_WRONG_GUESSES = 7

SNOWMAN_1 = '*   *   *  '
SNOWMAN_2 = ' *   _ *   '
SNOWMAN_3 = '   _[_]_ * '
SNOWMAN_4 = '  * (")    '
SNOWMAN_5 = '  \( : )/ *'
SNOWMAN_6 = '* (_ : _)  '
SNOWMAN_7 = '-----------'


def snowman(snowman_word):

    """Complete the snowman function
    replace "pass" below with your own code
    It should print 'Congratuations, you win!'
    If the player wins and, 'Sorry, you lose!  The word was {snowman_word}' if the player loses
    """
    player_wins = False # Where do I put variables
    correct_lst = [] # Does this belong here
    wrong_lst = []

    print(build_word_list(snowman_word)) # make dictionaries. ****How do I do backslash thingie
    
    dashes = " "
    length = len(snowman_word)
    letter = ''
    print(f"Welcome to the snowman game! Guess the word. " + 
    f"Your word has {length} letters.  " + f"Your word is {snowman_word}.")
    print()

    for i in range(len(snowman_word)):
      dashes += "_ "
    print(dashes)

    for i in range(len(snowman_word)):
      letter = get_letter_from_user(wrong_lst, correct_lst)
      if letter in snowman_word:
        correct_lst.append(letter)
        print(f"correct_lst:{correct_lst}")
        
      else:
        wrong_lst.append(letter)
        
        print(f"wrong_lst:{wrong_lst}")
        num_wrong_guesses = len(wrong_lst)
        print_snowman_graphic(num_wrong_guesses)
    # print(f"{correct_lst=:,} | {wrong_lst=:,}")
    # print(get_letter_from_user(wrong_lst, correct_lst))

    # if player_wins == True:
    #   print('Congratuations, you win!')
    # elif player_wins == False:
    #   print (f'Sorry, you lose!  The word was {snowman_word}')
    
# 
def print_snowman_graphic(num_wrong_guesses):
    """This function prints a portion of the 
    snowman depending on the number of 
    wrong guesses
    """
    
    for i in range(1, num_wrong_guesses + 1):
        if(i == 1):
            print(SNOWMAN_1)
        if(i == 2):
            print(SNOWMAN_2)
        if(i == 3):
            print(SNOWMAN_3)
        if(i == 4):
            print(SNOWMAN_4)
        if(i == 5):
            print(SNOWMAN_5)
        if(i == 6):
            print(SNOWMAN_6)
        if(i == 7):
            print(SNOWMAN_7)

def build_word_list(word):
    """This function builds a list of dictionaries
    With each letter and if that letter has been guessed "guessed": False
    Example: [ { 'letter': 'a', 'guessed': False }, 'letter': 'b', 'guessed': False }, ]
    """
    word_list = []
    for letter in word:
        letter_dict = {"letter": letter, "guessed": False}
        word_list.append(letter_dict)
    return word_list

def print_word_list(word_list):
    """This function prints the letters of the word
    based on if that letter has been guessed or not
    """

    output_string = ""
    for elem in word_list:
        if elem["guessed"]:
            output_string += elem["letter"]
        else:
            output_string += "_"
        output_string += " "
    print(output_string)


def get_letter_from_user(wrong_list, correct_guesses_list):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        # NEW SECTION
        elif user_input_string in wrong_list or user_input_string in correct_guesses_list:
            print("You have already guessed that letter!")
        # END NEW SECTION
        else:
            valid_input = True

    return user_input_string

def update_and_check_word_list(list_of_letters, guessed_letter):
    all_letters_guessed = True
    for letter_dict in list_of_letters:
        if (guessed_letter == letter_dict["letter"]):
            letter_dict["guessed"] = True
        elif (not letter_dict["guessed"]):
            all_letters_guessed = False
    
    return all_letters_guessed
