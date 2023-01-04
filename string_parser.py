#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Jan 3, 2023
# This program asks the user to enter a sentence, then it parses
# the sentence and returns a list of words. Finally, the program
# displays the words one per line.


def parse_string(a_string):
    # ParseString function
    # Accepts a string and returns a list of words
    words = []
    word = ""
    for i in range(len(a_string)):
        if a_string[i] == " ":
            words.append(word)
            word = ""
        else:
            word = word + a_string[i]
    words.append(word)
    return words


def display_words(words):
    # DisplayWords function
    # Accepts a list of words and displays them, one per line
    for word in words:
        print(word)


def main():
    # Ask user to enter a sentence
    user_input = input("Enter a sentence: ")
    print()

    # Catch any invalid input
    if len(user_input) == 0:
        print("Invalid input. Please try again.")
        return

    # Call function to parse the string and return a list of words
    words = parse_string(user_input)

    # Call function to display the words, one per line
    display_words(words)


if __name__ == "__main__":
    main()
