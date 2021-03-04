# Problem Set 2, hangman.py
# Name: Lesley Reiderman

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
#import streamlit as st
#st.title('Hangman')

WORDLIST_FILENAME = "/Users/lesleyreiderman/Downloads/MIT Course Assignment/ps2/words.txt"

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

def check_is_digit(guess):
    if guess in abc:
        guess = guess
    else:
        print("User input is not a valid letter")
        guess = input('Try again...')
        check_is_digit(guess)
    return guess

def get_available_letters(letters_used):
    '''
    letters_used: list (of letters), which letters have been used so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been used.
    '''
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    list_difference = []
    for item in abc:
        if item not in letters_used:
            list_difference.append(item)
    return 'Words available: '+ '-'.join(list_difference)


def hangman(secret_word, guesses, letters_left, letters_guessed, letters_used):
    x = False
    if guesses > 0 and letters_left>0:
        guess = input('Insert the letter to play, there are ' + str(letters_left) +
                          ' letters left to guess and you have ' + str(guesses) +
                          ' guesses' + ' you have guess this letters: ' + ','.join(letters_guessed) +
                          ' --> ').lower()
        guess = check_is_digit(guess)
        guesses = guesses - 1
        letters_used.append(guess)
        for i in range(0, len(secret_word)):
            if secret_word[i] == guess:
                letters_guessed[i] = guess
                letters_left = letters_left-1
        print(get_available_letters(letters_used))
        result = hangman(secret_word, guesses, letters_left, letters_guessed, letters_used)
    if int(guesses) == 0 and letters_left>0:
        print('You do not have more guesses, Game over, your secret word was ' + secret_word)
    if letters_left == 0:
        print('Congrats!! You win the game, your secret word was '+str(secret_word))
        x = True
    return x


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    wordlist = load_words()
    z = load_words()
    secret_word = choose_word(wordlist)
    difficulty = input('Hi! we are playing Hangman, your secret word has ' + str(len(secret_word)) +
                               ' letters, and you can choose how many errors you can make. Good luck!, '
                               'Insert your difficulty')
    guesses = int(len(secret_word) + int(difficulty))
    letters_left = int(len(secret_word))
    letters_guessed=[]
    letters_used=[]
    for i in range(0,len(secret_word)):
        letters_guessed.insert(i,'-')
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']
    hangman(secret_word, guesses, letters_left, letters_guessed, letters_used)

