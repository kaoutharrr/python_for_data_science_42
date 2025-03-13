import sys


def encode_to_morse(text):
    """
    Encodes a string into Morse code.

    Args:
        text (str): The input string to encode.

    Returns:
        str: The Morse code representation of the input string.
    """
    morse = {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
        "F": "..-. ",
        "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ", "Q": "--.- ",
        "R": ".-. ",
        "S": "... ", "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ",
        "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ",
        "9": "----. ",
    }
    res = []
    for c in text.upper():
        if c in morse:
            res.append(morse[c])
        else:
            raise AssertionError("the arguments are bad")
    return "".join(res).strip()


def main():
    """
    check the args and call the encode funtion
    """
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        text = sys.argv[1]
        assert all(char.isalnum() or char.isspace() for char in text), \
            "the arguments are bad"
        print(encode_to_morse(text))
    except AssertionError as error:
        print("AssertionError: {}".format(error))


if __name__ == "__main__":
    main()
