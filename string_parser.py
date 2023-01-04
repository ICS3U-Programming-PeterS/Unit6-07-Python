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


def main():
    # user interface
    print("This program will ask the user for a sentence and then")
    print("display each word, without spaces, one per line. \n")

    # Ask user to enter a sentence
    user_input = input("Enter a string: ")

    # Catch any invalid input
    if len(user_input) == 0:
        print("Invalid input. Please try again.")
        return

    # Call function to parse the string and return a list of words
    words = parse_string(user_input)

    # display words
    print("The words in your sentence, without spaces, are:")
    for word in words:
        print(word)


if __name__ == "__main__":
    main()
