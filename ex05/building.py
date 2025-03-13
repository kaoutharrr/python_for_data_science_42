
import sys
import string


def count(text):
    """count all the different types in a text"""
    uppers = 0
    lowers = 0
    punt = 0
    digits = 0
    space = 0
    for c in text:
        if c.isupper():
            uppers += 1
        elif c.islower():
            lowers += 1
        elif c.isdigit():
            digits += 1
        elif c in string.punctuation:
            punt += 1
        elif c.isspace():
            space += 1

    print("The text contains {} characters: ".format(len(text)))
    print("{} upper letters".format(uppers))
    print("{} lower letters".format(lowers))
    print("{} punctuation marks".format(punt))
    print("{} spaces".format(space))
    print("{} digits".format(digits))


def main():
    """Main function to handle user input and process the text."""
    try:
        if len(sys.argv) == 1:
            text = input("What is the text to count? \n") + '\n'
        else:
            assert len(sys.argv) == 2, "More than one argument provided."
            text = sys.argv[1]
        count(text)
    except AssertionError as error:
        print("AssertionError: {}".format(error))


if __name__ == "__main__":
    main()
