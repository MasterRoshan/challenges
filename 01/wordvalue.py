from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""

    with open(DICTIONARY) as dictionary:
        word_list = dictionary.read().splitlines()
    return word_list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for ch in word.upper():
        try:
            value += LETTER_SCORES[ch]
        except KeyError:
            print("\nScrabble has no hyphens or personal pronouns for that matter\n")
    return value

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    values = []
    for word in words:
        values.append(calc_word_value(word))
    return words[values.index(max(values))]

if __name__ == "__main__":
    pass # run unittests to validate
