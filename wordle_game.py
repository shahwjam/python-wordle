"""
Wordle Game — Python Implementation
Author: Shahwan A
"""

import random
from english_words import get_english_words_set

# ANSI color codes for terminal output
GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RESET = "\033[0m"


def extractWordleWords(word_list):
    """Filter only valid 5-letter lowercase words."""
    return [word for word in word_list if len(word) == 5 and word.isalpha() and word.islower()]


def exactMatchLocs(word, guess):
    """Return indices where letters match exactly."""
    return [i for i in range(len(word)) if word[i] == guess[i]]


def partialMatchLocs(word, guess):
    """Return indices of letters that exist but are in the wrong position."""
    word_l = list(word)
    partial_loc = []
    for i, letter in enumerate(guess):
        if letter in word_l and letter != word[i]:
            partial_loc.append(i)
            word_l.remove(letter)
    return partial_loc


def wordleMatch(word, guess):
    """Return a string with colored Wordle feedback."""
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
    """Main game function."""
    # Get English words
    word_set = get_english_words_set(["web2"], lower=True)
    valid_words = extractWordleWords(word_set)

    if not valid_words:
        print("Word list is empty.")
        return

    target_word = random.choice(valid_words)

    print("Welcome to Wordle!")
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

    print("Out of attempts. The word was:", target_word)


if __name__ == "__main__":
    myWordle()
