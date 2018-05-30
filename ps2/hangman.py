# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    count = 0
    for letter in secret_word:
        if letter in letters_guessed:
            count += 1
            if count < len(secret_word):
                continue
            else:
                return(True)
        else:
            return(False)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_ "
    return(guessed_word)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    available_letters = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters += letter
        else:
            continue
    return(available_letters)




def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")


    remaining_guess = 6
    letters_guessed = []
    warnings = 3
    print("You have", warnings, "warnings left.")
    while remaining_guess > 0:
        while remaining_guess > 0:
            print("-------------")
            #print("You have", warnings, "warnings left.")
            print("You have", remaining_guess, "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            letter = input("Please guess a letter:")
            if letter not in string.ascii_letters:
                warnings -= 1
                if warnings >= 0:
                    print("Oops! That is not a valid letter. You have", warnings, "warnings left:",
                          get_guessed_word(secret_word, letters_guessed))
                else:
                    remaining_guess -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                          get_guessed_word(secret_word,letters_guessed))
            elif letter.lower() not in get_available_letters(letters_guessed):
                warnings -= 1
                if warnings >= 0:
                    print("Oops! You've already guessed that letter. You have", warnings, "warnings left:",
                          get_guessed_word(secret_word, letters_guessed))
                else:
                    remaining_guess -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                          get_guessed_word(secret_word, letters_guessed))
            elif letter.lower() not in secret_word:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                letters_guessed += letter.lower()
                remaining_guess -= 1
                break
            else:
                letter = letter.lower()
                letters_guessed += letter
                print("Good guess:", get_guessed_word(secret_word, letters_guessed) + ".")
                break
        if is_word_guessed(secret_word, letters_guessed):
            uq_letters = set(secret_word)
            score = remaining_guess * len(uq_letters)
            print("-------------")
            print("Congratulations, you won!")
            print("Your total score for this game is %d." % score)
            break
        elif remaining_guess == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was", secret_word + ".")
            break



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_ns = my_word.replace(" ", "")
    tested = []
    blank_char = []
    if len(my_word_ns) == len(other_word):
        for i in range(0, len(my_word_ns) + 1):
            # print(blank_char)
            # print(tested)
            if tested == list(my_word_ns):
                for char in blank_char:
                    if char in tested:
                        return False
                    else:
                        return True
            else:
                if my_word_ns[i] == other_word[i]:
                    tested += my_word_ns[i]
                elif my_word_ns[i] == "_":
                    tested += my_word_ns[i]
                    blank_char += other_word[i]
                else:
                    # print(tested)
                    return False
                    break # PyCharm said this was unreachable but maybe it was wrong. Test with "ab_ le" and "apple".
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)
        else:
            continue
    if len(possible_matches) != 0:
        print("Possible word matches are:\n" + ", ".join(possible_matches))
    else:
        print("No matches found")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    remaining_guess = 6
    letters_guessed = []
    warnings = 3
    print("You have", warnings, "warnings left.")
    while remaining_guess > 0:
        while remaining_guess > 0:
            print("-------------")
            # print("You have", warnings, "warnings left.")
            print("You have", remaining_guess, "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            letter = input("Please guess a letter:")
            if letter == "*":
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            elif letter not in string.ascii_letters:
                warnings -= 1
                if warnings >= 0:
                    print("Oops! That is not a valid letter. You have", warnings, "warnings left:",
                          get_guessed_word(secret_word, letters_guessed))
                else:
                    remaining_guess -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                          get_guessed_word(secret_word, letters_guessed))
            elif letter.lower() not in get_available_letters(letters_guessed):
                warnings -= 1
                if warnings >= 0:
                    print("Oops! You've already guessed that letter. You have", warnings, "warnings left:",
                          get_guessed_word(secret_word, letters_guessed))
                else:
                    remaining_guess -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                          get_guessed_word(secret_word, letters_guessed))
            elif letter.lower() not in secret_word:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                letters_guessed += letter.lower()
                remaining_guess -= 1
                break
            else:
                letter = letter.lower()
                letters_guessed += letter
                print("Good guess:", get_guessed_word(secret_word, letters_guessed) + ".")
                break
        if is_word_guessed(secret_word, letters_guessed):
            uq_letters = set(secret_word)
            score = remaining_guess * len(uq_letters)
            print("-------------")
            print("Congratulations, you won!")
            print("Your total score for this game is %d." % score)
            break
        elif remaining_guess == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was", secret_word + ".")
            break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    #
    # hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = "tendonitis"
    # hangman(secret_word)
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
