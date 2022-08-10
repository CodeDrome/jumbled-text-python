import random
from datetime import datetime


def jumble(text, amount):

    """
    Jumbles the letters (except first and last) of the words
    in text. Amount is a decimal between 0.0 and 1.0 and
    specifies the amount of jumbling to be carried out.
    """

    jumbled_words = []
    word = ""

    for index, character in enumerate(text):

        if character.isalpha():

            word += character

        else:

            word = _scramble(word, amount)
            jumbled_words.append(word)
            jumbled_words.append(character)
            word = ""

        if index == (len(text) - 1):

            word = _scramble(word, amount)
            jumbled_words.append(word)

    return "".join(jumbled_words)


def _scramble(word, amount):

    if len(word) > 3:

        random.seed(datetime.now())

        i = 0
        l = len(word)
        max = (l * amount) - 1
        letters = list(word)

        while i < max:

            c1 = random.randint(1, l - 2)
            c2 = random.randint(1, l - 2)

            if c1 != c2:

                letters[c1] = chr(ord(letters[c1]) ^ ord(letters[c2]))
                letters[c2] = chr(ord(letters[c1]) ^ ord(letters[c2]))
                letters[c1] = chr(ord(letters[c1]) ^ ord(letters[c2]))

                i += 1

        return "".join(letters)

    else:

        return word
