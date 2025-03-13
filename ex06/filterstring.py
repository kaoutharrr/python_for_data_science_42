from ft_filter import ft_filter
import sys


def filter_string(S, N):
    """
    Filters words from string S that have a length greater than N.
    Args:
    S (str): The input string.
    N (int): The minimum length of words to include.
    Returns:
    list: A list of words with length greater than N."""
    words = S.split()
    filtered_words = ft_filter(lambda word: len(word) > N, words)
    return list(filtered_words)


def main():
    """checks the args and calls the filter function"""
    try:
        assert len(sys.argv) == 3, ": the arguments are bad"
        assert isinstance(sys.argv[1], str), ": the arguments are bad"
        assert sys.argv[2].isdigit(), ": the arguments are bad"
        N = (int(sys.argv[2]))
        S = sys.argv[1]
        print(filter_string(S, N))
    except AssertionError as error:
        print("AssertionError: {}".format(error))


if __name__ == "__main__":
    main()
