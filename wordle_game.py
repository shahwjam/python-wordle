"""
Wordle Game — Python Implementation
Author: Shahwan A


Description:
This program implements a terminal-based version of the popular Wordle game.
The player has six attempts to guess a randomly selected five-letter word.
After each guess, the program provides colored feedback:

    Green  → correct letter in correct position
    Yellow → correct letter in wrong position
    Gray   → letter not in the word

Features:
- Random word selection from dictionary
- Input validation
- Color-coded feedback
- Modular function design
- Clean, readable structure

Dependencies:
- english-words package

Run:
    pip install english-words
    python hw8pr5.py
"""


import random
from english_words import get_english_words_set

# ANSI color codes for terminal output
GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RESET = "\033[0m"


def extractWordleWords(word_list):
    """
    Filters a word list and returns only valid Wordle words.

    A valid word:
    - has length 5
    - contains only alphabetic characters
    - is lowercase

    Parameters
    ----------
    word_list : iterable
        Collection of words.

    Returns
    -------
    list
        List of valid 5-letter lowercase words.
    """
    filtered = []
    for word in word_list:
        if len(word) == 5 and word.isalpha() and word.islower():
            filtered.append(word)
    return filtered


def exactMatchLocs(word, guess):
    """
    Finds positions where guess letters exactly match target word letters.

    Parameters
    ----------
    word : str
        Target word.
    guess : str
        User guess.

    Returns
    -------
    list
        Indices where letters match exactly.
    """
    result = []
    for i in range(len(word)):
        if word[i] == guess[i]:
            result.append(i)
    return result


def partialMatchLocs(word, guess):
    """
    Finds positions where letters exist in the word but in different positions.

    Ensures letters are not double-counted.

    Parameters
    ----------
    word : str
        Target word.
    guess : str
        User guess.

    Returns
    -------
    list
        Indices where letters exist but are misplaced.
    """
    word_l = list(word)
    partial_loc = []

    for i in range(len(guess)):
        letter = guess[i]
        if letter in word_l and letter != word[i]:
            partial_loc.append(i)
            word_l.remove(letter)

    return partial_loc


def upperCase(myLetter):
    """
    Converts a single letter to uppercase.

    Parameters
    ----------
    myLetter : str
        Single character string.

    Returns
    -------
    str
        Uppercase version of the letter.
    """
    return myLetter.upper()


def wordleMatch(word, guess):
    """
    Generates a colored Wordle feedback string.

    Rules:
    - Green = correct letter & position
    - Yellow = correct letter wrong position
    - Gray = not in word

    Parameters
    ----------
    word : str
        Target word.
    guess : str
        Player guess.

    Returns
    -------
    str
        Colored feedback string.
    """

    if len(word) != len(guess):
        return "*" * len(word)

    result = [""] * len(word)

    exact = exactMatchLocs(word, guess)
    partial = partialMatchLocs(word, guess)

    for i in range(len(word)):
        if i in exact:
            result[i] = GREEN + guess[i].upper() + RESET
        elif i in partial:
            result[i] = YELLOW + guess[i] + RESET
        else:
            result[i] = GRAY + guess[i] + RESET

    return "".join(result)


def myWordle():
    """
    Main game controller for Wordle.

    Handles:
    - Word selection
    - User input
    - Attempt tracking
    - Feedback display
    - Win/lose conditions
    """

    word_set = get_english_words_set(["web2"], lower=True)
    valid_words = extractWordleWords(word_set)

    if not valid_words:
        print("Word list is empty.")
        return

    target_word = random.choice(valid_words)

    print("Welcome to Wordle!!!!!!")
    print("Guess the 5-letter word. You have 6 attempts.\n")

    for attempt in range(1, 7):

        guess = input(f"Attempt {attempt}: Enter your 5-letter guess: ").lower()

        if len(guess) != 5:
            print("Please enter a 5-letter word!\n")
            continue

        if guess == target_word:
            print(GREEN + "Congratulations! You guessed the word!" + RESET)
            return

        print(wordleMatch(target_word, guess))
        print()

    print("Out of attempts.")
    print("The word was:", target_word)


# Run game
if __name__ == "__main__":
    myWordle()
# CSCI 1550: HW 8, Problem 5
# Filename: hw8pr5.py
# Name: Shahwan A
# Task: 5-letter word madness ... WORDLE!

import random 
from english_words import get_english_words_set


# Task 1:
def extractWordleWords(word_list):  #Function 1: Extract Wordle Words
     word_list= []          
     for word in word_list:
          if len(word) == 5 and not word[0].upper(): #If the word is 5 letter and lower case
               word_list.append(word)                   # Add the word to word list 
     return word_list 

#test_word= ['apple', 'Dan', 'green', 'ABCDEFGH']
#filter= extractWordleWords(test_word)
#print (filter)




# Task 2: Helper Functions : 

# Function to find the exact location of the leeters 
# Ai assictance : https://chatgpt.com/share/67dce3c6-f594-800c-ad10-4b5f500f2ce0
def exactMatchLocs(word,guess):
     
     result =[]                     # Store the results in a empty list
     for i  in range(len(word)):    # If the location of letter in word is    
          if word[i] ==  guess[i]:  # same as lcation guess add it to resut
               result.append(i)
     return result 

#test1 = "hi"
#test2 = "hey "
#result = exactMatchLocs(test1, test2)
#print(result)
# Function to find the partial match location of letter 
def partialMatchLocs(word,guess):
    word_l = list(word)         # Convert word to a list so we track 
                                # i as a number 
    partial_loc = []            # A list to store Match locations                           
    for i in range(len(guess)): # 
         k = guess[i]
         if  k in word_l and k != word[i]:
              partial_loc.append(i)   
              word_l. remove(k)  #remove the first occurrence to prevent double-counting
         else: 
              pass 
    
    
    return partial_loc 

#test1 ='hello'
#test2 = 'holla'
#result = partialMatchLocs(test1,test2)


# Function to Covnert a string from lower case to upper case 
# Ai: https://chatgpt.com/share/67dda490-a588-800c-adc5-0058cae4b66c
def upperCase(myLetter):
    
     upperCase= chr(ord(myLetter)- 32)
     return upperCase
#print(upperCase('a'))



def wordleMatch(word, guess):
  
     #the length of two words should be 
    if len(word) != len(guess):
        return '*' * len(word)
    
    # Create initial asterisk result
    result = ['*'] * len(word)
    
    # Handle exact matches (uppercase letters)
    exact_matches = exactMatchLocs(word, guess)
    for idx in exact_matches:
        result[idx] = upperCase(guess[idx])
    
    # Handle partial matches (lowercase letters)
    partial_matches = partialMatchLocs(word, guess)
    for idx in partial_matches:
        if result[idx] == '*':
            result[idx] = guess[idx]
    
    return ''.join(result)


#print(wordleMatch('hello', 'hxllo'))

def myWordle():
  
    # Get  word list
    word_list = ew.english_words_set
    valid_words = extractWordleWords(word_list)
    
    # Choose random word
    target_word = random.choice(valid_words)
    
    print("Welcome to Wordle!!!!!!")
    print("Guess the 5-letter word. You have 6 attempts.")
    
    for attempt in range(1, 7):
        
        guess = input("Attempt" (attempt), ": Enter your 5-letter guess: ").lower()
        
        # Validate guess length
        if len(guess) != 5:
            print("Please enter a 5-letter word!")
            continue
        
        # Check for win condition
        if guess == target_word:
            print(" Congratulations! You guessed the word", (target_word))
            return
        
        # Show match result
        match_result = wordleMatch(target_word, guess)
        print(match_result)
    
     # you lost !!!!!!
    print(" Sorry, you're out of attempts the word was :" , target_word)


     
     

     
     



#myWordle()

        


              
         
         
         
             
        
        
         
         
         
         
     
     
     











     
     















    
           

